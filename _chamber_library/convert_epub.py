#!/usr/bin/env python3
"""
Chamber Library Conversion Script
Converts EPUB files to Markdown with YAML frontmatter for Chamber integration
"""

import os
import subprocess
import re
import yaml
from pathlib import Path
from datetime import datetime

def sanitize_filename(filename):
    """Convert filename to safe format for Chamber canon"""
    # Remove .epub extension
    name = filename.replace('.epub', '')
    # Replace spaces and special chars with hyphens
    name = re.sub(r'[^\w\-_]', '-', name)
    # Remove multiple consecutive hyphens
    name = re.sub(r'-+', '-', name)
    # Remove leading/trailing hyphens
    name = name.strip('-').lower()
    return name

def extract_metadata_from_epub(epub_path):
    """Extract title and author from EPUB using multiple methods"""
    title = None
    author = None
    
    # Method 1: Try pandoc metadata extraction
    try:
        result = subprocess.run([
            'pandoc', str(epub_path), '--to=markdown', '--standalone'
        ], capture_output=True, text=True, timeout=30)
        
        content = result.stdout
        lines = content.split('\n')
        
        # Look for YAML frontmatter
        if lines and lines[0].strip() == '---':
            yaml_end = -1
            for i, line in enumerate(lines[1:], 1):
                if line.strip() == '---':
                    yaml_end = i
                    break
            
            if yaml_end > 0:
                yaml_content = '\n'.join(lines[1:yaml_end])
                try:
                    metadata = yaml.safe_load(yaml_content)
                    if isinstance(metadata, dict):
                        title = metadata.get('title')
                        author = metadata.get('author')
                except:
                    pass
        
        # Method 2: Look for title patterns in content
        if not title or not author:
            # Look for title in first 100 lines
            for i, line in enumerate(lines[:100]):
                line = line.strip()
                
                # Skip empty lines and image references
                if not line or line.startswith('![') or line.startswith('['):
                    continue
                
                # Look for title patterns
                if not title:
                    # Check for standalone title-like lines
                    if (line.isupper() and len(line.split()) <= 8 and 
                        len(line) > 3 and not line.startswith('#')):
                        title = line.title()
                    elif line.startswith('# ') and len(line) > 3:
                        title = line[2:].strip()
                
                # Look for author patterns
                if not author:
                    # Common author patterns
                    author_patterns = [
                        r'^([A-Z][a-z]+ [A-Z][a-z]+)$',  # First Last
                        r'^([A-Z][a-z]+ [A-Z]\. [A-Z][a-z]+)$',  # First M. Last
                        r'^([A-Z][A-Z ]+)$'  # ALL CAPS NAME
                    ]
                    
                    for pattern in author_patterns:
                        match = re.match(pattern, line)
                        if match and len(match.group(1)) > 4:
                            author = match.group(1)
                            break
                
                if title and author:
                    break
                    
    except Exception as e:
        print(f"Metadata extraction warning: {e}")
    
    # Method 3: Try filename extraction as fallback
    if not title:
        filename = epub_path.name.replace('.epub', '')
        # Clean up filename for title
        if ' - ' in filename:
            parts = filename.split(' - ')
            title = parts[0].strip()
            if not author and len(parts) > 1:
                author = parts[-1].strip()
        else:
            title = filename
    
    # Clean up extracted values
    if title:
        title = re.sub(r'\s+', ' ', title).strip()
        title = title[:100]  # Reasonable length limit
    
    if author:
        author = re.sub(r'\s+', ' ', author).strip()
        author = author[:50]  # Reasonable length limit
        
    return title or "Unknown Title", author or "Unknown Author"

def map_author_to_voice(author):
    """Map author name to Chamber voice, with special handling for key figures"""
    if not author or author == "Unknown Author":
        return "Unknown Voice"
    
    # Key Chamber voices - exact matches
    voice_mappings = {
        'Gaston Bachelard': 'Gaston Bachelard',
        'Christopher Alexander': 'Christopher Alexander', 
        'Walter Benjamin': 'Walter Benjamin',
        'Hannah Arendt': 'Hannah Arendt',
        'Simone Weil': 'Simone Weil',
        'Emmanuel Levinas': 'Emmanuel Levinas',
        'Martin Heidegger': 'Martin Heidegger',
        'Robin Wall Kimmerer': 'Robin Wall Kimmerer',
        'Shoshana Zuboff': 'Shoshana Zuboff',
        'John Berger': 'John Berger',
        'Aldus Manutius': 'Aldus Manutius'
    }
    
    # Check for exact matches first
    if author in voice_mappings:
        return voice_mappings[author]
    
    # Check for partial matches (last name)
    author_lower = author.lower()
    for full_name, voice in voice_mappings.items():
        if full_name.split()[-1].lower() in author_lower:
            return voice
    
    # Default: use author name as voice
    return author

def determine_quote_style(author):
    """Determine appropriate quote style based on author"""
    if not author or author == "Unknown Author":
        return "standard"
    
    # Style mappings based on philosophical tradition
    poetic_voices = ['Gaston Bachelard', 'Walter Benjamin', 'John Berger']
    analytical_voices = ['Hannah Arendt', 'Shoshana Zuboff']
    contemplative_voices = ['Simone Weil', 'Emmanuel Levinas']
    
    if author in poetic_voices:
        return "poetic"
    elif author in analytical_voices:
        return "analytical"
    elif author in contemplative_voices:
        return "contemplative"
    else:
        return "standard"

def convert_epub_to_markdown(epub_path, output_dir):
    """Convert single EPUB to Markdown with Chamber YAML frontmatter"""
    epub_name = epub_path.name
    safe_name = sanitize_filename(epub_name)
    output_file = output_dir / f"{safe_name}.md"
    
    print(f"Converting: {epub_name}")
    
    # Check if this is a directory (Apple Books format) or file
    if epub_path.is_dir():
        # This is an unpacked EPUB directory - pandoc can handle this directly
        actual_epub = epub_path
    else:
        actual_epub = epub_path
    
    # Extract basic metadata
    title, author = extract_metadata_from_epub(actual_epub)
    
    # Convert with pandoc
    try:
        subprocess.run([
            'pandoc', str(actual_epub),
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
            'source_format': 'epub',
            'converted_with': 'pandoc',
            'date_converted': datetime.now().strftime('%Y-%m-%d'),
            'segment_strategy': 'chapter',
            'file': output_file.name,
            'tags': [],  # To be populated during semantic analysis
            'quote_style': quote_style
        }
        
        # Write with YAML frontmatter
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write('---\n')
            yaml.dump(frontmatter, f, default_flow_style=False, allow_unicode=True)
            f.write('---\n\n')
            f.write(content)
        
        print(f"✅ Converted: {safe_name}.md")
        return True
        
    except subprocess.TimeoutExpired:
        print(f"❌ Timeout converting: {epub_name}")
        return False
    except Exception as e:
        print(f"❌ Error converting {epub_name}: {e}")
        return False

def main():
    """Main conversion process"""
    source_dir = Path("source_epubs")
    output_dir = Path("converted_texts")
    
    if not source_dir.exists():
        print("❌ source_epubs directory not found")
        return
    
    output_dir.mkdir(exist_ok=True)
    
    # Find actual .epub files (not directories)
    epub_files = []
    for epub_path in source_dir.rglob("*.epub"):
        if epub_path.is_file():  # Only actual files, not directories
            epub_files.append(epub_path)
    
    print(f"Found {len(epub_files)} actual EPUB files")
    
    successful = 0
    failed = 0
    
    for epub_file in epub_files[:5]:  # Start with first 5 for testing
        if convert_epub_to_markdown(epub_file, output_dir):
            successful += 1
        else:
            failed += 1
    
    print(f"\nConversion complete:")
    print(f"✅ Successful: {successful}")
    print(f"❌ Failed: {failed}")

if __name__ == "__main__":
    main()