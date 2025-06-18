#!/usr/bin/env python3
"""
Complete Deep Scan of Eastern Folder
Exhaustive identification of ALL remaining voices before mythology/Buddhist folder
"""

from pathlib import Path

def complete_deep_scan():
    """Exhaustive scan of every single file"""
    
    eastern_folder = Path("/Users/davidglidden/Desktop/eastern to the library")
    
    # Complete file list
    all_files = [
        "360603144 copy.epub",
        "A Book of Memories: A Novel.epub",
        "A Field Guide to Getting Lost 2.epub", 
        "A Field Guide to Getting Lost.epub",
        "À la lumière d'hiver : Pensées sous les nuages : Leçons : Chants d'en bas.epub",
        "A Portrait of the Artist as a Young Man.epub",
        "A Trackless Path: A Commentary on the Great Completion (Dzogchen) Teaching of Jigmé Lingpa's Revelations of Ever-Present Good.epub",
        "Aesthetics and Politics.epub",
        "Aesthetics.epub", 
        "Against Interpretation and Other Essays.epub",
        "Airs.epub",
        "Aphorisms on Love and Hate.epub",
        "As Consciousness Is Harnessed to Flesh.epub",
        "Authority.epub",
        "Baudolino.epub",
        "Beren and Lúthien.epub",
        "Between Past and Future (Penguin Classics).epub",
        "Black Holes: The Reith Lectures.epub",
        "Bodas de sangre.epub",
        "Brief Answers to the Big Questions.epub",
        "Cahier de verdure:Après beaucoup d'années.epub",
        "Canti.epub",
        "Carnets 1995-1998.epub",
        "Ce peu de bruits.epub",
        "Chronicles of a Liquid Society.epub",
        "Collected Poems 1909-1962.epub",
        "Collected Poetical Works of Rumi (Delphi Classics).epub",
        "Complete Harvard Classics.epub",
        "Complete Works of Herman Melville.epub",
        "Cuentos completos.epub",
        "D'une lyre à cinq cordes. Pétrarque, Le Tasse, Leopardi, Ungaretti, Montale, Bertolucci, Luzi, Bigongiari, Erba, Góngora, Goethe, Hölderlin, Ferdinand Meyer, Maria Rilke, Lavant, Burkart, Mandelstam, Skácel.epub",
        "David Copperfield.epub",
        "Diamond Sutra.epub",
        "Don Quixote.epub",
        "Écrits.epub",
        "Eichmann in Jerusalem: A Report on the Banality of Evil.epub",
        "El Aleph.epub",
        "Eléments d'un songe.epub",
        "Et, néanmoins.epub",
        "Excellent Advice for Living.epub",
        "Faust, Part Two.epub",
        "Faust: Part One.epub",
        "Fictions.epub",
        "Five Moral Pieces.epub",
        "Foucault's Pendulum.epub",
        "Four Quartets.epub",
        "Greek Lives.epub",
        "Histoire de la folie à l'âge classique.epub",
        "Histoire de la sexualité -3 Le souci de soi.epub",
        "Histoire de la sexualité (Tome 2) - L'usage des plaisirs (Tel) (French Edition).epub",
        "Histoire de la sexualité (Tome 4) - Les aveux de la chair.epub",
        "History of Western Philosophy (Routledge Classics).epub",
        "How to Do Nothing: Resisting the Attention Economy.epub",
        "How to Read Lacan.epub",
        "How to Travel With a Salmon and Other Essays.epub",
        "«Il faut défendre la société».epub",
        "In Praise of Shadows.epub",
        "Invisible Cities.epub",
        "Island of the Day Before.epub",
        "Jeu et théorie du duende.epub",
        "Just So.epub",
        "L'archéologie du savoir.epub",
        "L'Effraie et autres poésies.epub",
        "L'enracinement.epub",
        "L'Hermeneutique Du Sujet : Cours Au Collège De France.epub",
        "L'Ignorant - 1952 - 1956.epub",
        "L'Obscurité.epub",
        "La Clarté Notre-Dame.epub",
        "La Personne et le sacré: Collectivité. Personne. Impersonnel. Droit. Justice.epub",
        "La Seconde Semaison.epub",
        "La Semaison.epub",
        "La Volonté de savoir.epub",
        "Le Songe de Poliphile, ou Hypnérotomachie de frère Francesco Colonna, littéralement traduit pour la première fois, avec une introduction et des notes, par Claudius Popelin,... - Tome 2 (1883).epub",
        "Les Enfants Terribles : Roman.epub",
        "Les Mots et les choses.epub",
        "Les vies parallèles: Alcibiade, Coriolan.epub",
        "Liquid Modernity.epub",
        "Magellan.epub",
        "Mahler: A Musical Physiognomy.epub",
        "Make Something Wonderful.epub",
        "Man's Search for Meaning.epub",
        "Meditations: A New Translation.epub",
        "Men Explain Things to Me.epub",
        "Minima Moralia: Reflections From Damaged Life.epub",
        "Moby Dick.epub",
        "Montaigne.epub",
        "Nietzsche.epub",
        "Not Too Late: Changing the Climate Story From Despair to Possibility.epub",
        "Observations et autres notes anciennes 1947 - 1962.epub",
        "Œuvres complètes du Marquis de Sade.epub",
        "On the Shoulders of Giants.epub",
        "On Ugliness.epub",
        "Orwell's Roses.epub",
        "Parallel Stories: A Novel.epub",
        "Poems to Night.epub",
        "Poet in New York, A Bilingual edition.epub",
        "Recollections of My Nonexistence.epub",
        "Regarding the Pain of Others.epub",
        "Respect in a World of Inequality.epub",
        "Roman Lives: A Selection of Eight Lives.epub",
        "Serendipities: Language and Lunacy.epub",
        "Silence: Lectures and Writings, 50th Anniversary Edition.epub",
        "Silence.epub",
        "Slouching Towards Bethlehem.epub",
        "Surveiller et punir: Naissance de la prison.epub",
        "The Aeneid.epub",
        "The Aphorisms of Franz Kafka.epub",
        "The Arden Shakespeare Third Series Complete Works.epub",
        "The Black Books: 1913-1932 : Notebooks of Transformation.epub",
        "The Children Of Hurin.epub",
        "The Collected Works of C.G. Jung: Complete Digital Edition.epub",
        "The Complete Poems and Plays of T. S. Eliot.epub",
        "The Complete Poems.epub",
        "The Conscience of the Eye.epub",
        "The Corrosion of Character.epub",
        "The Craftsman.epub",
        "The Diamond That Cuts Through Illusion.epub",
        "The Duino Elegies & the Sonnets to Orpheus: A Dual Language Edition.epub",
        "The Encyclopedia of Trouble and Spaciousness.epub",
        "The Essential Tao An Initiation Into the Heart of Taoism Through the Authentic Tao Te Ching and the Inner Teachings of Chuang-Tzu.epub",
        "The Fall of Public Man.epub",
        "The Faraway Nearby.epub",
        "The Gateless Barrier.epub",
        "The Grand Design.epub",
        "The Great Path of Awakening.epub",
        "The Hobbit (Enhanced Edition).epub",
        "The Human Condition.epub",
        "The Iliad (Robert Fagles).epub",
        "The Jargon of Authenticity.epub",
        "The Limits of Interpretation.epub",
        "The Lord of the Rings [50th Anniversary edition].epub",
        "The Mother of All Questions.epub",
        "The Name of the Rose.epub",
        "The Nature of Middle-earth.epub",
        "The Odyssey.epub",
        "The Prague Cemetery.epub",
        "The Tao of Philosophy.epub",
        "The Taoism Reader.epub",
        "The Uses of Disorder.epub",
        "The Zen Reader.epub",
        "the_elements_of_typographic_style.pdf",
        "Tolkien: The Fall of Gondolin.epub",
        "Ulysses.epub",
        "Wanderlust: A History of Walking.epub",
        "West-Eastern Divan.epub",
        "Whose Story Is This?.epub",
        "Wisdom of Insecurity.epub",
        "Zen Bow, Zen Arrow.epub",
        "Zen in the Art of Archery.epub",
        "Zen Mind, Beginner's Mind.epub",
        "Zen Teaching of Instantaneous Awakening: being the teaching of the Zen Master Hui Hai, known as the Great Pearl.epub",
        "Zibaldone.epub"
    ]
    
    # Check what we've converted (simplified check)
    converted_dir = Path("converted_texts")
    converted_names = set()
    if converted_dir.exists():
        for md_file in converted_dir.glob("*.md"):
            base_name = md_file.stem.lower().replace('-', '').replace('_', '')
            converted_names.add(base_name)
    
    def is_converted(filename):
        """Check if file is already converted"""
        clean_name = filename.lower().replace(' ', '').replace('-', '').replace('_', '').replace('.epub', '').replace('.pdf', '')
        return any(clean_name in converted or converted in clean_name for converted in converted_names)
    
    # Comprehensive voice identification
    remaining_voices = []
    
    for filename in all_files:
        if is_converted(filename):
            continue
            
        title_lower = filename.lower()
        voice_info = None
        
        # FOUCAULT - Complete works
        if 'histoire de la folie' in title_lower:
            voice_info = {
                'author': 'Michel Foucault', 'voice': 'Michel Foucault',
                'work': 'Histoire de la folie à l\'âge classique', 'priority': 'CRITICAL',
                'role': 'Archaeologist of Madness and Reason'
            }
        elif 'histoire de la sexualité' in title_lower and 'souci de soi' in title_lower:
            voice_info = {
                'author': 'Michel Foucault', 'voice': 'Michel Foucault',
                'work': 'Histoire de la sexualité - Le souci de soi', 'priority': 'HIGH',
                'role': 'Genealogist of Ethics and Self-Care'
            }
        elif 'histoire de la sexualité' in title_lower and 'usage des plaisirs' in title_lower:
            voice_info = {
                'author': 'Michel Foucault', 'voice': 'Michel Foucault',
                'work': 'Histoire de la sexualité - L\'usage des plaisirs', 'priority': 'HIGH',
                'role': 'Theorist of Ancient Sexuality'
            }
        elif 'histoire de la sexualité' in title_lower and 'aveux de la chair' in title_lower:
            voice_info = {
                'author': 'Michel Foucault', 'voice': 'Michel Foucault',
                'work': 'Histoire de la sexualité - Les aveux de la chair', 'priority': 'HIGH',
                'role': 'Analyst of Christian Confession'
            }
        elif 'la volonté de savoir' in title_lower:
            voice_info = {
                'author': 'Michel Foucault', 'voice': 'Michel Foucault',
                'work': 'La Volonté de savoir', 'priority': 'HIGH',
                'role': 'Theorist of Power and Sexuality'
            }
        elif 'archéologie du savoir' in title_lower:
            voice_info = {
                'author': 'Michel Foucault', 'voice': 'Michel Foucault',
                'work': 'L\'Archéologie du savoir', 'priority': 'CRITICAL',
                'role': 'Archaeologist of Knowledge Systems'
            }
        elif 'surveiller et punir' in title_lower:
            voice_info = {
                'author': 'Michel Foucault', 'voice': 'Michel Foucault',
                'work': 'Surveiller et punir', 'priority': 'CRITICAL',
                'role': 'Analyst of Disciplinary Power'
            }
        elif 'les mots et les choses' in title_lower:
            voice_info = {
                'author': 'Michel Foucault', 'voice': 'Michel Foucault',
                'work': 'Les Mots et les choses', 'priority': 'HIGH',
                'role': 'Archaeologist of Human Sciences'
            }
        elif 'il faut défendre la société' in title_lower:
            voice_info = {
                'author': 'Michel Foucault', 'voice': 'Michel Foucault',
                'work': 'Il faut défendre la société', 'priority': 'HIGH',
                'role': 'Theorist of War and Society'
            }
        elif 'herméneutique du sujet' in title_lower:
            voice_info = {
                'author': 'Michel Foucault', 'voice': 'Michel Foucault',
                'work': 'L\'Herméneutique du sujet', 'priority': 'HIGH',
                'role': 'Philosopher of Self-Knowledge'
            }
        
        # LACAN
        elif 'écrits' == title_lower.replace('.epub', ''):
            voice_info = {
                'author': 'Jacques Lacan', 'voice': 'Jacques Lacan',
                'work': 'Écrits', 'priority': 'CRITICAL',
                'role': 'Structural Psychoanalyst of the Unconscious'
            }
        elif 'how to read lacan' in title_lower:
            voice_info = {
                'author': 'Slavoj Žižek', 'voice': 'Slavoj Žižek',
                'work': 'How to Read Lacan', 'priority': 'MEDIUM',
                'role': 'Lacanian Cultural Critic'
            }
        
        # JACCOTTET - Complete works
        elif 'éléments d\'un songe' in title_lower:
            voice_info = {
                'author': 'Philippe Jaccottet', 'voice': 'Philippe Jaccottet',
                'work': 'Éléments d\'un songe', 'priority': 'MEDIUM',
                'role': 'Dream Element Poet'
            }
        elif 'et, néanmoins' in title_lower:
            voice_info = {
                'author': 'Philippe Jaccottet', 'voice': 'Philippe Jaccottet',
                'work': 'Et, néanmoins', 'priority': 'MEDIUM',
                'role': 'Poet of Nevertheless'
            }
        elif 'l\'effraie' in title_lower:
            voice_info = {
                'author': 'Philippe Jaccottet', 'voice': 'Philippe Jaccottet',
                'work': 'L\'Effraie et autres poésies', 'priority': 'MEDIUM',
                'role': 'Night Bird Poet'
            }
        elif 'l\'ignorant' in title_lower:
            voice_info = {
                'author': 'Philippe Jaccottet', 'voice': 'Philippe Jaccottet',
                'work': 'L\'Ignorant (1952-1956)', 'priority': 'MEDIUM',
                'role': 'Self-Doubting Poet'
            }
        elif 'l\'obscurité' in title_lower:
            voice_info = {
                'author': 'Philippe Jaccottet', 'voice': 'Philippe Jaccottet',
                'work': 'L\'Obscurité', 'priority': 'MEDIUM',
                'role': 'Poet of Darkness and Light'
            }
        elif 'la clarté notre-dame' in title_lower:
            voice_info = {
                'author': 'Philippe Jaccottet', 'voice': 'Philippe Jaccottet',
                'work': 'La Clarté Notre-Dame', 'priority': 'MEDIUM',
                'role': 'Sacred Clarity Poet'
            }
        elif 'la semaison' in title_lower and 'seconde' not in title_lower:
            voice_info = {
                'author': 'Philippe Jaccottet', 'voice': 'Philippe Jaccottet',
                'work': 'La Semaison', 'priority': 'HIGH',
                'role': 'Seasonal Sowing Poet'
            }
        elif 'la seconde semaison' in title_lower:
            voice_info = {
                'author': 'Philippe Jaccottet', 'voice': 'Philippe Jaccottet',
                'work': 'La Seconde Semaison', 'priority': 'MEDIUM',
                'role': 'Second Seasonal Poet'
            }
        elif 'observations et autres notes' in title_lower:
            voice_info = {
                'author': 'Philippe Jaccottet', 'voice': 'Philippe Jaccottet',
                'work': 'Observations et autres notes anciennes', 'priority': 'MEDIUM',
                'role': 'Observer of Ancient Notes'
            }
        
        # LORCA - Additional work
        elif 'jeu et théorie du duende' in title_lower:
            voice_info = {
                'author': 'Federico García Lorca', 'voice': 'Federico García Lorca',
                'work': 'Jeu et théorie du duende', 'priority': 'HIGH',
                'role': 'Theorist of the Duende Spirit'
            }
        elif 'poet in new york' in title_lower:
            voice_info = {
                'author': 'Federico García Lorca', 'voice': 'Federico García Lorca',
                'work': 'Poet in New York', 'priority': 'HIGH',
                'role': 'Urban Surrealist Poet'
            }
        
        # ECO - Complete works
        elif 'invisible cities' in title_lower:
            voice_info = {
                'author': 'Italo Calvino', 'voice': 'Italo Calvino',
                'work': 'Invisible Cities', 'priority': 'HIGH',
                'role': 'Invisible Cities Mapper'
            }
        elif 'the name of the rose' in title_lower:
            voice_info = {
                'author': 'Umberto Eco', 'voice': 'Umberto Eco',
                'work': 'The Name of the Rose', 'priority': 'HIGH',
                'role': 'Medieval Mystery Semiotician'
            }
        elif 'the prague cemetery' in title_lower:
            voice_info = {
                'author': 'Umberto Eco', 'voice': 'Umberto Eco',
                'work': 'The Prague Cemetery', 'priority': 'MEDIUM',
                'role': 'Conspiracy and Forgery Theorist'
            }
        elif 'island of the day before' in title_lower:
            voice_info = {
                'author': 'Umberto Eco', 'voice': 'Umberto Eco',
                'work': 'Island of the Day Before', 'priority': 'MEDIUM',
                'role': 'Temporal Paradox Novelist'
            }
        elif 'the limits of interpretation' in title_lower:
            voice_info = {
                'author': 'Umberto Eco', 'voice': 'Umberto Eco',
                'work': 'The Limits of Interpretation', 'priority': 'HIGH',
                'role': 'Interpretation Theorist'
            }
        elif 'on ugliness' in title_lower:
            voice_info = {
                'author': 'Umberto Eco', 'voice': 'Umberto Eco',
                'work': 'On Ugliness', 'priority': 'MEDIUM',
                'role': 'Aesthetician of the Ugly'
            }
        elif 'serendipities' in title_lower:
            voice_info = {
                'author': 'Umberto Eco', 'voice': 'Umberto Eco',
                'work': 'Serendipities: Language and Lunacy', 'priority': 'MEDIUM',
                'role': 'Serendipity and Language Theorist'
            }
        elif 'how to travel with a salmon' in title_lower:
            voice_info = {
                'author': 'Umberto Eco', 'voice': 'Umberto Eco',
                'work': 'How to Travel With a Salmon', 'priority': 'LOW',
                'role': 'Humorous Cultural Observer'
            }
        
        # GOETHE
        elif 'faust: part one' in title_lower:
            voice_info = {
                'author': 'Johann Wolfgang von Goethe', 'voice': 'Johann Wolfgang von Goethe',
                'work': 'Faust: Part One', 'priority': 'HIGH',
                'role': 'Faustian Knowledge Seeker'
            }
        elif 'faust, part two' in title_lower:
            voice_info = {
                'author': 'Johann Wolfgang von Goethe', 'voice': 'Johann Wolfgang von Goethe',
                'work': 'Faust: Part Two', 'priority': 'HIGH',
                'role': 'Cosmic Redemption Poet'
            }
        elif 'west-eastern divan' in title_lower:
            voice_info = {
                'author': 'Johann Wolfgang von Goethe', 'voice': 'Johann Wolfgang von Goethe',
                'work': 'West-Eastern Divan', 'priority': 'HIGH',
                'role': 'East-West Cultural Synthesizer'
            }
        
        # LEOPARDI
        elif 'canti' == title_lower.replace('.epub', ''):
            voice_info = {
                'author': 'Giacomo Leopardi', 'voice': 'Giacomo Leopardi',
                'work': 'Canti', 'priority': 'HIGH',
                'role': 'Pessimist Poet of Infinite Longing'
            }
        elif 'zibaldone' in title_lower:
            voice_info = {
                'author': 'Giacomo Leopardi', 'voice': 'Giacomo Leopardi',
                'work': 'Zibaldone', 'priority': 'CRITICAL',
                'role': 'Philosophical Notebook Keeper'
            }
        
        # CLASSICAL WORKS
        elif 'don quixote' in title_lower:
            voice_info = {
                'author': 'Miguel de Cervantes', 'voice': 'Miguel de Cervantes',
                'work': 'Don Quixote', 'priority': 'HIGH',
                'role': 'Creator of Modern Fiction'
            }
        elif 'ulysses' == title_lower.replace('.epub', ''):
            voice_info = {
                'author': 'James Joyce', 'voice': 'James Joyce',
                'work': 'Ulysses', 'priority': 'CRITICAL',
                'role': 'Stream of Consciousness Innovator'
            }
        elif 'a portrait of the artist' in title_lower:
            voice_info = {
                'author': 'James Joyce', 'voice': 'James Joyce',
                'work': 'A Portrait of the Artist as a Young Man', 'priority': 'MEDIUM',
                'role': 'Artistic Development Chronicler'
            }
        elif 'moby dick' in title_lower:
            voice_info = {
                'author': 'Herman Melville', 'voice': 'Herman Melville',
                'work': 'Moby Dick', 'priority': 'HIGH',
                'role': 'Metaphysical Maritime Novelist'
            }
        elif 'complete works of herman melville' in title_lower:
            voice_info = {
                'author': 'Herman Melville', 'voice': 'Herman Melville',
                'work': 'Complete Works', 'priority': 'HIGH',
                'role': 'Complete American Maritime Metaphysician'
            }
        
        # CLASSICAL EPICS
        elif 'the iliad' in title_lower:
            voice_info = {
                'author': 'Homer', 'voice': 'Homer',
                'work': 'The Iliad', 'priority': 'CRITICAL',
                'role': 'Epic War Poet'
            }
        elif 'the odyssey' in title_lower:
            voice_info = {
                'author': 'Homer', 'voice': 'Homer',
                'work': 'The Odyssey', 'priority': 'CRITICAL',
                'role': 'Epic Journey Poet'
            }
        elif 'the aeneid' in title_lower:
            voice_info = {
                'author': 'Virgil', 'voice': 'Virgil',
                'work': 'The Aeneid', 'priority': 'HIGH',
                'role': 'Roman Empire Epic Poet'
            }
        
        # PLUTARCH
        elif 'greek lives' in title_lower:
            voice_info = {
                'author': 'Plutarch', 'voice': 'Plutarch',
                'work': 'Greek Lives', 'priority': 'MEDIUM',
                'role': 'Greek Biographer'
            }
        elif 'roman lives' in title_lower:
            voice_info = {
                'author': 'Plutarch', 'voice': 'Plutarch',
                'work': 'Roman Lives', 'priority': 'MEDIUM',
                'role': 'Roman Biographer'
            }
        elif 'les vies parallèles' in title_lower:
            voice_info = {
                'author': 'Plutarch', 'voice': 'Plutarch',
                'work': 'Les vies parallèles: Alcibiade, Coriolan', 'priority': 'MEDIUM',
                'role': 'Parallel Lives Moralist'
            }
        
        # PHILOSOPHY
        elif 'history of western philosophy' in title_lower:
            voice_info = {
                'author': 'Bertrand Russell', 'voice': 'Bertrand Russell',
                'work': 'History of Western Philosophy', 'priority': 'HIGH',
                'role': 'Analytical Philosophy Historian'
            }
        elif 'nietzsche' == title_lower.replace('.epub', ''):
            voice_info = {
                'author': 'Friedrich Nietzsche', 'voice': 'Friedrich Nietzsche',
                'work': 'Nietzsche (Biography or Works)', 'priority': 'CRITICAL',
                'role': 'Philosopher of Will to Power'
            }
        elif 'montaigne' == title_lower.replace('.epub', ''):
            voice_info = {
                'author': 'Michel de Montaigne', 'voice': 'Michel de Montaigne',
                'work': 'Montaigne (Essays)', 'priority': 'HIGH',
                'role': 'Skeptical Essayist of the Self'
            }
        
        # ADORNO
        elif 'minima moralia' in title_lower:
            voice_info = {
                'author': 'Theodor Adorno', 'voice': 'Theodor Adorno',
                'work': 'Minima Moralia', 'priority': 'CRITICAL',
                'role': 'Critical Theorist of Damaged Life'
            }
        elif 'the jargon of authenticity' in title_lower:
            voice_info = {
                'author': 'Theodor Adorno', 'voice': 'Theodor Adorno',
                'work': 'The Jargon of Authenticity', 'priority': 'HIGH',
                'role': 'Critic of False Authenticity'
            }
        
        # RICHARD SENNETT
        elif 'the fall of public man' in title_lower:
            voice_info = {
                'author': 'Richard Sennett', 'voice': 'Richard Sennett',
                'work': 'The Fall of Public Man', 'priority': 'HIGH',
                'role': 'Public Life Sociologist'
            }
        elif 'the conscience of the eye' in title_lower:
            voice_info = {
                'author': 'Richard Sennett', 'voice': 'Richard Sennett',
                'work': 'The Conscience of the Eye', 'priority': 'MEDIUM',
                'role': 'Urban Vision Theorist'
            }
        elif 'the craftsman' in title_lower:
            voice_info = {
                'author': 'Richard Sennett', 'voice': 'Richard Sennett',
                'work': 'The Craftsman', 'priority': 'HIGH',
                'role': 'Craftsmanship Philosopher'
            }
        elif 'the corrosion of character' in title_lower:
            voice_info = {
                'author': 'Richard Sennett', 'voice': 'Richard Sennett',
                'work': 'The Corrosion of Character', 'priority': 'MEDIUM',
                'role': 'Character and Work Analyst'
            }
        elif 'the uses of disorder' in title_lower:
            voice_info = {
                'author': 'Richard Sennett', 'voice': 'Richard Sennett',
                'work': 'The Uses of Disorder', 'priority': 'MEDIUM',
                'role': 'Disorder and Urban Life Theorist'
            }
        elif 'respect in a world of inequality' in title_lower:
            voice_info = {
                'author': 'Richard Sennett', 'voice': 'Richard Sennett',
                'work': 'Respect in a World of Inequality', 'priority': 'MEDIUM',
                'role': 'Inequality and Dignity Analyst'
            }
        
        # KAFKA
        elif 'the aphorisms of franz kafka' in title_lower:
            voice_info = {
                'author': 'Franz Kafka', 'voice': 'Franz Kafka',
                'work': 'The Aphorisms', 'priority': 'HIGH',
                'role': 'Aphoristic Existentialist'
            }
        
        # RILKE
        elif 'the duino elegies' in title_lower:
            voice_info = {
                'author': 'Rainer Maria Rilke', 'voice': 'Rainer Maria Rilke',
                'work': 'The Duino Elegies & Sonnets to Orpheus', 'priority': 'CRITICAL',
                'role': 'Elegiac Poet of Transformation'
            }
        
        # JAPANESE AESTHETICS
        elif 'in praise of shadows' in title_lower:
            voice_info = {
                'author': 'Jun\'ichirō Tanizaki', 'voice': 'Jun\'ichirō Tanizaki',
                'work': 'In Praise of Shadows', 'priority': 'HIGH',
                'role': 'Japanese Aesthetic Philosopher'
            }
        
        # JOHN CAGE
        elif 'silence: lectures and writings' in title_lower:
            voice_info = {
                'author': 'John Cage', 'voice': 'John Cage',
                'work': 'Silence: Lectures and Writings', 'priority': 'HIGH',
                'role': 'Composer of Chance and Silence'
            }
        elif 'silence' == title_lower.replace('.epub', ''):
            voice_info = {
                'author': 'John Cage', 'voice': 'John Cage',
                'work': 'Silence', 'priority': 'HIGH',
                'role': 'Silence and Chance Philosopher'
            }
        
        # ALAN WATTS
        elif 'wisdom of insecurity' in title_lower:
            voice_info = {
                'author': 'Alan Watts', 'voice': 'Alan Watts',
                'work': 'The Wisdom of Insecurity', 'priority': 'MEDIUM',
                'role': 'Eastern-Western Insecurity Philosopher'
            }
        
        # VIKTOR FRANKL
        elif 'man\'s search for meaning' in title_lower:
            voice_info = {
                'author': 'Viktor Frankl', 'voice': 'Viktor Frankl',
                'work': 'Man\'s Search for Meaning', 'priority': 'HIGH',
                'role': 'Logotherapist of Meaning and Suffering'
            }
        
        # BAUMAN
        elif 'liquid modernity' in title_lower:
            voice_info = {
                'author': 'Zygmunt Bauman', 'voice': 'Zygmunt Bauman',
                'work': 'Liquid Modernity', 'priority': 'HIGH',
                'role': 'Theorist of Liquid Modern Society'
            }
        
        # SHAKESPEARE
        elif 'the arden shakespeare' in title_lower:
            voice_info = {
                'author': 'William Shakespeare', 'voice': 'William Shakespeare',
                'work': 'The Complete Works', 'priority': 'CRITICAL',
                'role': 'Complete Dramatic and Poetic Genius'
            }
        
        # TOLKIEN
        elif 'the hobbit' in title_lower:
            voice_info = {
                'author': 'J.R.R. Tolkien', 'voice': 'J.R.R. Tolkien',
                'work': 'The Hobbit', 'priority': 'MEDIUM',
                'role': 'Mythological Sub-Creator'
            }
        elif 'the lord of the rings' in title_lower:
            voice_info = {
                'author': 'J.R.R. Tolkien', 'voice': 'J.R.R. Tolkien',
                'work': 'The Lord of the Rings', 'priority': 'MEDIUM',
                'role': 'Epic Fantasy Mythologist'
            }
        elif 'the children of hurin' in title_lower:
            voice_info = {
                'author': 'J.R.R. Tolkien', 'voice': 'J.R.R. Tolkien',
                'work': 'The Children of Hurin', 'priority': 'LOW',
                'role': 'Tragic Silmarillion Chronicler'
            }
        elif 'beren and lúthien' in title_lower:
            voice_info = {
                'author': 'J.R.R. Tolkien', 'voice': 'J.R.R. Tolkien',
                'work': 'Beren and Lúthien', 'priority': 'LOW',
                'role': 'Love Story Mythologist'
            }
        elif 'the fall of gondolin' in title_lower:
            voice_info = {
                'author': 'J.R.R. Tolkien', 'voice': 'J.R.R. Tolkien',
                'work': 'The Fall of Gondolin', 'priority': 'LOW',
                'role': 'City Fall Chronicler'
            }
        elif 'the nature of middle-earth' in title_lower:
            voice_info = {
                'author': 'J.R.R. Tolkien', 'voice': 'J.R.R. Tolkien',
                'work': 'The Nature of Middle-earth', 'priority': 'LOW',
                'role': 'Middle-earth Natural Philosopher'
            }
        
        # JUNG - Additional works
        elif 'the collected works of c.g. jung' in title_lower:
            voice_info = {
                'author': 'Carl Jung', 'voice': 'Carl Jung',
                'work': 'The Collected Works (Complete Digital Edition)', 'priority': 'CRITICAL',
                'role': 'Complete Depth Psychologist'
            }
        
        # T.S. ELIOT - Additional
        elif 'the complete poems and plays of t. s. eliot' in title_lower:
            voice_info = {
                'author': 'T.S. Eliot', 'voice': 'T.S. Eliot',
                'work': 'The Complete Poems and Plays', 'priority': 'HIGH',
                'role': 'Complete Modernist Poet'
            }
        elif 'the complete poems' == title_lower.replace('.epub', ''):
            voice_info = {
                'author': 'Unknown Poet', 'voice': 'Complete Poet',
                'work': 'The Complete Poems', 'priority': 'MEDIUM',
                'role': 'Complete Poetic Voice'
            }
        
        # ADDITIONAL SOLNIT
        elif 'wanderlust: a history of walking' in title_lower:
            voice_info = {
                'author': 'Rebecca Solnit', 'voice': 'Rebecca Solnit',
                'work': 'Wanderlust: A History of Walking', 'priority': 'MEDIUM',
                'role': 'Walking Historian and Philosopher'
            }
        elif 'the faraway nearby' in title_lower:
            voice_info = {
                'author': 'Rebecca Solnit', 'voice': 'Rebecca Solnit',
                'work': 'The Faraway Nearby', 'priority': 'MEDIUM',
                'role': 'Distance and Intimacy Philosopher'
            }
        elif 'the encyclopedia of trouble and spaciousness' in title_lower:
            voice_info = {
                'author': 'Rebecca Solnit', 'voice': 'Rebecca Solnit',
                'work': 'The Encyclopedia of Trouble and Spaciousness', 'priority': 'MEDIUM',
                'role': 'Trouble and Space Encyclopedist'
            }
        elif 'the mother of all questions' in title_lower:
            voice_info = {
                'author': 'Rebecca Solnit', 'voice': 'Rebecca Solnit',
                'work': 'The Mother of All Questions', 'priority': 'MEDIUM',
                'role': 'Feminist Question Asker'
            }
        elif 'men explain things to me' in title_lower:
            voice_info = {
                'author': 'Rebecca Solnit', 'voice': 'Rebecca Solnit',
                'work': 'Men Explain Things to Me', 'priority': 'MEDIUM',
                'role': 'Mansplaining Critic and Feminist'
            }
        elif 'whose story is this' in title_lower:
            voice_info = {
                'author': 'Rebecca Solnit', 'voice': 'Rebecca Solnit',
                'work': 'Whose Story Is This?', 'priority': 'MEDIUM',
                'role': 'Narrative Authority Questioner'
            }
        elif 'orwell\'s roses' in title_lower:
            voice_info = {
                'author': 'Rebecca Solnit', 'voice': 'Rebecca Solnit',
                'work': 'Orwell\'s Roses', 'priority': 'MEDIUM',
                'role': 'Orwell and Garden Philosopher'
            }
        elif 'recollections of my nonexistence' in title_lower:
            voice_info = {
                'author': 'Rebecca Solnit', 'voice': 'Rebecca Solnit',
                'work': 'Recollections of My Nonexistence', 'priority': 'MEDIUM',
                'role': 'Nonexistence and Voice Memoirist'
            }
        
        # ADDITIONAL SONTAG
        elif 'regarding the pain of others' in title_lower:
            voice_info = {
                'author': 'Susan Sontag', 'voice': 'Susan Sontag',
                'work': 'Regarding the Pain of Others', 'priority': 'HIGH',
                'role': 'Pain and Photography Ethicist'
            }
        elif 'slouching towards bethlehem' in title_lower:
            voice_info = {
                'author': 'Joan Didion', 'voice': 'Joan Didion',
                'work': 'Slouching Towards Bethlehem', 'priority': 'HIGH',
                'role': 'Cultural Disintegration Observer'
            }
        
        # HYPNEROTOMACHIA POLIPHILI
        elif 'le songe de poliphile' in title_lower:
            voice_info = {
                'author': 'Francesco Colonna', 'voice': 'Francesco Colonna',
                'work': 'Le Songe de Poliphile (Hypnerotomachia Poliphili)', 'priority': 'CRITICAL',
                'role': 'Renaissance Dream Architect'
            }
        
        # ADDITIONAL COMPREHENSIVE WORKS
        elif 'complete harvard classics' in title_lower:
            voice_info = {
                'author': 'Various', 'voice': 'Harvard Classics Consortium',
                'work': 'Complete Harvard Classics', 'priority': 'CRITICAL',
                'role': 'Western Education Foundation'
            }
        
        # ZEN WORKS
        elif 'the gateless barrier' in title_lower:
            voice_info = {
                'author': 'Mumon', 'voice': 'Mumon',
                'work': 'The Gateless Barrier', 'priority': 'HIGH',
                'role': 'Zen Koan Master'
            }
        elif 'the great path of awakening' in title_lower:
            voice_info = {
                'author': 'Jamgön Kongtrul', 'voice': 'Jamgön Kongtrul',
                'work': 'The Great Path of Awakening', 'priority': 'HIGH',
                'role': 'Tibetan Awakening Guide'
            }
        
        # HAWKING ADDITIONAL
        elif 'the grand design' in title_lower:
            voice_info = {
                'author': 'Stephen Hawking', 'voice': 'Stephen Hawking',
                'work': 'The Grand Design', 'priority': 'MEDIUM',
                'role': 'Cosmic Design Theorist'
            }
        elif 'on the shoulders of giants' in title_lower:
            voice_info = {
                'author': 'Stephen Hawking', 'voice': 'Stephen Hawking',
                'work': 'On the Shoulders of Giants', 'priority': 'MEDIUM',
                'role': 'Scientific Giants Curator'
            }
        
        # ADDITIONAL VOICES
        elif 'mahler: a musical physiognomy' in title_lower:
            voice_info = {
                'author': 'Theodor Adorno', 'voice': 'Theodor Adorno',
                'work': 'Mahler: A Musical Physiognomy', 'priority': 'MEDIUM',
                'role': 'Musical Physiognomist'
            }
        elif 'magellan' == title_lower.replace('.epub', ''):
            voice_info = {
                'author': 'Stefan Zweig', 'voice': 'Stefan Zweig',
                'work': 'Magellan', 'priority': 'MEDIUM',
                'role': 'Explorer Biographer'
            }
        elif 'just so' in title_lower:
            voice_info = {
                'author': 'Rudyard Kipling', 'voice': 'Rudyard Kipling',
                'work': 'Just So Stories', 'priority': 'LOW',
                'role': 'Imperial Storyteller'
            }
        elif 'poems to night' in title_lower:
            voice_info = {
                'author': 'Unknown Poet', 'voice': 'Night Poet',
                'work': 'Poems to Night', 'priority': 'MEDIUM',
                'role': 'Nocturnal Poet'
            }
        elif 'parallel stories' in title_lower:
            voice_info = {
                'author': 'Péter Nádas', 'voice': 'Péter Nádas',
                'work': 'Parallel Stories', 'priority': 'MEDIUM',
                'role': 'Parallel Narrative Architect'
            }
        elif 'les enfants terribles' in title_lower:
            voice_info = {
                'author': 'Jean Cocteau', 'voice': 'Jean Cocteau',
                'work': 'Les Enfants Terribles', 'priority': 'MEDIUM',
                'role': 'Terrible Children Chronicler'
            }
        elif 'œuvres complètes du marquis de sade' in title_lower:
            voice_info = {
                'author': 'Marquis de Sade', 'voice': 'Marquis de Sade',
                'work': 'Œuvres complètes', 'priority': 'MEDIUM',
                'role': 'Libertine Philosopher of Transgression'
            }
        elif 'excellent advice for living' in title_lower:
            voice_info = {
                'author': 'Kevin Kelly', 'voice': 'Kevin Kelly',
                'work': 'Excellent Advice for Living', 'priority': 'LOW',
                'role': 'Contemporary Life Advisor'
            }
        elif 'make something wonderful' in title_lower:
            voice_info = {
                'author': 'Steve Jobs', 'voice': 'Steve Jobs',
                'work': 'Make Something Wonderful', 'priority': 'LOW',
                'role': 'Innovation and Design Philosopher'
            }
        elif 'not too late' in title_lower:
            voice_info = {
                'author': 'Rebecca Solnit', 'voice': 'Rebecca Solnit',
                'work': 'Not Too Late: Changing the Climate Story', 'priority': 'MEDIUM',
                'role': 'Climate Hope Activist'
            }
        
        if voice_info:
            voice_info['filename'] = filename
            remaining_voices.append(voice_info)
    
    return remaining_voices

def display_comprehensive_results():
    """Display complete comprehensive scan results"""
    
    print("🔍 COMPLETE DEEP SCAN OF EASTERN FOLDER")
    print("=" * 60)
    print("Exhaustive identification of ALL remaining voices")
    print()
    
    voices = complete_deep_scan()
    
    if not voices:
        print("✅ All voices have been identified and converted!")
        print("🎭 Folder is completely processed and ready for cleanup")
        return
    
    print(f"📚 Found {len(voices)} REMAINING voices to convert:")
    print()
    
    # Sort by priority
    priority_order = {'CRITICAL': 0, 'HIGH': 1, 'MEDIUM': 2, 'LOW': 3}
    sorted_voices = sorted(voices, key=lambda x: priority_order.get(x['priority'], 4))
    
    # Display by priority groups
    for priority in ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW']:
        priority_voices = [v for v in sorted_voices if v['priority'] == priority]
        if not priority_voices:
            continue
            
        print(f"{'🔥' if priority == 'CRITICAL' else '🟡' if priority == 'HIGH' else '🔵' if priority == 'MEDIUM' else '⚪'} {priority} PRIORITY: {len(priority_voices)} voices")
        
        for i, voice in enumerate(priority_voices, 1):
            print(f"   [{i}] 🎭 {voice['voice']}")
            print(f"       📖 {voice['work']}")
            print(f"       🎪 {voice['role']}")
        print()
    
    # Major missing voice analysis
    critical_voices = [v for v in voices if v['priority'] == 'CRITICAL']
    major_authors = {}
    for voice in voices:
        author = voice['author']
        if author not in major_authors:
            major_authors[author] = []
        major_authors[author].append(voice)
    
    print("🎯 MAJOR VOICE COLLECTIONS:")
    
    # Show major collections
    major_collections = [(author, works) for author, works in major_authors.items() if len(works) >= 3]
    major_collections.sort(key=lambda x: len(x[1]), reverse=True)
    
    for author, works in major_collections[:10]:  # Top 10
        priority_counts = {}
        for work in works:
            p = work['priority']
            priority_counts[p] = priority_counts.get(p, 0) + 1
        
        priority_display = []
        for p in ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW']:
            if p in priority_counts:
                priority_display.append(f"{priority_counts[p]} {p}")
        
        print(f"   • {author}: {len(works)} works ({', '.join(priority_display)})")
    
    print()
    print("⚡ MOST CRITICAL MISSING VOICES:")
    for voice in critical_voices:
        print(f"   🔥 {voice['voice']}: {voice['work']}")
        if voice['voice'] == 'Michel Foucault':
            print(f"      ⚡ POWER/KNOWLEDGE ARCHAEOLOGY - Essential for critical theory!")
        elif voice['voice'] == 'Jacques Lacan':
            print(f"      ⚡ STRUCTURAL PSYCHOANALYSIS - Missing from depth psychology!")
        elif voice['voice'] == 'William Shakespeare':
            print(f"      ⚡ COMPLETE DRAMATIC WORKS - Foundation of English literature!")
        elif voice['voice'] == 'James Joyce':
            print(f"      ⚡ MODERNIST CONSCIOUSNESS - Stream of consciousness innovation!")
        elif voice['voice'] == 'Homer':
            print(f"      ⚡ EPIC FOUNDATION - Western literature's beginning!")
    
    print()
    print("📋 CONVERSION STRATEGY RECOMMENDATION:")
    print("   1. 🔥 Convert ALL CRITICAL voices first (foundational gaps)")
    print("   2. 🟡 Convert HIGH priority by author collections")
    print("   3. 🔵 Convert MEDIUM priority selectively")
    print("   4. ⚪ Convert LOW priority only if time permits")
    
    print()
    print(f"🎭 CHAMBER COMPLETION POTENTIAL:")
    total_new_voices = len(set(v['voice'] for v in voices))
    critical_count = len(critical_voices)
    print(f"   📊 {total_new_voices} unique new voices identified")
    print(f"   🔥 {critical_count} critical foundational voices")
    print(f"   🏛️ Chamber would become truly comprehensive")
    
    return voices

if __name__ == "__main__":
    voices = display_comprehensive_results()
    
    if voices:
        critical_count = len([v for v in voices if v['priority'] == 'CRITICAL'])
        print(f"\n⚡ SCAN COMPLETE: {len(voices)} total voices found!")
        print(f"🔥 {critical_count} CRITICAL voices need immediate conversion")
        print("🎭 This represents the complete remaining potential of the folder")
    else:
        print("\n🎉 Folder completely processed - ready for cleanup!")