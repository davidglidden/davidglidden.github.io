#!/usr/bin/env python3
"""
Comprehensive Voice Identification
Scan all remaining texts in folder to identify potential Chamber voices
"""

from pathlib import Path

def identify_all_remaining_voices():
    """Comprehensively identify all potential Chamber voices"""
    
    eastern_folder = Path("/Users/davidglidden/Desktop/eastern to the library")
    
    # Get all EPUB files we haven't processed yet
    all_files = list(eastern_folder.glob("*.epub"))
    
    converted_dir = Path("converted_texts")
    
    # Check which ones we've already converted
    converted_files = set()
    if converted_dir.exists():
        for md_file in converted_dir.glob("*.md"):
            # Try to match back to original EPUB names
            base_name = md_file.stem.replace('-', ' ').replace('_', ' ').lower()
            converted_files.add(base_name)
    
    potential_voices = {}
    
    for epub_file in all_files:
        title = epub_file.stem
        title_lower = title.lower()
        
        # Skip if already processed (rough matching)
        already_processed = False
        title_clean = title_lower.replace(' ', '').replace('-', '').replace('_', '')
        for converted in converted_files:
            converted_clean = converted.replace(' ', '').replace('-', '').replace('_', '')
            if converted_clean in title_clean or title_clean in converted_clean:
                already_processed = True
                break
        
        if already_processed:
            continue
        
        # Identify potential voices
        voice_info = None
        
        # Spanish Literature
        if 'bodas de sangre' in title_lower:
            voice_info = {
                'author': 'Federico García Lorca',
                'voice': 'Federico García Lorca',
                'work': 'Bodas de sangre (Blood Wedding)',
                'priority': 'HIGH',
                'role': 'Tragic Poet of Andalusia',
                'domains': ['tragedy', 'andalusian_culture', 'folk_poetry', 'death_and_love']
            }
        
        # French Poetry - Philippe Jaccottet
        elif 'à la lumière d\'hiver' in title_lower or 'lumiere' in title_lower:
            voice_info = {
                'author': 'Philippe Jaccottet',
                'voice': 'Philippe Jaccottet',
                'work': 'À la lumière d\'hiver',
                'priority': 'HIGH',
                'role': 'Poet of Light and Landscape',
                'domains': ['light', 'landscape', 'contemplation', 'seasonal_meditation']
            }
        
        elif 'cahier de verdure' in title_lower:
            voice_info = {
                'author': 'Philippe Jaccottet',
                'voice': 'Philippe Jaccottet', 
                'work': 'Cahier de verdure',
                'priority': 'MEDIUM',
                'role': 'Nature Contemplative',
                'domains': ['nature', 'greenness', 'botanical_meditation', 'time_passage']
            }
        
        elif 'ce peu de bruits' in title_lower:
            voice_info = {
                'author': 'Philippe Jaccottet',
                'voice': 'Philippe Jaccottet',
                'work': 'Ce peu de bruits',
                'priority': 'MEDIUM', 
                'role': 'Minimalist Sound Poet',
                'domains': ['sound', 'silence', 'minimal_poetry', 'acoustic_meditation']
            }
        
        elif 'carnets' in title_lower and '1995-1998' in title:
            voice_info = {
                'author': 'Philippe Jaccottet',
                'voice': 'Philippe Jaccottet',
                'work': 'Carnets 1995-1998',
                'priority': 'MEDIUM',
                'role': 'Notebook Poet and Observer',
                'domains': ['notebooks', 'daily_observation', 'poetic_process', 'temporal_meditation']
            }
        
        elif 'airs' == title_lower:
            voice_info = {
                'author': 'Philippe Jaccottet',
                'voice': 'Philippe Jaccottet',
                'work': 'Airs',
                'priority': 'MEDIUM',
                'role': 'Poet of Atmosphere and Breath',
                'domains': ['atmosphere', 'breath', 'air', 'elemental_poetry']
            }
        
        # Multi-poet Anthology
        elif 'd\'une lyre à cinq cordes' in title_lower:
            voice_info = {
                'author': 'Multiple Poets',
                'voice': 'European Poetic Constellation',
                'work': 'D\'une lyre à cinq cordes (Anthology)',
                'priority': 'CRITICAL',
                'role': 'Multi-Voice Poetic Ensemble',
                'domains': ['european_poetry', 'poetic_tradition', 'multilingual_verse', 'lyric_constellation'],
                'contains': ['Pétrarque', 'Le Tasse', 'Leopardi', 'Ungaretti', 'Montale', 
                           'Góngora', 'Goethe', 'Hölderlin', 'Rilke', 'Mandelstam']
            }
        
        # Individual literary works we might have missed
        elif 'complete harvard classics' in title_lower:
            voice_info = {
                'author': 'Various',
                'voice': 'Harvard Classics Anthology',
                'work': 'Complete Harvard Classics',
                'priority': 'MEDIUM',
                'role': 'Classical Education Compendium',
                'domains': ['classical_education', 'western_canon', 'anthology', 'foundational_texts']
            }
        
        elif 'aesthetics and politics' in title_lower:
            voice_info = {
                'author': 'Walter Benjamin et al.',
                'voice': 'Frankfurt School Collective',
                'work': 'Aesthetics and Politics',
                'priority': 'HIGH',
                'role': 'Critical Theory Ensemble',
                'domains': ['critical_theory', 'aesthetics', 'politics', 'marxist_criticism']
            }
        
        elif 'aesthetics' == title_lower:
            voice_info = {
                'author': 'Georg Wilhelm Friedrich Hegel',
                'voice': 'Georg Wilhelm Friedrich Hegel',
                'work': 'Aesthetics',
                'priority': 'HIGH',
                'role': 'Systematic Aesthetician',
                'domains': ['systematic_aesthetics', 'art_philosophy', 'beauty_theory', 'hegelian_dialectic']
            }
        
        elif 'authority' == title_lower:
            voice_info = {
                'author': 'Unknown',
                'voice': 'Authority Theorist',
                'work': 'Authority',
                'priority': 'MEDIUM',
                'role': 'Power Structure Analyst',
                'domains': ['authority', 'power', 'governance', 'social_structures']
            }
        
        elif 'a trackless path' in title_lower and 'dzogchen' in title_lower:
            voice_info = {
                'author': 'Jigmé Lingpa',
                'voice': 'Jigmé Lingpa',
                'work': 'A Trackless Path (Dzogchen Teaching)',
                'priority': 'HIGH',
                'role': 'Dzogchen Master of the Great Completion',
                'domains': ['dzogchen', 'tibetan_buddhism', 'great_completion', 'tibetan_mysticism']
            }
        
        # Add more identifications as needed...
        
        if voice_info:
            potential_voices[title] = voice_info
    
    return potential_voices

def display_remaining_voices():
    """Display all remaining potential voices"""
    
    print("🔍 COMPREHENSIVE VOICE IDENTIFICATION")
    print("=" * 55)
    print("Scanning for ALL remaining potential Chamber voices...")
    print()
    
    voices = identify_all_remaining_voices()
    
    if not voices:
        print("✅ All voices in folder have been identified and processed!")
        return
    
    print(f"📚 Found {len(voices)} additional potential voices:")
    print()
    
    # Sort by priority
    priority_order = {'CRITICAL': 0, 'HIGH': 1, 'MEDIUM': 2, 'LOW': 3}
    sorted_voices = sorted(voices.items(), 
                          key=lambda x: priority_order.get(x[1]['priority'], 4))
    
    for i, (title, info) in enumerate(sorted_voices, 1):
        print(f"[{i}] 🎭 {info['voice']} ({info['priority']})")
        print(f"    📖 {info['work']}")
        print(f"    ✍️  {info['author']}")
        print(f"    🎪 {info['role']}")
        print(f"    📋 Domains: {', '.join(info['domains'])}")
        if 'contains' in info:
            print(f"    👥 Contains: {', '.join(info['contains'][:5])}{'...' if len(info['contains']) > 5 else ''}")
        print()
    
    # Summary by priority
    critical = [v for v in voices.values() if v['priority'] == 'CRITICAL']
    high = [v for v in voices.values() if v['priority'] == 'HIGH'] 
    medium = [v for v in voices.values() if v['priority'] == 'MEDIUM']
    
    print("📊 VOICE PRIORITY BREAKDOWN:")
    print(f"🔥 CRITICAL: {len(critical)} voices")
    for v in critical:
        print(f"   • {v['voice']}: {v['work']}")
    
    print(f"🟡 HIGH: {len(high)} voices")
    for v in high:
        print(f"   • {v['voice']}: {v['work']}")
    
    print(f"🔵 MEDIUM: {len(medium)} voices") 
    for v in medium:
        print(f"   • {v['voice']}: {v['work']}")
    
    print()
    print("🎯 CHAMBER ENHANCEMENT POTENTIAL:")
    print(f"   • French poetry tradition: Philippe Jaccottet")
    print(f"   • Spanish tragic poetry: Federico García Lorca")
    print(f"   • European poetic constellation: Multi-voice anthology")
    print(f"   • Tibetan Buddhist mysticism: Dzogchen teachings")
    print(f"   • Aesthetic philosophy: Hegel and critical theory")
    print()
    print("📋 RECOMMENDATION:")
    print("   Convert CRITICAL and HIGH priority voices first")
    print("   These will significantly enhance Chamber's poetic and mystical capabilities")
    
    return voices

if __name__ == "__main__":
    voices = display_remaining_voices()
    
    if voices:
        print(f"\n✨ {len(voices)} additional Chamber voices identified!")
        print("🎭 Ready for conversion to complete the constellation")
    else:
        print("\n🎉 Voice identification complete - all potential voices found!")