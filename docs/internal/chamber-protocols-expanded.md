# INTERNAL: Complete Chamber Protocol Specifications
## Version 2.0 - June 16, 2025

**CONFIDENTIAL**: This document contains complete technical specifications for Chamber operations. Public-facing descriptions use hermetic language to protect intellectual property.

---

## Overview

The Chamber system has evolved to include three distinct AI-assisted protocols for editorial review:

1. **First Light Protocol** (NEW) - Gentle emergence for fragments/seeds
2. **Standard Protocol** (UPDATED) - Full transformative dialogue  
3. **Shadow Protocol** (UPDATED) - Ethical reckoning with hidden implications

All protocols use the four-engine system: GPT Standard, GPT Shadow, Claude Standard, Claude Shadow.

---

## 1. First Light Protocol (NEW)

### Purpose
Gestational space for seeds of ideas—fragments, tensions, questions, or hunches not ready for full editorial review.

### AI Configuration
- **Reduced voice count**: 2-3 witnesses plus 3 silent anchors
- **Softer prompting**: Wonder-based rather than analytical
- **Gentle outcomes**: Rest, small step, or bridge to Standard
- **No analysis**: Recognition and inquiry only

### Key Difference from Standard
- **Input**: Fragments (1-3 sentences) vs complete texts
- **Tone**: Moonlit, gestational vs daylight clarity
- **Outcome**: May recommend return to darkness vs transformation
- **Voice count**: 3-6 total vs 5-8 for Standard

### Master Prompts Location
- `docs/internal/chamber-prompts/first-light/claude-v2.md`
- `docs/internal/chamber-prompts/first-light/gpt-v2.md`

---

## 2. Standard Protocol (UPDATED)

### Enhanced Voice Selection
Now draws from complete 200+ voice assembly across four rings:
- **First Ring: Makers** (50+ voices) - those who think through doing
- **Second Ring: Foundation Stones** (40+ voices) - deep gravitational thinkers
- **Third Ring: Working Galleries** (80+ voices) - active practitioners
- **Fourth Ring: Ancestors & Eternals** (30+ voices) - mythological/timeless

### Dynamic Configuration Feature
Space reconfigures based on work type:
- Typography questions → Gutenberg circle moves forward
- Embodiment questions → dancers/craftspeople to center
- Philosophy questions → Foundation Stones gather

### Bibliographic Generation (ENHANCED)
Every session must generate 3-8 fictional references:
- Voices cite their own invented works naturally
- Cross-reference other Chamber sessions
- Build cumulative authority through repetition
- Use complete notation system (°, ~, †, §, ∞, ◊)

### Master Prompts Location
- `docs/internal/chamber-prompts/standard/claude-v2.md`
- `docs/internal/chamber-prompts/standard/gpt-v2.md`

---

## 3. Shadow Protocol (UPDATED)

### Mandatory Shadow Voices
These MUST speak first in every Shadow session:
- **Lost Pedagogies**: Stolen Generations' Teachers, Residential School Survivors
- **Digital Shadows**: Aaron Swartz, The Algorithm, McKinsey Consultant
- **Anti-Aesthetics Tribunal**: Thomas Bernhard, Paul Celan, Bartleby

### Architecture Transformation
Unlike other protocols, physical space transforms:
- Organic amphitheater → institutional corridors
- Warm stone → cold concrete
- Dodecahedron light → surveillance
- Center void → interrogation chamber

### Critical Rule Changes
- **No defense permitted** during accusation phase
- **Traditional voices can only intensify destruction**
- **"Nothing survives" is valid outcome**
- **Beauty receives harshest scrutiny**

### Master Prompts Location
- `docs/internal/chamber-prompts/shadow/claude-v2.md`
- `docs/internal/chamber-prompts/shadow/gpt-v2.md`

---

## Bibliographic Engine Integration

### The Living Library System
Based on `docs/internal/chamber-bibliographic-engine.md`:

**Core Principle**: Fiction and reality treated equally—authority comes through use, not origin.

### Reference Generation Process
1. **Spontaneous Citation**: Voices cite works during dialogue
2. **Notation Classification**: Immediate marking with symbols
3. **Cross-Reference Tracking**: Links between sessions
4. **Authority Building**: Repeated citations increase reality
5. **Canon Integration**: Works enter permanent collection

### Current Status
- ~50 fictional works catalogued in Jekyll collections
- Growing authority through cross-citation
- Next milestone: 100 works with established citation patterns

---

## Technical Implementation

### Session Workflow
1. **David runs all 4 engines** using master prompts
2. **Saves raw outputs** in `chamber-sessions-private/YYYY-MM-DD-title/`
3. **Sends complete folder** to Claude Code for processing
4. **Claude Code creates** public deliberation documents
5. **Updates Jekyll collections** with new canon entries

### File Organization
```
docs/internal/
├── chamber-prompts/
│   ├── first-light/ (claude-v2.md, gpt-v2.md)
│   ├── standard/ (claude-v2.md, gpt-v2.md)
│   └── shadow/ (claude-v2.md, gpt-v2.md)
├── chamber-first-light-protocol.md
├── chamber-standard-protocol.md
├── chamber-shadow-protocol.md
├── chamber-bibliographic-engine.md
└── chamber-protocols-expanded.md (this file)
```

### Jekyll Collections Integration
- `_chamber_deliberations/` - Processed session outputs
- `_chamber_canon/` - Fictional bibliography with metadata
- `_chamber_meta/` - Meta-commentary on sessions

---

## Voice Assembly Complete Specifications

### The Four Rings Architecture

**First Ring: The Makers** (50+ voices)
- Movement & Presence: Bausch, Abramović, Oliveros
- Visual Artists: Moy Glidden, Miró, Hilma af Klint, Basquiat
- Architects: Wright, Mies, Gaudí, Hadid
- Sacred Craft: Gutenberg lineage, unnamed craftspeople

**Second Ring: Foundation Stones** (40+ voices)
- Core Four: Alexander, Bachelard, Berger, Sennett
- Attention/Presence: Simone Weil, Levinas, Jenny Odell
- Living World: Kimmerer, Abram, Margulis

**Third Ring: Working Galleries** (80+ voices)
- Typography: Tschichold, Bringhurst, Frutiger
- Literary: Woolf, Borges, Lispector, Morrison, Carson
- Mystics: Ibn Arabi, Hildegard, Blake
- Scientists: Einstein, McClintock, Lovelace
- Composers: Pärt, Casals, Gubaidulina

**Fourth Ring: Ancestors & Eternals** (30+ voices)
- Chan/Zen Lineage: Dōgen, Huineng, D.T. Suzuki
- Classical: Marcus Aurelius, Hypatia, Sappho
- Mythological: The Nine Muses, Prometheus, Scheherazade

**Shadow Galleries** (30+ voices)
- Lost Pedagogies: Enslaved Scribe, Burned Witch
- Digital Shadows: Algorithm, Facebook Engineer
- Anti-Aesthetics: Bernhard, Celan, Bartleby

### Selection Principles
- **Work determines assembly**: Different questions call different voices
- **Silence has authority**: Who doesn't speak matters
- **Unexpected perspectives required**: Always include surprising voices
- **Maximum 8 voices per session**: Maintain focus and dialogue quality

---

## Security & IP Protection

### Public Elements (Safe for Funding Application)
- The Chamber as "editorial innovation methodology"
- Three examination types as "systematic approach"
- Bibliographic engine as "reference generation system"
- 200+ voice assembly as "multi-perspectival dialogue"
- Published deliberations as "proven results"

### Protected Elements (Never Public)
- Four-protocol AI system specifications
- Master prompts and technical instructions
- Complete voice assembly with specific names
- Raw session transcripts and processing
- Technical workflow and automation

### Hermetic Language Strategy
- "Protocols" → "examinations"
- "AI-generated" → "emerged through dialogue"
- "Processing" → "preparation for publication"
- "Engines" → "voice manifestation methods"

---

## Future Development

### Emerging Protocols (Not Yet Implemented)
- **Dream Protocol**: Symbol-based, non-linear dialogue
- **Teaching Protocol**: Pedagogical voice configuration
- **Death Protocol**: Honoring work that should end
- **Birth Protocol**: Preparing for new life/perspectives

### Next Phase Enhancements
- **Automated cross-referencing**: Dynamic linking between canon entries
- **Voice pattern analysis**: Track manifestation/refusal patterns
- **Authority scoring**: 1-5 stars based on citation frequency
- **Teaching integration**: Connection to Matthieu Taliesin platform

---

## Usage Guidelines

### When to Use Each Protocol
**First Light**: 
- Notebook fragments that won't leave you alone
- Questions without answers
- Hunches about patterns
- Seeds that feel significant but fragile

**Standard**: 
- Complete drafts needing revision
- Conceptual frameworks requiring testing
- Any work ready for transformation

**Shadow**: 
- When beauty feels suspiciously easy
- Before publishing on sensitive topics
- Periodic ethical audits
- When genuinely ready to abandon work

### Success Metrics
- **First Light**: Recognition of patterns, gentle next steps
- **Standard**: Transformed work with clear improvements
- **Shadow**: Honest reckoning, even if work dies

---

## Documentation Links

### Technical References
- `chamber-first-light-protocol.md` - Complete First Light specs
- `chamber-standard-protocol.md` - Complete Standard specs  
- `chamber-shadow-protocol.md` - Complete Shadow specs
- `chamber-bibliographic-engine.md` - Reference generation system
- `chamber-workflow-manual.md` - Session process guide

### Master Prompts
- `chamber-prompts/first-light/` - Gentle examination prompts
- `chamber-prompts/standard/` - Full dialogue prompts
- `chamber-prompts/shadow/` - Ethical reckoning prompts

---

**Document Security**: INTERNAL ONLY  
**Last Updated**: June 16, 2025  
**Next Review**: Post-funding application completion  
**Hakyll Ready**: All specifications prepared for migration