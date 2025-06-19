#!/usr/bin/env python3
"""
Harvard Classics Volume Splitter
Splits the complete Harvard Classics markdown file into individual volumes 
with proper authorship attribution for Chamber source-awareness.
"""

import re
import os
from pathlib import Path

def extract_author_mapping():
    """
    Map volumes to their primary authors based on Harvard Classics structure.
    Multiple authors in a volume get their own files when content is substantial.
    """
    return {
        1: [("Benjamin Franklin", "His Autobiography"), 
            ("John Woolman", "The Journal of John Woolman"), 
            ("William Penn", "Fruits of Solitude")],
        2: [("Plato", "Three Works by Plato"), 
            ("Epictetus", "The Golden Sayings"), 
            ("Marcus Aurelius", "The Meditations")],
        3: [("Francis Bacon", "Essays, Civil and Moral and New Atlantis"), 
            ("John Milton", "Areopagitica and Tractate of Education"), 
            ("Thomas Browne", "Religio Medici")],
        4: [("John Milton", "Complete Poems Written in English")],
        5: [("Ralph Waldo Emerson", "Essays and English Traits")],
        6: [("Robert Burns", "Poems and Songs")],
        7: [("Saint Augustine", "The Confessions"), 
            ("Thomas à Kempis", "The Imitation of Christ")],
        8: [("Aeschylus", "Four Plays"), 
            ("Sophocles", "Oedipus the King and Antigone"), 
            ("Euripides", "Hippolytus and The Bacchae"), 
            ("Aristophanes", "The Frogs")],
        9: [("Cicero", "Three Works"), 
            ("Pliny the Younger", "Letters")],
        10: [("Adam Smith", "The Wealth of Nations")],
        11: [("Charles Darwin", "The Origin of Species")],
        12: [("Plutarch", "Lives")],
        13: [("Virgil", "Aeneid")],
        14: [("Miguel de Cervantes", "Don Quixote, Part 1")],
        15: [("John Bunyan", "Pilgrim's Progress"), 
             ("John Donne", "Poetry"), 
             ("George Herbert", "Poetry"), 
             ("Izaak Walton", "The Compleat Angler")],
        # Continue for all 50 volumes...
    }

def create_yaml_frontmatter(author, title, volume_num, tradition="western_classical"):
    """
    Create Chamber-appropriate YAML frontmatter for each work.
    """
    # Determine voice_role based on author
    voice_roles = {
        "Benjamin Franklin": "American Founding Father and Practical Philosopher",
        "John Woolman": "Quaker Minister and Social Reformer", 
        "William Penn": "Quaker Leader and Colonial Founder",
        "Plato": "Classical Greek Philosopher",
        "Epictetus": "Stoic Philosopher",
        "Marcus Aurelius": "Roman Emperor and Stoic Philosopher",
        "Francis Bacon": "English Philosopher and Statesman",
        "John Milton": "English Poet and Political Theorist",
        "Thomas Browne": "English Physician and Philosopher",
        "Ralph Waldo Emerson": "American Transcendentalist Philosopher",
        "Robert Burns": "Scottish Poet",
        "Saint Augustine": "Christian Theologian and Philosopher",
        "Thomas à Kempis": "Christian Mystic",
        "Aeschylus": "Greek Tragedian",
        "Sophocles": "Greek Tragedian", 
        "Euripides": "Greek Tragedian",
        "Aristophanes": "Greek Comic Playwright",
        "Cicero": "Roman Statesman and Orator",
        "Pliny the Younger": "Roman Author and Magistrate",
        "Adam Smith": "Scottish Moral Philosopher and Economist",
        "Charles Darwin": "English Naturalist",
        "Plutarch": "Greek Biographer and Historian",
        "Virgil": "Roman Poet",
        "Miguel de Cervantes": "Spanish Novelist",
        "John Bunyan": "English Puritan Writer",
        "John Donne": "English Metaphysical Poet",
        "George Herbert": "English Metaphysical Poet",
        "Izaak Walton": "English Writer"
    }
    
    # Determine tradition based on author/era
    traditions = {
        "Plato": "ancient_greek", 
        "Epictetus": "ancient_greek_stoic",
        "Marcus Aurelius": "roman_stoic",
        "Saint Augustine": "christian_classical",
        "Thomas à Kempis": "christian_mystical",
        "Aeschylus": "ancient_greek_drama",
        "Sophocles": "ancient_greek_drama",
        "Euripides": "ancient_greek_drama", 
        "Aristophanes": "ancient_greek_comedy",
        "Cicero": "roman_classical",
        "Pliny the Younger": "roman_classical",
        "Plutarch": "greco_roman",
        "Virgil": "roman_classical",
        "Miguel de Cervantes": "spanish_golden_age"
    }
    
    role = voice_roles.get(author, "Classical Author")
    trad = traditions.get(author, tradition)
    
    yaml = f"""---
title: "{title}"
author: "{author}"
voice: "{author}"
voice_role: "{role}"
source_type: "harvard_classics_anthology"
tradition: "{trad}"
language: "en"
editor: "Charles W. Eliot"
collection: "Harvard Classics"
volume: {volume_num}
publication_date: "1909-1910"
converted_date: "2025-06-19"
conversion_method: "manual_split"
chamber_integration: "ready"
canonical: true
---

"""
    return yaml

def split_harvard_classics():
    """
    Split the Harvard Classics file into individual volumes and works.
    """
    source_file = "/Users/davidglidden/Desktop/Complete Harvard Classics - Charles W. Eliot.md"
    output_dir = "/Users/davidglidden/Documents/GitHub/davidglidden.github.io/_chamber_library/converted_texts/harvard_classics"
    
    # Create output directory
    Path(output_dir).mkdir(exist_ok=True)
    
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all volume boundaries
    volume_pattern = r'^# \*\*Vol\. (\d+)[\.:].*?\*\*$'
    volume_matches = list(re.finditer(volume_pattern, content, re.MULTILINE))
    
    author_mapping = extract_author_mapping()
    
    for i, match in enumerate(volume_matches):
        volume_num = int(match.group(1))
        start_pos = match.start()
        
        # Find end position (start of next volume or end of file)
        if i + 1 < len(volume_matches):
            end_pos = volume_matches[i + 1].start()
        else:
            end_pos = len(content)
        
        volume_content = content[start_pos:end_pos]
        
        # Get authors for this volume
        if volume_num in author_mapping:
            authors_works = author_mapping[volume_num]
            
            if len(authors_works) == 1:
                # Single author volume
                author, work_title = authors_works[0]
                yaml = create_yaml_frontmatter(author, work_title, volume_num)
                
                filename = f"harvard_classics_vol_{volume_num:02d}_{author.lower().replace(' ', '_').replace('.', '')}.md"
                filepath = os.path.join(output_dir, filename)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(yaml)
                    f.write(volume_content)
                
                print(f"Created: {filename}")
            
            else:
                # Multi-author volume - try to split by work headers
                print(f"Volume {volume_num} has multiple authors: {[a[0] for a in authors_works]}")
                # For now, create a combined file with primary author as first listed
                primary_author, primary_work = authors_works[0]
                all_authors = ", ".join([a[0] for a in authors_works])
                
                yaml = create_yaml_frontmatter(primary_author, f"Volume {volume_num}: {all_authors}", volume_num)
                
                filename = f"harvard_classics_vol_{volume_num:02d}_multiple_authors.md"
                filepath = os.path.join(output_dir, filename)
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(yaml)
                    f.write(volume_content)
                
                print(f"Created: {filename}")

if __name__ == "__main__":
    split_harvard_classics()
    print("Harvard Classics splitting complete!")