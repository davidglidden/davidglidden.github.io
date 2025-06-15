# Project Memory
## Animal Rationis Capax Development History

*Chronological record of major developments and decisions*

---

## December 2024 - The Chamber Implementation

### Revolutionary Editorial System
- **Complete Chamber architecture**: Implemented four-protocol AI-assisted editorial system
- **Bliki functionality**: Dynamic cross-referencing and interconnected knowledge web
- **First operational session**: Khunrath owl emblem meditation through Standard/Shadow protocols
- **Living fictional canon**: 8 major fictional works generated and catalogued
- **Voice tracking system**: Comprehensive tracking of manifestations and refusals across sessions

### Core Chamber Components
- **Four protocols**: GPT Standard, GPT Shadow, Claude Standard, Claude Shadow
- **Fictional bibliography**: Borgesian approach where works exist through citation
- **Source notation system**: Six marker types (°, ~, †, §, ∞, ◊) for different fictional work categories
- **Meta-commentary**: Analysis of AI divergences and protocol differences
- **Session archive**: Complete deliberation documentation with cross-references

### Technical Implementation
- **Jekyll collections**: chamber_canon, chamber_deliberations, chamber_meta
- **Dynamic cross-referencing**: Automatic linking between canon entries and sessions
- **Custom Chamber layout**: Contextual navigation and discovery sidebar
- **Bliki CSS**: Comprehensive styling for interconnected content
- **Voice tracking**: Dedicated `/chamber/voices/` section for pattern analysis

### First Session Insights
- **Shadow Protocol power**: Complete rejection revealed hidden violence in aesthetic philosophy
- **AI perspective differences**: Claude builds elaborate worlds, GPT provides compressed insights
- **Fictional canon emergence**: Works like *Extinction Protocols*§ and *Behavioral Blindness Index*° gained authority through citation
- **Voice manifestation patterns**: 15+ voices spoke, 5 refused participation

### Key Design Decisions
- **Chamber privacy**: Operational tools private (`docs/internal/`), results public
- **Shadow rejection as feature**: Text survival/rejection both publishable outcomes
- **Gray source markers**: Visual consistency with existing design system
- **Manual workflow**: David runs protocols, Claude processes for publication

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

## January 2025 - Chamber Obfuscation & Migration Decision

### Critical Intellectual Property Protection
- **Issue identified**: Chamber methodology exposed in public documentation
- **Immediate response**: Obfuscated all public-facing Chamber documents while preserving internal technical detail
- **Key principle**: "Show the magic, hide the machinery"

### Obfuscation Implementation
- **chamber/about.md**: Complete rewrite removing all technical implementation details
- **chamber/index.md**: Removed AI methodology references, changed "protocols" to "examination"
- **Chamber canon entries**: Changed "Generated through" to "Emerged through" across all entries
- **Jekyll template update**: Modified `_layouts/chamber.html` for future entries
- **Sessions archive**: Decided to make internal-only post-migration

### Site-Wide Updates
- **Council → Chamber**: Updated all navigation references site-wide
- **Chamber enfilade**: Implemented dedicated navigation for Chamber section
- **Language refinement**: Replaced technical terms with mysterious alternatives throughout

### Migration Decision
- **Critical realization**: Jekyll limitations preventing proper Chamber implementation
- **Hakyll advantages identified**:
  - Native authentication for protected content
  - Pandoc AST manipulation for advanced typography
  - Compile-time Chamber processing
  - Type-safe content handling
- **Migration plan created**: Comprehensive 3-4 week roadmap documented
- **Server ready**: Docker container with Hakyll already prepared

### Final Jekyll State Documentation
- **74 posts** with sophisticated semantic typing
- **Complete Chamber system** with 3 collections, cross-referencing, voice tracking
- **No broken links** or missing references
- **All HTTP links updated** to HTTPS
- **Obsolete files removed** (now.json)
- **Migration prerequisites documented** for server admin

### Key Decisions
- **Pause Jekyll work**: No more patches on old system
- **Migration priority**: Foundation change before feature additions
- **Public Chamber content**: Deliberations, Canon, Voices (obfuscated)
- **Protected content**: Session archives, meta-commentary, technical details

---

## Future Memory

### For Next Sessions
*Record significant decisions and reasoning here*

### Emerging Patterns
*Note new ways of working that develop*

### Lessons Learned

#### From Chamber Implementation
- **AI collaboration benefits from systematic approach**: Four-protocol structure ensures comprehensive perspective
- **Shadow Protocol is essential**: Without ruthless ethical reckoning, beauty becomes complicity
- **Fictional bibliographies have real power**: Works cited into existence gain genuine authority
- **Bliki functionality transforms static sites**: Dynamic cross-referencing creates living knowledge systems
- **Voice tracking reveals patterns**: Emergence and refusal patterns show deeper dialogue dynamics

#### Technical Insights
- **Jekyll collections powerful for complex content**: Enable sophisticated content relationships
- **SCSS variable consistency crucial**: Build system fails fast when variables undefined
- **Incremental implementation works**: Build foundation, then layer functionality
- **Documentation prevents context loss**: Detailed commit messages and project memory essential

---

*This document grows with our collaboration. Each significant session should add to the memory.*