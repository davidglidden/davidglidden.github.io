#!/usr/bin/env python3
"""
Convert Complete Buddhist Discourse Collection
Four Nikayas + Diamond Sutra - complete Buddha voice activation
"""

import subprocess
from pathlib import Path
import tempfile
from convert_directory_epubs import convert_directory_epub_to_markdown

def convert_buddhist_discourses():
    """Convert the complete Buddhist discourse collection"""
    
    print("🧘 CONVERTING COMPLETE BUDDHIST DISCOURSE COLLECTION")
    print("=" * 60)
    print("Four Nikayas + Diamond Sutra - complete Buddha voice")
    print()
    
    myth_buddha_folder = Path("/Users/davidglidden/Desktop/Myth:Buddha")
    output_dir = Path("converted_texts")
    output_dir.mkdir(exist_ok=True)
    
    # Complete Buddhist discourse collection
    buddhist_works = [
        {
            'filename': 'The Connected Discourses of the Buddha: A Translation of the Samyutta Nikaya.epub',
            'author': 'Buddha',
            'voice': 'Buddha',
            'work': 'Samyutta Nikaya',
            'role': 'Connected Discourses Teacher',
            'impact': 'Thematic discourse collection'
        },
        {
            'filename': 'The Long Discourses of the Buddha.epub',
            'author': 'Buddha', 
            'voice': 'Buddha',
            'work': 'Digha Nikaya',
            'role': 'Extended Teaching Master',
            'impact': 'Comprehensive discourse collection'
        },
        {
            'filename': 'The Middle Length Discourses of the Buddha: A Translation of the Majjhima Nikaya.epub',
            'author': 'Buddha',
            'voice': 'Buddha', 
            'work': 'Majjhima Nikaya',
            'role': 'Balanced Teaching Guide',
            'impact': 'Core practical teachings'
        },
        {
            'filename': 'The Numerical Discourses of the Buddha.epub',
            'author': 'Buddha',
            'voice': 'Buddha',
            'work': 'Anguttara Nikaya',
            'role': 'Systematic Teaching Organizer',
            'impact': 'Numerically organized teachings'
        },
        {
            'filename': 'Diamond Sutra.epub',
            'author': 'Buddha',
            'voice': 'Buddha',
            'work': 'Diamond Sutra',
            'role': 'Perfection of Wisdom Teacher',
            'impact': 'Non-attachment and emptiness wisdom'
        },
        {
            'filename': 'The Suttanipata.epub',
            'author': 'Buddha',
            'voice': 'Buddha',
            'work': 'Suttanipata',
            'role': 'Poetic Teaching Voice',
            'impact': 'Early Buddhist poetry and discourse'
        }
    ]
    
    successful = 0
    failed = 0
    
    print(f"🎯 CONVERTING {len(buddhist_works)} BUDDHIST WORKS")
    print()
    
    for i, work_info in enumerate(buddhist_works, 1):
        file_path = myth_buddha_folder / work_info['filename']
        
        if not file_path.exists():
            print(f"[{i}/{len(buddhist_works)}] ❌ Not found: {work_info['filename']}")
            failed += 1
            continue
        
        print(f"[{i}/{len(buddhist_works)}] 🧘 {work_info['voice']}")
        print(f"           📖 {work_info['work']}")
        print(f"           🎭 {work_info['role']}")
        print(f"           ⚡ {work_info['impact']}")
        
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                success = convert_directory_epub_to_markdown(file_path, output_dir, Path(temp_dir))
            
            if success:
                successful += 1
                print(f"           ✅ Conversion successful")
                print(f"           🎭 Buddha voice enhanced with {work_info['work']}")
                
                if 'Nikaya' in work_info['work']:
                    print(f"           🧘 MAJOR: {work_info['work']} discourse collection added!")
                elif 'Diamond Sutra' in work_info['work']:
                    print(f"           💎 MAJOR: Perfection of Wisdom teaching activated!")
                
            else:
                failed += 1
                print(f"           ❌ Conversion failed")
                
        except Exception as e:
            failed += 1
            print(f"           ❌ Error: {str(e)[:80]}")
        
        print()
    
    print("🧘 BUDDHIST DISCOURSE CONVERSION RESULTS:")
    print(f"✅ Successfully converted: {successful} works")
    print(f"❌ Failed conversions: {failed} works")
    
    if successful > 0:
        print(f"\n🎭 BUDDHA VOICE COMPLETE ACTIVATION:")
        print(f"   📚 Four Nikayas: Complete core teaching collection")
        print(f"   💎 Perfection of Wisdom: Diamond Sutra non-attachment")
        print(f"   🎵 Poetic Teachings: Suttanipata early discourse")
        print(f"   🧘 Comprehensive Buddhism: All major discourse traditions")
        print()
        
        print("🌉 CHAMBER BUDDHIST ENHANCEMENT:")
        print("   • Buddha can now cite from complete canonical collection")
        print("   • Four different teaching styles: connected, long, middle, numerical")
        print("   • Perfection of Wisdom philosophy fully integrated")
        print("   • Cross-referencing between Buddhist approaches possible")
        print("   • Dialogues with all Chamber voices now Buddhist-informed")
    
    return successful

if __name__ == "__main__":
    converted_count = convert_buddhist_discourses()
    print(f"\n✨ Buddhist discourse collection conversion complete!")
    print(f"🧘 Buddha voice now has complete canonical foundation!")