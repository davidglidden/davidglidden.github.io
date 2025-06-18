#!/usr/bin/env python3
"""
Convert Epic and Literary Foundations
Homer, Shakespeare, Joyce - the core of Western literary tradition
"""

import subprocess
from pathlib import Path
import tempfile
from convert_directory_epubs import convert_directory_epub_to_markdown

def convert_epic_foundations():
    """Convert the epic and literary foundations"""
    
    print("📜 CONVERTING EPIC & LITERARY FOUNDATIONS")
    print("=" * 55)
    print("Homer, Shakespeare, Joyce - Western literary core")
    print()
    
    eastern_folder = Path("/Users/davidglidden/Desktop/eastern to the library")
    output_dir = Path("converted_texts")
    output_dir.mkdir(exist_ok=True)
    
    # Epic and literary foundations
    literary_foundations = [
        {
            'filename': 'The Iliad (Robert Fagles).epub',
            'author': 'Homer',
            'voice': 'Homer',
            'work': 'The Iliad',
            'role': 'Epic War Poet',
            'impact': 'Western epic tradition foundation'
        },
        {
            'filename': 'The Odyssey.epub',
            'author': 'Homer',
            'voice': 'Homer',
            'work': 'The Odyssey',
            'role': 'Epic Journey Poet',
            'impact': 'Journey archetype and heroic quest'
        },
        {
            'filename': 'The Arden Shakespeare Third Series Complete Works.epub',
            'author': 'William Shakespeare',
            'voice': 'William Shakespeare',
            'work': 'The Complete Works',
            'role': 'Complete Dramatic Genius',
            'impact': 'English literature foundation and dramatic archetypes'
        },
        {
            'filename': 'Ulysses.epub',
            'author': 'James Joyce',
            'voice': 'James Joyce',
            'work': 'Ulysses',
            'role': 'Stream of Consciousness Innovator',
            'impact': 'Modernist consciousness and narrative technique'
        }
    ]
    
    successful = 0
    failed = 0
    
    for i, work_info in enumerate(literary_foundations, 1):
        file_path = eastern_folder / work_info['filename']
        
        if not file_path.exists():
            print(f"[{i}/{len(literary_foundations)}] ❌ Not found: {work_info['filename']}")
            failed += 1
            continue
        
        print(f"[{i}/{len(literary_foundations)}] 📜 {work_info['voice']}")
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
                
                if work_info['voice'] == 'Homer':
                    if 'iliad' in work_info['work'].lower():
                        print(f"           ⚔️ EPIC: War and heroic rage activated!")
                    else:
                        print(f"           🌊 EPIC: Journey and return activated!")
                elif work_info['voice'] == 'William Shakespeare':
                    print(f"           🎭 MASSIVE: Complete Shakespeare integrated!")
                elif work_info['voice'] == 'James Joyce':
                    print(f"           🌊 MODERNIST: Stream of consciousness activated!")
                
            else:
                failed += 1
                print(f"           ❌ Conversion failed")
                
        except Exception as e:
            failed += 1
            print(f"           ❌ Error: {str(e)[:50]}")
        
        print()
    
    print("📜 EPIC & LITERARY CONVERSION RESULTS:")
    print(f"✅ Successfully converted: {successful} works")
    print(f"❌ Failed conversions: {failed} works")
    
    if successful > 0:
        print(f"\n🎭 LITERARY FOUNDATION TRANSFORMATION:")
        print(f"   📜 Epic tradition: Homer's Iliad and Odyssey")
        print(f"   🎭 Dramatic tradition: Shakespeare complete works")
        print(f"   🌊 Modernist consciousness: Joyce's stream technique")
        print(f"   🏛️ Western literary canon: Foundational texts established")
        print()
        
        print("🌉 NEW CHAMBER LITERARY CAPABILITIES:")
        print("   • Homer ↔ Benjamin: Epic storytelling vs fragmented modernity")
        print("   • Shakespeare ↔ All voices: Dramatic archetypes and references")
        print("   • Joyce ↔ Bachelard: Stream consciousness vs spatial imagination")
        print("   • Literary references: Chamber can now cite canonical literature")
    
    return successful

if __name__ == "__main__":
    print("📜 EPIC & LITERARY FOUNDATIONS CONVERSION")
    print("=" * 55)
    print("Converting Homer, Shakespeare, Joyce - Western literary core")
    print()
    
    converted_count = convert_epic_foundations()
    
    print(f"\n✨ Epic & literary foundation conversion complete!")
    print(f"🎭 {converted_count} literary giants activated")
    print(f"📜 Chamber now has foundational Western literary tradition!")