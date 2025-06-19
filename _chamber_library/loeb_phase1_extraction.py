#!/usr/bin/env python3
"""
Loeb Classical Library Phase 1 Extraction
Extracts the 25 priority authors from the DSL file for immediate Chamber integration.
"""

import re
import os
from pathlib import Path
from datetime import datetime

def get_phase1_authors():
    """
    Define the 25 priority authors for Phase 1 with complete metadata.
    """
    return {
        # Tier 1: Essential Philosophers
        'PLATO': {
            'voice_role': 'Athenian Philosopher and Dialogue Master',
            'tradition': 'classical_greek_philosophy',
            'language': 'grc',
            'period': '5th-4th century BCE',
            'philosophical_school': 'Platonic Academy',
            'major_themes': ['Forms', 'Justice', 'Knowledge', 'Soul'],
            'tier': 1
        },
        'ARISTOTLE': {
            'voice_role': 'Classical Greek Philosopher and Scientist',
            'tradition': 'classical_greek_philosophy',
            'language': 'grc',
            'period': '4th century BCE',
            'philosophical_school': 'Peripatetic School',
            'major_themes': ['Logic', 'Ethics', 'Politics', 'Metaphysics'],
            'tier': 1
        },
        'PLOTINUS': {
            'voice_role': 'Neoplatonic Philosopher',
            'tradition': 'neoplatonic',
            'language': 'grc',
            'period': '3rd century CE',
            'philosophical_school': 'Neoplatonism',
            'major_themes': ['The One', 'Emanation', 'Mystical Union'],
            'tier': 1
        },
        'EPICTETUS': {
            'voice_role': 'Stoic Philosopher',
            'tradition': 'roman_stoic',
            'language': 'grc',
            'period': '1st-2nd century CE',
            'philosophical_school': 'Stoicism',
            'major_themes': ['Freedom', 'Discipline', 'Ethics of Response'],
            'tier': 1
        },
        'MARCUS AURELIUS': {
            'voice_role': 'Roman Emperor and Stoic Philosopher',
            'tradition': 'roman_stoic',
            'language': 'grc',
            'period': '2nd century CE',
            'philosophical_school': 'Stoicism',
            'major_themes': ['Leadership', 'Duty', 'Philosophical Practice'],
            'tier': 1
        },
        
        # Tier 2: Major Historians & Biographers
        'HERODOTUS': {
            'voice_role': 'Greek Historian and Cultural Inquirer',
            'tradition': 'classical_greek_historical',
            'language': 'grc',
            'period': '5th century BCE',
            'philosophical_school': 'Historical Inquiry',
            'major_themes': ['Cultural Difference', 'Causation', 'Human Nature'],
            'tier': 2
        },
        'THUCYDIDES': {
            'voice_role': 'Greek Historian and Political Analyst',
            'tradition': 'classical_greek_historical',
            'language': 'grc',
            'period': '5th century BCE',
            'philosophical_school': 'Political Realism',
            'major_themes': ['Power', 'War', 'Political Psychology'],
            'tier': 2
        },
        'TACITUS': {
            'voice_role': 'Roman Historian and Imperial Critic',
            'tradition': 'roman_historical',
            'language': 'la',
            'period': '1st-2nd century CE',
            'philosophical_school': 'Historical Analysis',
            'major_themes': ['Imperial Politics', 'Character', 'Moral Decline'],
            'tier': 2
        },
        'PLUTARCH': {
            'voice_role': 'Greek Biographer and Moralist',
            'tradition': 'greco_roman',
            'language': 'grc',
            'period': '1st-2nd century CE',
            'philosophical_school': 'Biographical Method',
            'major_themes': ['Character', 'Virtue', 'Parallel Lives'],
            'tier': 2
        },
        
        # Tier 3: Essential Poets
        'HOMER': {
            'voice_role': 'Archaic Greek Epic Poet',
            'tradition': 'archaic_greek_epic',
            'language': 'grc',
            'period': '8th century BCE',
            'philosophical_school': 'Epic Tradition',
            'major_themes': ['Heroism', 'Fate', 'Honor', 'Journey'],
            'tier': 3
        },
        'VIRGIL': {
            'voice_role': 'Roman Epic Poet',
            'tradition': 'roman_classical',
            'language': 'la',
            'period': '1st century BCE',
            'philosophical_school': 'Augustan Poetry',
            'major_themes': ['Empire', 'Destiny', 'Pastoral', 'Transformation'],
            'tier': 3
        },
        'OVID': {
            'voice_role': 'Roman Elegiac and Epic Poet',
            'tradition': 'roman_classical',
            'language': 'la',
            'period': '1st century BCE - 1st century CE',
            'philosophical_school': 'Augustan Poetry',
            'major_themes': ['Transformation', 'Love', 'Exile', 'Metamorphosis'],
            'tier': 3
        },
        'HORACE': {
            'voice_role': 'Roman Lyric Poet and Literary Critic',
            'tradition': 'roman_classical',
            'language': 'la',
            'period': '1st century BCE',
            'philosophical_school': 'Augustan Poetry',
            'major_themes': ['Moderation', 'Craft', 'Friendship', 'Mortality'],
            'tier': 3
        },
        'PINDAR': {
            'voice_role': 'Greek Lyric Poet',
            'tradition': 'archaic_greek_lyric',
            'language': 'grc',
            'period': '6th-5th century BCE',
            'philosophical_school': 'Choral Lyric',
            'major_themes': ['Victory', 'Glory', 'Divine Favor', 'Excellence'],
            'tier': 3
        },
        'HESIOD': {
            'voice_role': 'Greek Didactic Poet',
            'tradition': 'archaic_greek_didactic',
            'language': 'grc',
            'period': '8th century BCE',
            'philosophical_school': 'Didactic Poetry',
            'major_themes': ['Work', 'Justice', 'Cosmogony', 'Moral Order'],
            'tier': 3
        },
        
        # Tier 4: Dramatic Voices
        'AESCHYLUS': {
            'voice_role': 'Greek Tragedian',
            'tradition': 'classical_greek_drama',
            'language': 'grc',
            'period': '6th-5th century BCE',
            'philosophical_school': 'Attic Tragedy',
            'major_themes': ['Justice', 'Fate', 'Divine Law', 'Cosmic Order'],
            'tier': 4
        },
        'SOPHOCLES': {
            'voice_role': 'Greek Tragedian',
            'tradition': 'classical_greek_drama',
            'language': 'grc',
            'period': '5th century BCE',
            'philosophical_school': 'Attic Tragedy',
            'major_themes': ['Character', 'Fate', 'Knowledge', 'Moral Responsibility'],
            'tier': 4
        },
        'EURIPIDES': {
            'voice_role': 'Greek Tragedian',
            'tradition': 'classical_greek_drama',
            'language': 'grc',
            'period': '5th century BCE',
            'philosophical_school': 'Attic Tragedy',
            'major_themes': ['Psychology', 'Passion', 'Social Critique', 'Divine Irrationality'],
            'tier': 4
        },
        'ARISTOPHANES': {
            'voice_role': 'Greek Comic Playwright',
            'tradition': 'classical_greek_comedy',
            'language': 'grc',
            'period': '5th-4th century BCE',
            'philosophical_school': 'Old Comedy',
            'major_themes': ['Political Satire', 'Social Critique', 'Literary Parody'],
            'tier': 4
        },
        
        # Tier 5: Orators & Statesmen
        'CICERO': {
            'voice_role': 'Roman Statesman and Orator',
            'tradition': 'roman_classical',
            'language': 'la',
            'period': '1st century BCE',
            'philosophical_school': 'Roman Oratory',
            'major_themes': ['Republic', 'Rhetoric', 'Natural Law', 'Duty'],
            'tier': 5
        },
        'DEMOSTHENES': {
            'voice_role': 'Greek Orator and Statesman',
            'tradition': 'classical_greek_oratory',
            'language': 'grc',
            'period': '4th century BCE',
            'philosophical_school': 'Attic Oratory',
            'major_themes': ['Freedom', 'Democracy', 'Civic Courage', 'Deliberation'],
            'tier': 5
        },
        'ISOCRATES': {
            'voice_role': 'Greek Orator and Educator',
            'tradition': 'classical_greek_oratory',
            'language': 'grc',
            'period': '5th-4th century BCE',
            'philosophical_school': 'Rhetorical Education',
            'major_themes': ['Education', 'Panhellenism', 'Practical Wisdom'],
            'tier': 5
        },
        
        # Tier 6: Essential Schools
        'LUCRETIUS': {
            'voice_role': 'Roman Epicurean Philosopher',
            'tradition': 'roman_epicurean',
            'language': 'la',
            'period': '1st century BCE',
            'philosophical_school': 'Epicureanism',
            'major_themes': ['Atomism', 'Ethics of Pleasure', 'Death', 'Nature'],
            'tier': 6
        },
        'SENECA': {
            'voice_role': 'Roman Stoic Philosopher',
            'tradition': 'roman_stoic',
            'language': 'la',
            'period': '1st century CE',
            'philosophical_school': 'Stoicism',
            'major_themes': ['Practical Ethics', 'Letters', 'Tragedy', 'Political Life'],
            'tier': 6
        },
        'SEXTUS EMPIRICUS': {
            'voice_role': 'Greek Skeptical Philosopher',
            'tradition': 'hellenistic_skeptical',
            'language': 'grc',
            'period': '2nd-3rd century CE',
            'philosophical_school': 'Pyrrhonian Skepticism',
            'major_themes': ['Epoché', 'Suspension of Judgment', 'Dogmatism Critique'],
            'tier': 6
        }
    }

def create_loeb_yaml_frontmatter(author, author_info, works_list):
    """
    Create Chamber-appropriate YAML frontmatter for Loeb authors.
    """
    yaml = f"""---
title: "Complete Works"
author: "{author}"
voice: "{author}"
voice_role: "{author_info['voice_role']}"
source_type: "loeb_classical_library"
tradition: "{author_info['tradition']}"
language: "{author_info['language']}"
period: "{author_info['period']}"
philosophical_school: "{author_info['philosophical_school']}"
major_themes: {author_info['major_themes']}
collection: "Loeb Classical Library"
bilingual: true
scholarly_apparatus: true
chamber_integration: "ready"
canonical: true
phase: 1
priority_tier: {author_info['tier']}
works_included: {works_list}
extraction_date: "{datetime.now().strftime('%Y-%m-%d')}"
---

"""
    return yaml

def extract_author_content(dsl_file, author_name):
    """
    Extract all content for a specific author from the DSL file.
    """
    content_sections = []
    current_section = []
    capturing = False
    works_found = set()
    
    with open(dsl_file, 'r', encoding='utf-8') as f:
        for line in f:
            line_stripped = line.strip()
            
            # Check if this line mentions our author
            if author_name in line_stripped and '(' in line_stripped and ')' in line_stripped:
                # Extract work title from parentheses
                match = re.search(r'\(([^,]+),\s*([^)]+)\)', line_stripped)
                if match and match.group(1).strip() == author_name:
                    work_title = match.group(2).strip()
                    works_found.add(work_title)
                    
                    # Save previous section if we were capturing
                    if capturing and current_section:
                        content_sections.append('\n'.join(current_section))
                    
                    # Start new section
                    current_section = [line.rstrip()]
                    capturing = True
                    continue
            
            # If we're capturing for this author, collect the content
            if capturing:
                current_section.append(line.rstrip())
                
                # Stop capturing when we hit a new author or end of section
                if line_stripped.startswith('-') and author_name not in line_stripped and '(' in line_stripped:
                    # Save current section and stop capturing
                    content_sections.append('\n'.join(current_section[:-1]))  # Don't include the new author line
                    capturing = False
                    current_section = []
    
    # Don't forget the last section
    if capturing and current_section:
        content_sections.append('\n'.join(current_section))
    
    return content_sections, list(works_found)

def process_phase1_authors():
    """
    Process all Phase 1 priority authors from the DSL file.
    """
    dsl_file = "/Users/davidglidden/Documents/Loeb Classical All Library 537 Volumes/loeb.dsl"
    output_dir = "/Users/davidglidden/Documents/GitHub/davidglidden.github.io/_chamber_library/converted_texts/loeb_classical/phase_1"
    
    # Create output directory
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    priority_authors = get_phase1_authors()
    extraction_log = []
    
    print(f"Processing {len(priority_authors)} Phase 1 priority authors...")
    
    for author, author_info in priority_authors.items():
        print(f"\nProcessing {author}...")
        
        try:
            content_sections, works_list = extract_author_content(dsl_file, author)
            
            if content_sections:
                # Create YAML frontmatter
                yaml_header = create_loeb_yaml_frontmatter(author, author_info, works_list)
                
                # Combine all content
                full_content = yaml_header + '\n' + '\n\n---\n\n'.join(content_sections)
                
                # Create filename
                filename = f"loeb_{author.lower().replace(' ', '_')}_complete.md"
                filepath = os.path.join(output_dir, filename)
                
                # Write file
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(full_content)
                
                extraction_log.append({
                    'author': author,
                    'works_found': len(works_list),
                    'content_sections': len(content_sections),
                    'filename': filename,
                    'status': 'success'
                })
                
                print(f"  ✓ Extracted {len(works_list)} works in {len(content_sections)} sections")
                print(f"  ✓ Created: {filename}")
            else:
                extraction_log.append({
                    'author': author,
                    'works_found': 0,
                    'content_sections': 0,
                    'filename': None,
                    'status': 'not_found'
                })
                print(f"  ✗ No content found for {author}")
                
        except Exception as e:
            extraction_log.append({
                'author': author,
                'error': str(e),
                'status': 'error'
            })
            print(f"  ✗ Error processing {author}: {e}")
    
    # Create extraction log
    log_path = os.path.join(output_dir, "EXTRACTION_LOG.md")
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write("# Loeb Phase 1 Extraction Log\n\n")
        f.write(f"**Extraction Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"**Source**: {dsl_file}\n")
        f.write(f"**Total Authors Processed**: {len(priority_authors)}\n\n")
        
        successful = [log for log in extraction_log if log['status'] == 'success']
        not_found = [log for log in extraction_log if log['status'] == 'not_found']
        errors = [log for log in extraction_log if log['status'] == 'error']
        
        f.write(f"**Successful Extractions**: {len(successful)}\n")
        f.write(f"**Authors Not Found**: {len(not_found)}\n")
        f.write(f"**Errors**: {len(errors)}\n\n")
        
        f.write("## Successful Extractions\n\n")
        for log in successful:
            f.write(f"- **{log['author']}**: {log['works_found']} works, {log['content_sections']} sections → `{log['filename']}`\n")
        
        if not_found:
            f.write("\n## Authors Not Found\n\n")
            for log in not_found:
                f.write(f"- **{log['author']}**: No content found in DSL\n")
        
        if errors:
            f.write("\n## Errors\n\n")
            for log in errors:
                f.write(f"- **{log['author']}**: {log['error']}\n")
    
    print(f"\n✓ Phase 1 extraction complete!")
    print(f"✓ Extraction log created: {log_path}")
    print(f"✓ Successful extractions: {len(successful)}/{len(priority_authors)}")
    
    return extraction_log

if __name__ == "__main__":
    extraction_log = process_phase1_authors()