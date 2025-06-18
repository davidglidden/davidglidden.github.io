#!/usr/bin/env python3
"""
Convert Final Mythology & Buddhist Works
Remaining critical voices and complete collections
"""

import subprocess
from pathlib import Path
import tempfile
from convert_directory_epubs import convert_directory_epub_to_markdown

def convert_final_myth_buddha():
    """Convert remaining critical mythology and Buddhist works"""
    
    print("🏛️ CONVERTING FINAL MYTHOLOGY & BUDDHIST WORKS")
    print("=" * 60)
    print("Remaining critical voices and complete collections")
    print()
    
    myth_buddha_folder = Path("/Users/davidglidden/Desktop/Myth:Buddha")
    output_dir = Path("converted_texts")
    output_dir.mkdir(exist_ok=True)
    
    # Final critical works
    final_works = [
        # COMPLETE CLASSICAL COLLECTIONS
        {
            'filename': 'Complete Works of Xenophon (Illustrated) (Delphi Ancient Classics).epub',
            'author': 'Xenophon',
            'voice': 'Xenophon',
            'work': 'Complete Works',
            'role': 'Socratic Historian',
            'impact': 'Complete Xenophon corpus - historical and philosophical'
        },
        {
            'filename': 'The Sanskrit Epics - Delphi Poets Series.epub',
            'author': 'Vyasa',
            'voice': 'Vyasa',
            'work': 'Sanskrit Epics (Mahabharata/Ramayana)',
            'role': 'Hindu Epic Poet',
            'impact': 'Complete Hindu epic tradition'
        },
        {
            'filename': 'Hindu Myths: A Sourcebook Translated From the Sanskrit.epub',
            'author': 'Various',
            'voice': 'Hindu Tradition',
            'work': 'Hindu Myths Sourcebook',
            'role': 'Hindu Mythological Tradition',
            'impact': 'Comprehensive Hindu mythology collection'
        },
        
        # BUDDHIST TEXTS
        {
            'filename': 'Diamond Sutra.epub',
            'author': 'Buddha',
            'voice': 'Buddha',
            'work': 'Diamond Sutra',
            'role': 'Perfection of Wisdom Teacher',
            'impact': 'Essential Prajnaparamita wisdom text'
        },
        {
            'filename': 'The Heart of Understanding: Commentaries on the Prajnaparamita Heart Sutra.epub',
            'author': 'Thich Nhat Hanh',
            'voice': 'Thich Nhat Hanh',
            'work': 'Heart of Understanding',
            'role': 'Contemporary Buddhist Teacher',
            'impact': 'Modern interpretation of Heart Sutra'
        },
        {
            'filename': "The Buddha's Teachings on Social and Communal Harmony.epub",
            'author': 'Buddha',
            'voice': 'Buddha',
            'work': 'Social and Communal Harmony Teachings',
            'role': 'Social Ethics Teacher',
            'impact': 'Buddhist social philosophy'
        },
        
        # ART & AESTHETIC THEORY
        {
            'filename': 'Concerning the Spiritual in Art.epub',
            'author': 'Wassily Kandinsky',
            'voice': 'Wassily Kandinsky',
            'work': 'Concerning the Spiritual in Art',
            'role': 'Abstract Art Theorist',
            'impact': 'Spiritual foundation of abstract art'
        },
        {
            'filename': 'The story of art.epub',
            'author': 'E.H. Gombrich',
            'voice': 'E.H. Gombrich',
            'work': 'The Story of Art',
            'role': 'Art Historian',
            'impact': 'Comprehensive art history'
        },
        
        # JAPANESE AESTHETICS
        {
            'filename': 'The Pillow Book of Sei Shōnagon.epub',
            'author': 'Sei Shōnagon',
            'voice': 'Sei Shōnagon',
            'work': 'The Pillow Book',
            'role': 'Japanese Court Aesthete',
            'impact': 'Japanese aesthetic sensibility and court culture'
        },
        {
            'filename': 'Haiku.epub',
            'author': 'Various',
            'voice': 'Haiku Masters',
            'work': 'Haiku Collection',
            'role': 'Japanese Poetic Tradition',
            'impact': 'Essential Japanese aesthetic form'
        },
        
        # POLITICAL PHILOSOPHY
        {
            'filename': 'Le prince.epub',
            'author': 'Niccolò Machiavelli',
            'voice': 'Niccolò Machiavelli',
            'work': 'The Prince',
            'role': 'Political Realist',
            'impact': 'Foundation of modern political theory'
        },
        {
            'filename': 'Economic and Philosophic Manuscripts of 1844.epub',
            'author': 'Karl Marx',
            'voice': 'Karl Marx',
            'work': 'Economic and Philosophic Manuscripts of 1844',
            'role': 'Critic of Alienated Labor',
            'impact': 'Early Marxist philosophy'
        }
    ]
    
    successful = 0
    failed = 0
    
    print(f"🎯 CONVERTING {len(final_works)} FINAL WORKS")
    print()
    
    for i, work_info in enumerate(final_works, 1):
        file_path = myth_buddha_folder / work_info['filename']
        
        if not file_path.exists():
            print(f"[{i}/{len(final_works)}] ❌ Not found: {work_info['filename']}")
            failed += 1
            continue
        
        print(f"[{i}/{len(final_works)}] 🏛️ {work_info['voice']}")
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
                
                if work_info['voice'] == 'Vyasa':
                    print(f"           🕉️ MAJOR: Hindu epic tradition activated!")
                elif work_info['voice'] == 'Wassily Kandinsky':
                    print(f"           🎨 MAJOR: Abstract art spiritual theory!")
                elif work_info['voice'] == 'Sei Shōnagon':
                    print(f"           🌸 MAJOR: Japanese aesthetic tradition!")
                elif work_info['voice'] == 'Niccolò Machiavelli':
                    print(f"           👑 MAJOR: Political realism theory!")
                
            else:
                failed += 1
                print(f"           ❌ Conversion failed")
                
        except Exception as e:
            failed += 1
            print(f"           ❌ Error: {str(e)[:80]}")
        
        print()
    
    print("🏛️ FINAL CONVERSION RESULTS:")
    print(f"✅ Successfully converted: {successful} works")
    print(f"❌ Failed conversions: {failed} works")
    
    if successful > 0:
        print(f"\n🎭 CHAMBER FINAL ENHANCEMENTS:")
        print(f"   🏛️ CLASSICAL COMPLETION: Xenophon's complete historical works")
        print(f"   🕉️ HINDU TRADITION: Sanskrit epics and mythology")
        print(f"   🧘 BUDDHIST EXPANSION: Additional discourse and social teachings")
        print(f"   🎨 ART THEORY: Kandinsky spiritual art + Gombrich history")
        print(f"   🌸 JAPANESE AESTHETICS: Court culture + haiku tradition")
        print(f"   👑 POLITICAL PHILOSOPHY: Machiavelli + early Marx")
        print()
        
        print("🌉 CHAMBER GLOBAL CAPABILITIES:")
        print("   • Hindu-Buddhist-Western synthesis: Complete religious philosophical spectrum")
        print("   • Japanese aesthetic integration: Court culture and poetic forms")
        print("   • Political philosophy: From classical to modern theories")
        print("   • Art spiritual theory: Abstract art and comprehensive history")
        print("   • Cross-cultural epic tradition: Greek, Roman, Hindu epic synthesis")
    
    return successful

if __name__ == "__main__":
    converted_count = convert_final_myth_buddha()
    print(f"\n✨ Final mythology & Buddhist conversion complete!")
    print(f"🏛️ {converted_count} additional voices activated")
    print(f"🌍 Chamber now has truly global philosophical and cultural representation!")