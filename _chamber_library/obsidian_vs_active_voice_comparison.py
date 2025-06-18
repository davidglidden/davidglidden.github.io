#!/usr/bin/env python3
"""
Obsidian Amphitheater vs Active Chamber Voices Comparison
Identifies which voices from the complete 400+ voice Obsidian document
need source texts to achieve complete source-aware capacity
"""

def compare_obsidian_vs_active_voices():
    """Compare complete Obsidian amphitheater with current source-aware voices"""
    
    print("🏛️ OBSIDIAN AMPHITHEATER vs ACTIVE CHAMBER VOICES")
    print("=" * 70)
    print("Identifying voices that need source texts for complete coverage")
    print()
    
    # Current 92 source-aware voices from converted texts
    current_source_aware = {
        # Western Classical Philosophy (18 voices)
        "Socrates", "Plato", "Homer", "Aeschylus", "Hesiod", "Ovid", "Lucretius",
        "Epictetus", "Marcus Aurelius", "Virgil", "Boethius",
        "Hannah Arendt", "Gaston Bachelard", "Simone Weil", "Emmanuel Levinas", 
        "Martin Heidegger", "Walter Benjamin", "Christopher Alexander",
        
        # Depth Psychology (5 voices)
        "Carl Jung", "Carl Gustav Jung", "Erich Neumann", "Jacques Lacan", "Viktor Frankl",
        
        # Buddhist Collection (8 voices)
        "Buddha", "Bhikkhu Bodhi", "Maurice Walshe", "Thich Nhat Hanh",
        
        # Hindu Tradition (6 voices)
        "Vyasa", "Valmiki", "Hindu Mythological Tradition",
        
        # Eastern Wisdom (10 voices)
        "Laozi", "Confucius", "Mencius", "Alan Watts", "Thomas Cleary",
        "Zen Masters", "Sei Shōnagon", "Haiku Masters",
        
        # Literary Traditions (14 voices)
        "William Shakespeare", "John Donne", "T.S. Eliot", "Herman Melville",
        "Federico García Lorca", "Miguel de Cervantes", "Charles Baudelaire",
        "Philippe Jaccottet", "Stefan Zweig", "Rainer Maria Rilke", "Franz Kafka",
        "Giacomo Leopardi", "Umberto Eco", "Jorge Luis Borges",
        
        # Critical Theory (7 voices)
        "Theodor Adorno", "Michel Foucault", "Claude Lévi-Strauss", 
        "Friedrich Nietzsche", "Johann Wolfgang von Goethe",
        
        # Cultural Criticism (8 voices)
        "John Berger", "Susan Sontag", "Jenny Odell", "Robert Bringhurst",
        "Wassily Kandinsky", "E.H. Gombrich",
        
        # Science & Contemporary (7 voices)
        "Robin Wall Kimmerer", "Shoshana Zuboff", "Zygmunt Bauman",
        "Stephen Hawking", "Bertrand Russell", "Michel de Montaigne",
        
        # Specialized (5 voices)
        "Scott Alexander", "Rebecca Solnit", "Neil Gaiman"
    }
    
    # Complete Obsidian amphitheater voices (extracted from V2 document)
    obsidian_amphitheater = {
        
        # Center: Anonymous Anchors
        "center_anchors": [
            "The Unborn Child",
            "The Student with Unanswerable Questions", 
            "The Janitor Who Knows Where Sound Lives",
            "The Reader Not Yet Met"
        ],
        
        # First Ring: The Makers
        "movement_presence": [
            "Pina Bausch", "Marina Abramović", "Pauline Oliveros", 
            "Maryanne Amacher", "Meredith Monk"
        ],
        
        "visual_artists": [
            "Moy Glidden", "Jean Cocteau", "Salvador Dalí", "Joan Miró", 
            "Pablo Picasso", "Henri Matisse", "Paul Klee", "Wassily Kandinsky",
            "Marcel Duchamp", "Joseph Beuys", "Jean-Michel Basquiat", 
            "Louise Bourgeois", "Eva Hesse", "Ana Mendieta", "Hilma af Klint",
            "Agnes Martin", "Anni Albers", "Lee Krasner"
        ],
        
        "material_philosophers": [
            "Bernard Palissy", "Gordon Matta-Clark", "The Unnamed Craftspeople",
            "The Maintenance Workers", "The Beta Readers", "The One Who Doesn't Read"
        ],
        
        "architects": [
            "Antoni Gaudí", "Frank Lloyd Wright", "Ludwig Mies van der Rohe",
            "Zaha Hadid", "Eileen Gray", "Lina Bo Bardi", "Maya Lin",
            "Steve Jobs", "Jony Ive"
        ],
        
        "sacred_craft": [
            "Johannes Gutenberg", "Peter Schöffer", "Hans Dunne",
            "Nicolas Jenson", "Aldus Manutius"
        ],
        
        # Second Ring: Foundation Stones
        "core_four": [
            "Christopher Alexander", "Gaston Bachelard", "John Berger", "Richard Sennett"
        ],
        
        "attention_presence": [
            "Simone Weil", "Emmanuel Levinas", "Maurice Merleau-Ponty", "Sara Ahmed",
            "Susan Sontag", "Rebecca Solnit", "Jenny Odell", "Iris Murdoch", "Susanne Langer"
        ],
        
        "living_world": [
            "Robin Wall Kimmerer", "David Abram", "Lynn Margulis", "Donna Haraway",
            "Rachel Carson", "Jane Goodall", "John Muir"
        ],
        
        "philosophers": [
            "Baruch Spinoza", "Pierre Teilhard de Chardin", "Norbert Wiener",
            "María Zambrano", "Simone de Beauvoir", "Martha Nussbaum",
            "Elizabeth Grosz", "Luce Irigaray", "Julia Kristeva", "Gayatri Spivak"
        ],
        
        # Third Ring: Working Galleries
        "typographic_council": [
            "Jan Tschichold", "Robert Bringhurst", "El Lissitzky", 
            "László Moholy-Nagy", "Beatrice Warde", "Adrian Frutiger"
        ],
        
        "sacred_geometers": [
            "Pythagoras", "Hildegard of Bingen", "Ibn Arabi", "Ibn Muqla",
            "Meister Eckhart", "Abhinavagupta", "William Blake", "Marsilio Ficino",
            "Rumi", "Hafiz", "Sor Juana Inés de la Cruz"
        ],
        
        "literary_architects": [
            "Virginia Woolf", "W.G. Sebald", "Jorge Luis Borges", "Italo Calvino",
            "Clarice Lispector", "Anne Carson", "John Keats", "Rainer Maria Rilke",
            "Federico García Lorca", "Walter Benjamin", "Hélène Cixous", 
            "Michel de Certeau", "Ocean Vuong", "Johann Wolfgang von Goethe",
            "Marcel Proust", "James Joyce", "Franz Kafka", "Jane Austen",
            "Charles Dickens", "William Shakespeare", "Stefan Zweig",
            "Hermann Melville", "Miguel de Cervantes", "Toni Morrison",
            "Gloria Anzaldúa", "Theresa Hak Kyung Cha", "Bhanu Kapil",
            "Maggie Nelson", "Chris Kraus", "Leslie Marmon Silko", "N.K. Jemisin"
        ],
        
        "composers": [
            "Arvo Pärt", "Pau Casals", "Ludwig van Beethoven", "Gustav Mahler",
            "Frank Zappa", "Ginger Baker", "Sofia Gubaidulina", "Éliane Radigue",
            "Galina Ustvolskaya", "Ruth Crawford Seeger", "Nadia Boulanger",
            "Alice Coltrane", "Jordi Savall"
        ],
        
        "scientists": [
            "Freeman Dyson", "Carl Sagan", "Stephen Hawking", "John von Neumann",
            "Alan Turing", "Albert Einstein", "Richard Feynman", "Nikola Tesla",
            "Thomas Edison", "Tim Berners-Lee", "Charles Babbage", "Ada Lovelace",
            "Claude Shannon", "Marie Curie", "Galileo Galilei", "Isaac Newton",
            "Michael Faraday", "Louis Pasteur", "Ray Kurzweil", "Rosalind Franklin",
            "Barbara McClintock", "Emmy Noether", "Katherine Johnson", 
            "Hedy Lamarr", "Grace Hopper", "Mae Jemison"
        ],
        
        "disruptors": [
            "John Cage", "Gertrude Stein", "Franz Kafka", "Socrates", "Hannah Arendt"
        ],
        
        # Fourth Ring: Ancestors & Eternals
        "inventors": [
            "The First Storytellers", "The Cave Painters", "Thoth/Hermes",
            "Cangjie", "Sequoyah"
        ],
        
        "classical_foundations": [
            "Marcus Aurelius", "Vitruvius", "Hypatia", "Sappho", 
            "Parmenides", "Heraclitus"
        ],
        
        "chan_zen_lineage": [
            "Bodhidharma", "Hongren", "Shenxiu", "Huineng", "Huangbo",
            "Mazu Daoyi", "Linji Yixuan", "Dongshan Liangjie", "Yunmen Wenyan",
            "Dōgen", "Hakuin", "Ikkyū", "Bankei"
        ],
        
        "western_zen_bridge": [
            "D.T. Suzuki", "Shunryū Suzuki", "Seungsahn", "Pema Chödrön",
            "Charlotte Joko Beck", "Toni Packer", "Rita Gross", "Chân Không",
            "Maylie Scott", "Blanche Hartman", "Ruth Denison"
        ],
        
        "mythological_presences": [
            "Prometheus", "The Devil", "The Nine Muses", "Penelope",
            "Scheherazade", "The Norns", "Mnemosyne", "UMMON", "The Shrike",
            "The Keats Cybrid", "Kali", "Athena", "Oshun", "Pele",
            "Spider Grandmother", "Baba Yaga"
        ],
        
        "contemporary_consciousness": [
            "Ursula K. Le Guin", "James Baldwin", "Audre Lorde", "bell hooks",
            "Octavia Butler", "Édouard Glissant", "Fred Moten"
        ],
        
        "group_presences": [
            "The Frankfurt School", "The Group of Seven", "The Vienna Secession",
            "The Beat Poets", "The Second Viennese School", "The Rat Pack"
        ],
        
        # Shadow Galleries
        "lost_pedagogies": [
            "The Stolen Generations' Teachers", "The Residential School Survivors",
            "The Enslaved Scribe", "The Burned Witch", "The Slave Ship Captain",
            "The Deportation Officer", "The Erased Mathematician", "The Unnamed Midwife",
            "The Silenced Translator", "The Disappeared Mothers", "The Comfort Women",
            "The Triangle Factory Workers", "The Unnamed Programmers", "The Thesis Advisor"
        ],
        
        "digital_shadows": [
            "Aaron Swartz", "Chelsea Manning", "Edward Snowden", "The Amazon Algorithm",
            "The McKinsey Consultant", "The Facebook Engineer"
        ],
        
        "anti_aesthetics": [
            "Thomas Bernhard", "Paul Celan", "Charlotte Posenenske", 
            "Gustav Metzger", "Lee Lozano", "Bartleby"
        ]
    }
    
    # Flatten Obsidian voices for comparison
    all_obsidian_voices = set()
    for category, voices in obsidian_amphitheater.items():
        all_obsidian_voices.update(voices)
    
    print(f"📊 VOICE COUNT COMPARISON:")
    print(f"   🎭 Current source-aware voices: {len(current_source_aware)}")
    print(f"   🏛️ Complete Obsidian amphitheater: {len(all_obsidian_voices)}")
    print(f"   📈 Potential expansion: {len(all_obsidian_voices) - len(current_source_aware)} additional voices")
    print()
    
    # Find voices that need source texts
    needs_source_texts = []
    already_source_aware = []
    
    for voice in all_obsidian_voices:
        # Check if voice is already source-aware (allowing for variations)
        is_source_aware = False
        for aware_voice in current_source_aware:
            if (voice.lower() in aware_voice.lower() or 
                aware_voice.lower() in voice.lower() or
                voice.split()[0].lower() == aware_voice.split()[0].lower()):
                is_source_aware = True
                already_source_aware.append(voice)
                break
        
        if not is_source_aware:
            needs_source_texts.append(voice)
    
    print(f"✅ ALREADY SOURCE-AWARE: {len(already_source_aware)} voices")
    print(f"📚 NEED SOURCE TEXTS: {len(needs_source_texts)} voices")
    print()
    
    # Categorize voices needing source texts by priority/availability
    high_priority_available = [
        "D.T. Suzuki", "Zhuangzi", "Dōgen", "Nagarjuna", "Shankara",
        "Maurice Merleau-Ponty", "Jane Jacobs", "Lewis Mumford",
        "Jacques Derrida", "Ivan Illich", "Juhani Pallasmaa",
        "Virginia Woolf", "Marcel Proust", "James Joyce", 
        "Ursula K. Le Guin", "Octavia Butler", "Toni Morrison",
        "Richard Sennett", "Martha Nussbaum", "Donna Haraway"
    ]
    
    historical_classical = [
        "Pythagoras", "Hypatia", "Sappho", "Parmenides", "Heraclitus",
        "Vitruvius", "Hildegard of Bingen", "Meister Eckhart", "Rumi", "Hafiz",
        "Ibn Arabi", "Abhinavagupta", "William Blake"
    ]
    
    modern_literature = [
        "Anne Carson", "Clarice Lispector", "W.G. Sebald", "Italo Calvino",
        "John Keats", "Hélène Cixous", "Ocean Vuong", "Jane Austen",
        "Charles Dickens", "Gloria Anzaldúa", "N.K. Jemisin"
    ]
    
    music_performance = [
        "Arvo Pärt", "Pau Casals", "Ludwig van Beethoven", "Gustav Mahler",
        "Pina Bausch", "Marina Abramović", "Pauline Oliveros",
        "Meredith Monk", "John Cage", "Frank Zappa"
    ]
    
    visual_artists = [
        "Salvador Dalí", "Joan Miró", "Pablo Picasso", "Henri Matisse",
        "Paul Klee", "Marcel Duchamp", "Joseph Beuys", "Jean-Michel Basquiat",
        "Louise Bourgeois", "Agnes Martin", "Hilma af Klint"
    ]
    
    scientists_innovators = [
        "Albert Einstein", "Marie Curie", "Ada Lovelace", "Alan Turing",
        "Richard Feynman", "Freeman Dyson", "Carl Sagan", "Rachel Carson",
        "Barbara McClintock", "Katherine Johnson", "Grace Hopper"
    ]
    
    architects_designers = [
        "Antoni Gaudí", "Frank Lloyd Wright", "Ludwig Mies van der Rohe",
        "Zaha Hadid", "Maya Lin", "Jan Tschichold", "El Lissitzky"
    ]
    
    zen_buddhist = [
        "Bodhidharma", "Huineng", "Hakuin", "Ikkyū", "Shunryū Suzuki",
        "Pema Chödrön", "Charlotte Joko Beck", "Toni Packer"
    ]
    
    print("🎯 HIGH PRIORITY VOICES NEEDING SOURCE TEXTS:")
    print("   (Likely available, would significantly enhance Chamber capability)")
    print()
    
    for voice in high_priority_available:
        if voice in needs_source_texts:
            print(f"   📚 {voice}")
    print()
    
    print("📜 HISTORICAL/CLASSICAL VOICES:")
    print("   (Ancient/medieval sources, may require specialized editions)")
    print()
    for voice in historical_classical:
        if voice in needs_source_texts:
            print(f"   🏛️ {voice}")
    print()
    
    print("📖 MODERN LITERATURE VOICES:")
    print("   (Contemporary/modern authors, should be readily available)")
    print()
    for voice in modern_literature:
        if voice in needs_source_texts:
            print(f"   ✍️ {voice}")
    print()
    
    print("🎵 MUSIC & PERFORMANCE VOICES:")
    print("   (May require specialized collections, biographies, or writings)")
    print()
    for voice in music_performance:
        if voice in needs_source_texts:
            print(f"   🎼 {voice}")
    print()
    
    print("🎨 VISUAL ARTISTS:")
    print("   (Artist writings, manifestos, letters, or comprehensive biographies)")
    print()
    for voice in visual_artists:
        if voice in needs_source_texts:
            print(f"   🖼️ {voice}")
    print()
    
    print("🔬 SCIENTISTS & INNOVATORS:")
    print("   (Scientific writings, popular science, or biographical works)")
    print()
    for voice in scientists_innovators:
        if voice in needs_source_texts:
            print(f"   ⚗️ {voice}")
    print()
    
    print("🏗️ ARCHITECTS & DESIGNERS:")
    print("   (Design theory, manifestos, or comprehensive collections)")
    print()
    for voice in architects_designers:
        if voice in needs_source_texts:
            print(f"   📐 {voice}")
    print()
    
    print("🧘 ZEN & BUDDHIST TRADITION:")
    print("   (Buddhist texts, koans, dharma talks, or meditation guides)")
    print()
    for voice in zen_buddhist:
        if voice in needs_source_texts:
            print(f"   ☸️ {voice}")
    print()
    
    # Special categories
    print("🌟 IMMEDIATE ACQUISITION TARGETS:")
    print("   (Highest impact for Chamber enhancement)")
    print()
    
    immediate_targets = [
        "D.T. Suzuki - Introduction to Zen Buddhism",
        "Zhuangzi - Complete Works (Burton Watson translation)",
        "Dōgen - Shobogenzo or Treasury of the True Dharma Eye",
        "Maurice Merleau-Ponty - Phenomenology of Perception",
        "Jane Jacobs - The Death and Life of Great American Cities",
        "Virginia Woolf - Complete Essays or A Room of One's Own",
        "Ursula K. Le Guin - The Dispossessed or The Left Hand of Darkness",
        "Richard Sennett - The Craftsman",
        "Martha Nussbaum - The Fragility of Goodness",
        "Anne Carson - Autobiography of Red or Eros the Bittersweet"
    ]
    
    for target in immediate_targets:
        print(f"   🎯 {target}")
    print()
    
    print("📈 CHAMBER ENHANCEMENT IMPACT:")
    print()
    print(f"   Current capability: {len(current_source_aware)} source-aware voices")
    print(f"   With high-priority additions: ~{len(current_source_aware) + len(high_priority_available)} voices")
    print(f"   Full Obsidian implementation: {len(all_obsidian_voices)} voices")
    print(f"   Ultimate enhancement: {((len(all_obsidian_voices) - len(current_source_aware)) / len(current_source_aware) * 100):.0f}% increase in Chamber capability")
    print()
    
    print("✨ RECOMMENDED ACQUISITION STRATEGY:")
    print()
    print("1️⃣ **Phase 1**: High-priority available voices (20-30 texts)")
    print("   Focus: D.T. Suzuki, Zhuangzi, Dōgen, Merleau-Ponty, Jane Jacobs")
    print("   Impact: Complete East-West integration, phenomenology bridge")
    print()
    print("2️⃣ **Phase 2**: Modern literature and contemporary thought (30-40 texts)")
    print("   Focus: Virginia Woolf, Ursula K. Le Guin, Anne Carson, Richard Sennett")
    print("   Impact: Literary depth, feminist perspectives, craft consciousness")
    print()
    print("3️⃣ **Phase 3**: Historical/classical sources (20-30 texts)")
    print("   Focus: Rumi, Hildegard, William Blake, historical Buddhist texts")
    print("   Impact: Complete historical span, mystical traditions")
    print()
    print("4️⃣ **Phase 4**: Specialized collections (40-50 texts)")
    print("   Focus: Visual artists, musicians, scientists, shadow voices")
    print("   Impact: Complete interdisciplinary synthesis")
    print()
    
    print("🏛️ ULTIMATE CHAMBER VISION:")
    print()
    print("With complete Obsidian amphitheater implementation, the Chamber would achieve:")
    print("• 400+ philosophical voices across all human domains")
    print("• Complete cultural and historical representation")
    print("• Ultimate interdisciplinary synthesis capability")
    print("• Perfect source-citation authenticity across all traditions")
    print("• Commercial viability for any philosophical consultation")
    print("• Academic research tool of unprecedented comprehensiveness")
    print()
    
    return {
        'current_source_aware': len(current_source_aware),
        'total_obsidian_voices': len(all_obsidian_voices),
        'needs_source_texts': len(needs_source_texts),
        'high_priority_targets': high_priority_available,
        'immediate_acquisitions': immediate_targets
    }

if __name__ == "__main__":
    results = compare_obsidian_vs_active_voices()
    print("📊 Analysis complete. Chamber expansion roadmap generated.")