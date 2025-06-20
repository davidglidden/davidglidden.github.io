# Chamber YAML Template Standards
## Standardized Frontmatter for Mode 1 Documents

**Version**: 1.0  
**Purpose**: Ensure consistent YAML frontmatter across all Chamber documents  
**Date**: 2025-06-20

---

## Analysis of Current Issues

The Chamber system currently has two different YAML structures in use:

1. **Older structure** (from 2024-12-28 deliberation): Complex, protocol-focused
2. **Newer structure** (from 2025-06-19 deliberation): Simplified, workflow-aligned

The layouts are flexible and use conditional logic, but this inconsistency causes:
- Display errors when expected fields are missing
- Confusion about which fields to use
- Broken cross-references between documents
- Difficulty maintaining the system

---

## Standardized Templates

### Deliberation YAML Template

```yaml
---
title: "Deliberation Title"
date: YYYY-MM-DD
category: deliberation
tags: [tag1, tag2, tag3]
voices_featured: 
  - voice-name-1
  - voice-name-2
  - voice-name-3
generated_works: N  # number of works
essential_question: "Core question that emerged"
canon_entries:  # slugs of canon entries, not full paths
  - work-slug-1
  - work-slug-2
source_session: "YYYY-MM-DD-session-name"
protocol_used: "standard"  # or "first-light" or "shadow"
platforms_analyzed: [gpt, claude]  # which AI platforms used
---
```

### Canon Entry YAML Template

```yaml
---
title: "Work Title"
author: "Voice Name"  # who spoke/wrote this in Chamber
work_type: "theoretical"  # or practical, poetic, critical, etc.
notation: "°"  # or ~, †, §, ∞, ※
status: "chamber-generated"  # matches directory structure
created_in_session: "YYYY-MM-DD-session-name"
voice_origin: "Primary Voice Name"  # main voice who generated this
category: "subject-area"  # philosophy, music-theory, etc.

# DATE FIELDS - CRITICAL: Choose ONE format only
date: 2025-01-15  # For actual dates - MUST be YYYY-MM-DD format, unquoted
# OR
date_range: "1970s-1980s"  # For ranges, periods, or special dates - ALWAYS quoted

tags: 
  - tag1
  - tag2
  - tag3
related_works:  # slugs of related canon entries
  - related-work-1
  - related-work-2
chamber_appearances:  # all sessions where cited
  - "YYYY-MM-DD-session-name"
---
```

---

## Critical Date Field Rules (Jekyll Requirement)

**Jekyll strictly enforces date format validation. Breaking these rules causes build failures.**

### ✅ CORRECT Date Usage

```yaml
# Actual dates - unquoted, YYYY-MM-DD format only
date: 2025-06-14
date: 1942-01-01
date: 1823-03-15

# Ranges, periods, approximations - quoted string in date_range field
date_range: "1970s-1980s"
date_range: "c. 1465"
date_range: "2019-present"
date_range: "1910-1970"
date_range: "Undated manuscript"
date_range: "1609 (shadow interpretation)"
```

### ❌ INCORRECT - These Will Break Jekyll Build

```yaml
# These cause "Invalid Date" errors:
date: 1970s-1980s        # Range without quotes
date: "1910-1970"       # Range in date field (even quoted)
date: c. 1465           # Approximation without quotes
date: 2019-present      # Range without quotes
date: Undated manuscript # Text without quotes
```

### Template Display Logic

The Chamber layout (`_layouts/chamber.html`) handles both:
- `date` fields: Formatted as year only (`{{ work.date | date: "%Y" }}`)
- `date_range` fields: Displayed as-is (`{{ work.date_range }}`)

### Hakyll Migration Note

**Hakyll will likely handle this more gracefully** - Haskell's type system can distinguish between dates and strings naturally. Consider unifying to single `date` field post-migration using:
- `Date` type for actual dates
- `String` type for ranges/approximations
- Union type `Date | String` for flexible handling

---

## Migration Notes

### Fields to Remove from Old Deliberations
- `protocol:` → migrate to `protocol_used:`
- `engines:` → migrate to `platforms_analyzed:`
- `lead_voice:` → incorporate into content
- `submitted_text_type:` → remove (not needed)
- `emergent_voices:` → migrate to `voices_featured:`
- `refusals:` → move into content body
- `canonical_refs:` → simplify to `canon_entries:` (just slugs)
- `fictional_works_created:` → use `generated_works:`
- `shadow_works_created:` → remove (include in generated_works)
- `work_survives_shadow:` → move to content
- `session_summary:` → move to content
- `layout: page` → remove (layout determined by location)
- `class:` → remove (not needed for Chamber content)
- `chamber: true` → remove (redundant with category)
- `encounter: true` → remove (not applicable to Chamber)

### Fields to Keep Consistent
- `title:` - always present
- `date:` - always in YYYY-MM-DD format
- `tags:` - always as array

### Canon Entry Consistency
- `notation:` should match `marker:` field if present
- `author:` is the voice who spoke the work in Chamber
- Directory placement must match `notation:` field:
  - ° (chamber-generated) → `/chamber/canon/chamber-generated/`
  - ~ (hybrid) → `/chamber/canon/hybrid/`
  - † (contested) → `/chamber/canon/contested/`
  - § (synthesis) → `/chamber/canon/synthesis/`
  - ∞ (hermetic) → `/chamber/canon/hermetic/`
  - ※ (miscellaneous) → `/chamber/canon/inventions/`

---

## Implementation Checklist

1. [ ] Update workflow documentation to use these templates
2. [ ] Fix existing deliberations to match standard
3. [ ] Fix existing canon entries to match standard  
4. [ ] Update includes/layouts if needed for new field names
5. [ ] Test cross-references work properly
6. [ ] Document in CLAUDE.md for future reference

---

## Benefits of Standardization

1. **Predictable display**: Layouts know which fields to expect
2. **Working cross-references**: Consistent naming enables bliki features
3. **Easier maintenance**: Clear which fields belong where
4. **Future migration**: Clean data structure for Hakyll migration
5. **Workflow clarity**: Matches Mode 1 workflow documentation

---

*This template standard should be used for all Chamber content going forward.*