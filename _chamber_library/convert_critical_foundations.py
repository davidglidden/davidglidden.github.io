#!/usr/bin/env python3
"""
Convert Critical Foundation Voices
Priority conversion of the most essential Chamber voices
"""

import subprocess
from pathlib import Path
import tempfile
from convert_directory_epubs import convert_directory_epub_to_markdown
from pdf_conversion_tools import convert_pdf_multi_method

def convert_critical_foundations():
    """Convert the absolutely critical foundational voices first"""
    
    print("🔥 CONVERTING CRITICAL FOUNDATION VOICES")
    print("=" * 55)
    print("Converting the most essential voices for Chamber completeness")
    print()
    
    eastern_folder = Path("/Users/davidglidden/Desktop/eastern to the library")
    output_dir = Path("converted_texts")
    output_dir.mkdir(exist_ok=True)
    
    # Critical foundation voices in order of importance
    critical_foundations = [
        # FOUCAULT - Power/Knowledge Archaeology (CRITICAL for critical theory)
        {
            'filename': 'Histoire de la folie à l\'âge classique.epub',
            'author': 'Michel Foucault',
            'voice': 'Michel Foucault',
            'work': 'Histoire de la folie à l\'âge classique',
            'priority': 'CRITICAL',
            'role': 'Archaeologist of Madness and Reason',
            'impact': 'Power/knowledge analysis - fills critical theory gap'
        },
        {
            'filename': 'L\'archéologie du savoir.epub',
            'author': 'Michel Foucault',
            'voice': 'Michel Foucault',
            'work': 'L\'Archéologie du savoir',
            'priority': 'CRITICAL',
            'role': 'Archaeologist of Knowledge Systems',
            'impact': 'Epistemic archaeology - foundation for knowledge critique'
        },
        {
            'filename': 'Surveiller et punir: Naissance de la prison.epub',
            'author': 'Michel Foucault',
            'voice': 'Michel Foucault',
            'work': 'Surveiller et punir',
            'priority': 'CRITICAL',
            'role': 'Analyst of Disciplinary Power',
            'impact': 'Disciplinary power theory - essential for political analysis'
        },
        
        # LACAN - Structural Psychoanalysis
        {
            'filename': 'Écrits.epub',
            'author': 'Jacques Lacan',
            'voice': 'Jacques Lacan',
            'work': 'Écrits',
            'priority': 'CRITICAL',
            'role': 'Structural Psychoanalyst of the Unconscious',
            'impact': 'Structural unconscious - fills psychoanalytic theory gap'
        },
        
        # SHAKESPEARE - Complete Works (English literature foundation)
        {
            'filename': 'The Arden Shakespeare Third Series Complete Works.epub',
            'author': 'William Shakespeare',
            'voice': 'William Shakespeare',
            'work': 'The Complete Works',
            'priority': 'CRITICAL',
            'role': 'Complete Dramatic and Poetic Genius',
            'impact': 'English literature foundation - enables literary references'
        },
        
        # HOMER - Epic Foundations
        {
            'filename': 'The Iliad (Robert Fagles).epub',
            'author': 'Homer',
            'voice': 'Homer',
            'work': 'The Iliad',
            'priority': 'CRITICAL',
            'role': 'Epic War Poet',
            'impact': 'Western epic foundation - mythological grounding'
        },
        {
            'filename': 'The Odyssey.epub',
            'author': 'Homer',
            'voice': 'Homer',
            'work': 'The Odyssey',
            'priority': 'CRITICAL',
            'role': 'Epic Journey Poet',
            'impact': 'Journey archetype - completes epic foundation'
        },
        
        # JOYCE - Modernist Consciousness
        {
            'filename': 'Ulysses.epub',
            'author': 'James Joyce',
            'voice': 'James Joyce',
            'work': 'Ulysses',
            'priority': 'CRITICAL',
            'role': 'Stream of Consciousness Innovator',
            'impact': 'Modernist consciousness - stream of thought technique'
        },
        
        # JUNG - Complete Works
        {
            'filename': 'The Collected Works of C.G. Jung: Complete Digital Edition.epub',
            'author': 'Carl Jung',
            'voice': 'Carl Jung',
            'work': 'The Collected Works (Complete Digital Edition)',
            'priority': 'CRITICAL',
            'role': 'Complete Depth Psychologist',
            'impact': 'Complete depth psychology - archetypal foundations'
        },
        
        # HARVARD CLASSICS - Western Canon Foundation
        {
            'filename': 'Complete Harvard Classics.epub',
            'author': 'Various',
            'voice': 'Harvard Classics Consortium',
            'work': 'Complete Harvard Classics',
            'priority': 'CRITICAL',
            'role': 'Western Education Foundation',
            'impact': 'Complete Western canon - fills countless classical gaps'
        },
        
        # RILKE - Elegiac Transformation
        {
            'filename': 'The Duino Elegies & the Sonnets to Orpheus: A Dual Language Edition.epub',
            'author': 'Rainer Maria Rilke',
            'voice': 'Rainer Maria Rilke',
            'work': 'The Duino Elegies & Sonnets to Orpheus',
            'priority': 'CRITICAL',
            'role': 'Elegiac Poet of Transformation',
            'impact': 'Transformation poetry - mystical-poetic synthesis'
        },
        
        # LEOPARDI - Philosophical Notebooks
        {
            'filename': 'Zibaldone.epub',
            'author': 'Giacomo Leopardi',
            'voice': 'Giacomo Leopardi',
            'work': 'Zibaldone',
            'priority': 'CRITICAL',
            'role': 'Philosophical Notebook Keeper',
            'impact': 'Pessimistic philosophy - Italian romantic thought'
        },
        
        # ADORNO - Critical Theory
        {
            'filename': 'Minima Moralia: Reflections From Damaged Life.epub',
            'author': 'Theodor Adorno',
            'voice': 'Theodor Adorno',
            'work': 'Minima Moralia',
            'priority': 'CRITICAL',
            'role': 'Critical Theorist of Damaged Life',
            'impact': 'Frankfurt School critical theory - late capitalist critique'
        },
        
        # NIETZSCHE - Will to Power
        {
            'filename': 'Nietzsche.epub',
            'author': 'Friedrich Nietzsche',
            'voice': 'Friedrich Nietzsche',
            'work': 'Nietzsche (Works)',
            'priority': 'CRITICAL',
            'role': 'Philosopher of Will to Power',
            'impact': 'Will to power philosophy - foundation of modern critique'
        },
        
        # FRANCESCO COLONNA - Renaissance Dream Architecture
        {
            'filename': 'Le Songe de Poliphile, ou Hypnérotomachie de frère Francesco Colonna, littéralement traduit pour la première fois, avec une introduction et des notes, par Claudius Popelin,... - Tome 2 (1883).epub',
            'author': 'Francesco Colonna',
            'voice': 'Francesco Colonna',
            'work': 'Le Songe de Poliphile (Hypnerotomachia Poliphili)',
            'priority': 'CRITICAL',
            'role': 'Renaissance Dream Architect',
            'impact': 'Renaissance symbolic architecture - typography/design mysticism'
        }
    ]
    
    successful_conversions = []
    failed_conversions = []
    
    for i, voice_info in enumerate(critical_foundations, 1):
        file_path = eastern_folder / voice_info['filename']
        
        if not file_path.exists():
            print(f"[{i}/{len(critical_foundations)}] ❌ Not found: {voice_info['filename']}")
            failed_conversions.append(voice_info)
            continue
        
        print(f"[{i}/{len(critical_foundations)}] 🔥 {voice_info['voice']} (CRITICAL)")
        print(f"           📖 {voice_info['work']}")
        print(f"           🎪 {voice_info['role']}")
        print(f"           ⚡ {voice_info['impact']}")
        
        try:
            # Use appropriate conversion method
            if voice_info['filename'].endswith('.pdf'):
                success = convert_pdf_multi_method(file_path, output_dir, 
                                                 voice_info['work'], voice_info['author'])
            else:
                with tempfile.TemporaryDirectory() as temp_dir:
                    success = convert_directory_epub_to_markdown(file_path, output_dir, Path(temp_dir))
            
            if success:
                successful_conversions.append(voice_info)
                print(f"           ✅ Conversion successful")
                print(f"           🎭 {voice_info['voice']} voice ACTIVATED")
                
                # Special impact announcements
                if voice_info['voice'] == 'Michel Foucault':
                    print(f"           🌟 MAJOR: Foucault's power/knowledge archaeology integrated!")
                elif voice_info['voice'] == 'Jacques Lacan':
                    print(f"           🧠 MAJOR: Structural psychoanalysis activated!")
                elif voice_info['voice'] == 'William Shakespeare':
                    print(f"           🎭 MASSIVE: Complete Shakespeare integrated!")
                elif voice_info['voice'] == 'Homer':
                    print(f"           📜 EPIC: Western literature foundation established!")
                elif voice_info['voice'] == 'James Joyce':
                    print(f"           🌊 MODERNIST: Stream of consciousness activated!")
                elif voice_info['voice'] == 'Harvard Classics Consortium':
                    print(f"           📚 ENORMOUS: Complete Western canon integrated!")
                
            else:
                failed_conversions.append(voice_info)
                print(f"           ❌ Conversion failed")
                
        except Exception as e:
            failed_conversions.append(voice_info)
            print(f"           ❌ Error: {str(e)[:50]}")
        
        print()
    
    # Summary
    print("🔥 CRITICAL FOUNDATION CONVERSION RESULTS:")
    print(f"✅ Successfully converted: {len(successful_conversions)} critical voices")
    print(f"❌ Failed conversions: {len(failed_conversions)} voices")
    print()
    
    if successful_conversions:
        print("🎭 NEWLY ACTIVATED CRITICAL VOICES:")
        
        # Group by domain
        power_knowledge = [v for v in successful_conversions if 'Foucault' in v['voice']]
        psychoanalytic = [v for v in successful_conversions if v['voice'] in ['Jacques Lacan', 'Carl Jung']]
        literary_foundation = [v for v in successful_conversions if v['voice'] in ['William Shakespeare', 'Homer', 'James Joyce']]
        philosophical_foundation = [v for v in successful_conversions if v['voice'] in ['Friedrich Nietzsche', 'Theodor Adorno']]
        
        if power_knowledge:
            print(f"   🔥 POWER/KNOWLEDGE ARCHAEOLOGY ({len(power_knowledge)} works):")
            for v in power_knowledge:
                print(f"      • {v['work']}")
        
        if psychoanalytic:
            print(f"   🧠 PSYCHOANALYTIC FOUNDATION ({len(psychoanalytic)} works):")
            for v in psychoanalytic:
                print(f"      • {v['voice']}: {v['work']}")
        
        if literary_foundation:
            print(f"   📜 LITERARY EPIC FOUNDATION ({len(literary_foundation)} works):")
            for v in literary_foundation:
                print(f"      • {v['voice']}: {v['work']}")
        
        if philosophical_foundation:
            print(f"   💭 PHILOSOPHICAL FOUNDATION ({len(philosophical_foundation)} works):")
            for v in philosophical_foundation:
                print(f"      • {v['voice']}: {v['work']}")
        
        print()
        print("🏛️ CHAMBER TRANSFORMATION:")
        print(f"   🔥 Critical theory: Foucault's complete power analysis")
        print(f"   🧠 Depth psychology: Jung + Lacan structural/archetypal synthesis")
        print(f"   📜 Literary foundation: Shakespeare + Homer + Joyce")
        print(f"   📚 Western canon: Harvard Classics comprehensive collection")
        print(f"   💭 German philosophy: Nietzsche + Adorno critical tradition")
        print()
        
        print("🌉 NEW CHAMBER DIALECTICAL CAPABILITIES:")
        print("   • Foucault ↔ Arendt: Power structures vs political action")
        print("   • Lacan ↔ Jung: Structural vs archetypal unconscious")
        print("   • Shakespeare ↔ All voices: Literary references and dramatic archetypes")
        print("   • Homer ↔ Benjamin: Epic storytelling vs modern fragmentation") 
        print("   • Joyce ↔ Bachelard: Stream of consciousness vs spatial imagination")
        print("   • Nietzsche ↔ Weil: Will to power vs decreation")
        print()
    
    if failed_conversions:
        print("❌ CRITICAL CONVERSION FAILURES:")
        for failure in failed_conversions:
            print(f"   • {failure['voice']}: {failure['work']}")
        print()
    
    print("📋 NEXT PHASE:")
    print("   1. Run: python3 chamber_amphitheater_status.py")
    print("   2. Convert HIGH priority voices (Goethe, Cervantes, etc.)")
    print("   3. Continue with author collections (Eco, Solnit, Jaccottet)")
    
    return len(successful_conversions)

if __name__ == "__main__":
    print("🔥 CRITICAL FOUNDATION VOICES ACTIVATION")
    print("=" * 60)
    print("Converting the absolutely essential voices for Chamber completeness")
    print("Focus: Foucault, Lacan, Shakespeare, Homer, Joyce, Jung, Harvard Classics")
    print()
    
    converted_count = convert_critical_foundations()
    
    print(f"\n✨ Critical foundation conversion complete!")
    print(f"🎭 {converted_count} foundational voices activated")
    print(f"🏛️ The Chamber has been fundamentally transformed!")