#!/usr/bin/env python3
"""
Directory EPUB Converter
Handle Apple Books directory-format EPUBs by creating temporary ZIP files
"""

import zipfile
import tempfile
import shutil
from pathlib import Path
from convert_epub import extract_metadata_from_epub, map_author_to_voice, determine_quote_style, sanitize_filename
import subprocess
import yaml
from datetime import datetime
import csv

def create_epub_from_directory(epub_dir, temp_dir):
    """Create a proper EPUB file from Apple Books directory format"""
    if not epub_dir.is_dir():
        return None
    
    # Create temporary EPUB file
    temp_epub = temp_dir / f"{epub_dir.name}.epub"
    
    try:
        with zipfile.ZipFile(temp_epub, 'w', zipfile.ZIP_DEFLATED) as epub_zip:
            # Add mimetype first (uncompressed)
            mimetype_file = epub_dir / "mimetype"
            if mimetype_file.exists():
                epub_zip.write(mimetype_file, "mimetype", compress_type=zipfile.ZIP_STORED)
            else:
                epub_zip.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
            
            # Add all other files
            for file_path in epub_dir.rglob("*"):
                if file_path.is_file() and file_path.name != "mimetype":
                    # Calculate relative path from epub_dir
                    relative_path = file_path.relative_to(epub_dir)
                    epub_zip.write(file_path, str(relative_path))
        
        return temp_epub
        
    except Exception as e:
        print(f"❌ Error creating EPUB from directory: {e}")
        return None

def convert_directory_epub_to_markdown(epub_dir, output_dir, temp_dir):
    """Convert directory-format EPUB to Markdown"""
    
    # Create temporary EPUB file
    temp_epub = create_epub_from_directory(epub_dir, temp_dir)
    if not temp_epub:
        return False
    
    try:
        # Extract metadata
        title, author = extract_metadata_from_epub(temp_epub)
        
        # Create output filename
        safe_name = sanitize_filename(epub_dir.name)
        output_file = output_dir / f"{safe_name}.md"
        
        # Convert with pandoc
        subprocess.run([
            'pandoc', str(temp_epub),
            '--to=markdown',
            '--output', str(output_file),
            '--wrap=preserve',
            '--markdown-headings=atx'
        ], check=True, timeout=120)
        
        # Read converted content
        with open(output_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Create Chamber voice mapping
        voice_name = map_author_to_voice(author)
        quote_style = determine_quote_style(author)
        
        # Create YAML frontmatter
        frontmatter = {
            'title': title,
            'author': author,
            'voice': voice_name,
            'canonical': True,
            'source_format': 'epub_directory',
            'converted_with': 'pandoc',
            'date_converted': datetime.now().strftime('%Y-%m-%d'),
            'segment_strategy': 'chapter',
            'file': output_file.name,
            'tags': [],
            'quote_style': quote_style
        }
        
        # Write with YAML frontmatter
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('---\n')
            yaml.dump(frontmatter, f, default_flow_style=False, allow_unicode=True)
            f.write('---\n\n')
            f.write(content)
        
        return True
        
    except Exception as e:
        print(f"❌ Conversion error: {e}")
        return False
    finally:
        # Clean up temporary file
        if temp_epub and temp_epub.exists():
            temp_epub.unlink()

def convert_chamber_directory_epubs():
    """Convert Chamber priority books from CSV, handling directory format"""
    
    csv_file = Path("apple_books_library.csv")
    if not csv_file.exists():
        print("❌ Library CSV not found")
        return
    
    # Get Chamber books from CSV
    chamber_authors = [
        'gaston bachelard', 'bachelard',
        'christopher alexander', 'alexander',
        'walter benjamin', 'benjamin', 
        'hannah arendt', 'arendt',
        'simone weil', 'weil',
        'emmanuel levinas', 'levinas',
        'martin heidegger', 'heidegger',
        'robin wall kimmerer', 'kimmerer',
        'john berger', 'berger'
    ]
    
    chamber_books = []
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for book in reader:
            author_lower = book['author'].lower()
            for search_term in chamber_authors:
                if search_term in author_lower:
                    epub_path = Path(book['path'])
                    if epub_path.exists() and epub_path.is_dir():  # Only directory EPUBs
                        chamber_books.append({
                            'path': epub_path,
                            'title': book['title'],
                            'author': book['author'],
                            'filename': book['filename']
                        })
                    break
    
    if not chamber_books:
        print("❌ No directory-format Chamber books found")
        return
    
    output_dir = Path("converted_texts")
    output_dir.mkdir(exist_ok=True)
    
    print(f"🏛️ CONVERTING {len(chamber_books)} CHAMBER DIRECTORY EPUBs")
    print("=" * 60)
    
    successful = 0
    failed = 0
    chamber_ready = []
    
    # Create temporary directory for EPUB creation
    with tempfile.TemporaryDirectory() as temp_dir_str:
        temp_dir = Path(temp_dir_str)
        
        for i, book in enumerate(chamber_books, 1):
            print(f"[{i:2d}/{len(chamber_books)}] {book['author']}")
            print(f"           {book['title'][:60]}...")
            
            try:
                if convert_directory_epub_to_markdown(book['path'], output_dir, temp_dir):
                    successful += 1
                    chamber_ready.append(f"{book['author']} - {book['title']}")
                    print(f"           ✅ Success")
                else:
                    failed += 1
                    print(f"           ❌ Failed")
            except KeyboardInterrupt:
                print(f"\n⏸️  Interrupted by user")
                break
            except Exception as e:
                failed += 1
                print(f"           ❌ Error: {str(e)[:50]}")
            
            # Progress every 10 books
            if i % 10 == 0:
                progress = i / len(chamber_books) * 100
                print(f"\n📈 Progress: {progress:.1f}%")
    
    # Results
    print(f"\n📊 CONVERSION COMPLETE")
    print("=" * 60)
    print(f"✅ Successfully converted: {successful}")
    print(f"❌ Failed: {failed}")
    print(f"🏛️ Chamber-ready texts: {len(chamber_ready)}")
    
    if successful > 0:
        success_rate = successful / (successful + failed) * 100
        print(f"📈 Success rate: {success_rate:.1f}%")
        
        # Show voice distribution
        voice_counts = {}
        for book_entry in chamber_ready:
            author = book_entry.split(' - ')[0]
            voice_counts[author] = voice_counts.get(author, 0) + 1
        
        print(f"\n🎭 CHAMBER VOICES READY:")
        for voice, count in sorted(voice_counts.items()):
            print(f"   ✅ {voice}: {count} books")
        
        print(f"\n🎉 CHAMBER PROTOCOLS CAN NOW BE ACTIVATED!")
        print(f"📄 Run: python3 analyze_library.py")
    
    return successful, failed, chamber_ready

if __name__ == "__main__":
    convert_chamber_directory_epubs()