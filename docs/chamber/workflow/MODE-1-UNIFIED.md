# Chamber Mode 1: Unified Workflow
## Complete Standard Processing Protocol

**Version**: 4.0 (Unified)  
**Date**: June 2025  
**Purpose**: Single source of truth for Mode 1 Chamber operations  
**Context**: David runs sessions → Claude Code processes for publication  
**Access**: Private - David Glidden only  

---

## Overview

Mode 1 is the **standard Chamber operation** where David runs multi-platform AI sessions and Claude Code processes results for publication. This workflow ensures consistent quality, proper archival, and IP protection.

### Key Characteristics
- **Multi-platform analysis**: GPT + Claude 
- **Three protocols**: Standard, First Light, Shadow
- **Complete archival**: All raw materials preserved indefinitely
- **Confidential meta-analysis**: Platform behavior and voice manifestation studies
- **Standardized publication**: Consistent YAML, proper categorization

---

# DAVID'S WORKFLOW (Steps 1-2)

## Step 1: Choose Protocol and Execute Session

Create session folder: `chamber-sessions-private/YYYY/YYYY-MM-DD-title/`

**Choose ONE protocol per session** using master prompts from `docs/chamber/protocols/prompts/`:

### For First Light Protocol:
Use prompts from `docs/chamber/protocols/prompts/first-light/`
1. **GPT First Light** → save as `[first-light]gpt-raw.txt`
2. **Claude First Light** → save as `[first-light]claude-raw.txt`
3. **Original text** → save as `[first-light]submitted-text.txt`

### For Standard Protocol:
Use prompts from `docs/chamber/protocols/prompts/standard/`
1. **GPT Standard** → save as `[standard]gpt-raw.txt`
2. **Claude Standard** → save as `[standard]claude-raw.txt`
3. **Original text** → save as `[standard]submitted-text.txt`

### For Shadow Protocol:
Use prompts from `docs/chamber/protocols/prompts/shadow/`
1. **GPT Shadow** → save as `[shadow]gpt-raw.txt`
2. **Claude Shadow** → save as `[shadow]claude-raw.txt`
3. **Original text** → save as `[shadow]submitted-text.txt`

**Optional:**
- `session-notes.md` - Any observations about the process

## Step 2: Send to Claude Code
**Notify with**: "New deliberation awaiting Mode 1 processing"

Include any notes about:
- Which voices surprised you
- Any fictional references that particularly stood out
- Overall impression of the session
- Reason for choosing this protocol

---

# CLAUDE CODE'S WORKFLOW (Steps 3-9)

## Step 3: Protocol Detection and Fictional Reference Extraction
1. **Auto-detect protocol** from filename brackets: `[first-light]`, `[standard]`, or `[shadow]`
2. **Read all session files** simultaneously using batch tool calls
3. **Hunt for fictional works** marked with notation (°, ~, †, §, ∞, ※)

Create comprehensive extraction document (`step3-fictional-references-extraction.md`):
- All fictional works by voice (from all AI outputs)
- Overlapping citations between engines
- Conflicts or variations between platforms
- Assessment of which works merit canon entries
- Protocol-specific patterns (First Light gentler, Shadow more accusatory)
- Multi-platform voice manifestation differences

## Step 4: Create Canon Entries

**Assessment criteria for canon development:**
- **Foundational** - could influence future Chamber thinking
- **Generative** - opens rather than closes inquiry
- **Substantial** - readers might want to investigate independently
- Leave ornamental/decorative citations as references until they prove necessary

### Directory Placement by Notation:
- **°** (Pure Chamber inventions) → `/chamber/canon/chamber-generated/`
- **~** (Hybrid - real author, imagined text) → `/chamber/canon/hybrid/`
- **†** (Contested/apocryphal sources) → `/chamber/canon/contested/`
- **§** (Chamber synthesis) → `/chamber/canon/synthesis/`
- **∞** (Hermetic/esoteric traditions) → `/chamber/canon/hermetic/`
- **※** (Miscellaneous works) → `/chamber/canon/inventions/`

### Required YAML Frontmatter:
```yaml
---
title: "Work Title"
author: "Voice Name"
work_type: "category"
notation: "°" # or ~, †, §, ∞, ※
status: "chamber-generated"
created_in_session: "YYYY-MM-DD-session-name"
voice_origin: "Primary Voice"
category: "subject-area"

# DATE FIELD - CRITICAL: Choose ONE format only
date: 2025-01-15  # For actual dates - MUST be YYYY-MM-DD format, unquoted
# OR
date_range: "1970s-1980s"  # For ranges/periods/special dates - ALWAYS quoted

tags: [tag1, tag2, tag3]
related_works: [work1, work2]
chamber_appearances: ["YYYY-MM-DD-session-name"]
---
```

**⚠️ CRITICAL DATE RULES:**
- **Actual dates**: `date: 2025-06-14` (unquoted, YYYY-MM-DD only)
- **Ranges/periods**: `date_range: "1970s-1980s"` (quoted string)
- **Never mix**: `date: "1910-1970"` will break Jekyll build
- **See**: `docs/chamber/workflow/yaml-templates.md` for complete rules

### Content Structure:
- Opening description with Chamber context
- Core thesis or argument
- Chamber dialogue excerpts
- Related voices and cross-references
- Implications or applications

## Step 5: Synthesize Deliberation Page
**Target location**: `/chamber/deliberations/YYYY-MM-DD-descriptive-title.md` (flat structure, no subdirectories)

### Synthesis approach:
- **Unified narrative** from all AI platform outputs
- **Voice authenticity** maintained across platforms
- **Primary dialogue** showcasing key exchanges
- **Emergent patterns** and tensions identified
- **Cross-platform insights** integrated seamlessly
- **Essential questions** that crystallized
- **Canon entry links** properly formatted

### Required YAML Frontmatter:
```yaml
---
title: "Deliberation Title"
date: YYYY-MM-DD
category: deliberation
tags: [theme1, theme2, theme3]
voices_featured: 
  - voice-name-1
  - voice-name-2
generated_works: N
essential_question: "Core question that emerged"
canon_entries:
  - work-slug-1
  - work-slug-2
source_session: "YYYY-MM-DD-session-name"
protocol_used: "standard" # or first-light, shadow
platforms_analyzed: [gpt, claude]
---
```

## Step 6: Multi-Platform Meta-Analysis
**Create**: `step6-meta-commentary.md` in session folder
**CONFIDENTIAL**: Meta-commentaries remain in private session archives only - they contain sensitive Chamber methodology analysis

### Analysis components:
- **Voice manifestation variations** across AI systems
- **Protocol outcome divergences** between platforms
- **Fictional generation patterns** (quantity, style, themes)
- **AI system behavioral analysis** (strengths, tendencies)
- **Platform-specific insights** for future reference
- **Complementary vs competitive** platform usage

### Cross-platform voice tracking:
- How did specific voices manifest differently?
- Which archetypal voices appeared where?
- What recommendations varied by platform?
- Which essential questions emerged from which system?

## Step 7: Jekyll Integration Planning
**Create**: `step7-jekyll-integration-plan.md`

### Integration checklist:
- [ ] All canon entries have proper directory placement
- [ ] Cross-links between deliberation and canon work
- [ ] YAML frontmatter validates across all files
- [ ] Source notation displays correctly (°, ~, †, §, ∞, ※)
- [ ] Related works cross-references functional
- [ ] Session archive navigation updated

### Link format verification:
- Deliberation to canon: `/chamber/canon/[category]/[filename]`
- Canon to deliberation: Links back to chamber appearances
- Between canon entries: Related works in frontmatter

## Step 8: Present Complete Package
**Files to present:**
- Synthesized deliberation (ready for `/chamber/deliberations/`)
- All canon entries (ready for proper `/chamber/canon/` subdirectories)
- Meta-commentary summary (confidential analysis remains in private archives)
- Jekyll integration verification

**Request feedback on:**
- Editorial voice and synthesis quality
- Canon entry completeness and placement
- Cross-platform analysis insights
- Missing patterns or voices
- Publication approval

## Step 9: Publish After Approval
1. **Place deliberation** in `/chamber/deliberations/` (flat structure, no protocol subdirectories)
2. **Place canon entries** in proper `/chamber/canon/` subdirectories by notation type
3. **Verify all links** work correctly using standardized YAML frontmatter
4. **Archive session materials** in chamber-sessions-private (including meta-commentary)
5. **Update TodoWrite** to mark workflow complete
6. **Document workflow improvements** if any

**IMPORTANT**: All deliberations go directly in `/chamber/deliberations/` - no more `standard/`, `first-light/`, or `shadow/` subdirectories. The protocol type is tracked in YAML frontmatter only.

**META-COMMENTARIES ARE CONFIDENTIAL**: These analyze AI platform differences and voice manifestation patterns - invaluable for Chamber development but must remain in private archives only.

---

# ENHANCED COLLABORATIVE WORKFLOW

## David's Responsibility: 
- Choose appropriate protocol for each text
- Run multi-platform Chamber sessions (GPT + Claude)
- Send session folder with notification: "New deliberation awaiting Mode 1 processing"
- Review and approve all synthesized content
- Maintain editorial control and Chamber authenticity

## Claude Code's Responsibility:
- Execute complete 9-step workflow systematically
- Use TodoWrite tool to track progress through steps
- Extract and synthesize multi-platform content
- Create Jekyll-ready publications with proper Chamber directory structure
- Present complete package for approval before publication
- Handle technical integration while preserving Chamber voice

## Key Enhancements in Version 4.0:
- **Unified workflow**: Single document replacing multiple overlapping guides
- **Standardized YAML**: Consistent frontmatter templates for all content types
- **Consolidated structure**: Flat deliberations, organized canon by notation type
- **Confidential meta-analysis**: Private archives protect IP while enabling development
- **Multi-platform synthesis**: Unified deliberations from multiple AI systems
- **Complete archival**: Permanent preservation policy for all materials
- **Correct notation system**: Official 6-marker system (°, ~, †, §, ∞, ※)

---

# ARCHIVE MANAGEMENT

## Permanent Preservation Policy
**All raw session files and processing documentation are kept indefinitely.**

### Storage Structure
```
chamber-sessions-private/
├── 2025/
│   ├── 2025-06-19-Savall-Prometheus-21/
│   │   ├── [standard]submitted-text.txt
│   │   ├── [standard]claude-raw.txt
│   │   ├── [standard]gpt-raw.txt
│   │   ├── step3-fictional-references-extraction.md
│   │   ├── step6-meta-commentary.md (CONFIDENTIAL)
│   │   ├── step7-jekyll-integration-plan.md
│   │   └── session-notes.md
└── README.md
```

### What We Preserve
- **All raw AI outputs**: Complete platform responses
- **Original submitted texts**: Exact source material
- **Processing documentation**: Step-by-step synthesis work
- **Meta-analysis**: Cross-platform behavioral insights (CONFIDENTIAL)
- **Integration plans**: Technical implementation details
- **Session notes**: David's observations and reasoning
- **Version iterations**: If sessions require re-processing

### Research Value
- **Chamber methodology evolution**: Track synthesis improvements over time
- **Multi-platform AI collaboration**: Compare how different systems manifest archetypal voices
- **Cross-platform voice consistency**: Study how Chamber voices maintain authenticity across systems
- **Fictional work generation patterns**: Analyze how different platforms create Chamber canon
- **Editorial transformation documentation**: Complete record of human-AI collaborative editing

---

## Future Development

**Mode 1** represents the current standard operation. **Mode 2** will be developed once the source-aware Chamber is ready, enabling direct philosophical citation and enhanced voice authenticity through complete textual grounding.

---

**Version 4.0 consolidates all Mode 1 workflows with correct notation system, simplified platform naming, and standardized file naming conventions.**