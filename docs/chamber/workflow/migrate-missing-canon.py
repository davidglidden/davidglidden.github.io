#!/usr/bin/env python3
"""
Migrate Missing Canon Entries

This script identifies and migrates canon entries from old collections
that are missing from the current chamber/canon/ structure.
"""

import os
import yaml
import shutil
from pathlib import Path

# File locations
SITE_ROOT = Path(__file__).parent.parent.parent.parent
OLD_CHAMBER_CANON = SITE_ROOT / '_chamber_canon'
OLD_CANON = SITE_ROOT / '_canon'
CURRENT_CANON = SITE_ROOT / 'chamber' / 'canon'

# YAML field mappings for migration
CANON_FIELD_MAPPING = {
    'attributed_to': 'author',
    'marker': 'notation', 
    'source_type': 'work_type',
    'date_claimed': 'date',
    'first_cited': 'created_in_session'
}

# Fields to remove
FIELDS_TO_REMOVE = [
    'layout', 'class', 'chamber', 'encounter'
]


def load_yaml_frontmatter(filepath):
    """Load YAML frontmatter from a markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if not content.startswith('---'):
        return None, content
    
    end_index = content.find('\n---\n', 4)
    if end_index == -1:
        return None, content
    
    yaml_content = content[4:end_index]
    body_content = content[end_index + 5:]
    
    try:
        frontmatter = yaml.safe_load(yaml_content)
        return frontmatter, body_content
    except yaml.YAMLError as e:
        print(f"Error parsing YAML in {filepath}: {e}")
        return None, content


def save_markdown_file(filepath, frontmatter, body):
    """Save a markdown file with YAML frontmatter."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('---\n')
        yaml.dump(frontmatter, f, default_flow_style=False, allow_unicode=True)
        f.write('---\n')
        f.write(body)


def migrate_canon_yaml(frontmatter, source_path):
    """Migrate canon entry YAML to new standard."""
    if not frontmatter:
        return frontmatter
    
    # Apply field mappings
    for old_field, new_field in CANON_FIELD_MAPPING.items():
        if old_field in frontmatter:
            frontmatter[new_field] = frontmatter.pop(old_field)
    
    # Remove unwanted fields
    for field in FIELDS_TO_REMOVE:
        frontmatter.pop(field, None)
    
    # Determine status and category from content/path
    if 'status' not in frontmatter:
        frontmatter['status'] = 'chamber-generated'
    
    # Set category based on content if missing
    if 'category' not in frontmatter:
        title_lower = frontmatter.get('title', '').lower()
        if any(word in title_lower for word in ['music', 'sound', 'acoustic']):
            frontmatter['category'] = 'music-theory'
        elif any(word in title_lower for word in ['pattern', 'architecture', 'building']):
            frontmatter['category'] = 'architecture'
        elif any(word in title_lower for word in ['philosophy', 'ethics', 'metaphysics']):
            frontmatter['category'] = 'philosophy'
        elif any(word in title_lower for word in ['teaching', 'pedagogy', 'learning']):
            frontmatter['category'] = 'pedagogy'
        else:
            frontmatter['category'] = 'general'
    
    # Ensure required fields exist with defaults
    if 'tags' not in frontmatter:
        frontmatter['tags'] = ['chamber-work']
    
    if 'voice_origin' not in frontmatter and 'author' in frontmatter:
        frontmatter['voice_origin'] = frontmatter['author']
    
    if 'work_type' not in frontmatter:
        frontmatter['work_type'] = 'theoretical'
    
    if 'notation' not in frontmatter:
        frontmatter['notation'] = '°'  # Default to chamber-generated
    
    if 'created_in_session' not in frontmatter:
        frontmatter['created_in_session'] = 'unknown-session'
    
    return frontmatter


def determine_target_directory(frontmatter, filepath):
    """Determine which subdirectory a canon entry should go in."""
    notation = frontmatter.get('notation', '°')
    status = frontmatter.get('status', 'chamber-generated')
    
    # Map notation to directory
    if notation == '°':
        if 'invention' in str(filepath).lower():
            return 'inventions'
        else:
            return 'chamber-generated'
    elif notation == '~':
        return 'hybrid'
    elif notation == '†':
        return 'contested'
    elif notation == '§':
        return 'synthesis'
    elif notation == '∞':
        return 'hermetic'
    elif notation == '◊':
        return 'living'
    else:
        return 'chamber-generated'  # Default


def get_current_canon_files():
    """Get set of current canon file basenames."""
    current_files = set()
    for root, dirs, files in os.walk(CURRENT_CANON):
        for file in files:
            if file.endswith('.md') and file not in ['index.md', 'all.md', 'recent.md']:
                current_files.add(file)
    return current_files


def migrate_missing_files():
    """Migrate files from old collections that aren't in current structure."""
    print("MIGRATING MISSING CANON ENTRIES")
    print("=" * 50)
    
    current_files = get_current_canon_files()
    migrated_files = []
    skipped_duplicates = []
    
    # Process _chamber_canon
    if OLD_CHAMBER_CANON.exists():
        for root, dirs, files in os.walk(OLD_CHAMBER_CANON):
            for file in files:
                if file.endswith('.md'):
                    if file in current_files:
                        skipped_duplicates.append(f"_chamber_canon/{file}")
                        continue
                    
                    old_path = Path(root) / file
                    
                    # Load and migrate
                    frontmatter, body = load_yaml_frontmatter(old_path)
                    if frontmatter:
                        migrated_yaml = migrate_canon_yaml(frontmatter, old_path)
                        target_dir = determine_target_directory(migrated_yaml, old_path)
                        
                        # Ensure target directory exists
                        target_path = CURRENT_CANON / target_dir
                        target_path.mkdir(exist_ok=True)
                        
                        new_file_path = target_path / file
                        
                        print(f"\nMigrating: {old_path.relative_to(SITE_ROOT)}")
                        print(f"       to: {new_file_path.relative_to(SITE_ROOT)}")
                        print(f"  Category: {migrated_yaml.get('category', 'unknown')}")
                        print(f"  Notation: {migrated_yaml.get('notation', '?')}")
                        
                        save_markdown_file(new_file_path, migrated_yaml, body)
                        migrated_files.append(str(new_file_path.relative_to(SITE_ROOT)))
    
    # Process _canon
    if OLD_CANON.exists():
        for root, dirs, files in os.walk(OLD_CANON):
            for file in files:
                if file.endswith('.md'):
                    if file in current_files:
                        skipped_duplicates.append(f"_canon/{file}")
                        continue
                    
                    old_path = Path(root) / file
                    
                    # Load and migrate
                    frontmatter, body = load_yaml_frontmatter(old_path)
                    if frontmatter:
                        migrated_yaml = migrate_canon_yaml(frontmatter, old_path)
                        target_dir = determine_target_directory(migrated_yaml, old_path)
                        
                        # Ensure target directory exists
                        target_path = CURRENT_CANON / target_dir
                        target_path.mkdir(exist_ok=True)
                        
                        new_file_path = target_path / file
                        
                        print(f"\nMigrating: {old_path.relative_to(SITE_ROOT)}")
                        print(f"       to: {new_file_path.relative_to(SITE_ROOT)}")
                        print(f"  Category: {migrated_yaml.get('category', 'unknown')}")
                        print(f"  Notation: {migrated_yaml.get('notation', '?')}")
                        
                        save_markdown_file(new_file_path, migrated_yaml, body)
                        migrated_files.append(str(new_file_path.relative_to(SITE_ROOT)))
    
    # Summary
    print(f"\n\nMIGRATION COMPLETE")
    print("=" * 50)
    print(f"Files migrated: {len(migrated_files)}")
    print(f"Duplicates skipped: {len(skipped_duplicates)}")
    
    if migrated_files:
        print(f"\nMigrated files:")
        for file in migrated_files:
            print(f"  ✓ {file}")
    
    if skipped_duplicates:
        print(f"\nSkipped duplicates:")
        for file in skipped_duplicates:
            print(f"  ~ {file}")
    
    return migrated_files, skipped_duplicates


if __name__ == "__main__":
    migrated, skipped = migrate_missing_files()
    
    print(f"\n\nNext steps:")
    print("1. Verify migrated files look correct")
    print("2. Test site build")
    print("3. Remove old collections: _chamber_canon, _canon, _chamber_meta")