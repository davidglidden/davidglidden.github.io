#!/usr/bin/env python3
"""
Convert Key Philosophers
Nietzsche, Montaigne, Adorno - essential philosophical voices
"""

import subprocess
from pathlib import Path
import tempfile
from convert_directory_epubs import convert_directory_epub_to_markdown

def convert_key_philosophers():
    """Convert key philosophical voices"""
    
    print("💭 CONVERTING KEY PHILOSOPHERS")
    print("=" * 40)
    print("Nietzsche, Montaigne, Adorno - philosophical essentials")
    print()
    
    eastern_folder = Path("/Users/davidglidden/Desktop/eastern to the library")
    output_dir = Path("converted_texts")
    output_dir.mkdir(exist_ok=True)
    
    # Key philosophical works
    philosophical_works = [
        {
            'filename': 'Nietzsche.epub',
            'author': 'Friedrich Nietzsche',
            'voice': 'Friedrich Nietzsche',
            'work': 'Nietzsche (Works)',
            'role': 'Philosopher of Will to Power',
            'impact': 'Will to power and critique of values'
        },
        {
            'filename': 'Montaigne.epub',
            'author': 'Michel de Montaigne',
            'voice': 'Michel de Montaigne',
            'work': 'Montaigne (Essays)',
            'role': 'Skeptical Essayist of the Self',
            'impact': 'Skeptical self-examination and essay form'
        },
        {
            'filename': 'Minima Moralia: Reflections From Damaged Life.epub',
            'author': 'Theodor Adorno',
            'voice': 'Theodor Adorno',
            'work': 'Minima Moralia',
            'role': 'Critical Theorist of Damaged Life',
            'impact': 'Frankfurt School critical theory'
        },
        {
            'filename': 'Écrits.epub',
            'author': 'Jacques Lacan',
            'voice': 'Jacques Lacan',
            'work': 'Écrits',
            'role': 'Structural Psychoanalyst',
            'impact': 'Structural unconscious theory'
        }
    ]
    
    successful = 0
    failed = 0
    
    for i, work_info in enumerate(philosophical_works, 1):
        file_path = eastern_folder / work_info['filename']
        
        if not file_path.exists():
            print(f"[{i}/{len(philosophical_works)}] ❌ Not found: {work_info['filename']}")
            failed += 1
            continue
        
        print(f"[{i}/{len(philosophical_works)}] 💭 {work_info['voice']}")
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
                
                if work_info['voice'] == 'Friedrich Nietzsche':
                    print(f"           ⚡ MAJOR: Will to power philosophy integrated!")
                elif work_info['voice'] == 'Michel de Montaigne':
                    print(f"           📝 MAJOR: Skeptical essay tradition established!")
                elif work_info['voice'] == 'Theodor Adorno':
                    print(f"           🔥 MAJOR: Critical theory foundation activated!")
                elif work_info['voice'] == 'Jacques Lacan':
                    print(f"           🧠 MAJOR: Structural psychoanalysis integrated!")
                
            else:
                failed += 1
                print(f"           ❌ Conversion failed")
                
        except Exception as e:
            failed += 1
            print(f"           ❌ Error: {str(e)[:50]}")
        
        print()
    
    print("💭 PHILOSOPHICAL CONVERSION RESULTS:")
    print(f"✅ Successfully converted: {successful} works")
    print(f"❌ Failed conversions: {failed} works")
    
    if successful > 0:
        print(f"\n🎭 PHILOSOPHICAL TRANSFORMATION:")
        print(f"   ⚡ Nietzschean critique: Will to power and value critique")
        print(f"   📝 Skeptical tradition: Montaigne's self-examination")
        print(f"   🔥 Critical theory: Adorno's damaged life analysis")
        print(f"   🧠 Structural analysis: Lacanian unconscious")
        print()
        
        print("🌉 NEW CHAMBER PHILOSOPHICAL CAPABILITIES:")
        print("   • Nietzsche ↔ Weil: Will to power vs decreation")
        print("   • Montaigne ↔ All voices: Skeptical self-examination")
        print("   • Adorno ↔ Benjamin: Critical theory synthesis")
        print("   • Lacan ↔ Jung: Structural vs archetypal unconscious")
    
    return successful

if __name__ == "__main__":
    print("💭 KEY PHILOSOPHERS CONVERSION")
    print("=" * 40)
    print("Converting essential philosophical voices")
    print()
    
    converted_count = convert_key_philosophers()
    
    print(f"\n✨ Key philosophers conversion complete!")
    print(f"🎭 {converted_count} philosophical voices activated")
    print(f"💭 Chamber philosophical foundations significantly enhanced!")