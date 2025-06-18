#!/usr/bin/env python3
"""
Chamber Amphitheater Status
Visual representation of which voices have source-aware capacity vs empty seats
"""

import csv
from pathlib import Path
from collections import defaultdict

def get_current_voice_status():
    """Analyze which voices have actual source texts vs are just hollow names"""
    
    # Read converted texts to see who actually has source material
    converted_dir = Path("converted_texts")
    voice_texts = defaultdict(list)
    
    if converted_dir.exists():
        for md_file in converted_dir.glob("*.md"):
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract YAML frontmatter
                if content.startswith('---\n'):
                    yaml_end = content.find('\n---\n', 4)
                    if yaml_end > 0:
                        yaml_content = content[4:yaml_end]
                        lines = yaml_content.split('\n')
                        
                        author = None
                        title = None
                        voice = None
                        
                        for line in lines:
                            if line.startswith('author:'):
                                author = line.split(':', 1)[1].strip().strip('"\'')
                            elif line.startswith('title:'):
                                title = line.split(':', 1)[1].strip().strip('"\'')
                            elif line.startswith('voice:'):
                                voice = line.split(':', 1)[1].strip().strip('"\'')
                        
                        if voice and title:
                            voice_texts[voice].append(title)
                        elif author and title:
                            voice_texts[author].append(title)
                            
            except Exception as e:
                continue
    
    return voice_texts

def create_amphitheater_visualization():
    """Create visual amphitheater representation of Chamber voices"""
    
    voice_texts = get_current_voice_status()
    
    # Complete Chamber amphitheater seating arrangement
    amphitheater = {
        # Core Western Philosophical Voices (Center Ring)
        'center_ring': [
            ('Gaston Bachelard', 'Phenomenologist of Space'),
            ('Hannah Arendt', 'Political Philosopher'), 
            ('Simone Weil', 'Mystic of Attention'),
            ('Emmanuel Levinas', 'Philosopher of the Face'),
            ('Martin Heidegger', 'Philosopher of Being'),
            ('Walter Benjamin', 'Critical Theorist'),
        ],
        
        # Contemporary and Applied Voices (Second Ring)
        'second_ring': [
            ('Christopher Alexander', 'Architect of Patterns'),
            ('John Berger', 'Critic of Ways of Seeing'),
            ('Carl Jung', 'Depth Psychologist'),
            ('Robin Wall Kimmerer', 'Indigenous Scientist'),
            ('Shoshana Zuboff', 'Surveillance Capitalism Critic'),
            ('Aldus Manutius', 'Master of Typography'),
        ],
        
        # Eastern Wisdom Traditions (Third Ring)
        'third_ring': [
            ('Laozi', 'Sage of the Way'),
            ('Zhuangzi', 'Master of Transformation'),
            ('Nagarjuna', 'Philosopher of Emptiness'),
            ('Dogen', 'Zen Master of Being-Time'),
            ('Huang Po', 'Chan Master of No-Mind'),
            ('Shankara', 'Advaita Philosopher'),
        ],
        
        # Contemporary Eastern and Bridge Voices (Fourth Ring)
        'fourth_ring': [
            ('Thich Nhat Hanh', 'Engaged Buddhist'),
            ('D.T. Suzuki', 'East-West Bridge'),
            ('Krishnamurti', 'Radical Questioner'),
            ('Confucius', 'Teacher of Social Harmony'),
            ('Mencius', 'Moral Philosopher'),
            ('Ramanuja', 'Devotional Philosopher'),
        ],
        
        # Extended Constellation (Outer Ring)
        'outer_ring': [
            ('Maurice Merleau-Ponty', 'Phenomenologist of Perception'),
            ('Jane Jacobs', 'Urban Life Observer'),
            ('Lewis Mumford', 'Technology Critic'),
            ('Jacques Derrida', 'Deconstructionist'),
            ('Juhani Pallasmaa', 'Phenomenological Architect'),
            ('Ivan Illich', 'Convivial Tools Theorist'),
        ]
    }
    
    def get_voice_status(voice_name):
        """Determine if voice has source-aware capacity"""
        # Direct match
        if voice_name in voice_texts and voice_texts[voice_name]:
            return 'SOURCE_AWARE', len(voice_texts[voice_name])
        
        # Check for partial matches (different name formats)
        for existing_voice in voice_texts:
            if voice_name.split()[-1].lower() in existing_voice.lower():
                return 'SOURCE_AWARE', len(voice_texts[existing_voice])
            if existing_voice.split()[-1].lower() in voice_name.lower():
                return 'SOURCE_AWARE', len(voice_texts[existing_voice])
        
        return 'EMPTY_SEAT', 0
    
    with open("chamber_amphitheater_status.md", "w") as f:
        f.write("# The Chamber Amphitheater: Voice Status Map\n\n")
        f.write("*Visual representation of which voices have source-aware capacity vs empty seats*\n\n")
        
        f.write("## Legend\n")
        f.write("- **🎭 SOURCE-AWARE** = Voice has converted texts available for citations\n")
        f.write("- **👻 EMPTY SEAT** = Voice exists in concept only, no source texts\n")
        f.write("- **Numbers** = Count of available texts for source-aware voices\n\n")
        
        f.write("---\n\n")
        
        # Process each ring
        for ring_name, voices in amphitheater.items():
            ring_display = ring_name.replace('_', ' ').title()
            f.write(f"## {ring_display}\n\n")
            
            source_aware_count = 0
            empty_seat_count = 0
            
            for voice_name, voice_role in voices:
                status, text_count = get_voice_status(voice_name)
                
                if status == 'SOURCE_AWARE':
                    source_aware_count += 1
                    f.write(f"🎭 **{voice_name}** ({text_count} texts) - *{voice_role}*  \n")
                    f.write(f"   ✅ **SOURCE-AWARE CAPACITY ACTIVE**  \n")
                    if voice_name in voice_texts:
                        key_texts = voice_texts[voice_name][:3]  # Show first 3 texts
                        f.write(f"   📚 Key texts: {', '.join(key_texts)}")
                        if len(voice_texts[voice_name]) > 3:
                            f.write(f" (+{len(voice_texts[voice_name])-3} more)")
                        f.write("  \n")
                else:
                    empty_seat_count += 1
                    f.write(f"👻 **{voice_name}** - *{voice_role}*  \n")
                    f.write(f"   ❌ **EMPTY SEAT** - No source texts available  \n")
                
                f.write("  \n")
            
            # Ring summary
            total_voices = len(voices)
            completion_percent = (source_aware_count / total_voices) * 100
            f.write(f"**{ring_display} Status**: {source_aware_count}/{total_voices} voices active ({completion_percent:.1f}%)  \n")
            f.write("  \n")
            f.write("---\n\n")
        
        # Overall amphitheater summary
        total_voices = sum(len(voices) for voices in amphitheater.values())
        total_source_aware = 0
        total_empty = 0
        
        for ring_name, voices in amphitheater.items():
            for voice_name, voice_role in voices:
                status, text_count = get_voice_status(voice_name)
                if status == 'SOURCE_AWARE':
                    total_source_aware += 1
                else:
                    total_empty += 1
        
        f.write("## Chamber Amphitheater Summary\n\n")
        f.write(f"**Total Seats**: {total_voices}  \n")
        f.write(f"**🎭 Source-Aware Voices**: {total_source_aware}  \n")
        f.write(f"**👻 Empty Seats**: {total_empty}  \n")
        f.write(f"**Amphitheater Completion**: {(total_source_aware/total_voices)*100:.1f}%  \n\n")
        
        # Readiness by domain
        f.write("## Readiness by Philosophical Domain\n\n")
        
        domains = {
            'Western Classical': ['Gaston Bachelard', 'Hannah Arendt', 'Simone Weil', 'Emmanuel Levinas', 'Martin Heidegger', 'Walter Benjamin'],
            'Contemporary Western': ['Christopher Alexander', 'John Berger', 'Carl Jung', 'Robin Wall Kimmerer', 'Shoshana Zuboff', 'Aldus Manutius'],
            'Eastern Traditional': ['Laozi', 'Zhuangzi', 'Nagarjuna', 'Dogen', 'Huang Po', 'Shankara'],
            'Contemporary Eastern': ['Thich Nhat Hanh', 'D.T. Suzuki', 'Krishnamurti', 'Confucius', 'Mencius', 'Ramanuja'],
            'Extended Bridge Voices': ['Maurice Merleau-Ponty', 'Jane Jacobs', 'Lewis Mumford', 'Jacques Derrida', 'Juhani Pallasmaa', 'Ivan Illich']
        }
        
        for domain_name, domain_voices in domains.items():
            active_in_domain = 0
            for voice in domain_voices:
                status, _ = get_voice_status(voice)
                if status == 'SOURCE_AWARE':
                    active_in_domain += 1
            
            domain_percent = (active_in_domain / len(domain_voices)) * 100
            status_icon = "🟢" if domain_percent >= 70 else "🟡" if domain_percent >= 30 else "🔴"
            
            f.write(f"{status_icon} **{domain_name}**: {active_in_domain}/{len(domain_voices)} ({domain_percent:.1f}%)  \n")
        
        f.write("\n")
        
        # Critical gaps
        f.write("## Critical Empty Seats (High Impact)\n\n")
        
        critical_missing = []
        for ring_name, voices in amphitheater.items():
            for voice_name, voice_role in voices:
                status, _ = get_voice_status(voice_name)
                if status == 'EMPTY_SEAT':
                    # Determine criticality
                    if voice_name in ['Laozi', 'Dogen', 'Nagarjuna', 'Aldus Manutius']:
                        critical_missing.append((voice_name, voice_role, 'CRITICAL'))
                    elif voice_name in ['Zhuangzi', 'Thich Nhat Hanh', 'Maurice Merleau-Ponty', 'Jane Jacobs']:
                        critical_missing.append((voice_name, voice_role, 'HIGH'))
        
        if critical_missing:
            f.write("**Most needed for Chamber completion**:\n\n")
            for voice, role, priority in critical_missing:
                priority_icon = "🔥" if priority == 'CRITICAL' else "🟡"
                f.write(f"{priority_icon} **{voice}** - *{role}* ({priority} priority)  \n")
        
        f.write("\n")
        
        # Dialectical readiness
        f.write("## Dialectical Readiness Assessment\n\n")
        
        f.write("**Currently Possible Dialogues**:\n")
        possible_dialogues = [
            "🎭 Bachelard ↔ Berger ↔ Benjamin (Space, Seeing, Experience)",
            "🎭 Arendt ↔ Weil ↔ Zuboff (Politics, Attention, Power)",
            "🎭 Heidegger ↔ Alexander ↔ Kimmerer (Being, Patterns, Ecology)",
            "🎭 Jung ↔ Weil ↔ Bachelard (Psychology, Spirituality, Imagination)"
        ]
        
        for dialogue in possible_dialogues:
            f.write(f"- {dialogue}  \n")
        
        f.write("\n**Missing Critical Dialogues**:\n")
        missing_dialogues = [
            "👻 Eastern-Western Integration (Need: Laozi, Dogen, Nagarjuna)",
            "👻 Typography-Design Wisdom (Need: Aldus Manutius)",
            "👻 Urban-Pattern Dialogue (Need: Jane Jacobs)",
            "👻 Phenomenological Bridge (Need: Merleau-Ponty)"
        ]
        
        for dialogue in missing_dialogues:
            f.write(f"- {dialogue}  \n")
        
        f.write("\n")
        
        # Next phase recommendations
        f.write("## Next Phase Recommendations\n\n")
        f.write("**Phase 1: Fill Critical Empty Seats** (4-6 acquisitions)  \n")
        f.write("- Focus on Laozi, Dogen, Aldus Manutius, Merleau-Ponty  \n")
        f.write("- Enables East-West integration and completes core domains  \n\n")
        
        f.write("**Phase 2: Expand Eastern Representation** (6-8 acquisitions)  \n")
        f.write("- Add remaining Buddhist, Taoist, and Vedantic voices  \n")
        f.write("- Achieves global philosophical representation  \n\n")
        
        f.write("**Phase 3: Complete Extended Constellation** (remaining seats)  \n")
        f.write("- Fill specialized and bridge voices  \n")
        f.write("- Achieves maximum dialectical richness  \n\n")
        
        f.write("---\n\n")
        f.write("*The Chamber amphitheater shows both our achievements and remaining work.*  \n")
        f.write(f"*Current status: {total_source_aware} voices speaking, {total_empty} seats awaiting their texts.*\n")
    
    print("📄 Amphitheater status saved to: chamber_amphitheater_status.md")
    
    # Quick console summary
    print(f"\n🏛️ CHAMBER AMPHITHEATER STATUS:")
    print(f"   🎭 Source-aware voices: {total_source_aware}")
    print(f"   👻 Empty seats: {total_empty}")
    print(f"   📊 Completion: {(total_source_aware/total_voices)*100:.1f}%")
    
    return voice_texts, total_source_aware, total_empty

if __name__ == "__main__":
    print("🏛️ MAPPING CHAMBER AMPHITHEATER STATUS")
    print("=" * 60)
    
    voice_texts, active_voices, empty_seats = create_amphitheater_visualization()
    
    print(f"\n✨ Amphitheater status map complete!")
    print(f"📋 See chamber_amphitheater_status.md for full visualization")