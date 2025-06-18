#!/usr/bin/env python3
"""
Convert Eastern Philosophy Texts from Desktop Folder
Process the critical Eastern texts from the assembled folder
"""

import subprocess
from pathlib import Path
import tempfile
import zipfile
import shutil
from convert_epub import (
    convert_epub_to_markdown, 
    map_author_to_voice, 
    determine_quote_style,
    sanitize_filename
)

def get_eastern_texts_to_convert():
    """List of critical Eastern texts to prioritize for conversion"""
    
    eastern_folder = Path("/Users/davidglidden/Desktop/eastern to the library")
    
    # Priority Eastern texts identified
    priority_texts = [
        "Diamond Sutra.epub",
        "The Diamond That Cuts Through Illusion.epub", 
        "The Essential Tao An Initiation Into the Heart of Taoism Through the Authentic Tao Te Ching and the Inner Teachings of Chuang-Tzu.epub",
        "The Tao of Philosophy.epub",
        "The Taoism Reader.epub", 
        "The Zen Reader.epub",
        "Zen Bow, Zen Arrow.epub",
        "Zen in the Art of Archery.epub",
        "Zen Mind, Beginner's Mind.epub",
        "Zen Teaching of Instantaneous Awakening: being the teaching of the Zen Master Hui Hai, known as the Great Pearl.epub",
        "Collected Poetical Works of Rumi (Delphi Classics).epub"
    ]
    
    # Check which ones exist
    existing_texts = []
    for text in priority_texts:
        epub_path = eastern_folder / text
        if epub_path.exists():
            existing_texts.append(epub_path)
            print(f"✅ Found: {text}")
        else:
            print(f"❌ Missing: {text}")
    
    return existing_texts

def map_eastern_text_to_voice(title):
    """Map Eastern text titles to Chamber voices"""
    
    voice_mapping = {
        # Buddhist texts
        'diamond sutra': 'Buddha',
        'diamond that cuts': 'Thich Nhat Hanh',
        
        # Taoist texts  
        'essential tao': 'Laozi',
        'tao of philosophy': 'Alan Watts',
        'taoism reader': 'Laozi',
        
        # Zen texts
        'zen reader': 'D.T. Suzuki',
        'zen mind': 'Shunryu Suzuki',
        'zen bow': 'Eugen Herrigel',
        'zen in the art': 'Eugen Herrigel', 
        'zen teaching': 'Hui Hai',
        'instantaneous awakening': 'Hui Hai',
        
        # Sufi/Islamic
        'rumi': 'Rumi'
    }
    
    title_lower = title.lower()
    for key, voice in voice_mapping.items():
        if key in title_lower:
            return voice
    
    return "Eastern Sage"

def determine_eastern_author(title):
    """Determine likely author from title"""
    
    author_mapping = {
        'diamond sutra': 'Buddha',
        'diamond that cuts': 'Thich Nhat Hanh',
        'essential tao': 'Laozi/Zhuangzi',
        'tao of philosophy': 'Alan Watts',
        'taoism reader': 'Various',
        'zen reader': 'Various Zen Masters',
        'zen mind': 'Shunryu Suzuki',
        'zen bow': 'Eugen Herrigel',
        'zen in the art': 'Eugen Herrigel',
        'zen teaching': 'Hui Hai',
        'instantaneous awakening': 'Hui Hai',
        'rumi': 'Jalal ad-Din Rumi'
    }
    
    title_lower = title.lower()
    for key, author in author_mapping.items():
        if key in title_lower:
            return author
    
    return "Unknown Eastern Author"

def convert_eastern_texts():
    """Convert priority Eastern texts to Chamber format"""
    
    print("🌏 CONVERTING EASTERN PHILOSOPHICAL TEXTS")
    print("=" * 55)
    
    # Get texts to convert
    eastern_texts = get_eastern_texts_to_convert()
    
    if not eastern_texts:
        print("❌ No Eastern texts found to convert")
        return
    
    print(f"\n📚 Converting {len(eastern_texts)} Eastern philosophical works...")
    print()
    
    output_dir = Path("converted_texts")
    output_dir.mkdir(exist_ok=True)
    
    successful_conversions = []
    failed_conversions = []
    
    for i, epub_path in enumerate(eastern_texts, 1):
        title = epub_path.stem
        author = determine_eastern_author(title)
        voice = map_eastern_text_to_voice(title)
        
        print(f"[{i}/{len(eastern_texts)}] 🎭 {voice}")
        print(f"           📖 {title}")
        print(f"           ✍️  {author}")
        
        try:
            # Convert using existing EPUB conversion function
            success = convert_epub_to_markdown(epub_path, output_dir)
            
            if success:
                successful_conversions.append({
                    'title': title,
                    'author': author, 
                    'voice': voice,
                    'path': epub_path
                })
                print(f"           ✅ Conversion successful")
                print(f"           🎭 {voice} voice ACTIVATED")
            else:
                failed_conversions.append({
                    'title': title,
                    'path': epub_path,
                    'error': 'Conversion failed'
                })
                print(f"           ❌ Conversion failed")
                
        except Exception as e:
            failed_conversions.append({
                'title': title,
                'path': epub_path,
                'error': str(e)
            })
            print(f"           ❌ Error: {str(e)[:50]}")
        
        print()
    
    # Summary
    print("📊 EASTERN CONVERSION RESULTS:")
    print(f"✅ Successfully converted: {len(successful_conversions)} texts")
    print(f"❌ Failed conversions: {len(failed_conversions)} texts")
    print()
    
    if successful_conversions:
        print("🎭 NEWLY ACTIVATED EASTERN VOICES:")
        voice_counts = {}
        for conv in successful_conversions:
            voice = conv['voice']
            voice_counts[voice] = voice_counts.get(voice, 0) + 1
        
        for voice, count in voice_counts.items():
            texts = [c['title'] for c in successful_conversions if c['voice'] == voice]
            print(f"   • {voice}: {count} text{'s' if count > 1 else ''}")
            for text in texts[:2]:  # Show first 2 texts
                print(f"     - {text[:60]}...")
            if len(texts) > 2:
                print(f"     - (+{len(texts)-2} more)")
        print()
        
        print("🏛️ CHAMBER ENHANCEMENT:")
        print(f"   • Eastern wisdom texts: +{len(successful_conversions)}")
        print(f"   • Buddhist tradition: Enhanced") 
        print(f"   • Taoist tradition: Enhanced")
        print(f"   • Zen tradition: Established")
        print(f"   • Sufi tradition: Added")
        print()
        
        print("🌉 NEW DIALECTICAL POSSIBILITIES:")
        print("   • Buddha ↔ Weil: Suffering and attention")
        print("   • Rumi ↔ Levinas: Love and infinity") 
        print("   • Shunryu Suzuki ↔ Bachelard: Beginner's mind and wonder")
        print("   • Hui Hai ↔ Benjamin: Instantaneous awakening and experience")
        print()
    
    if failed_conversions:
        print("❌ CONVERSION FAILURES (manual processing needed):")
        for failure in failed_conversions:
            print(f"   • {failure['title']}: {failure['error']}")
        print()
    
    print("📋 NEXT STEPS:")
    print("   1. Run: python3 chamber_amphitheater_status.py")
    print("   2. Test Eastern-Western voice integration")
    print("   3. Clean up source folder if desired")
    
    return len(successful_conversions)

if __name__ == "__main__":
    print("🌏 EASTERN TEXTS CHAMBER INTEGRATION")
    print("=" * 50)
    print("Converting critical Eastern philosophical works from assembled folder")
    print()
    
    converted_count = convert_eastern_texts()
    
    print(f"\n✨ Eastern integration complete!")
    print(f"🎭 {converted_count} new Eastern voices activated for the Chamber")
    print(f"🌍 The Chamber now approaches true global philosophical representation")