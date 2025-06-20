#!/usr/bin/env python3
"""
Chamber Count Validation Script
Ensures deliberation YAML matches actual canon entries created.
Run this after any Chamber processing to verify accuracy.
"""

import os
import re
import glob
import yaml
from pathlib import Path

def extract_frontmatter(file_path):
    """Extract YAML frontmatter from markdown file"""
    with open(file_path, 'r') as f:
        content = f.read()
    
    # Match YAML frontmatter between --- lines
    match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if match:
        try:
            return yaml.safe_load(match.group(1))
        except yaml.YAMLError:
            return None
    return None

def validate_deliberation(delib_path):
    """Validate a single deliberation file"""
    print(f"\n📋 Validating: {os.path.basename(delib_path)}")
    
    frontmatter = extract_frontmatter(delib_path)
    if not frontmatter:
        print("❌ Could not parse YAML frontmatter")
        return False
    
    session_id = frontmatter.get('source_session', '')
    claimed_count = frontmatter.get('generated_works', 0)
    claimed_entries = frontmatter.get('canon_entries', [])
    
    # Find actual canon entries for this session
    canon_files = glob.glob('chamber/canon/*/*.md')
    actual_entries = []
    
    for canon_file in canon_files:
        canon_frontmatter = extract_frontmatter(canon_file)
        if canon_frontmatter:
            if (canon_frontmatter.get('created_in_session') == session_id or
                session_id in str(canon_frontmatter.get('chambers_cited_in', []))):
                slug = Path(canon_file).stem
                actual_entries.append(slug)
    
    actual_count = len(actual_entries)
    
    print(f"  Session: {session_id}")
    print(f"  Claimed works: {claimed_count}")
    print(f"  Actual works: {actual_count}")
    print(f"  Claimed entries: {len(claimed_entries)}")
    
    # Validation checks
    success = True
    
    if claimed_count != actual_count:
        print(f"❌ COUNT MISMATCH: claimed {claimed_count}, actual {actual_count}")
        success = False
    else:
        print("✅ Count matches")
    
    if len(claimed_entries) != actual_count:
        print(f"❌ ENTRY LIST MISMATCH: listed {len(claimed_entries)}, actual {actual_count}")
        success = False
    else:
        print("✅ Entry list length matches")
    
    # Check if all actual entries are listed
    missing_entries = set(actual_entries) - set(claimed_entries)
    extra_entries = set(claimed_entries) - set(actual_entries)
    
    if missing_entries:
        print(f"❌ MISSING ENTRIES: {missing_entries}")
        success = False
    
    if extra_entries:
        print(f"❌ EXTRA ENTRIES: {extra_entries}")
        success = False
    
    if not missing_entries and not extra_entries and actual_entries:
        print("✅ All entries properly listed")
    
    return success

def main():
    """Validate all Chamber deliberations"""
    print("🔍 Chamber Count Validation")
    print("=" * 40)
    
    deliberation_files = glob.glob('chamber/deliberations/*.md')
    deliberation_files = [f for f in deliberation_files if not f.endswith('index.md')]
    
    all_valid = True
    
    for delib_file in sorted(deliberation_files):
        is_valid = validate_deliberation(delib_file)
        if not is_valid:
            all_valid = False
    
    print("\n" + "=" * 40)
    if all_valid:
        print("✅ ALL DELIBERATIONS VALID")
    else:
        print("❌ VALIDATION FAILED - Fix mismatches above")
        print("\nTo fix, update deliberation YAML:")
        print("- Set generated_works to actual count")
        print("- Update canon_entries array with correct slugs")
        print("- Ensure session IDs match between files")
    
    return all_valid

if __name__ == "__main__":
    main()