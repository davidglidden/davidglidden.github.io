#!/usr/bin/env python3
"""
Chamber YAML Frontmatter Audit Tool

This script audits all Chamber deliberations and canon entries to identify
which files need to be updated to match the standardized YAML template.
"""

import os
import yaml
import sys
from pathlib import Path

# Expected fields for each document type
DELIBERATION_FIELDS = {
    'required': ['title', 'date', 'category', 'tags', 'voices_featured', 
                 'generated_works', 'essential_question', 'canon_entries', 
                 'source_session'],
    'optional': ['protocol_used', 'platforms_analyzed']
}

CANON_FIELDS = {
    'required': ['title', 'author', 'work_type', 'notation', 'status', 
                 'created_in_session', 'voice_origin', 'category', 'tags'],
    'optional': ['related_works', 'chamber_appearances']
}

# Old fields that should be removed or migrated
OLD_FIELDS = [
    'protocol', 'engines', 'lead_voice', 'submitted_text_type', 
    'emergent_voices', 'refusals', 'canonical_refs', 'fictional_works_created',
    'shadow_works_created', 'work_survives_shadow', 'session_summary',
    'layout', 'class', 'chamber', 'encounter'
]


def extract_yaml_frontmatter(filepath):
    """Extract YAML frontmatter from a markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if not content.startswith('---'):
        return None
    
    # Find the closing ---
    end_index = content.find('\n---\n', 4)
    if end_index == -1:
        return None
    
    yaml_content = content[4:end_index]
    try:
        return yaml.safe_load(yaml_content)
    except yaml.YAMLError as e:
        print(f"Error parsing YAML in {filepath}: {e}")
        return None


def audit_file(filepath, expected_fields, file_type):
    """Audit a single file for YAML compliance."""
    frontmatter = extract_yaml_frontmatter(filepath)
    if not frontmatter:
        return {
            'file': filepath,
            'type': file_type,
            'status': 'NO_FRONTMATTER',
            'issues': ['No YAML frontmatter found']
        }
    
    issues = []
    
    # Check for missing required fields
    for field in expected_fields['required']:
        if field not in frontmatter:
            issues.append(f"Missing required field: {field}")
    
    # Check for old fields that should be removed
    old_fields_present = []
    for field in OLD_FIELDS:
        if field in frontmatter:
            old_fields_present.append(field)
    
    if old_fields_present:
        issues.append(f"Old fields to remove/migrate: {', '.join(old_fields_present)}")
    
    # Check specific field formats
    if 'date' in frontmatter:
        date_str = str(frontmatter['date'])
        if not date_str or len(date_str) != 10 or date_str[4] != '-' or date_str[7] != '-':
            issues.append(f"Date format issue: {date_str} (should be YYYY-MM-DD)")
    
    if 'tags' in frontmatter and not isinstance(frontmatter['tags'], list):
        issues.append("Tags should be an array")
    
    status = 'OK' if not issues else 'NEEDS_UPDATE'
    
    return {
        'file': filepath,
        'type': file_type,
        'status': status,
        'issues': issues,
        'current_fields': list(frontmatter.keys())
    }


def main():
    """Run the audit on all Chamber files."""
    base_path = Path(__file__).parent.parent.parent.parent  # Go up to site root
    
    # Audit deliberations
    deliberations_path = base_path / 'chamber' / 'deliberations'
    deliberation_results = []
    
    for root, dirs, files in os.walk(deliberations_path):
        for file in files:
            if file.endswith('.md') and file != 'index.md':
                filepath = os.path.join(root, file)
                result = audit_file(filepath, DELIBERATION_FIELDS, 'deliberation')
                deliberation_results.append(result)
    
    # Audit canon entries
    canon_path = base_path / 'chamber' / 'canon'
    canon_results = []
    
    for root, dirs, files in os.walk(canon_path):
        # Skip index files
        if 'chamber/canon' in root and root != str(canon_path):
            for file in files:
                if file.endswith('.md') and file not in ['index.md', 'all.md', 'recent.md']:
                    filepath = os.path.join(root, file)
                    result = audit_file(filepath, CANON_FIELDS, 'canon')
                    canon_results.append(result)
    
    # Print results
    print("CHAMBER YAML FRONTMATTER AUDIT REPORT")
    print("=" * 50)
    print()
    
    print("DELIBERATIONS:")
    print("-" * 30)
    for result in deliberation_results:
        print(f"\n{result['file'].replace(str(base_path), '.')}")
        print(f"Status: {result['status']}")
        if result['issues']:
            print("Issues:")
            for issue in result['issues']:
                print(f"  - {issue}")
        if result['status'] == 'NEEDS_UPDATE':
            print(f"Current fields: {', '.join(result['current_fields'])}")
    
    print("\n\nCANON ENTRIES:")
    print("-" * 30)
    for result in canon_results:
        print(f"\n{result['file'].replace(str(base_path), '.')}")
        print(f"Status: {result['status']}")
        if result['issues']:
            print("Issues:")
            for issue in result['issues']:
                print(f"  - {issue}")
        if result['status'] == 'NEEDS_UPDATE':
            print(f"Current fields: {', '.join(result['current_fields'])}")
    
    # Summary
    print("\n\nSUMMARY:")
    print("-" * 30)
    delib_need_update = sum(1 for r in deliberation_results if r['status'] == 'NEEDS_UPDATE')
    canon_need_update = sum(1 for r in canon_results if r['status'] == 'NEEDS_UPDATE')
    
    print(f"Deliberations needing update: {delib_need_update}/{len(deliberation_results)}")
    print(f"Canon entries needing update: {canon_need_update}/{len(canon_results)}")
    print(f"Total files needing update: {delib_need_update + canon_need_update}")


if __name__ == "__main__":
    main()