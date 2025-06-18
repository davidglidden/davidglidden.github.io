#!/usr/bin/env python3
"""
Convert Mythological Foundations
Greek mythological corpus - Homer, Ovid, Hesiod
"""

import subprocess
from pathlib import Path
import tempfile
from convert_directory_epubs import convert_directory_epub_to_markdown

def convert_mythology_foundations():
    """Convert core mythological foundation texts"""
    
    print("📜 CONVERTING MYTHOLOGICAL FOUNDATIONS")
    print("=" * 50)
    print("Greek mythological corpus - archetypal framework")
    print()
    
    myth_buddha_folder = Path("/Users/davidglidden/Desktop/Myth:Buddha")
    output_dir = Path("converted_texts")
    output_dir.mkdir(exist_ok=True)
    
    # Core mythological foundation works
    mythological_works = [
        {
            'filename': 'Homère.epub',
            'author': 'Homer',
            'voice': 'Homer',
            'work': 'Complete Works (Iliad & Odyssey)',
            'role': 'Epic Foundation Poet',
            'impact': 'Complete Homeric corpus'
        },
        {
            'filename': 'Les Métamorphoses.epub',
            'author': 'Ovid',
            'voice': 'Ovid',
            'work': 'Metamorphoses',
            'role': 'Transformation Mythographer',
            'impact': 'Essential transformation mythology'
        },
        {
            'filename': 'Théogonie.epub',
            'author': 'Hesiod',
            'voice': 'Hesiod',
            'work': 'Theogony',
            'role': 'Cosmogonic Poet',
            'impact': 'Greek creation mythology'
        },
        {
            'filename': 'The Oresteia: Agamemnon; The Libation Bearers; The Eumenides.epub',
            'author': 'Aeschylus',
            'voice': 'Aeschylus',
            'work': 'The Oresteia',
            'role': 'Tragic Justice Dramatist',
            'impact': 'Foundation trilogy of Greek tragedy'
        },
        {
            'filename': 'Norse Mythology.epub',
            'author': 'Neil Gaiman',
            'voice': 'Neil Gaiman',
            'work': 'Norse Mythology',
            'role': 'Contemporary Mythologist',
            'impact': 'Norse mythological framework'
        }
    ]
    
    successful = 0
    failed = 0
    
    print(f"🎯 CONVERTING {len(mythological_works)} MYTHOLOGICAL WORKS")
    print()
    
    for i, work_info in enumerate(mythological_works, 1):
        file_path = myth_buddha_folder / work_info['filename']
        
        if not file_path.exists():
            print(f"[{i}/{len(mythological_works)}] ❌ Not found: {work_info['filename']}")
            failed += 1
            continue
        
        print(f"[{i}/{len(mythological_works)}] 📜 {work_info['voice']}")
        print(f"           📖 {work_info['work']}")
        print(f"           🎭 {work_info['role']}")
        print(f"           ⚡ {work_info['impact']}")
        
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                success = convert_directory_epub_to_markdown(file_path, output_dir, Path(temp_dir))
            
            if success:
                successful += 1
                print(f"           ✅ Conversion successful")
                print(f"           🎭 {work_info['voice']} voice ACTIVATED")
                
                if work_info['voice'] == 'Homer':
                    print(f"           📜 MAJOR: Complete Homeric epic corpus!")
                elif work_info['voice'] == 'Ovid':
                    print(f"           🦋 MAJOR: Transformation mythology activated!")
                elif work_info['voice'] == 'Hesiod':
                    print(f"           🌌 MAJOR: Cosmogonic foundation established!")
                elif work_info['voice'] == 'Aeschylus':
                    print(f"           🎭 MAJOR: Greek tragedy foundation!")
                elif work_info['voice'] == 'Neil Gaiman':
                    print(f"           🗡️ MAJOR: Norse mythology integrated!")
                
            else:
                failed += 1
                print(f"           ❌ Conversion failed")
                
        except Exception as e:
            failed += 1
            print(f"           ❌ Error: {str(e)[:80]}")
        
        print()
    
    print("📜 MYTHOLOGICAL FOUNDATIONS CONVERSION RESULTS:")
    print(f"✅ Successfully converted: {successful} works")
    print(f"❌ Failed conversions: {failed} works")
    
    if successful > 0:
        print(f"\n🎭 CHAMBER MYTHOLOGICAL ENHANCEMENT:")
        print(f"   📜 GREEK EPIC: Homer's complete corpus (Iliad & Odyssey)")
        print(f"   🦋 TRANSFORMATION: Ovid's metamorphosis mythology")
        print(f"   🌌 COSMOGONY: Hesiod's creation and divine genealogy")
        print(f"   🎭 TRAGEDY: Aeschylus' Oresteia justice cycle")
        print(f"   🗡️ NORSE: Northern European mythological framework")
        print()
        
        print("🌉 CHAMBER ARCHETYPAL CAPABILITIES:")
        print("   • Homer ↔ All epic voices: Foundation epic references")
        print("   • Ovid ↔ Jung: Transformation mythology and psychology")
        print("   • Hesiod ↔ Creation voices: Cosmogonic frameworks")
        print("   • Aeschylus ↔ Drama voices: Tragic conflict patterns")
        print("   • Norse ↔ Greek mythology: Comparative archetypal systems")
        print("   • Complete mythological reference system for all Chamber voices")
    
    return successful

if __name__ == "__main__":
    converted_count = convert_mythology_foundations()
    print(f"\n✨ Mythological foundations conversion complete!")
    print(f"📜 {converted_count} mythological voices activated")
    print(f"🏛️ Chamber now has comprehensive archetypal foundation!")