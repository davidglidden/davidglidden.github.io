#!/usr/bin/env python3
"""
Convert Essential Collections
Complete key authors and add critical missing voices
"""

import subprocess
from pathlib import Path
import tempfile
from convert_directory_epubs import convert_directory_epub_to_markdown

def convert_essential_collections():
    """Convert essential works and complete author collections"""
    
    print("📚 CONVERTING ESSENTIAL COLLECTIONS")
    print("=" * 50)
    print("Completing key authors and adding critical voices")
    print()
    
    eastern_folder = Path("/Users/davidglidden/Desktop/eastern to the library")
    output_dir = Path("converted_texts")
    output_dir.mkdir(exist_ok=True)
    
    # Essential collections and critical missing voices
    essential_works = [
        # CERVANTES - Modern fiction foundation
        {
            'filename': 'Don Quixote.epub',
            'author': 'Miguel de Cervantes',
            'voice': 'Miguel de Cervantes',
            'work': 'Don Quixote',
            'role': 'Creator of Modern Fiction',
            'impact': 'Foundation of modern novel form'
        },
        
        # GOETHE - Complete Faust
        {
            'filename': 'Faust: Part One.epub',
            'author': 'Johann Wolfgang von Goethe',
            'voice': 'Johann Wolfgang von Goethe',
            'work': 'Faust: Part One',
            'role': 'Faustian Knowledge Seeker',
            'impact': 'Romantic quest for ultimate knowledge'
        },
        {
            'filename': 'Faust, Part Two.epub',
            'author': 'Johann Wolfgang von Goethe',
            'voice': 'Johann Wolfgang von Goethe',
            'work': 'Faust: Part Two',
            'role': 'Cosmic Redemption Poet',
            'impact': 'Cosmic drama and romantic completion'
        },
        {
            'filename': 'West-Eastern Divan.epub',
            'author': 'Johann Wolfgang von Goethe',
            'voice': 'Johann Wolfgang von Goethe',
            'work': 'West-Eastern Divan',
            'role': 'East-West Cultural Synthesizer',
            'impact': 'Cultural synthesis between East and West'
        },
        
        # LEOPARDI - Complete works
        {
            'filename': 'Canti.epub',
            'author': 'Giacomo Leopardi',
            'voice': 'Giacomo Leopardi',
            'work': 'Canti',
            'role': 'Pessimist Poet of Infinite Longing',
            'impact': 'Italian romantic pessimism'
        },
        
        # RILKE - Elegiac transformation
        {
            'filename': 'The Duino Elegies & the Sonnets to Orpheus: A Dual Language Edition.epub',
            'author': 'Rainer Maria Rilke',
            'voice': 'Rainer Maria Rilke',
            'work': 'The Duino Elegies & Sonnets to Orpheus',
            'role': 'Elegiac Poet of Transformation',
            'impact': 'Transformation poetry and mystical experience'
        },
        
        # KAFKA - Aphoristic wisdom
        {
            'filename': 'The Aphorisms of Franz Kafka.epub',
            'author': 'Franz Kafka',
            'voice': 'Franz Kafka',
            'work': 'The Aphorisms',
            'role': 'Aphoristic Existentialist',
            'impact': 'Existential anxiety and bureaucratic absurdity'
        },
        
        # MELVILLE - American literature
        {
            'filename': 'Moby Dick.epub',
            'author': 'Herman Melville',
            'voice': 'Herman Melville',
            'work': 'Moby Dick',
            'role': 'Metaphysical Maritime Novelist',
            'impact': 'American metaphysical literature'
        },
        
        # VIRGIL - Roman epic
        {
            'filename': 'The Aeneid.epub',
            'author': 'Virgil',
            'voice': 'Virgil',
            'work': 'The Aeneid',
            'role': 'Roman Empire Epic Poet',
            'impact': 'Roman imperial mythology'
        },
        
        # BERTRAND RUSSELL - Analytical philosophy
        {
            'filename': 'History of Western Philosophy (Routledge Classics).epub',
            'author': 'Bertrand Russell',
            'voice': 'Bertrand Russell',
            'work': 'History of Western Philosophy',
            'role': 'Analytical Philosophy Historian',
            'impact': 'Comprehensive philosophical history'
        },
        
        # VIKTOR FRANKL - Meaning and suffering
        {
            'filename': 'Man\'s Search for Meaning.epub',
            'author': 'Viktor Frankl',
            'voice': 'Viktor Frankl',
            'work': 'Man\'s Search for Meaning',
            'role': 'Logotherapist of Meaning and Suffering',
            'impact': 'Meaning-centered psychology from Holocaust experience'
        },
        
        # BAUMAN - Liquid modernity
        {
            'filename': 'Liquid Modernity.epub',
            'author': 'Zygmunt Bauman',
            'voice': 'Zygmunt Bauman',
            'work': 'Liquid Modernity',
            'role': 'Theorist of Liquid Modern Society',
            'impact': 'Contemporary social theory'
        }
    ]
    
    successful = 0
    failed = 0
    
    for i, work_info in enumerate(essential_works, 1):
        file_path = eastern_folder / work_info['filename']
        
        if not file_path.exists():
            print(f"[{i}/{len(essential_works)}] ❌ Not found: {work_info['filename']}")
            failed += 1
            continue
        
        print(f"[{i}/{len(essential_works)}] 📚 {work_info['voice']}")
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
                
                # Special announcements
                if work_info['voice'] == 'Miguel de Cervantes':
                    print(f"           🏰 MAJOR: Modern fiction foundation established!")
                elif work_info['voice'] == 'Johann Wolfgang von Goethe':
                    print(f"           ⚡ GOETHE: German romantic tradition enhanced!")
                elif work_info['voice'] == 'Rainer Maria Rilke':
                    print(f"           🌟 MAJOR: Elegiac transformation poetry activated!")
                elif work_info['voice'] == 'Herman Melville':
                    print(f"           🐋 AMERICAN: Metaphysical literature tradition!")
                
            else:
                failed += 1
                print(f"           ❌ Conversion failed")
                
        except Exception as e:
            failed += 1
            print(f"           ❌ Error: {str(e)[:50]}")
        
        print()
    
    print("📚 ESSENTIAL COLLECTIONS CONVERSION RESULTS:")
    print(f"✅ Successfully converted: {successful} works")
    print(f"❌ Failed conversions: {failed} works")
    
    if successful > 0:
        print(f"\n🎭 CHAMBER ENHANCEMENT:")
        print(f"   🏰 Modern fiction: Cervantes' Don Quixote")
        print(f"   ⚡ German romanticism: Goethe's complete Faust")
        print(f"   🌟 Transformation poetry: Rilke's Elegies")
        print(f"   🐋 American literature: Melville's Moby Dick")
        print(f"   📜 Roman epic: Virgil's Aeneid")
        print(f"   💭 Analytical philosophy: Russell's comprehensive history")
        print(f"   🏛️ Literary and philosophical canon: Significantly expanded")
        print()
        
        print("🌉 NEW CHAMBER CAPABILITIES:")
        print("   • Cervantes ↔ All voices: Modern fiction references")
        print("   • Goethe ↔ Faust theme: Knowledge, ambition, redemption")
        print("   • Rilke ↔ Mystical voices: Transformation and transcendence")
        print("   • Melville ↔ Philosophical voices: Metaphysical American literature")
        print("   • Russell ↔ All philosophers: Analytical perspective on tradition")
    
    return successful

if __name__ == "__main__":
    print("📚 ESSENTIAL COLLECTIONS CONVERSION")
    print("=" * 50)
    print("Converting critical literary and philosophical works")
    print()
    
    converted_count = convert_essential_collections()
    
    print(f"\n✨ Essential collections conversion complete!")
    print(f"🎭 {converted_count} essential voices activated")
    print(f"📚 Chamber literary and philosophical canon significantly enhanced!")