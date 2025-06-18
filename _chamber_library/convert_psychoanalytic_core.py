#!/usr/bin/env python3
"""
Convert Psychoanalytic Core
Lacan and Jung - structural and archetypal unconscious
"""

import subprocess
from pathlib import Path
import tempfile
from convert_directory_epubs import convert_directory_epub_to_markdown

def convert_psychoanalytic_core():
    """Convert the psychoanalytic foundations"""
    
    print("🧠 CONVERTING PSYCHOANALYTIC CORE")
    print("=" * 45)
    print("Lacan and Jung - unconscious foundations")
    print()
    
    eastern_folder = Path("/Users/davidglidden/Desktop/eastern to the library")
    output_dir = Path("converted_texts")
    output_dir.mkdir(exist_ok=True)
    
    # Psychoanalytic core works
    psychoanalytic_works = [
        {
            'filename': 'Écrits.epub',
            'author': 'Jacques Lacan',
            'voice': 'Jacques Lacan',
            'work': 'Écrits',
            'role': 'Structural Psychoanalyst of the Unconscious',
            'impact': 'Structural unconscious and language theory'
        },
        {
            'filename': 'The Collected Works of C.G. Jung: Complete Digital Edition.epub',
            'author': 'Carl Jung',
            'voice': 'Carl Jung',
            'work': 'The Collected Works (Complete Digital Edition)',
            'role': 'Complete Depth Psychologist',
            'impact': 'Archetypal psychology and collective unconscious'
        }
    ]
    
    successful = 0
    failed = 0
    
    for i, work_info in enumerate(psychoanalytic_works, 1):
        file_path = eastern_folder / work_info['filename']
        
        if not file_path.exists():
            print(f"[{i}/{len(psychoanalytic_works)}] ❌ Not found: {work_info['filename']}")
            failed += 1
            continue
        
        print(f"[{i}/{len(psychoanalytic_works)}] 🧠 {work_info['voice']}")
        print(f"           📖 {work_info['work']}")
        print(f"           🎪 {work_info['role']}")
        print(f"           ⚡ {work_info['impact']}")
        
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                success = convert_directory_epub_to_markdown(file_path, output_dir, Path(temp_dir))
            
            if success:
                successful += 1
                print(f"           ✅ Conversion successful")
                print(f"           🎭 {work_info['voice']} voice ACTIVATED")
                
                if work_info['voice'] == 'Jacques Lacan':
                    print(f"           🧠 MAJOR: Structural psychoanalysis integrated!")
                elif work_info['voice'] == 'Carl Jung':
                    print(f"           🌟 MAJOR: Complete Jung activated!")
                
            else:
                failed += 1
                print(f"           ❌ Conversion failed")
                
        except Exception as e:
            failed += 1
            print(f"           ❌ Error: {str(e)[:50]}")
        
        print()
    
    print("🧠 PSYCHOANALYTIC CONVERSION RESULTS:")
    print(f"✅ Successfully converted: {successful} works")
    print(f"❌ Failed conversions: {failed} works")
    
    if successful > 0:
        print(f"\n🎭 PSYCHOANALYTIC TRANSFORMATION:")
        print(f"   🧠 Structural unconscious: Lacan's language theory")
        print(f"   🌟 Archetypal psychology: Jung's collective unconscious")
        print(f"   💭 Psychoanalytic synthesis: Structural + Archetypal")
        print(f"   🏛️ Depth psychology: Complete foundation")
        print()
        
        print("🌉 NEW CHAMBER PSYCHOANALYTIC CAPABILITIES:")
        print("   • Lacan ↔ Jung: Structural vs archetypal unconscious")
        print("   • Lacan ↔ Levinas: Language and the Other")
        print("   • Jung ↔ Weil: Archetypal vs mystical psychology")
        print("   • Psychoanalytic reading: All voices can reference unconscious dynamics")
    
    return successful

if __name__ == "__main__":
    print("🧠 PSYCHOANALYTIC CORE CONVERSION")
    print("=" * 45)
    print("Converting Lacan and Jung - unconscious foundations")
    print()
    
    converted_count = convert_psychoanalytic_core()
    
    print(f"\n✨ Psychoanalytic core conversion complete!")
    print(f"🎭 {converted_count} psychoanalytic voices activated")
    print(f"🧠 Chamber now has deep psychological foundations!")