#!/usr/bin/env python3
"""
Chamber Structure Migration Script

This script consolidates all Chamber deliberations and canon entries,
standardizes their YAML frontmatter, and ensures consistent file locations.
"""

import os
import yaml
import shutil
from pathlib import Path
from datetime import datetime

# File locations
SITE_ROOT = Path(__file__).parent.parent.parent.parent
OLD_DELIBERATIONS = SITE_ROOT / '_chamber_deliberations'
NEW_DELIBERATIONS = SITE_ROOT / 'chamber' / 'deliberations'
CANON_ROOT = SITE_ROOT / 'chamber' / 'canon'

# YAML field mappings for migration
DELIBERATION_FIELD_MAPPING = {
    'emergent_voices': 'voices_featured',
    'fictional_works_created': 'generated_works',
    'protocol': 'protocol_used',
    'engines': 'platforms_analyzed'
}

CANON_FIELD_MAPPING = {
    'attributed_to': 'author',
    'marker': 'notation',
    'source_type': 'work_type',
    'date_claimed': 'date',
    'first_cited': 'created_in_session'
}

# Fields to remove
FIELDS_TO_REMOVE = [
    'layout', 'class', 'chamber', 'encounter', 'lead_voice', 
    'submitted_text_type', 'refusals', 'canonical_refs',
    'shadow_works_created', 'work_survives_shadow', 'session_summary'
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


def migrate_deliberation_yaml(frontmatter):
    """Migrate deliberation YAML to new standard."""
    if not frontmatter:
        return frontmatter
    
    # Apply field mappings
    for old_field, new_field in DELIBERATION_FIELD_MAPPING.items():
        if old_field in frontmatter:
            frontmatter[new_field] = frontmatter.pop(old_field)
    
    # Remove unwanted fields
    for field in FIELDS_TO_REMOVE:
        frontmatter.pop(field, None)
    
    # Ensure required fields exist with defaults
    if 'category' not in frontmatter:
        frontmatter['category'] = 'deliberation'
    
    if 'tags' not in frontmatter:
        frontmatter['tags'] = ['chamber-examination']
    
    if 'generated_works' not in frontmatter:
        frontmatter['generated_works'] = 0
    
    if 'essential_question' not in frontmatter:
        frontmatter['essential_question'] = 'To be determined from content'
    
    if 'canon_entries' not in frontmatter:
        frontmatter['canon_entries'] = []
    
    if 'source_session' not in frontmatter:
        # Try to extract from filename
        filename = frontmatter.get('filename', '')
        if filename:
            parts = filename.split('-')
            if len(parts) >= 3:
                frontmatter['source_session'] = '-'.join(parts[:3])
    
    # Ensure platforms_analyzed is a list
    if 'platforms_analyzed' in frontmatter and isinstance(frontmatter['platforms_analyzed'], str):
        frontmatter['platforms_analyzed'] = [frontmatter['platforms_analyzed']]
    
    return frontmatter


def migrate_canon_yaml(frontmatter, directory_name):
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
    
    # Set status based on directory
    if 'status' not in frontmatter:
        if 'chamber-generated' in directory_name:
            frontmatter['status'] = 'chamber-generated'
        elif 'hybrid' in directory_name:
            frontmatter['status'] = 'hybrid'
        elif 'contested' in directory_name:
            frontmatter['status'] = 'contested'
        elif 'hermetic' in directory_name:
            frontmatter['status'] = 'hermetic'
        elif 'inventions' in directory_name:
            frontmatter['status'] = 'chamber-generated'
        else:
            frontmatter['status'] = 'unknown'
    
    # Set category based on directory if missing
    if 'category' not in frontmatter:
        if 'music' in directory_name or 'music' in frontmatter.get('title', '').lower():
            frontmatter['category'] = 'music-theory'
        elif 'philosophy' in directory_name or any(word in frontmatter.get('title', '').lower() 
                                                  for word in ['philosophy', 'ethics', 'metaphysics']):
            frontmatter['category'] = 'philosophy'
        else:
            frontmatter['category'] = 'general'
    
    # Ensure required fields exist with defaults
    if 'tags' not in frontmatter:
        frontmatter['tags'] = ['chamber-work']
    
    if 'voice_origin' not in frontmatter and 'author' in frontmatter:
        frontmatter['voice_origin'] = frontmatter['author']
    
    return frontmatter


def migrate_deliberations():
    """Migrate all deliberations to consolidated location."""
    print("MIGRATING DELIBERATIONS")
    print("=" * 40)
    
    # Ensure target directory exists
    NEW_DELIBERATIONS.mkdir(parents=True, exist_ok=True)
    
    migrated_files = []
    
    # Process files from _chamber_deliberations
    if OLD_DELIBERATIONS.exists():
        for root, dirs, files in os.walk(OLD_DELIBERATIONS):
            for file in files:
                if file.endswith('.md') and file != 'index.md':
                    old_path = Path(root) / file
                    new_path = NEW_DELIBERATIONS / file
                    
                    print(f"\nMigrating: {old_path.relative_to(SITE_ROOT)}")
                    print(f"       to: {new_path.relative_to(SITE_ROOT)}")
                    
                    # Load and migrate YAML
                    frontmatter, body = load_yaml_frontmatter(old_path)
                    if frontmatter:
                        frontmatter['filename'] = file  # Add for source_session extraction
                        migrated_yaml = migrate_deliberation_yaml(frontmatter)
                        
                        # Save to new location
                        save_markdown_file(new_path, migrated_yaml, body)
                        migrated_files.append(str(new_path.relative_to(SITE_ROOT)))
                    else:
                        # Just copy if no frontmatter
                        shutil.copy2(old_path, new_path)
    
    # Process files already in chamber/deliberations subdirectories
    for subdir in ['standard', 'first-light', 'shadow']:
        subdir_path = NEW_DELIBERATIONS / subdir
        if subdir_path.exists():
            for file in subdir_path.glob('*.md'):
                if file.name != 'index.md':
                    new_path = NEW_DELIBERATIONS / file.name
                    
                    print(f"\nFlattening: {file.relative_to(SITE_ROOT)}")
                    print(f"        to: {new_path.relative_to(SITE_ROOT)}")
                    
                    # Load and migrate YAML
                    frontmatter, body = load_yaml_frontmatter(file)
                    if frontmatter:
                        frontmatter['filename'] = file.name
                        migrated_yaml = migrate_deliberation_yaml(frontmatter)
                        
                        # Save to flattened location
                        save_markdown_file(new_path, migrated_yaml, body)
                        migrated_files.append(str(new_path.relative_to(SITE_ROOT)))
                    
                    # Remove original
                    file.unlink()
            
            # Remove empty subdirectory
            if subdir_path.exists() and not any(subdir_path.iterdir()):
                subdir_path.rmdir()
    
    print(f"\nMigrated {len(migrated_files)} deliberation files")
    return migrated_files


def migrate_canon_entries():
    """Migrate all canon entries to standardized YAML."""
    print("\nMIGRATING CANON ENTRIES")
    print("=" * 40)
    
    migrated_files = []
    
    for root, dirs, files in os.walk(CANON_ROOT):
        for file in files:
            if file.endswith('.md') and file not in ['index.md', 'all.md', 'recent.md']:
                filepath = Path(root) / file
                directory_name = Path(root).name
                
                print(f"\nMigrating: {filepath.relative_to(SITE_ROOT)}")
                
                # Load and migrate YAML
                frontmatter, body = load_yaml_frontmatter(filepath)
                if frontmatter:
                    migrated_yaml = migrate_canon_yaml(frontmatter, directory_name)
                    
                    # Save back to same location
                    save_markdown_file(filepath, migrated_yaml, body)
                    migrated_files.append(str(filepath.relative_to(SITE_ROOT)))
    
    print(f"\nMigrated {len(migrated_files)} canon entry files")
    return migrated_files


def cleanup_old_structure():
    """Remove old _chamber_deliberations directory."""
    print("\nCLEANING UP OLD STRUCTURE")
    print("=" * 40)
    
    if OLD_DELIBERATIONS.exists():
        print(f"Removing: {OLD_DELIBERATIONS.relative_to(SITE_ROOT)}")
        shutil.rmtree(OLD_DELIBERATIONS)
        print("✓ Old _chamber_deliberations directory removed")
    else:
        print("✓ Old directory already removed")


def main():
    """Run the complete migration."""
    print("CHAMBER STRUCTURE MIGRATION")
    print("=" * 50)
    print(f"Site root: {SITE_ROOT}")
    print(f"Timestamp: {datetime.now().isoformat()}")
    print()
    
    # Run migrations
    deliberations = migrate_deliberations()
    canon_entries = migrate_canon_entries()
    cleanup_old_structure()
    
    # Summary
    print("\nMIGRATION COMPLETE")
    print("=" * 50)
    print(f"Deliberations migrated: {len(deliberations)}")
    print(f"Canon entries migrated: {len(canon_entries)}")
    print(f"Total files processed: {len(deliberations) + len(canon_entries)}")
    
    print("\nNext steps:")
    print("1. Run the site locally to test")
    print("2. Update _config.yml if needed to remove _chamber_deliberations collection")
    print("3. Verify all cross-references work properly")
    print("4. Commit changes after testing")


if __name__ == "__main__":
    main()