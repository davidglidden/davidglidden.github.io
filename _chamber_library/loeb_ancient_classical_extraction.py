#!/usr/bin/env python3
"""
Loeb Ancient & Classical Sources Extraction
Extracts the additional authors from the acquisition lists that are available in Loeb.
"""

import re
import os
from pathlib import Path
from datetime import datetime

def get_ancient_classical_authors():
    """
    Define the Ancient & Classical authors from acquisition lists that are available in Loeb.
    """
    return {
        'SAPPHO': {
            'voice_role': 'Ancient Greek Lyric Poet',
            'tradition': 'archaic_greek_lyric',
            'language': 'grc',
            'period': '7th-6th century BCE',
            'philosophical_school': 'Lesbian Poetry',
            'major_themes': ['Love', 'Beauty', 'Female Voice', 'Desire'],
            'acquisition_list_title': 'Complete Poems'
        },
        'PARMENIDES': {
            'voice_role': 'Pre-Socratic Philosopher',
            'tradition': 'pre_socratic',
            'language': 'grc',
            'period': '6th-5th century BCE',
            'philosophical_school': 'Eleatic School',
            'major_themes': ['Being', 'Truth', 'Appearance', 'Unity'],
            'acquisition_list_title': 'The Way of Truth'
        },
        'HERACLITUS': {
            'voice_role': 'Pre-Socratic Philosopher',
            'tradition': 'pre_socratic',
            'language': 'grc',
            'period': '6th-5th century BCE',
            'philosophical_school': 'Ephesian Philosophy',
            'major_themes': ['Flow', 'Change', 'Logos', 'Unity of Opposites'],
            'acquisition_list_title': 'Fragments'
        },
        'PYTHAGORAS': {
            'voice_role': 'Pre-Socratic Philosopher and Mathematician',
            'tradition': 'pre_socratic',
            'language': 'grc',
            'period': '6th century BCE',
            'philosophical_school': 'Pythagorean School',
            'major_themes': ['Number', 'Cosmos', 'Harmony', 'Soul'],
            'acquisition_list_title': 'The Golden Verses'
        },
        'VITRUVIUS': {
            'voice_role': 'Roman Architect and Engineer',
            'tradition': 'roman_technical',
            'language': 'la',
            'period': '1st century BCE',
            'philosophical_school': 'Classical Architecture',
            'major_themes': ['Architecture', 'Design Principles', 'Proportion', 'Utility'],
            'acquisition_list_title': 'The Ten Books on Architecture'
        },
        'AUGUSTINE': {
            'voice_role': 'Christian Theologian and Philosopher',
            'tradition': 'christian_classical',
            'language': 'la',
            'period': '4th-5th century CE',
            'philosophical_school': 'Christian Platonism',
            'major_themes': ['Confession', 'Time', 'Memory', 'Divine Grace'],
            'acquisition_list_title': 'Confessions'
        }
    }

def create_ancient_yaml_frontmatter(author, author_info):
    """
    Create Chamber-appropriate YAML frontmatter for Ancient & Classical authors.
    """
    yaml = f"""---
title: "{author_info['acquisition_list_title']}"
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
acquisition_list: "Ancient & Classical Sources"
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

def process_ancient_classical_authors():
    """
    Process Ancient & Classical authors from the acquisition lists that are available in Loeb.
    """
    dsl_file = "/Users/davidglidden/Documents/Loeb Classical All Library 537 Volumes/loeb.dsl"
    output_dir = "/Users/davidglidden/Documents/GitHub/davidglidden.github.io/_chamber_library/converted_texts/loeb_classical/ancient_classical"
    
    # Create output directory
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    ancient_authors = get_ancient_classical_authors()
    extraction_log = []
    
    print(f"Processing {len(ancient_authors)} Ancient & Classical authors from acquisition lists...")
    
    for author, author_info in ancient_authors.items():
        print(f"\nProcessing {author}...")
        
        try:
            content_sections, works_list = extract_author_content(dsl_file, author)
            
            if content_sections:
                # Create YAML frontmatter
                yaml_header = create_ancient_yaml_frontmatter(author, author_info)
                
                # Combine all content
                full_content = yaml_header + '\n' + '\n\n---\n\n'.join(content_sections)
                
                # Create filename
                filename = f"loeb_{author.lower().replace(' ', '_')}_ancient_classical.md"
                filepath = os.path.join(output_dir, filename)
                
                # Write file
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(full_content)
                
                extraction_log.append({
                    'author': author,
                    'works_found': len(works_list),
                    'content_sections': len(content_sections),
                    'filename': filename,
                    'status': 'success',
                    'acquisition_title': author_info['acquisition_list_title']
                })
                
                print(f"  ✓ Extracted {len(works_list)} works in {len(content_sections)} sections")
                print(f"  ✓ Created: {filename}")
            else:
                extraction_log.append({
                    'author': author,
                    'works_found': 0,
                    'content_sections': 0,
                    'filename': None,
                    'status': 'not_found',
                    'acquisition_title': author_info['acquisition_list_title']
                })
                print(f"  ✗ No content found for {author}")
                
        except Exception as e:
            extraction_log.append({
                'author': author,
                'error': str(e),
                'status': 'error',
                'acquisition_title': author_info['acquisition_list_title']
            })
            print(f"  ✗ Error processing {author}: {e}")
    
    # Create extraction log
    log_path = os.path.join(output_dir, "ANCIENT_CLASSICAL_EXTRACTION_LOG.md")
    with open(log_path, 'w', encoding='utf-8') as f:
        f.write("# Ancient & Classical Sources Extraction Log\n\n")
        f.write(f"**Extraction Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write(f"**Source**: {dsl_file}\n")
        f.write(f"**Authors from Acquisition Lists**: {len(ancient_authors)}\n\n")
        
        successful = [log for log in extraction_log if log['status'] == 'success']
        not_found = [log for log in extraction_log if log['status'] == 'not_found']
        errors = [log for log in extraction_log if log['status'] == 'error']
        
        f.write(f"**Successful Extractions**: {len(successful)}\n")
        f.write(f"**Authors Not Found**: {len(not_found)}\n")
        f.write(f"**Errors**: {len(errors)}\n\n")
        
        f.write("## Successful Extractions\n\n")
        for log in successful:
            f.write(f"- **{log['author']}** ({log['acquisition_title']}): {log['works_found']} works, {log['content_sections']} sections → `{log['filename']}`\n")
        
        if not_found:
            f.write("\n## Authors Not Found\n\n")
            for log in not_found:
                f.write(f"- **{log['author']}** ({log['acquisition_title']}): No content found in DSL\n")
        
        if errors:
            f.write("\n## Errors\n\n")
            for log in errors:
                f.write(f"- **{log['author']}** ({log['acquisition_title']}): {log['error']}\n")
    
    print(f"\n✓ Ancient & Classical extraction complete!")
    print(f"✓ Extraction log created: {log_path}")
    print(f"✓ Successful extractions: {len(successful)}/{len(ancient_authors)}")
    
    return extraction_log

if __name__ == "__main__":
    extraction_log = process_ancient_classical_authors()