# Changelog
## Animal Rationis Capax Development Log

*All notable changes to this project will be documented in this file.*

---

## [The Chamber Implementation] - 2024-12-15

### Added
- **The Chamber editorial system**: Editorial amphitheater for textual transformation through historical and contemporary voices
- **Bliki functionality**: Dynamic cross-referencing and interconnected knowledge web
- **Fictional bibliography system**: Borgesian works cited into existence with growing authority
- **Voice tracking**: Comprehensive analysis of manifestations and refusals across sessions
- **First operational session**: Khunrath owl emblem meditation examined through dual protocols
- **Living canon**: Growing collection of fictional works created through citation
- **Session documentation**: Complete deliberations and examination processes
- **Jekyll collections**: Organized content structure for canon, deliberations, and analysis
- **Custom Chamber interface**: Contextual navigation and discovery features
- **Source notation system**: Six marker types (°, ~, †, §, ∞, ◊) for different fictional work categories

### Technical Implementation
- Dynamic cross-referencing between canon entries and sessions
- Reverse linking showing which deliberations cite each fictional work
- Automated related works suggestions based on shared voices and themes
- Chamber navigation with breadcrumbs and contextual tools
- Content discovery sidebar with recent activity
- Enhanced canon index with dynamic categorization
- Voice pattern tracking across sessions
- Complete session archive with cross-references

### Key Insights
- **Dual examination power**: Constructive dialogue and shadow examination reveal hidden aspects
- **Voice manifestation patterns**: Different types of voices emerge for different text types
- **Fictional canon emergence**: Works gain authority through citation and cross-reference
- **Bliki transformation**: Static site becomes living, interconnected knowledge system

---

## [Chamber Obfuscation & Migration Decision] - 2025-01-15

### Changed
- **Chamber public documentation**: Obfuscated all public-facing Chamber pages to protect intellectual property
- **Council → Chamber**: Updated all site-wide navigation references
- **Chamber enfilade**: Implemented dedicated navigation system for Chamber section
- **Language refinement**: Changed "Generated through" to "Emerged through" across all canon entries
- **Jekyll template**: Updated chamber.html layout for future entries

### Added
- **Hakyll migration plan**: Comprehensive 3-4 week roadmap for platform migration
- **Content audit**: Complete analysis of 74 posts and complex Chamber system
- **Protected content strategy**: Session archives to become authentication-protected post-migration

### Technical
- **Final Jekyll cleanup**: Removed obsolete files, updated HTTP links to HTTPS
- **Documentation updates**: PROJECT-MEMORY.md and CLAUDE-COLLABORATION-PROTOCOL.md updated with migration decision
- **Migration prerequisites**: Documented server access requirements for Hakyll transition

### Decision
- **Platform migration**: Moving from Jekyll/GitHub Pages to Hakyll on private server for enhanced capabilities
- **Rationale**: Native authentication, Pandoc AST manipulation, compile-time Chamber processing

### Final Polish
- **Typography compliance**: Fixed small caps violations in navigation-philosophy.md and Chamber pages
- **Encounter modifier fix**: Corrected encounters.html to display ✦ (four-pointed star) per style guide
- **Chamber navigation**: Centered enfilade navigation, added "Back to About" links
- **404 page fix**: Resolved header/footer overlap on desktop/tablet with responsive viewport calculations
- **Template consistency**: Updated chamber_navigation.html for complete obfuscation

---

## [Semantic Types System] - 2024-06-01 to 2024-06-30

### Added
- **Glimpse semantic type**: Pure image presentation without titles, full-bleed layout
- **Photo-essay semantic type**: Sequential visual narratives with titles and contained layout
- **Ornamental system**: Semantic breathing marks for each content type
- **Create scripts**: Python tools for generating glimpse and photo-essay posts
- **Type specimens page**: Complete typography demonstration
- **Enhanced archive pages**: Dedicated views for each semantic type

### Changed
- Converted 15+ observation posts to glimpse semantic type
- Modified `_layouts/post.html` to hide titles for glimpses, show metadata
- Updated `_sass/klise/_utilities.scss` for full-bleed image CSS
- Refined responsive typography and spacing system

### Design Philosophy
- **Glimpse insight**: "A glimpse is an event that happens to you"
- **Photo-essay distinction**: "A photo essay is a journey you choose to begin"
- **Layout differences**: Full-bleed for glimpses (interruption), text column for photo-essays (narrative)
- **Metadata approach**: Location and camera info as whisper-level context

---

## [Foundation] - Pre-2024-06-01

### Established
- Jekyll 3.8.3 with modified Klisé theme
- Typography system: EB Garamond (body), IBM Plex Sans (interface), IBM Plex Mono (code)
- Semantic post types: observation, fragment, essay, meditation, pattern, gloss, correspondence, offering, performance, teaching, interlude
- Privacy-first architecture: No tracking, self-hosted fonts, local-first philosophy
- Responsive design with 8px rhythm grid
- Documentation system: CLAUDE.md, style guides, collaboration protocols

### Core Values
- Contemplative reading over internet urgency
- Beauty with ethical responsibility
- Craft as manifestation of values
- "Animal Rationis Capax" - capable of thoughtful response

---

## Version Notes

### Naming Convention
- **[Major Feature]** - Significant new functionality or system
- **[Enhancement]** - Improvement to existing features
- **[Fix]** - Bug fixes and corrections

### Documentation Updates
Each major release includes updates to:
- `docs/internal/PROJECT-MEMORY.md` - Development history and insights
- `docs/internal/CLAUDE-COLLABORATION-PROTOCOL.md` - Working relationship patterns
- This `CHANGELOG.md` - Public-facing development log

---

*"Every change serves the reader's contemplative attention."*