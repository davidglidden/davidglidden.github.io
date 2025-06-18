#!/usr/bin/env python3
"""
Apple Books Library CSV Extractor
Extract title and author information from EPUB files to create a searchable CSV
"""

import csv
import subprocess
import xml.etree.ElementTree as ET
from pathlib import Path
import re
import zipfile
from collections import defaultdict

def extract_metadata_from_epub_file(epub_path):
    """Extract metadata from actual EPUB file"""
    title = None
    author = None
    
    try:
        with zipfile.ZipFile(epub_path, 'r') as epub_zip:
            # Look for content.opf or similar metadata files
            metadata_files = [f for f in epub_zip.namelist() if f.endswith('.opf') or 'content.opf' in f]
            
            if metadata_files:
                opf_content = epub_zip.read(metadata_files[0]).decode('utf-8', errors='ignore')
                
                # Parse OPF XML
                try:
                    root = ET.fromstring(opf_content)
                    
                    # Define namespace
                    ns = {'dc': 'http://purl.org/dc/elements/1.1/'}
                    
                    # Extract title
                    title_elem = root.find('.//dc:title', ns)
                    if title_elem is not None:
                        title = title_elem.text
                    
                    # Extract author/creator
                    creator_elem = root.find('.//dc:creator', ns)
                    if creator_elem is not None:
                        author = creator_elem.text
                        
                except ET.ParseError:
                    pass
                    
    except Exception as e:
        pass
    
    return title, author

def extract_metadata_from_epub_dir(epub_dir):
    """Extract metadata from unpacked EPUB directory"""
    title = None
    author = None
    
    try:
        # Look for OPF files
        opf_files = list(epub_dir.rglob("*.opf"))
        
        if opf_files:
            with open(opf_files[0], 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
            
            # Parse XML
            try:
                root = ET.fromstring(content)
                ns = {'dc': 'http://purl.org/dc/elements/1.1/'}
                
                title_elem = root.find('.//dc:title', ns)
                if title_elem is not None:
                    title = title_elem.text
                
                creator_elem = root.find('.//dc:creator', ns)
                if creator_elem is not None:
                    author = creator_elem.text
                    
            except ET.ParseError:
                pass
        
        # Fallback: look in iTunes metadata
        itunes_files = list(epub_dir.glob("iTunesMetadata.plist"))
        if itunes_files and not title:
            try:
                with open(itunes_files[0], 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    
                # Simple plist parsing for title and author
                if '<key>itemName</key>' in content:
                    start = content.find('<key>itemName</key>') + len('<key>itemName</key>')
                    start = content.find('<string>', start) + len('<string>')
                    end = content.find('</string>', start)
                    if end > start:
                        title = content[start:end]
                
                if '<key>artistName</key>' in content:
                    start = content.find('<key>artistName</key>') + len('<key>artistName</key>')
                    start = content.find('<string>', start) + len('<string>')
                    end = content.find('</string>', start)
                    if end > start:
                        author = content[start:end]
                        
            except Exception:
                pass
                
    except Exception as e:
        pass
    
    return title, author

def extract_from_filename(filename):
    """Extract title and author from filename as fallback"""
    name = filename.replace('.epub', '')
    
    # Common patterns: "Title - Author", "Author - Title", etc.
    if ' - ' in name:
        parts = name.split(' - ')
        if len(parts) == 2:
            return parts[0].strip(), parts[1].strip()
        elif len(parts) > 2:
            # Try to guess which is title vs author
            # Usually title comes first
            return parts[0].strip(), ' - '.join(parts[1:]).strip()
    
    return name, None

def create_library_csv():
    """Create CSV file with all EPUB titles and authors"""
    source_dir = Path("source_epubs")
    
    if not source_dir.exists():
        print("❌ source_epubs directory not found")
        return
    
    # Collect all EPUB items
    epub_items = []
    
    # Regular EPUB files
    for epub_file in source_dir.rglob("*.epub"):
        if epub_file.is_file():
            epub_items.append(('file', epub_file))
    
    # Directory-format EPUBs
    for item in source_dir.iterdir():
        if item.is_dir() and item.name.endswith('.epub'):
            epub_items.append(('dir', item))
    
    print(f"📚 Processing {len(epub_items)} EPUB items...")
    
    library_data = []
    processed = 0
    
    for item_type, epub_path in epub_items:
        processed += 1
        if processed % 50 == 0:
            print(f"   Processed {processed}/{len(epub_items)}...")
        
        title = None
        author = None
        
        # Extract metadata based on type
        if item_type == 'file':
            title, author = extract_metadata_from_epub_file(epub_path)
        else:  # directory
            title, author = extract_metadata_from_epub_dir(epub_path)
        
        # Fallback to filename
        if not title or not author:
            filename_title, filename_author = extract_from_filename(epub_path.name)
            title = title or filename_title
            author = author or filename_author
        
        # Clean up extracted data
        if title:
            title = re.sub(r'\s+', ' ', title).strip()[:200]
        if author:
            author = re.sub(r'\s+', ' ', author).strip()[:100]
        
        library_data.append({
            'filename': epub_path.name,
            'title': title or 'Unknown Title',
            'author': author or 'Unknown Author',
            'type': item_type,
            'path': str(epub_path)
        })
    
    # Write to CSV
    csv_file = "apple_books_library.csv"
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=['filename', 'title', 'author', 'type', 'path'])
        writer.writeheader()
        writer.writerows(library_data)
    
    print(f"✅ Library CSV created: {csv_file}")
    print(f"📊 Total books: {len(library_data)}")
    
    # Create summary statistics
    authors = defaultdict(int)
    for book in library_data:
        authors[book['author']] += 1
    
    print(f"\n📈 TOP AUTHORS:")
    for author, count in sorted(authors.items(), key=lambda x: x[1], reverse=True)[:10]:
        if author != 'Unknown Author':
            print(f"   {author}: {count} books")
    
    # Look for John Berger specifically
    berger_books = [book for book in library_data if 'berger' in book['author'].lower()]
    if berger_books:
        print(f"\n🎭 JOHN BERGER BOOKS FOUND: {len(berger_books)}")
        for book in berger_books:
            print(f"   • {book['title']} - {book['author']}")
    
    return csv_file, library_data

if __name__ == "__main__":
    csv_file, library_data = create_library_csv()
    print(f"\n💡 Use the CSV file to search and filter your library")
    print(f"   Open {csv_file} in Excel/Numbers for easy browsing")