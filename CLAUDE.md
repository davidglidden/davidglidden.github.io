# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Essential Documentation

**For complete context, see the documentation system in `/docs/`:**

- **[Collaboration Protocol](docs/internal/collaboration-protocol.md)** — Working relationship and communication patterns
- **[Project Memory](docs/internal/project-memory.md)** — Development history and decision rationale  
- **[Style Guide](docs/style-guide.md)** — Complete semantic types and editorial guidelines
- **[Typography Guide](docs/typography-guide.md)** — Internal typography documentation
- **[Design Dialogues](docs/DESIGN-DIALOGUES.md)** — Preserved advisor conversations

## Essential Commands

### Development
```bash
bundle exec jekyll serve       # Start local development server at http://localhost:4000
bundle exec jekyll build       # Build site for production to _site/
bundle install                 # Install Ruby dependencies from Gemfile
```

### Git Workflow
The site is deployed via GitHub Pages on the `master` branch. Any commits to master will automatically deploy.

## Quick Reference

### Architecture Overview
- **Jekyll 3.8.3** with modified Klisé theme (migrating to Hakyll)
- **Semantic post types** determine both content style and reader approach
- **Typography system**: EB Garamond (body), IBM Plex Sans (interface), IBM Plex Mono (code)
- **Chamber library**: 136 converted texts with 92+ philosophical voices
- **Privacy-first**: No tracking, self-hosted fonts, local-first philosophy

### Key Principles
- **Read context first**: Always check the documentation system
- **Think systematically**: Consider implications across the complete site
- **Document rationale**: Preserve reasoning behind significant decisions
- **Honor the philosophy**: Every choice serves contemplative reading
- **Chamber integration**: All voices now have source-aware capacity

### Working Style
- **Be concise**: Match David's communication style
- **Ask thoughtful questions**: When uncertain, clarify rather than assume
- **Consult advisors**: For design decisions, channel Berger, Alexander, Manutius, etc.
- **Update documentation**: Add to project memory as work progresses
- **Chamber awareness**: 136 texts spanning all major philosophical traditions ready for citation
- **Migration readiness**: Hakyll deployment prepared with enhanced capabilities

## Chamber Workflow

### Mode 1 Processing
When David submits: **"New deliberation awaiting Mode 1 processing"**

**Follow**: [docs/chamber/workflow/MODE-1-UNIFIED.md](docs/chamber/workflow/MODE-1-UNIFIED.md)

**Key steps:**
1. Read all session files from `chamber-sessions-private/YYYY/session-name/`
2. Extract fictional works and assess for canon entries
3. Synthesize unified deliberation with standardized YAML
4. Create canon entries in proper `/chamber/canon/` subdirectories
5. Generate confidential meta-commentary (stays in private archives)
6. Present complete package for approval before publication

**Important:** All content uses standardized YAML templates from [yaml-templates.md](docs/chamber/workflow/yaml-templates.md)

---

*For detailed guidance on our collaboration, see [docs/internal/collaboration-protocol.md](docs/internal/collaboration-protocol.md)*