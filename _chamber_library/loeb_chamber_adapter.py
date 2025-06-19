#!/usr/bin/env python3
"""
Loeb Classical Library Chamber Adapter
Converts the Loeb DSL format into Chamber-ready markdown files with proper
voice attribution and classical tradition mapping.
"""

import re
import os
from pathlib import Path
from collections import defaultdict

def parse_loeb_dsl(dsl_file):
    """
    Parse the Loeb DSL file to extract authors, works, and content structure.
    """
    authors = {}
    works = defaultdict(list)
    current_work = None
    
    with open(dsl_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            
            # Extract work entries
            if line.startswith('-') and '(' in line and ')' in line:
                # Format: -001.001 (APOLLONIUS OF RHODES, Argonautica)
                match = re.match(r'^-([0-9]+\.[0-9]+)\s+\(([^,]+),\s*([^)]+)\)', line)
                if match:
                    entry_id, author, work_title = match.groups()
                    current_work = f"{author}_{work_title}".replace(' ', '_').replace(',', '')
                    
                    # Store author and work info
                    authors[author] = {
                        'name': author,
                        'works': set()
                    }
                    authors[author]['works'].add(work_title)
                    
                    works[current_work].append({
                        'entry_id': entry_id,
                        'author': author,
                        'title': work_title,
                        'line': line
                    })
    
    return authors, works

def get_classical_voice_mapping():
    """
    Map classical authors to Chamber voice specifications.
    """
    return {
        'APOLLONIUS OF RHODES': {
            'voice_role': 'Hellenistic Epic Poet',
            'tradition': 'hellenistic_greek',
            'language': 'grc',  # Ancient Greek
            'period': '3rd century BCE',
            'canonical': True
        },
        'HOMER': {
            'voice_role': 'Archaic Greek Epic Poet',
            'tradition': 'archaic_greek',
            'language': 'grc',
            'period': '8th century BCE',
            'canonical': True
        },
        'PLATO': {
            'voice_role': 'Classical Greek Philosopher',
            'tradition': 'classical_greek_philosophy',
            'language': 'grc',
            'period': '5th-4th century BCE',
            'canonical': True
        },
        'ARISTOTLE': {
            'voice_role': 'Classical Greek Philosopher',
            'tradition': 'classical_greek_philosophy',
            'language': 'grc',
            'period': '4th century BCE',
            'canonical': True
        },
        'CICERO': {
            'voice_role': 'Roman Statesman and Orator',
            'tradition': 'roman_classical',
            'language': 'la',  # Latin
            'period': '1st century BCE',
            'canonical': True
        },
        'SENECA': {
            'voice_role': 'Roman Stoic Philosopher',
            'tradition': 'roman_stoic',
            'language': 'la',
            'period': '1st century CE',
            'canonical': True
        },
        'TACITUS': {
            'voice_role': 'Roman Historian',
            'tradition': 'roman_historical',
            'language': 'la',
            'period': '1st-2nd century CE',
            'canonical': True
        },
        'VIRGIL': {
            'voice_role': 'Roman Epic Poet',
            'tradition': 'roman_classical',
            'language': 'la',
            'period': '1st century BCE',
            'canonical': True
        },
        'OVID': {
            'voice_role': 'Roman Elegiac Poet',
            'tradition': 'roman_classical',
            'language': 'la',
            'period': '1st century BCE - 1st century CE',
            'canonical': True
        },
        'HORACE': {
            'voice_role': 'Roman Lyric Poet',
            'tradition': 'roman_classical',
            'language': 'la',
            'period': '1st century BCE',
            'canonical': True
        },
        'HERODOTUS': {
            'voice_role': 'Greek Historian',
            'tradition': 'classical_greek_historical',
            'language': 'grc',
            'period': '5th century BCE',
            'canonical': True
        },
        'THUCYDIDES': {
            'voice_role': 'Greek Historian',
            'tradition': 'classical_greek_historical',
            'language': 'grc',
            'period': '5th century BCE',
            'canonical': True
        },
        'AESCHYLUS': {
            'voice_role': 'Greek Tragedian',
            'tradition': 'classical_greek_drama',
            'language': 'grc',
            'period': '6th-5th century BCE',
            'canonical': True
        },
        'SOPHOCLES': {
            'voice_role': 'Greek Tragedian',
            'tradition': 'classical_greek_drama',
            'language': 'grc',
            'period': '5th century BCE',
            'canonical': True
        },
        'EURIPIDES': {
            'voice_role': 'Greek Tragedian',
            'tradition': 'classical_greek_drama',
            'language': 'grc',
            'period': '5th century BCE',
            'canonical': True
        },
        'ARISTOPHANES': {
            'voice_role': 'Greek Comic Playwright',
            'tradition': 'classical_greek_comedy',
            'language': 'grc',
            'period': '5th-4th century BCE',
            'canonical': True
        },
        'PLUTARCH': {
            'voice_role': 'Greek Biographer and Moralist',
            'tradition': 'greco_roman',
            'language': 'grc',
            'period': '1st-2nd century CE',
            'canonical': True
        },
        'PLOTINUS': {
            'voice_role': 'Neoplatonic Philosopher',
            'tradition': 'neoplatonic',
            'language': 'grc',
            'period': '3rd century CE',
            'canonical': True
        }
    }

def create_loeb_yaml_frontmatter(author, work_title, voice_mapping):
    """
    Create Chamber-appropriate YAML frontmatter for Loeb texts.
    """
    author_info = voice_mapping.get(author, {
        'voice_role': 'Classical Author',
        'tradition': 'classical_antiquity',
        'language': 'grc',
        'period': 'Classical Period',
        'canonical': True
    })
    
    yaml = f"""---
title: "{work_title}"
author: "{author}"
voice: "{author}"
voice_role: "{author_info['voice_role']}"
source_type: "loeb_classical_library"
tradition: "{author_info['tradition']}"
language: "{author_info['language']}"
collection: "Loeb Classical Library"
publication_date: "1912-2024"
converted_date: "2025-06-19"
conversion_method: "dsl_adapter"
chamber_integration: "ready"
canonical: {str(author_info['canonical']).lower()}
period: "{author_info['period']}"
bilingual: true
scholarly_apparatus: true
---

"""
    return yaml

def analyze_loeb_collection():
    """
    Analyze the Loeb DSL file to understand its scope and structure.
    """
    dsl_file = "/Users/davidglidden/Documents/Loeb Classical All Library 537 Volumes/loeb.dsl"
    
    print("Analyzing Loeb Classical Library DSL structure...")
    
    # Get basic stats
    with open(dsl_file, 'r', encoding='utf-8') as f:
        total_lines = sum(1 for _ in f)
    
    # Parse authors and works
    authors, works = parse_loeb_dsl(dsl_file)
    
    print(f"Total DSL lines: {total_lines:,}")
    print(f"Unique authors: {len(authors)}")
    print(f"Unique works: {len(works)}")
    
    # Show sample authors
    print("\nSample authors found:")
    for i, (author, info) in enumerate(list(authors.items())[:10]):
        print(f"  {author}: {len(info['works'])} works")
    
    # Get voice mapping coverage
    voice_mapping = get_classical_voice_mapping()
    mapped_authors = [a for a in authors.keys() if a in voice_mapping]
    unmapped_authors = [a for a in authors.keys() if a not in voice_mapping]
    
    print(f"\nVoice mapping coverage:")
    print(f"  Mapped authors: {len(mapped_authors)}")
    print(f"  Unmapped authors: {len(unmapped_authors)}")
    
    if unmapped_authors:
        print("\nFirst 10 unmapped authors:")
        for author in unmapped_authors[:10]:
            print(f"  {author}")
    
    return authors, works

def generate_loeb_chamber_files():
    """
    Generate Chamber-ready files from Loeb DSL.
    Note: This creates metadata files. Actual text extraction would require
    the accompanying zip file or individual text files.
    """
    authors, works = analyze_loeb_collection()
    voice_mapping = get_classical_voice_mapping()
    
    output_dir = "/Users/davidglidden/Documents/GitHub/davidglidden.github.io/_chamber_library/converted_texts/loeb_classical"
    Path(output_dir).mkdir(exist_ok=True)
    
    # Create inventory file
    inventory_path = os.path.join(output_dir, "loeb_inventory.md")
    with open(inventory_path, 'w', encoding='utf-8') as f:
        f.write("# Loeb Classical Library Inventory\n\n")
        f.write(f"Total authors: {len(authors)}\n")
        f.write(f"Total works: {len(works)}\n\n")
        
        f.write("## Authors and Works\n\n")
        for author, info in sorted(authors.items()):
            f.write(f"### {author}\n")
            for work in sorted(info['works']):
                f.write(f"- {work}\n")
            f.write("\n")
    
    print(f"Created Loeb inventory at: {inventory_path}")
    return authors, works

if __name__ == "__main__":
    authors, works = generate_loeb_chamber_files()
    print("Loeb Classical Library analysis complete!")