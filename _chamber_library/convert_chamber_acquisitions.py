#!/usr/bin/env python3
"""
Convert New Chamber Acquisitions
Handle both EPUB and PDF files for critical Chamber voice texts
"""

import shutil
import tempfile
from pathlib import Path
from convert_epub import convert_epub_to_markdown, sanitize_filename, map_author_to_voice, determine_quote_style
import subprocess
import yaml
from datetime import datetime

def convert_pdf_to_markdown(pdf_path, output_dir):
    """Convert PDF to Markdown using pandoc"""
    try:
        # Extract basic metadata from filename
        filename = pdf_path.name
        if "Walter Benjamin" in filename or "Benjamin" in filename:
            author = "Walter Benjamin"
            if "Arcades" in filename:
                title = "The Arcades Project"
            else:
                title = filename.replace('.pdf', '')
        else:
            # Try to extract from filename pattern
            if ' (' in filename and ')' in filename:
                parts = filename.split(' (')
                title = parts[0]
                author_part = parts[1].replace(')', '').replace('.pdf', '')
                author = author_part
            else:
                title = filename.replace('.pdf', '')
                author = "Unknown Author"
        
        # Create output filename
        safe_name = sanitize_filename(filename)
        output_file = output_dir / f"{safe_name}.md"
        
        print(f"Converting PDF: {title}")
        
        # Convert with pandoc
        subprocess.run([
            'pandoc', str(pdf_path),
            '--to=markdown',
            '--output', str(output_file),
            '--wrap=preserve',
            '--markdown-headings=atx'
        ], check=True, timeout=180)
        
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
            'source_format': 'pdf',
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
        print(f"❌ PDF conversion error: {e}")
        return False

def convert_chamber_acquisitions():
    """Convert the new Chamber acquisition files"""
    
    acquisition_files = [
        {
            'path': Path("/Users/davidglidden/Desktop/for the chamber/The Work of Art in the Age of Mechani (Benjamin).epub"),
            'type': 'epub',
            'expected_author': 'Walter Benjamin',
            'expected_title': 'The Work of Art in the Age of Mechanical Reproduction'
        },
        {
            'path': Path("/Users/davidglidden/Desktop/for the chamber/The Arcades Project (Walter Benjamin).pdf"),
            'type': 'pdf',
            'expected_author': 'Walter Benjamin', 
            'expected_title': 'The Arcades Project'
        },
        {
            'path': Path("/Users/davidglidden/Desktop/for the chamber/A Pattern Language (Christopher Alexander).epub"),
            'type': 'epub',
            'expected_author': 'Christopher Alexander',
            'expected_title': 'A Pattern Language'
        },
        {
            'path': Path("/Users/davidglidden/Desktop/for the chamber/The Age of Surveillance Capitalism.epub"),
            'type': 'epub', 
            'expected_author': 'Shoshana Zuboff',
            'expected_title': 'The Age of Surveillance Capitalism'
        }
    ]
    
    output_dir = Path("converted_texts")
    output_dir.mkdir(exist_ok=True)
    
    print("🏛️ CONVERTING CRITICAL CHAMBER ACQUISITIONS")
    print("=" * 60)
    print("Processing essential works for Chamber completion...")
    print()
    
    successful = 0
    failed = 0
    new_voices_activated = []
    
    with tempfile.TemporaryDirectory() as temp_dir_str:
        temp_dir = Path(temp_dir_str)
        
        for i, file_info in enumerate(acquisition_files, 1):
            file_path = file_info['path']
            
            print(f"[{i}/{len(acquisition_files)}] {file_info['expected_author']}")
            print(f"           {file_info['expected_title']}")
            
            if not file_path.exists():
                print(f"           ❌ File not found: {file_path}")
                failed += 1
                continue
            
            try:
                if file_info['type'] == 'epub':
                    if file_path.is_dir():
                        from convert_directory_epubs import convert_directory_epub_to_markdown
                        success = convert_directory_epub_to_markdown(file_path, output_dir, temp_dir)
                    else:
                        success = convert_epub_to_markdown(file_path, output_dir)
                else:  # PDF
                    success = convert_pdf_to_markdown(file_path, output_dir)
                
                if success:
                    successful += 1
                    new_voices_activated.append(f"{file_info['expected_author']} - {file_info['expected_title']}")
                    print(f"           ✅ Success - Chamber voice activated")
                else:
                    failed += 1
                    print(f"           ❌ Failed")
                    
            except Exception as e:
                failed += 1
                print(f"           ❌ Error: {str(e)[:50]}")
    
    print(f"\n📊 CHAMBER ACQUISITION RESULTS")
    print("=" * 60)
    print(f"✅ Successfully converted: {successful}")
    print(f"❌ Failed: {failed}")
    
    if successful > 0:
        print(f"\n🎭 NEW CHAMBER VOICES ACTIVATED:")
        for voice in new_voices_activated:
            print(f"  ✅ {voice}")
        
        # Calculate new chamber readiness
        print(f"\n🏛️ CHAMBER STATUS UPGRADE:")
        if successful >= 3:
            print("🟢 MAJOR UPGRADE - Multiple core voices now active")
            print("   Benjamin dialectical capacity significantly enhanced")
            if any("Alexander" in voice for voice in new_voices_activated):
                print("   Pattern language analysis now available")
            if any("Zuboff" in voice for voice in new_voices_activated):
                print("   Contemporary technology critique now active")
        
        print(f"\n🚀 NEXT STEPS:")
        print(f"   1. Run: python3 analyze_library.py")
        print(f"   2. Update Chamber readiness assessment")
        print(f"   3. Test enhanced dialectical capabilities")
        print(f"   4. Begin advanced Chamber protocols")
    
    return successful, failed, new_voices_activated

if __name__ == "__main__":
    successful, failed, new_voices_activated = convert_chamber_acquisitions()
    
    if successful > 0:
        print(f"\n✨ {successful} critical Chamber works successfully integrated!")
        print(f"🏛️ The Chamber's intellectual foundation has been significantly strengthened")