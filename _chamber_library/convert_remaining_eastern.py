#!/usr/bin/env python3
"""
Convert Remaining Eastern Texts
Continue with the remaining valuable Eastern philosophical works
"""

import subprocess
from pathlib import Path
import tempfile
from convert_directory_epubs import convert_directory_epub_to_markdown

def convert_remaining_eastern_texts():
    """Convert the remaining Eastern texts"""
    
    print("🌸 CONVERTING REMAINING EASTERN TEXTS")
    print("=" * 45)
    
    eastern_folder = Path("/Users/davidglidden/Desktop/eastern to the library")
    output_dir = Path("converted_texts")
    output_dir.mkdir(exist_ok=True)
    
    # Remaining valuable Eastern texts
    remaining_texts = [
        "The Tao of Philosophy.epub",
        "The Taoism Reader.epub", 
        "The Zen Reader.epub",
        "Zen Bow, Zen Arrow.epub",
        "Zen Teaching of Instantaneous Awakening: being the teaching of the Zen Master Hui Hai, known as the Great Pearl.epub",
        "Collected Poetical Works of Rumi (Delphi Classics).epub",
        "Meditations: A New Translation.epub"
    ]
    
    successful = 0
    failed = 0
    
    for i, text_name in enumerate(remaining_texts, 1):
        epub_path = eastern_folder / text_name
        
        if not epub_path.exists():
            print(f"[{i}/{len(remaining_texts)}] ❌ Not found: {text_name}")
            failed += 1
            continue
        
        print(f"[{i}/{len(remaining_texts)}] 📚 Converting: {text_name[:50]}...")
        
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                success = convert_directory_epub_to_markdown(epub_path, output_dir, Path(temp_dir))
            
            if success:
                successful += 1
                print(f"   ✅ Successfully converted")
                
                # Determine voice activation
                if "tao of philosophy" in text_name.lower():
                    print(f"   🎭 Alan Watts voice ACTIVATED")
                elif "taoism reader" in text_name.lower():
                    print(f"   🎭 Taoist Sages anthology ACTIVATED")
                elif "zen reader" in text_name.lower():
                    print(f"   🎭 Zen Masters anthology ACTIVATED")
                elif "zen bow" in text_name.lower():
                    print(f"   🎭 Zen Arts tradition ENHANCED")
                elif "hui hai" in text_name.lower():
                    print(f"   🎭 Hui Hai voice ACTIVATED")
                elif "rumi" in text_name.lower():
                    print(f"   🎭 Rumi voice ACTIVATED")
                elif "meditations" in text_name.lower():
                    print(f"   🎭 Marcus Aurelius voice ACTIVATED")
                    
            else:
                failed += 1
                print(f"   ❌ Conversion failed")
                
        except Exception as e:
            failed += 1
            print(f"   ❌ Error: {str(e)[:50]}")
        
        print()
    
    print("📊 REMAINING EASTERN CONVERSION RESULTS:")
    print(f"✅ Successfully converted: {successful} texts")
    print(f"❌ Failed conversions: {failed} texts")
    
    if successful > 0:
        print(f"\n🎭 ADDITIONAL CHAMBER ENHANCEMENT:")
        print(f"   • Alan Watts: Eastern-Western bridge philosophy")
        print(f"   • Zen Masters: Classical Chan/Zen wisdom") 
        print(f"   • Hui Hai: Instantaneous awakening teaching")
        print(f"   • Rumi: Sufi mystical poetry")
        print(f"   • Stoic wisdom: Marcus Aurelius meditations")
        print()
        
        print("🌉 EXPANDED DIALECTICAL POSSIBILITIES:")
        print("   • Alan Watts ↔ Jung: Eastern psychology meets depth psychology")
        print("   • Rumi ↔ Levinas: Mystical love and infinite responsibility")
        print("   • Hui Hai ↔ Benjamin: Sudden awakening and shock experience") 
        print("   • Marcus Aurelius ↔ Weil: Stoic attention and spiritual practice")
        print()
        
        print("📋 NEXT STEPS:")
        print("   1. Run: python3 chamber_amphitheater_status.py")
        print("   2. Clean up eastern folder if desired")
        print("   3. Test enhanced Eastern-Western dialogues")
    
    return successful

if __name__ == "__main__":
    print("🌸 REMAINING EASTERN TEXTS CHAMBER INTEGRATION")
    print("=" * 55)
    print("Converting additional Eastern philosophical works")
    print()
    
    converted_count = convert_remaining_eastern_texts()
    
    print(f"\n✨ Remaining Eastern integration complete!")
    print(f"🎭 {converted_count} additional Eastern voices activated")
    print(f"🌏 Chamber Eastern collection significantly enhanced")