#!/usr/bin/env python3
"""
Convert Priority Eastern Texts from Directory EPUBs
Focus on the most critical Eastern philosophical works first
"""

import subprocess
from pathlib import Path
import tempfile
import zipfile
import shutil
from convert_directory_epubs import convert_directory_epub_to_markdown

def convert_priority_eastern_texts():
    """Convert the most critical Eastern texts first"""
    
    print("🌏 CONVERTING PRIORITY EASTERN TEXTS")
    print("=" * 50)
    
    eastern_folder = Path("/Users/davidglidden/Desktop/eastern to the library")
    output_dir = Path("converted_texts")
    output_dir.mkdir(exist_ok=True)
    
    # Most critical Eastern texts for Chamber
    priority_texts = [
        "Diamond Sutra.epub",
        "Zen Mind, Beginner's Mind.epub", 
        "The Essential Tao An Initiation Into the Heart of Taoism Through the Authentic Tao Te Ching and the Inner Teachings of Chuang-Tzu.epub",
        "The Diamond That Cuts Through Illusion.epub",
        "Zen in the Art of Archery.epub"
    ]
    
    successful = 0
    failed = 0
    
    for i, text_name in enumerate(priority_texts, 1):
        epub_path = eastern_folder / text_name
        
        if not epub_path.exists():
            print(f"[{i}/{len(priority_texts)}] ❌ Not found: {text_name}")
            failed += 1
            continue
        
        print(f"[{i}/{len(priority_texts)}] 📚 Converting: {text_name}")
        
        try:
            # Use our directory EPUB converter with temp directory
            with tempfile.TemporaryDirectory() as temp_dir:
                success = convert_directory_epub_to_markdown(epub_path, output_dir, Path(temp_dir))
            
            if success:
                successful += 1
                print(f"   ✅ Successfully converted")
                
                # Determine voice activation
                if "diamond sutra" in text_name.lower():
                    print(f"   🎭 Buddha voice ACTIVATED")
                elif "zen mind" in text_name.lower():
                    print(f"   🎭 Shunryu Suzuki voice ACTIVATED")
                elif "essential tao" in text_name.lower():
                    print(f"   🎭 Laozi/Zhuangzi voices ENHANCED")
                elif "diamond that cuts" in text_name.lower():
                    print(f"   🎭 Thich Nhat Hanh voice ACTIVATED")
                elif "zen in the art" in text_name.lower():
                    print(f"   🎭 Eugen Herrigel voice ACTIVATED")
            else:
                failed += 1
                print(f"   ❌ Conversion failed")
                
        except Exception as e:
            failed += 1
            print(f"   ❌ Error: {str(e)[:50]}")
        
        print()
    
    print("📊 PRIORITY EASTERN CONVERSION RESULTS:")
    print(f"✅ Successfully converted: {successful} texts")
    print(f"❌ Failed conversions: {failed} texts")
    
    if successful > 0:
        print(f"\n🎭 CHAMBER ENHANCEMENT:")
        print(f"   • Buddhist wisdom: Diamond Sutra activated")
        print(f"   • Zen tradition: Beginner's Mind established") 
        print(f"   • Taoist synthesis: Essential Tao integrated")
        print(f"   • Engaged Buddhism: Thich Nhat Hanh active")
        print(f"   • Zen arts: Archery meditation included")
        print()
        
        print("🌉 NEW DIALECTICAL POSSIBILITIES:")
        print("   • Buddha ↔ Weil: Suffering and decreation")
        print("   • Shunryu Suzuki ↔ Bachelard: Beginner's mind and wonder")
        print("   • Thich Nhat Hanh ↔ Kimmerer: Interbeing and reciprocity")
        print("   • Eugen Herrigel ↔ Alexander: Zen arts and patterns")
        print()
        
        print("📋 NEXT STEPS:")
        print("   1. Run: python3 chamber_amphitheater_status.py")
        print("   2. Continue with remaining Eastern texts")
        print("   3. Test Eastern-Western voice integration")
    
    return successful

if __name__ == "__main__":
    print("🏹 PRIORITY EASTERN TEXTS CHAMBER INTEGRATION")
    print("=" * 55)
    print("Converting the most critical Eastern philosophical works first")
    print()
    
    converted_count = convert_priority_eastern_texts()
    
    print(f"\n✨ Priority Eastern integration complete!")
    print(f"🎭 {converted_count} critical Eastern voices activated")
    print(f"🌏 Chamber now has essential Buddhist and Taoist foundations")