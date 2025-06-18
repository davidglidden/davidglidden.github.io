#!/usr/bin/env python3
"""
Convert Essential Philosophy & Poetry
Key philosophical and poetic voices from the mythology/Buddhist collection
"""

import subprocess
from pathlib import Path
import tempfile
from convert_directory_epubs import convert_directory_epub_to_markdown

def convert_essential_philosophy():
    """Convert essential philosophical and poetic works"""
    
    print("💭 CONVERTING ESSENTIAL PHILOSOPHY & POETRY")
    print("=" * 55)
    print("Key philosophical voices and poetic traditions")
    print()
    
    myth_buddha_folder = Path("/Users/davidglidden/Desktop/Myth:Buddha")
    output_dir = Path("converted_texts")
    output_dir.mkdir(exist_ok=True)
    
    # Essential philosophical and poetic works
    essential_works = [
        # PLATONIC FOUNDATION
        {
            'filename': 'The Republic of Plato.epub',
            'author': 'Plato',
            'voice': 'Plato',
            'work': 'The Republic',
            'role': 'Philosopher of Justice and Forms',
            'impact': 'Foundation of political philosophy'
        },
        {
            'filename': 'The Trial and Death of Socrates (Third Edition): Euthyphro, Apology, Crito, Death Scene From Phaedo.epub',
            'author': 'Socrates/Plato',
            'voice': 'Socrates',
            'work': 'Trial and Death Collection',
            'role': 'Gadfly Philosopher',
            'impact': 'Socratic method and philosophical martyrdom'
        },
        
        # STOIC PHILOSOPHY
        {
            'filename': 'The Art of Living: The Classical Mannual on Virtue, Happiness, and Effectiveness.epub',
            'author': 'Epictetus',
            'voice': 'Epictetus',
            'work': 'The Art of Living',
            'role': 'Stoic Ethics Teacher',
            'impact': 'Practical stoic philosophy'
        },
        {
            'filename': 'The Consolation of Philosophy.epub',
            'author': 'Boethius',
            'voice': 'Boethius',
            'work': 'The Consolation of Philosophy',
            'role': 'Christian Philosopher',
            'impact': 'Medieval synthesis of classical and Christian thought'
        },
        
        # POETRY COLLECTIONS
        {
            'filename': 'John Donne: Collected Poetry.epub',
            'author': 'John Donne',
            'voice': 'John Donne',
            'work': 'Collected Poetry',
            'role': 'Metaphysical Poet',
            'impact': 'Metaphysical poetry and divine love'
        },
        {
            'filename': 'Les Fleurs du Mal.epub',
            'author': 'Charles Baudelaire',
            'voice': 'Charles Baudelaire',
            'work': 'Les Fleurs du Mal',
            'role': 'Symbolist Poet of Beauty and Decay',
            'impact': 'Modernist poetry and aesthetic theory'
        },
        
        # ARCHETYPAL PSYCHOLOGY
        {
            'filename': 'The Great Mother: An Analysis of the Archetype.epub',
            'author': 'Erich Neumann',
            'voice': 'Erich Neumann',
            'work': 'The Great Mother',
            'role': 'Archetypal Analyst',
            'impact': 'Jungian analysis of Great Mother archetype'
        },
        
        # NATURAL PHILOSOPHY
        {
            'filename': 'The Nature of Things.epub',
            'author': 'Lucretius',
            'voice': 'Lucretius',
            'work': 'De Rerum Natura',
            'role': 'Atomist Poet-Philosopher',
            'impact': 'Poetic materialism and atomic theory'
        }
    ]
    
    successful = 0
    failed = 0
    
    print(f"🎯 CONVERTING {len(essential_works)} ESSENTIAL WORKS")
    print()
    
    for i, work_info in enumerate(essential_works, 1):
        file_path = myth_buddha_folder / work_info['filename']
        
        if not file_path.exists():
            print(f"[{i}/{len(essential_works)}] ❌ Not found: {work_info['filename']}")
            failed += 1
            continue
        
        print(f"[{i}/{len(essential_works)}] 💭 {work_info['voice']}")
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
                
                if work_info['voice'] == 'Plato':
                    print(f"           🏛️ MAJOR: Platonic philosophy foundation!")
                elif work_info['voice'] == 'Socrates':
                    print(f"           🗣️ MAJOR: Socratic method activated!")
                elif work_info['voice'] == 'John Donne':
                    print(f"           🌟 MAJOR: Metaphysical poetry tradition!")
                elif work_info['voice'] == 'Charles Baudelaire':
                    print(f"           🌹 MAJOR: Symbolist poetry activated!")
                elif work_info['voice'] == 'Erich Neumann':
                    print(f"           🌙 MAJOR: Great Mother archetype!")
                
            else:
                failed += 1
                print(f"           ❌ Conversion failed")
                
        except Exception as e:
            failed += 1
            print(f"           ❌ Error: {str(e)[:80]}")
        
        print()
    
    print("💭 ESSENTIAL PHILOSOPHY CONVERSION RESULTS:")
    print(f"✅ Successfully converted: {successful} works")
    print(f"❌ Failed conversions: {failed} works")
    
    if successful > 0:
        print(f"\n🎭 CHAMBER PHILOSOPHICAL ENHANCEMENT:")
        print(f"   🏛️ PLATONIC FOUNDATION: Republic + Socratic dialogues")
        print(f"   ⚔️ STOIC ETHICS: Epictetus + Boethius wisdom")
        print(f"   🌟 METAPHYSICAL POETRY: Donne's divine love poetry")
        print(f"   🌹 SYMBOLIST TRADITION: Baudelaire's aesthetic theory")
        print(f"   🌙 ARCHETYPAL PSYCHOLOGY: Great Mother analysis")
        print(f"   ⚛️ MATERIALIST POETRY: Lucretius' atomic philosophy")
        print()
        
        print("🌉 CHAMBER ENHANCED CAPABILITIES:")
        print("   • Plato ↔ All voices: Forms and political philosophy")
        print("   • Socrates ↔ All voices: Questioning and dialectical method")
        print("   • Stoic voices ↔ Buddhist voices: Practical wisdom synthesis")
        print("   • Donne ↔ Mystical voices: Metaphysical poetry and divine love")
        print("   • Baudelaire ↔ Aesthetic voices: Beauty, decay, and modernity")
        print("   • Neumann ↔ Jung: Archetypal psychology expansion")
    
    return successful

if __name__ == "__main__":
    converted_count = convert_essential_philosophy()
    print(f"\n✨ Essential philosophy & poetry conversion complete!")
    print(f"💭 {converted_count} philosophical voices activated")
    print(f"🏛️ Chamber philosophical and poetic foundations significantly enhanced!")