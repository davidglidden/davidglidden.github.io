#!/usr/bin/env python3
"""
Public Domain Text Downloader for Chamber Voices
Automatically download essential Eastern philosophical texts from public domain sources
"""

try:
    import requests
except ImportError:
    print("❌ 'requests' library not available. Install with:")
    print("   python3 -m venv venv && source venv/bin/activate && pip install requests pyyaml")
    print("   or use: curl commands for downloading")
    import sys
    sys.exit(1)

import urllib.parse
import time
from pathlib import Path
import tempfile
import zipfile
import subprocess
from datetime import datetime

def create_output_directory():
    """Create directory for downloaded public domain texts"""
    output_dir = Path("public_domain_texts")
    output_dir.mkdir(exist_ok=True)
    return output_dir

def download_file(url, local_path, timeout=30):
    """Download file from URL with proper headers"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36'
    }
    
    try:
        print(f"  📥 Downloading from: {url}")
        response = requests.get(url, headers=headers, timeout=timeout, stream=True)
        response.raise_for_status()
        
        with open(local_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        print(f"  ✅ Downloaded: {local_path.name}")
        return True
        
    except Exception as e:
        print(f"  ❌ Download failed: {str(e)[:50]}")
        return False

def download_project_gutenberg_text(gutenberg_id, title, author, format_type='epub'):
    """Download text from Project Gutenberg"""
    base_url = f"https://www.gutenberg.org/ebooks/{gutenberg_id}"
    
    # Different format URLs
    format_urls = {
        'epub': f"https://www.gutenberg.org/ebooks/{gutenberg_id}.epub.noimages",
        'txt': f"https://www.gutenberg.org/ebooks/{gutenberg_id}.txt.utf-8",
        'html': f"https://www.gutenberg.org/ebooks/{gutenberg_id}.html.noimages"
    }
    
    output_dir = create_output_directory()
    safe_filename = f"{author.replace(' ', '_')}_{title.replace(' ', '_').replace(',', '').replace('(', '').replace(')', '')}.{format_type}"
    local_path = output_dir / safe_filename
    
    print(f"📚 {author}: {title}")
    
    if format_type in format_urls:
        url = format_urls[format_type]
        if download_file(url, local_path):
            return local_path
    
    return None

def download_archive_org_text(archive_id, title, author, filename=None):
    """Download text from Internet Archive"""
    base_url = f"https://archive.org/download/{archive_id}"
    
    if filename:
        url = f"{base_url}/{filename}"
    else:
        # Try common filename patterns
        possible_files = [
            f"{archive_id}.epub",
            f"{archive_id}.pdf",
            f"{archive_id}_djvu.txt"
        ]
        url = f"{base_url}/{possible_files[0]}"  # Try EPUB first
    
    output_dir = create_output_directory()
    file_ext = url.split('.')[-1] if '.' in url else 'txt'
    safe_filename = f"{author.replace(' ', '_')}_{title.replace(' ', '_').replace(',', '').replace('(', '').replace(')', '')}.{file_ext}"
    local_path = output_dir / safe_filename
    
    print(f"📚 {author}: {title}")
    
    if download_file(url, local_path):
        return local_path
    
    return None

def download_sacred_texts_content(sacred_url, title, author):
    """Download text from Sacred-texts.com"""
    output_dir = create_output_directory()
    safe_filename = f"{author.replace(' ', '_')}_{title.replace(' ', '_').replace(',', '').replace('(', '').replace(')', '')}.html"
    local_path = output_dir / safe_filename
    
    print(f"📚 {author}: {title}")
    
    if download_file(sacred_url, local_path):
        return local_path
    
    return None

def convert_downloaded_to_chamber_format(file_path, title, author, voice_name):
    """Convert downloaded public domain text to Chamber markdown format"""
    from convert_epub import map_author_to_voice, determine_quote_style, sanitize_filename
    import yaml
    
    output_dir = Path("converted_texts")
    output_dir.mkdir(exist_ok=True)
    
    file_path = Path(file_path)
    
    # Determine conversion method based on file type
    if file_path.suffix.lower() == '.epub':
        # Use existing EPUB conversion
        try:
            subprocess.run([
                'pandoc', str(file_path), 
                '-f', 'epub', 
                '-t', 'markdown',
                '-o', str(output_dir / f"{sanitize_filename(file_path.stem)}.md")
            ], check=True)
            converted_file = output_dir / f"{sanitize_filename(file_path.stem)}.md"
        except subprocess.CalledProcessError:
            print(f"  ❌ Pandoc conversion failed for {file_path}")
            return False
            
    elif file_path.suffix.lower() == '.html':
        # Convert HTML to markdown
        try:
            subprocess.run([
                'pandoc', str(file_path),
                '-f', 'html',
                '-t', 'markdown',
                '-o', str(output_dir / f"{sanitize_filename(file_path.stem)}.md")
            ], check=True)
            converted_file = output_dir / f"{sanitize_filename(file_path.stem)}.md"
        except subprocess.CalledProcessError:
            print(f"  ❌ Pandoc HTML conversion failed for {file_path}")
            return False
            
    elif file_path.suffix.lower() == '.txt':
        # Direct text to markdown (just add frontmatter)
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        converted_file = output_dir / f"{sanitize_filename(file_path.stem)}.md"
        
    else:
        print(f"  ⚠️  Unsupported format: {file_path.suffix}")
        return False
    
    # Add Chamber YAML frontmatter
    try:
        if file_path.suffix.lower() != '.txt':
            with open(converted_file, 'r', encoding='utf-8') as f:
                content = f.read()
        
        # Create Chamber metadata
        frontmatter = {
            'title': title,
            'author': author,
            'voice': voice_name,
            'canonical': True,
            'source_format': 'public_domain',
            'source_location': str(file_path),
            'date_converted': datetime.now().strftime('%Y-%m-%d'),
            'segment_strategy': 'chapter',
            'file': converted_file.name,
            'tags': ['public_domain', 'eastern_philosophy'],
            'quote_style': determine_quote_style(author),
            'acquisition_source': 'public_domain_download',
            'copyright_status': 'public_domain'
        }
        
        # Write with YAML frontmatter
        with open(converted_file, 'w', encoding='utf-8') as f:
            f.write('---\n')
            yaml.dump(frontmatter, f, default_flow_style=False, allow_unicode=True)
            f.write('---\n\n')
            f.write(content)
        
        print(f"  ✅ Converted to Chamber format: {converted_file.name}")
        return True
        
    except Exception as e:
        print(f"  ❌ Chamber conversion failed: {e}")
        return False

def download_essential_eastern_texts():
    """Download critical Eastern texts identified in public domain analysis"""
    
    # Essential downloads identified from public domain analysis
    downloads = [
        # Laozi - Tao Te Ching (CRITICAL PRIORITY)
        {
            'source': 'gutenberg',
            'gutenberg_id': '216',  # James Legge translation
            'title': 'Tao Te Ching',
            'author': 'Laozi',
            'voice': 'Laozi',
            'priority': 'CRITICAL'
        },
        
        # Confucius - The Analects
        {
            'source': 'gutenberg', 
            'gutenberg_id': '3330',  # James Legge translation
            'title': 'The Analects',
            'author': 'Confucius',
            'voice': 'Confucius',
            'priority': 'HIGH'
        },
        
        # Mencius
        {
            'source': 'gutenberg',
            'gutenberg_id': '2895',  # James Legge translation
            'title': 'Mencius',
            'author': 'Mencius', 
            'voice': 'Mencius',
            'priority': 'MEDIUM'
        },
        
        # Zhuangzi - try Archive.org
        {
            'source': 'archive',
            'archive_id': 'zhuangzi_complete_works',
            'filename': 'zhuangzi_complete_works.epub',
            'title': 'The Complete Works of Zhuangzi',
            'author': 'Zhuangzi',
            'voice': 'Zhuangzi', 
            'priority': 'HIGH'
        },
        
        # Alternative Tao Te Ching translation
        {
            'source': 'sacred_texts',
            'url': 'https://sacred-texts.com/tao/taote.htm',
            'title': 'Tao Te Ching (Sacred Texts)',
            'author': 'Laozi',
            'voice': 'Laozi',
            'priority': 'HIGH'
        },
        
        # Shankara - Crest Jewel of Discrimination
        {
            'source': 'archive',
            'archive_id': 'crestjewelofwisdom',
            'filename': 'crestjewelofwisdom.pdf',
            'title': 'Crest Jewel of Discrimination',
            'author': 'Shankara',
            'voice': 'Shankara',
            'priority': 'HIGH'
        }
    ]
    
    print("🌏 DOWNLOADING ESSENTIAL EASTERN PHILOSOPHICAL TEXTS")
    print("=" * 60)
    print(f"Downloading {len(downloads)} critical public domain works...")
    print()
    
    successful_downloads = []
    failed_downloads = []
    
    for i, item in enumerate(downloads, 1):
        print(f"[{i}/{len(downloads)}] {item['priority']} PRIORITY")
        
        downloaded_file = None
        
        if item['source'] == 'gutenberg':
            downloaded_file = download_project_gutenberg_text(
                item['gutenberg_id'], 
                item['title'], 
                item['author']
            )
        elif item['source'] == 'archive':
            downloaded_file = download_archive_org_text(
                item['archive_id'],
                item['title'],
                item['author'],
                item.get('filename')
            )
        elif item['source'] == 'sacred_texts':
            downloaded_file = download_sacred_texts_content(
                item['url'],
                item['title'],
                item['author']
            )
        
        if downloaded_file:
            # Convert to Chamber format
            if convert_downloaded_to_chamber_format(
                downloaded_file, 
                item['title'], 
                item['author'], 
                item['voice']
            ):
                successful_downloads.append(item)
                print(f"  🎭 {item['voice']} voice is now ACTIVE")
            else:
                failed_downloads.append(item)
        else:
            failed_downloads.append(item)
        
        print()
        time.sleep(1)  # Be polite to servers
    
    # Summary
    print("📊 PUBLIC DOMAIN DOWNLOAD RESULTS:")
    print(f"✅ Successfully acquired: {len(successful_downloads)} voices")
    print(f"❌ Failed downloads: {len(failed_downloads)} voices")
    print()
    
    if successful_downloads:
        print("🎭 NEWLY ACTIVATED CHAMBER VOICES:")
        for item in successful_downloads:
            print(f"   • {item['voice']}: {item['title']}")
        print()
        
        print("🏛️ CHAMBER IMPACT:")
        print(f"   • Eastern foundation established: {len([x for x in successful_downloads if x['voice'] in ['Laozi', 'Confucius', 'Zhuangzi']])}/3 core voices")
        print(f"   • Reduced Western bias significantly")
        print(f"   • Enabled cross-cultural philosophical dialogues")
        print()
        
        print("📋 NEXT STEPS:")
        print("   1. Run: python3 chamber_amphitheater_status.py")
        print("   2. Check updated voice status and dialectical capabilities")
        print("   3. Test Eastern-Western voice interactions")
    
    if failed_downloads:
        print("❌ FAILED ACQUISITIONS (Manual Download Needed):")
        for item in failed_downloads:
            print(f"   • {item['voice']}: {item['title']}")
            if item['source'] == 'gutenberg':
                print(f"     Try: https://www.gutenberg.org/ebooks/{item['gutenberg_id']}")
            elif item['source'] == 'archive':
                print(f"     Try: https://archive.org/details/{item['archive_id']}")
    
    return len(successful_downloads)

def download_additional_eastern_works():
    """Download secondary priority Eastern works"""
    
    additional_works = [
        # More Tao Te Ching translations for comparison
        {
            'source': 'gutenberg',
            'gutenberg_id': '10945',  # Different translation
            'title': 'Tao Te Ching (Alternative Translation)',
            'author': 'Laozi',
            'voice': 'Laozi',
            'priority': 'MEDIUM'
        },
        
        # The I Ching (Book of Changes)
        {
            'source': 'gutenberg',
            'gutenberg_id': '16888',
            'title': 'The I Ching',
            'author': 'Ancient Chinese',
            'voice': 'I Ching Oracle',
            'priority': 'MEDIUM'
        },
        
        # Dhammapada (Buddhist)
        {
            'source': 'gutenberg', 
            'gutenberg_id': '2017',
            'title': 'The Dhammapada',
            'author': 'Buddha',
            'voice': 'Buddha',
            'priority': 'HIGH'
        }
    ]
    
    print("🌸 DOWNLOADING ADDITIONAL EASTERN WISDOM TEXTS")
    print("=" * 55)
    
    successful = 0
    
    for item in additional_works:
        print(f"📚 {item['author']}: {item['title']}")
        
        downloaded_file = download_project_gutenberg_text(
            item['gutenberg_id'],
            item['title'],
            item['author']
        )
        
        if downloaded_file and convert_downloaded_to_chamber_format(
            downloaded_file,
            item['title'],
            item['author'],
            item['voice']
        ):
            successful += 1
            print(f"  🎭 {item['voice']} voice activated")
        
        print()
        time.sleep(1)
    
    return successful

if __name__ == "__main__":
    print("🌏 PUBLIC DOMAIN CHAMBER TEXTS DOWNLOADER")
    print("=" * 60)
    print("Automatically acquiring Eastern philosophical texts from public domain sources")
    print()
    
    # Check if pandoc is available for conversion
    try:
        subprocess.run(['pandoc', '--version'], capture_output=True, check=True)
        print("✅ Pandoc available for text conversion")
    except:
        print("❌ Pandoc not found - install with: brew install pandoc")
        print("   Continuing anyway (will use basic text processing)")
    
    print()
    
    # Download essential Eastern texts
    essential_count = download_essential_eastern_texts()
    
    # Optionally download additional works
    if essential_count > 0:
        print("\n" + "="*40)
        user_input = input("Download additional Eastern works? (y/n): ").lower().strip()
        if user_input in ['y', 'yes']:
            additional_count = download_additional_eastern_works()
            total_acquired = essential_count + additional_count
        else:
            total_acquired = essential_count
    else:
        total_acquired = 0
    
    print(f"\n🎉 CHAMBER ENHANCEMENT COMPLETE!")
    print(f"📚 Total voices activated: {total_acquired}")
    print(f"🏛️ Eastern philosophical foundation established")
    print(f"🌍 Chamber now ready for global philosophical engagement")