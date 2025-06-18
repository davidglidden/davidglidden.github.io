#!/usr/bin/env python3
"""
Final Comprehensive Scan
Identify ALL remaining voices including any new additions
"""

from pathlib import Path

def final_comprehensive_scan():
    """Scan for all voices including new additions"""
    
    eastern_folder = Path("/Users/davidglidden/Desktop/eastern to the library")
    
    # Get all files
    all_files = []
    try:
        all_files = list(eastern_folder.glob("*"))
    except:
        print("❌ Cannot access folder")
        return
    
    print(f"📚 Scanning {len(all_files)} total files...")
    print()
    
    # Check what we've already converted
    converted_dir = Path("converted_texts")
    converted_names = set()
    if converted_dir.exists():
        for md_file in converted_dir.glob("*.md"):
            base_name = md_file.stem.lower().replace('-', '').replace('_', '')
            converted_names.add(base_name)
    
    new_voices = []
    
    for file_path in all_files:
        if not file_path.name.endswith('.epub') and not file_path.name.endswith('.pdf'):
            continue
            
        filename = file_path.name
        title_lower = filename.lower()
        
        # Check if already converted (rough matching)
        file_clean = title_lower.replace(' ', '').replace('-', '').replace('_', '').replace('.epub', '').replace('.pdf', '')
        already_converted = any(converted in file_clean or file_clean in converted for converted in converted_names)
        
        if already_converted:
            continue
        
        # Identify potential new voices
        voice_info = None
        
        # NEW ADDITIONS SCAN
        
        # Michel Foucault - Major missing voice!
        if 'histoire de la folie' in title_lower:
            voice_info = {
                'author': 'Michel Foucault',
                'voice': 'Michel Foucault',
                'work': 'Histoire de la folie à l\'âge classique',
                'priority': 'CRITICAL',
                'role': 'Archaeologist of Knowledge and Power',
                'domains': ['madness', 'power', 'knowledge', 'archaeology_of_ideas']
            }
        elif 'histoire de la sexualité' in title_lower and 'souci de soi' in title_lower:
            voice_info = {
                'author': 'Michel Foucault',
                'voice': 'Michel Foucault',
                'work': 'Histoire de la sexualité - Le souci de soi',
                'priority': 'HIGH',
                'role': 'Genealogist of Ethics and Sexuality',
                'domains': ['sexuality', 'ethics', 'care_of_self', 'ancient_ethics']
            }
        elif 'histoire de la sexualité' in title_lower and 'usage des plaisirs' in title_lower:
            voice_info = {
                'author': 'Michel Foucault',
                'voice': 'Michel Foucault',
                'work': 'Histoire de la sexualité - L\'usage des plaisirs',
                'priority': 'HIGH',
                'role': 'Theorist of Pleasure and Ethics',
                'domains': ['pleasure', 'ancient_sexuality', 'ethical_formation', 'greek_ethics']
            }
        
        # Jacques Lacan - Psychoanalytic structuralist
        elif 'écrits' == title_lower.replace('.epub', ''):
            voice_info = {
                'author': 'Jacques Lacan',
                'voice': 'Jacques Lacan',
                'work': 'Écrits',
                'priority': 'CRITICAL',
                'role': 'Structural Psychoanalyst of the Unconscious',
                'domains': ['structural_psychoanalysis', 'unconscious', 'language', 'desire']
            }
        
        # Giacomo Leopardi - Italian pessimist poet
        elif 'canti' == title_lower.replace('.epub', ''):
            voice_info = {
                'author': 'Giacomo Leopardi',
                'voice': 'Giacomo Leopardi',
                'work': 'Canti',
                'priority': 'HIGH',
                'role': 'Pessimist Poet of Infinite Longing',
                'domains': ['pessimism', 'infinity', 'longing', 'italian_romanticism']
            }
        
        # More Philippe Jaccottet
        elif 'éléments d\'un songe' in title_lower:
            voice_info = {
                'author': 'Philippe Jaccottet',
                'voice': 'Philippe Jaccottet',
                'work': 'Éléments d\'un songe',
                'priority': 'MEDIUM',
                'role': 'Dream Element Poet',
                'domains': ['dreams', 'elements', 'poetic_fragments', 'contemplation']
            }
        elif 'et, néanmoins' in title_lower:
            voice_info = {
                'author': 'Philippe Jaccottet',
                'voice': 'Philippe Jaccottet',
                'work': 'Et, néanmoins',
                'priority': 'MEDIUM',
                'role': 'Poet of Nevertheless',
                'domains': ['persistence', 'hope', 'nevertheless', 'affirmation']
            }
        
        # Cervantes - Don Quixote
        elif 'don quixote' in title_lower:
            voice_info = {
                'author': 'Miguel de Cervantes',
                'voice': 'Miguel de Cervantes',
                'work': 'Don Quixote',
                'priority': 'HIGH',
                'role': 'Creator of Modern Fiction and Idealistic Delusion',
                'domains': ['idealism', 'reality_vs_fiction', 'chivalry', 'modern_novel']
            }
        
        # Goethe - Faust (both parts)
        elif 'faust: part one' in title_lower:
            voice_info = {
                'author': 'Johann Wolfgang von Goethe',
                'voice': 'Johann Wolfgang von Goethe',
                'work': 'Faust: Part One',
                'priority': 'HIGH',
                'role': 'Romantic Seeker of Ultimate Knowledge',
                'domains': ['faustian_bargain', 'knowledge_limits', 'romanticism', 'tragic_ambition']
            }
        elif 'faust, part two' in title_lower:
            voice_info = {
                'author': 'Johann Wolfgang von Goethe',
                'voice': 'Johann Wolfgang von Goethe',
                'work': 'Faust: Part Two',
                'priority': 'MEDIUM',
                'role': 'Cosmic Poet of Redemption',
                'domains': ['redemption', 'cosmic_drama', 'romantic_completion', 'eternal_feminine']
            }
        
        # Dickens
        elif 'david copperfield' in title_lower:
            voice_info = {
                'author': 'Charles Dickens',
                'voice': 'Charles Dickens', 
                'work': 'David Copperfield',
                'priority': 'MEDIUM',
                'role': 'Social Novelist of Human Character',
                'domains': ['social_criticism', 'character_development', 'victorian_society', 'bildungsroman']
            }
        
        # Plutarch
        elif 'greek lives' in title_lower:
            voice_info = {
                'author': 'Plutarch',
                'voice': 'Plutarch',
                'work': 'Greek Lives',
                'priority': 'MEDIUM',
                'role': 'Biographer of Great Lives',
                'domains': ['biography', 'character', 'moral_example', 'classical_virtue']
            }
        
        # Additional Umberto Eco
        elif 'five moral pieces' in title_lower:
            voice_info = {
                'author': 'Umberto Eco',
                'voice': 'Umberto Eco',
                'work': 'Five Moral Pieces',
                'priority': 'MEDIUM',
                'role': 'Moral Essayist and Cultural Critic',
                'domains': ['moral_philosophy', 'cultural_criticism', 'ethics', 'contemporary_morality']
            }
        
        # Add to new voices if identified
        if voice_info:
            voice_info['filename'] = filename
            new_voices.append(voice_info)
    
    return new_voices

def display_new_voices():
    """Display all newly identified voices"""
    
    print("🔍 FINAL COMPREHENSIVE VOICE SCAN")
    print("=" * 50)
    print("Scanning for any new additions made during conversion...")
    print()
    
    new_voices = final_comprehensive_scan()
    
    if not new_voices:
        print("✅ No new voices found - all potential Chamber voices have been identified!")
        print("🎭 The folder is ready for cleanup.")
        return
    
    print(f"🆕 Found {len(new_voices)} NEW potential voices:")
    print()
    
    # Sort by priority
    priority_order = {'CRITICAL': 0, 'HIGH': 1, 'MEDIUM': 2, 'LOW': 3}
    sorted_voices = sorted(new_voices, key=lambda x: priority_order.get(x['priority'], 4))
    
    for i, voice in enumerate(sorted_voices, 1):
        print(f"[{i}] 🎭 {voice['voice']} ({voice['priority']})")
        print(f"    📖 {voice['work']}")
        print(f"    ✍️  {voice['author']}")
        print(f"    🎪 {voice['role']}")
        print(f"    📋 Domains: {', '.join(voice['domains'])}")
        print()
    
    # Summary by priority and importance
    critical = [v for v in new_voices if v['priority'] == 'CRITICAL']
    high = [v for v in new_voices if v['priority'] == 'HIGH']
    
    print("🎯 NEW VOICE PRIORITY ANALYSIS:")
    
    if critical:
        print(f"🔥 CRITICAL: {len(critical)} voices")
        for v in critical:
            print(f"   • {v['voice']}: {v['work']}")
            if v['voice'] == 'Michel Foucault':
                print(f"     ⚡ MAJOR GAP: Power/knowledge archaeology missing from Chamber!")
            elif v['voice'] == 'Jacques Lacan':
                print(f"     ⚡ MAJOR GAP: Structural psychoanalysis missing from Chamber!")
    
    if high:
        print(f"🟡 HIGH: {len(high)} voices")
        for v in high:
            print(f"   • {v['voice']}: {v['work']}")
    
    print()
    print("🏛️ CHAMBER IMPACT OF NEW VOICES:")
    
    # Check for major missing theorists
    major_voices = [v['voice'] for v in new_voices]
    if 'Michel Foucault' in major_voices:
        print("   🔥 FOUCAULT: Power, knowledge, madness - CRITICAL missing voice!")
    if 'Jacques Lacan' in major_voices:
        print("   🔥 LACAN: Structural psychoanalysis - CRITICAL missing voice!")
    if 'Giacomo Leopardi' in major_voices:
        print("   🌙 LEOPARDI: Italian pessimistic poetry")
    if 'Miguel de Cervantes' in major_voices:
        print("   🏰 CERVANTES: Foundational modern fiction")
    if 'Johann Wolfgang von Goethe' in major_voices:
        print("   ⚡ GOETHE: Romantic totality and Faustian ambition")
    
    print()
    print("🌉 NEW DIALECTICAL POSSIBILITIES:")
    if 'Michel Foucault' in major_voices:
        print("   • Foucault ↔ Arendt: Power structures and political theory")
        print("   • Foucault ↔ Benjamin: Archaeological vs. historical materialism")
    if 'Jacques Lacan' in major_voices:
        print("   • Lacan ↔ Jung: Structural vs. archetypal unconscious")
        print("   • Lacan ↔ Levinas: Language and the Other")
    
    print()
    print("📋 RECOMMENDATION:")
    if critical:
        print("   🔥 CONVERT CRITICAL VOICES IMMEDIATELY:")
        for v in critical:
            print(f"      - {v['voice']}: {v['work']}")
        print("   These represent major gaps in Chamber's theoretical coverage!")
    
    return new_voices

if __name__ == "__main__":
    new_voices = display_new_voices()
    
    if new_voices:
        critical_count = len([v for v in new_voices if v['priority'] == 'CRITICAL'])
        total_count = len(new_voices)
        print(f"\n⚡ {critical_count} CRITICAL and {total_count} total new voices found!")
        print("🎭 Conversion recommended before folder cleanup")
    else:
        print("\n🎉 Complete voice scan finished - folder ready for cleanup!")