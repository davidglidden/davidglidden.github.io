# Project Memory
## Animal Rationis Capax Development History

*Chronological record of major developments and decisions*

---

## June 2025 - Semantic Types Implementation

### Major Accomplishments
- **Glimpse semantic type**: Implemented pure image presentation without titles
- **Photo-essay semantic type**: Sequential visual narratives with proper framing
- **Ornamental system**: Complete set of semantic breathing marks
- **Type specimens page**: Full typography demonstration
- **Create scripts**: Automated glimpse and photo-essay generation

### Key Decisions & Rationale
- **Glimpse presentation**: No titles based on Berger's insight that "a glimpse is an event that happens to you"
- **Photo-essay framing**: Titles maintained because "a photo essay is a journey you choose to begin"
- **Layout differences**: Full-bleed for glimpses (interruption), text column for photo-essays (narrative contract)
- **Metadata approach**: Location and camera info as whisper-level context below images

### Design Dialogues
- Extensive consultation with Berger, Mohr, Alexander, Manutius on visual presentation
- Established that glimpses break reading frame while photo-essays maintain it
- Preserved reasoning in DESIGN-DIALOGUES.md

### Technical Implementations
- Modified `_layouts/post.html` to hide titles for glimpses, show metadata
- Updated `_sass/klise/_utilities.scss` for full-bleed image CSS
- Created executable Python scripts for content generation
- Converted 15+ observation posts to glimpse semantic type

---

## Pre-June 2025 - Foundation Work

### Site Architecture
- Jekyll 3.8.3 with modified Klisé theme
- Typography system: EB Garamond, IBM Plex Sans/Mono
- Semantic post types system established
- Privacy-first approach (no tracking, self-hosted fonts)

### Content Organization
- Semantic archive pages for each post type
- Ornamental breathing marks system
- Encounter and chamber modifier system
- Responsive design with 8px rhythm grid

### Documentation Structure
- CLAUDE.md for essential project instructions
- Style guide for complete semantic reference
- Typography guides (internal and public)
- Enfilade navigation for About pages

---

## Ongoing Patterns

### Communication Style
- David: Concise, philosophical, design-conscious
- Claude: Systematic, documentation-focused, advisor-consulting
- Both: Iterative refinement through dialogue

### Decision Process
1. Understand the need/opportunity
2. Consult advisors when appropriate
3. Implement thoughtfully
4. Document rationale
5. Test implications

### Quality Standards
- Every change serves contemplative philosophy
- Form follows function, beauty carries responsibility
- Reader experience prioritized over technical convenience
- Historical grounding balanced with contemporary needs

---

## Future Memory

### For Next Sessions
*Record significant decisions and reasoning here*

### Emerging Patterns
*Note new ways of working that develop*

### Lessons Learned
*Capture insights about what works well*

---

*This document grows with our collaboration. Each significant session should add to the memory.*