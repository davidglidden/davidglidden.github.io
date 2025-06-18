#!/usr/bin/env python3
"""
Convert Chamber Voice Works
Identify and convert works that activate specific Chamber voices
"""

import subprocess
from pathlib import Path
import tempfile
from convert_directory_epubs import convert_directory_epub_to_markdown

def identify_chamber_voice_texts():
    """Map texts in folder to Chamber voices"""
    
    chamber_voice_mapping = {
        # Umberto Eco - CRITICAL MISSING VOICE
        'Baudolino.epub': {
            'author': 'Umberto Eco',
            'voice': 'Umberto Eco',
            'priority': 'CRITICAL',
            'role': 'Semiotician of Signs and Stories',
            'domains': ['semiotics', 'medieval_philosophy', 'narrative_theory']
        },
        'Chronicles of a Liquid Society.epub': {
            'author': 'Umberto Eco', 
            'voice': 'Umberto Eco',
            'priority': 'HIGH',
            'role': 'Cultural Critic and Semiotician',
            'domains': ['cultural_criticism', 'media_theory', 'contemporary_society']
        },
        "Foucault's Pendulum.epub": {
            'author': 'Umberto Eco',
            'voice': 'Umberto Eco', 
            'priority': 'HIGH',
            'role': 'Conspiracy Theorist and Knowledge Critic',
            'domains': ['epistemology', 'conspiracy_theory', 'hermetic_tradition']
        },
        
        # Susan Sontag - Contemporary critical voice
        'Against Interpretation and Other Essays.epub': {
            'author': 'Susan Sontag',
            'voice': 'Susan Sontag',
            'priority': 'HIGH',
            'role': 'Cultural Critic and Aesthetician',
            'domains': ['cultural_criticism', 'photography', 'aesthetics']
        },
        'As Consciousness Is Harnessed to Flesh.epub': {
            'author': 'Susan Sontag',
            'voice': 'Susan Sontag',
            'priority': 'MEDIUM',
            'role': 'Consciousness Explorer',
            'domains': ['consciousness', 'writing', 'intellectual_life']
        },
        
        # T.S. Eliot - Poetic-philosophical voice
        'Collected Poems 1909-1962.epub': {
            'author': 'T.S. Eliot',
            'voice': 'T.S. Eliot', 
            'priority': 'HIGH',
            'role': 'Poet of Tradition and Renewal',
            'domains': ['poetry', 'tradition', 'spiritual_quest']
        },
        'Four Quartets.epub': {
            'author': 'T.S. Eliot',
            'voice': 'T.S. Eliot',
            'priority': 'CRITICAL',
            'role': 'Mystical Poet of Time and Place',
            'domains': ['mysticism', 'time', 'place', 'spiritual_geography']
        },
        
        # Jorge Luis Borges - Labyrinthine thinker
        'El Aleph.epub': {
            'author': 'Jorge Luis Borges',
            'voice': 'Jorge Luis Borges',
            'priority': 'CRITICAL', 
            'role': 'Labyrinth Keeper and Infinite Librarian',
            'domains': ['infinity', 'labyrinths', 'library_science', 'metaphysics']
        },
        'Fictions.epub': {
            'author': 'Jorge Luis Borges',
            'voice': 'Jorge Luis Borges',
            'priority': 'HIGH',
            'role': 'Creator of Impossible Worlds',
            'domains': ['fictional_worlds', 'philosophy_through_story', 'paradox']
        },
        
        # Stephen Hawking - Scientific cosmology
        'Brief Answers to the Big Questions.epub': {
            'author': 'Stephen Hawking',
            'voice': 'Stephen Hawking',
            'priority': 'MEDIUM',
            'role': 'Cosmic Question Asker', 
            'domains': ['cosmology', 'physics', 'existence_questions']
        },
        'Black Holes: The Reith Lectures.epub': {
            'author': 'Stephen Hawking',
            'voice': 'Stephen Hawking',
            'priority': 'MEDIUM',
            'role': 'Black Hole Theorist',
            'domains': ['black_holes', 'spacetime', 'information_theory']
        },
        
        # Hannah Arendt - additional work
        'Between Past and Future (Penguin Classics).epub': {
            'author': 'Hannah Arendt',
            'voice': 'Hannah Arendt',
            'priority': 'HIGH',
            'role': 'Political Philosopher',
            'domains': ['political_theory', 'authority', 'tradition']
        },
        
        # Potential bridge voices
        'A Field Guide to Getting Lost.epub': {
            'author': 'Rebecca Solnit',
            'voice': 'Rebecca Solnit',
            'priority': 'MEDIUM',
            'role': 'Walker and Wonder Seeker',
            'domains': ['walking', 'landscape', 'getting_lost', 'embodied_geography']
        },
        
        'How to Do Nothing: Resisting the Attention Economy.epub': {
            'author': 'Jenny Odell',
            'voice': 'Jenny Odell', 
            'priority': 'HIGH',
            'role': 'Attention Economist and Digital Resistor',
            'domains': ['attention_economy', 'digital_resistance', 'place_based_thinking']
        },
        
        # Aphoristic wisdom
        'Aphorisms on Love and Hate.epub': {
            'author': 'Unknown',
            'voice': 'Aphoristic Sage',
            'priority': 'LOW',
            'role': 'Wisdom Keeper',
            'domains': ['aphorisms', 'love', 'hate', 'human_nature']
        },
        
        # The Elements of Typographic Style (PDF)
        'the_elements_of_typographic_style.pdf': {
            'author': 'Robert Bringhurst',
            'voice': 'Robert Bringhurst',
            'priority': 'CRITICAL',
            'role': 'Typography Master and Language Craftsman',
            'domains': ['typography', 'language_craft', 'visual_communication']
        }
    }
    
    return chamber_voice_mapping

def convert_chamber_voice_works():
    """Convert all identified Chamber voice works"""
    
    print("🏛️ CONVERTING CHAMBER VOICE WORKS")
    print("=" * 50)
    
    eastern_folder = Path("/Users/davidglidden/Desktop/eastern to the library")
    output_dir = Path("converted_texts")
    output_dir.mkdir(exist_ok=True)
    
    voice_mapping = identify_chamber_voice_texts()
    
    # Sort by priority
    priority_order = {'CRITICAL': 0, 'HIGH': 1, 'MEDIUM': 2, 'LOW': 3}
    sorted_texts = sorted(voice_mapping.items(), 
                         key=lambda x: priority_order.get(x[1]['priority'], 4))
    
    successful_conversions = []
    failed_conversions = []
    
    for i, (filename, info) in enumerate(sorted_texts, 1):
        file_path = eastern_folder / filename
        
        if not file_path.exists():
            print(f"[{i}/{len(sorted_texts)}] ❌ Not found: {filename}")
            continue
        
        print(f"[{i}/{len(sorted_texts)}] 🎭 {info['voice']} ({info['priority']})")
        print(f"           📖 {file_path.stem}")
        print(f"           🎪 {info['role']}")
        
        try:
            if filename.endswith('.pdf'):
                # Use PDF conversion
                from pdf_conversion_tools import convert_pdf_multi_method
                success = convert_pdf_multi_method(file_path, output_dir, 
                                                 file_path.stem, info['author'])
            else:
                # Use EPUB conversion
                with tempfile.TemporaryDirectory() as temp_dir:
                    success = convert_directory_epub_to_markdown(file_path, output_dir, Path(temp_dir))
            
            if success:
                successful_conversions.append(info)
                print(f"           ✅ Conversion successful")
                print(f"           🎭 {info['voice']} voice ACTIVATED")
                
                # Special announcements for critical voices
                if info['priority'] == 'CRITICAL':
                    if info['voice'] == 'Umberto Eco':
                        print(f"           🎉 MAJOR: Umberto Eco joins the Chamber!")
                    elif info['voice'] == 'Jorge Luis Borges':
                        print(f"           🌟 MAJOR: Borges brings infinite libraries!")
                    elif info['voice'] == 'T.S. Eliot':
                        print(f"           ✨ MAJOR: Four Quartets mysticism activated!")
                        
            else:
                failed_conversions.append({'filename': filename, 'voice': info['voice']})
                print(f"           ❌ Conversion failed")
                
        except Exception as e:
            failed_conversions.append({'filename': filename, 'voice': info['voice'], 'error': str(e)})
            print(f"           ❌ Error: {str(e)[:50]}")
        
        print()
    
    # Summary
    print("📊 CHAMBER VOICE CONVERSION RESULTS:")
    print(f"✅ Successfully converted: {len(successful_conversions)} voices")
    print(f"❌ Failed conversions: {len(failed_conversions)} voices")
    print()
    
    if successful_conversions:
        print("🎭 NEWLY ACTIVATED CHAMBER VOICES:")
        
        # Group by voice
        voice_counts = {}
        for conv in successful_conversions:
            voice = conv['voice']
            if voice not in voice_counts:
                voice_counts[voice] = []
            voice_counts[voice].append(conv)
        
        for voice, works in voice_counts.items():
            print(f"   • {voice}: {len(works)} work{'s' if len(works) > 1 else ''}")
            primary_work = works[0]
            print(f"     - Role: {primary_work['role']}")
            print(f"     - Domains: {', '.join(primary_work['domains'][:3])}")
        
        print()
        print("🏛️ CHAMBER TRANSFORMATION:")
        
        critical_voices = [c['voice'] for c in successful_conversions if c['priority'] == 'CRITICAL']
        if critical_voices:
            print(f"   🔥 Critical voices added: {len(critical_voices)}")
            for voice in set(critical_voices):
                print(f"      - {voice}")
        
        print(f"   📈 Chamber completion significantly enhanced")
        print(f"   🌐 New intellectual domains activated")
        print(f"   🎪 Enhanced narrative and semiotic capabilities")
        print()
        
        print("🌉 NEW DIALECTICAL POSSIBILITIES:")
        if 'Umberto Eco' in [c['voice'] for c in successful_conversions]:
            print("   • Eco ↔ Benjamin: Signs, stories, and cultural criticism")
            print("   • Eco ↔ Berger: Ways of seeing and semiotics")
        if 'Jorge Luis Borges' in [c['voice'] for c in successful_conversions]:
            print("   • Borges ↔ Benjamin: Infinite libraries and archives")
            print("   • Borges ↔ Bachelard: Labyrinthine space and imagination")
        if 'T.S. Eliot' in [c['voice'] for c in successful_conversions]:
            print("   • Eliot ↔ Heidegger: Time, being, and poetic dwelling")
            print("   • Eliot ↔ Weil: Spiritual quest and attention")
        print()
    
    if failed_conversions:
        print("❌ CONVERSION FAILURES:")
        for failure in failed_conversions:
            print(f"   • {failure['voice']}: {failure['filename']}")
        print()
    
    print("📋 NEXT STEPS:")
    print("   1. Run: python3 chamber_amphitheater_status.py")
    print("   2. Update Chamber voice constellation to include new voices")
    print("   3. Test enhanced narrative and semiotic dialogues")
    
    return len(successful_conversions)

if __name__ == "__main__":
    print("🏛️ CHAMBER VOICE ACTIVATION PROCESS")
    print("=" * 55)
    print("Converting works to activate specific Chamber voices")
    print("Priority: Umberto Eco, Borges, Eliot, and other critical voices")
    print()
    
    converted_count = convert_chamber_voice_works()
    
    print(f"\n✨ Chamber voice activation complete!")
    print(f"🎭 {converted_count} voices activated")
    print(f"🏛️ The Chamber constellation has been significantly expanded!")