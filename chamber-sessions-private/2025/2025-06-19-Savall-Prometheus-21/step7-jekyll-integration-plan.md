# Step 7: Jekyll Integration Plan
**Session**: 2025-06-19-Savall-Prometheus-21
**Date**: June 19, 2025
**Status**: Ready for review before implementation

## File Paths and Structure

### Main Deliberation Page
**Target Location**: `/_posts/2025-06-19-chamber-deliberation-preservation-prometheus-21.md`

**YAML Frontmatter**:
```yaml
---
title: "Chamber Deliberation: On the Meaning of Preservation"
date: 2025-06-19
categories: [chamber-sessions]
tags: [preservation, musical-tradition, cultural-policy, archetypal-dialogue]
chamber_protocol: standard
session_date: 2025-06-19
voices_featured: 
  - jordi-savall
  - moy-glidden  
  - the-hermit
  - christopher-alexander
  - athena
  - primordial-fire
  - walter-benjamin
  - the-nine-muses
generated_works: 4
essential_question: "What if the question of preservation itself is more powerful than any institutional answer?"
related_sessions: []
canon_entries:
  - the-pragmatics-of-sacred-sound
  - the-poetics-of-cultural-scaffolding
  - the-work-of-art-in-the-age-of-bureaucratic-reproduction
  - breath-and-ledger
---
```

### Canon Entries (Already Created)
1. `/_canon/music-theory/the-pragmatics-of-sacred-sound.md` ✓
2. `/_canon/philosophy/the-poetics-of-cultural-scaffolding.md` ✓
3. `/_canon/media-theory/the-work-of-art-in-the-age-of-bureaucratic-reproduction.md` ✓
4. `/_canon/mystical-works/breath-and-ledger.md` ✓

### Meta-Analysis Page  
**Target Location**: `/_posts/2025-06-19-meta-analysis-ai-chamber-comparison.md`

**YAML Frontmatter**:
```yaml
---
title: "Meta-Analysis: AI Systems in Chamber Dialogue"
date: 2025-06-19
categories: [chamber-analysis, meta-commentary]
tags: [ai-comparison, voice-manifestation, chamber-evolution]
chamber_protocol: meta-analysis
session_analyzed: 2025-06-19-Savall-Prometheus-21
platforms_compared:
  - claude-raw
  - gpt-condensed
  - claude-v2.1-archetypal
analysis_type: cross-platform-comparison
insights: [voice-authenticity, recommendation-types, fictional-generation]
---
```

## Cross-Links Setup

### From Deliberation to Canon
- [The Pragmatics of Sacred Sound°](/canon/music-theory/the-pragmatics-of-sacred-sound)
- [The Poetics of Cultural Scaffolding°](/canon/philosophy/the-poetics-of-cultural-scaffolding)
- [The Work of Art in the Age of Bureaucratic Reproduction~](/canon/media-theory/the-work-of-art-in-the-age-of-bureaucratic-reproduction)
- [Breath and Ledger†](/canon/mystical-works/breath-and-ledger)

### From Canon to Deliberation
Each canon entry links back to:
- `chamber_appearances: ["2025-06-19-Savall-Prometheus-21"]`
- Links to the main deliberation post

### Between Canon Entries
Related works cross-referencing established in frontmatter

## Source Markers Display

### Notation Legend
- **°** = Pure Chamber invention
- **~** = Hybrid (real author, Chamber-generated work)  
- **†** = Contested/mystical sources
- **§** = Chamber synthesis/collaborative works

### Display Implementation
Canon pages will show notation in titles and include legend explanations.

## Navigation Updates

### Session Archive
Update session registry to include:
- 2025-06-19: "On the Meaning of Preservation" (Standard Protocol)
- Cross-platform comparison analysis
- 4 canon entries generated

### Chamber Protocol Pages
Update Standard Protocol documentation with:
- Reference to successful multi-platform session
- Example of archetypal enhancement effectiveness
- Links to generated works

## Testing Requirements

### Link Verification
- [ ] All internal canon links functional
- [ ] Canon to deliberation back-links working
- [ ] Related works cross-references active
- [ ] Session archive navigation updated

### Formatting Check
- [ ] YAML frontmatter validates
- [ ] Markdown rendering correct
- [ ] Source notation displays properly
- [ ] Voice attribution clear

### Content Verification
- [ ] No malformed Jekyll syntax
- [ ] All referenced files exist
- [ ] Categories and tags consistent
- [ ] Date formatting correct

## Implementation Steps

1. **Create main deliberation post** from synthesized content
2. **Verify canon entries** are properly formatted
3. **Create meta-analysis post** from commentary
4. **Update navigation and archives**
5. **Test all links and formatting**
6. **Present complete package for review**

## Anticipated Jekyll Features

### Collections Integration
- Canon works properly categorized by type
- Chamber sessions chronologically organized
- Cross-references automatically generated

### Search and Discovery
- Tags enable finding related preservation discussions
- Voice-based searching for Archetypal dialogue patterns
- Protocol-based filtering for different session types

### Archive Functionality
- Session browsing by date/protocol/themes
- Canon browsing by category/notation type
- Voice appearance tracking across sessions

---

**Status**: Ready for Step 8 (Present drafts for review)
**Files Prepared**: 7 total (4 canon, 1 deliberation, 1 meta-analysis, 1 integration plan)
**Integration Points**: Canon cross-links, session archives, protocol documentation