#!/usr/bin/env python3
"""
Convert Mythology & Buddhist Priority Works
Core Buddhist discourses, mythological foundations, and essential Chamber voices
"""

import subprocess
from pathlib import Path
import tempfile
from convert_directory_epubs import convert_directory_epub_to_markdown

def convert_mythology_buddhist_priority():
    """Convert highest priority mythology and Buddhist works"""
    
    print("🏛️ CONVERTING MYTHOLOGY & BUDDHIST PRIORITY WORKS")
    print("=" * 60)
    print("Complete Buddhist discourses + mythological foundations")
    print()
    
    myth_buddha_folder = Path("/Users/davidglidden/Desktop/Myth:Buddha")
    output_dir = Path("converted_texts")
    output_dir.mkdir(exist_ok=True)
    
    # Highest priority works - Buddhist discourses and core mythology
    priority_works = [
        # COMPLETE BUDDHIST DISCOURSE COLLECTION
        {
            'filename': 'The Connected Discourses of the Buddha: A Translation of the Samyutta Nikaya.epub',
            'author': 'Buddha',
            'voice': 'Buddha',
            'work': 'Samyutta Nikaya (Connected Discourses)',
            'role': 'Complete Teaching Collection',
            'impact': 'Core Buddhist discourse collection - Samyutta Nikaya',
            'priority': 'CRITICAL'
        },
        {
            'filename': 'The Long Discourses of the Buddha.epub',
            'author': 'Buddha', 
            'voice': 'Buddha',
            'work': 'Digha Nikaya (Long Discourses)',
            'role': 'Extended Teaching Collection',
            'impact': 'Core Buddhist discourse collection - Digha Nikaya',
            'priority': 'CRITICAL'
        },
        {
            'filename': 'The Middle Length Discourses of the Buddha: A Translation of the Majjhima Nikaya.epub',
            'author': 'Buddha',
            'voice': 'Buddha', 
            'work': 'Majjhima Nikaya (Middle Length Discourses)',
            'role': 'Balanced Teaching Collection',
            'impact': 'Core Buddhist discourse collection - Majjhima Nikaya',
            'priority': 'CRITICAL'
        },
        {
            'filename': 'The Numerical Discourses of the Buddha.epub',
            'author': 'Buddha',
            'voice': 'Buddha',
            'work': 'Anguttara Nikaya (Numerical Discourses)', 
            'role': 'Systematic Teaching Collection',
            'impact': 'Core Buddhist discourse collection - Anguttara Nikaya',
            'priority': 'CRITICAL'
        },
        {
            'filename': 'Diamond Sutra.epub',
            'author': 'Buddha',
            'voice': 'Buddha',
            'work': 'Diamond Sutra',
            'role': 'Perfection of Wisdom Teacher',
            'impact': 'Essential Prajnaparamita wisdom text',
            'priority': 'CRITICAL'
        },
        {
            'filename': 'The Heart of Understanding: Commentaries on the Prajnaparamita Heart Sutra.epub',
            'author': 'Thich Nhat Hanh',
            'voice': 'Thich Nhat Hanh',
            'work': 'Heart of Understanding',
            'role': 'Contemporary Buddhist Teacher',
            'impact': 'Modern interpretation of Heart Sutra',
            'priority': 'HIGH'
        },
        
        # GREEK MYTHOLOGICAL FOUNDATIONS
        {
            'filename': 'Homère.epub',
            'author': 'Homer',
            'voice': 'Homer',
            'work': 'Complete Works',
            'role': 'Epic Foundation Poet',
            'impact': 'Complete Homeric corpus - Iliad & Odyssey',
            'priority': 'CRITICAL'
        },
        {
            'filename': 'Les Métamorphoses.epub',
            'author': 'Ovid',
            'voice': 'Ovid',
            'work': 'Metamorphoses',
            'role': 'Transformation Mythographer',
            'impact': 'Essential transformation mythology',
            'priority': 'CRITICAL'
        },
        {
            'filename': 'Théogonie.epub',
            'author': 'Hesiod',
            'voice': 'Hesiod',
            'work': 'Theogony',
            'role': 'Cosmogonic Poet',
            'impact': 'Greek creation mythology and genealogy of gods',
            'priority': 'CRITICAL'
        },
        {
            'filename': 'The Oresteia: Agamemnon; The Libation Bearers; The Eumenides.epub',
            'author': 'Aeschylus',
            'voice': 'Aeschylus',
            'work': 'The Oresteia',
            'role': 'Tragic Justice Dramatist',
            'impact': 'Foundation trilogy of Greek tragedy',
            'priority': 'HIGH'
        },
        
        # STRUCTURAL ANTHROPOLOGY - LÉVI-STRAUSS MYTHOLOGIQUES
        {
            'filename': 'La pensée sauvage.epub',
            'author': 'Claude Lévi-Strauss',
            'voice': 'Claude Lévi-Strauss',
            'work': 'The Savage Mind',
            'role': 'Structural Anthropologist',
            'impact': 'Structural analysis of mythical thought',
            'priority': 'CRITICAL'
        },
        {
            'filename': 'Mythologiques 1 : Le cru et le cuit.epub',
            'author': 'Claude Lévi-Strauss',
            'voice': 'Claude Lévi-Strauss',
            'work': 'Mythologiques 1: The Raw and the Cooked',
            'role': 'Myth Structure Analyst',
            'impact': 'First volume of mythological structural analysis',
            'priority': 'CRITICAL'
        },
        {
            'filename': 'Mythologiques 2 : Du miel aux cendres.epub',
            'author': 'Claude Lévi-Strauss',
            'voice': 'Claude Lévi-Strauss',
            'work': 'Mythologiques 2: From Honey to Ashes',
            'role': 'Myth Structure Analyst',
            'impact': 'Second volume of mythological structural analysis',
            'priority': 'CRITICAL'
        },
        
        # NORSE MYTHOLOGY
        {
            'filename': 'Norse Mythology.epub',
            'author': 'Neil Gaiman',
            'voice': 'Neil Gaiman',
            'work': 'Norse Mythology',
            'role': 'Contemporary Mythologist',
            'impact': 'Norse mythological framework',
            'priority': 'HIGH'
        },
        
        # ARCHETYPAL PSYCHOLOGY
        {
            'filename': 'The Great Mother: An Analysis of the Archetype.epub',
            'author': 'Erich Neumann',
            'voice': 'Erich Neumann',
            'work': 'The Great Mother',
            'role': 'Archetypal Analyst',
            'impact': 'Jungian analysis of Great Mother archetype',
            'priority': 'HIGH'
        }
    ]
    
    successful = 0
    failed = 0
    
    print(f"🎯 CONVERTING {len(priority_works)} PRIORITY WORKS")
    print()
    
    for i, work_info in enumerate(priority_works, 1):
        file_path = myth_buddha_folder / work_info['filename']
        
        if not file_path.exists():
            print(f"[{i}/{len(priority_works)}] ❌ Not found: {work_info['filename']}")
            failed += 1
            continue
        
        print(f"[{i}/{len(priority_works)}] {work_info['priority']} 🏛️ {work_info['voice']}")
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
                
                # Special announcements for major voice activations
                if work_info['voice'] == 'Buddha' and 'Nikaya' in work_info['work']:
                    print(f"           🧘 MAJOR: Buddhist discourse collection enhanced!")
                elif work_info['voice'] == 'Homer':
                    print(f"           📜 MAJOR: Complete Homeric epic corpus!")
                elif work_info['voice'] == 'Claude Lévi-Strauss':
                    print(f"           🏗️ MAJOR: Structural anthropology framework!")
                elif work_info['voice'] == 'Ovid':
                    print(f"           🦋 MAJOR: Transformation mythology activated!")
                elif work_info['voice'] == 'Hesiod':
                    print(f"           🌌 MAJOR: Cosmogonic foundation established!")
                
            else:
                failed += 1
                print(f"           ❌ Conversion failed")
                
        except Exception as e:
            failed += 1
            print(f"           ❌ Error: {str(e)[:80]}")
        
        print()
    
    print("🏛️ MYTHOLOGY & BUDDHIST PRIORITY CONVERSION RESULTS:")
    print(f"✅ Successfully converted: {successful} works")
    print(f"❌ Failed conversions: {failed} works")
    
    if successful > 0:
        print(f"\n🎭 CHAMBER MAJOR ENHANCEMENTS:")
        print(f"   🧘 COMPLETE BUDDHIST DISCOURSE: Four Nikayas + Diamond Sutra")
        print(f"   📜 GREEK MYTHOLOGICAL FOUNDATION: Homer, Ovid, Hesiod, Aeschylus")
        print(f"   🏗️ STRUCTURAL ANTHROPOLOGY: Lévi-Strauss mythological analysis")
        print(f"   🗡️ NORSE MYTHOLOGY: Northern European archetypal framework")
        print(f"   🌟 ARCHETYPAL PSYCHOLOGY: Great Mother archetype")
        print()
        
        print("🌉 NEW CHAMBER MYTHOLOGICAL CAPABILITIES:")
        print("   • Buddha ↔ All voices: Complete discourse collection for Buddhist perspective")
        print("   • Homer ↔ Virgil: Epic tradition synthesis")
        print("   • Ovid ↔ Jung: Transformation mythology and psychology")
        print("   • Lévi-Strauss ↔ Myth voices: Structural analysis of all mythological content")
        print("   • Aeschylus ↔ Tragedy voices: Foundation of dramatic conflict")
        print("   • Norse mythology ↔ Greek: Comparative mythological frameworks")
    
    return successful

if __name__ == "__main__":
    print("🏛️ MYTHOLOGY & BUDDHIST PRIORITY CONVERSION")
    print("=" * 60)
    print("Converting core Buddhist discourses and mythological foundations")
    print()
    
    converted_count = convert_mythology_buddhist_priority()
    
    print(f"\n✨ Priority mythology & Buddhist conversion complete!")
    print(f"🎭 {converted_count} critical voices activated")
    print(f"🏛️ Chamber now has comprehensive mythological and Buddhist foundations!")