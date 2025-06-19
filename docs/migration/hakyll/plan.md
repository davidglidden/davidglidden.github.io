# Hakyll Migration Plan

**Current Status**: Jekyll site on GitHub Pages → Hakyll on private Docker server
**Timeline**: Ready to begin immediately upon server access
**Goal**: Complete site migration with enhanced capabilities for Chamber development

## Prerequisites & Server Access Requirements

### What Claude Code Needs:

1. **Server SSH Access:**
   - SSH connection string (user@hostname or IP)
   - Port number (if non-standard 22)
   - SSH key setup or temporary password access

2. **Docker Container Details:**
   - Container name/ID for the Hakyll environment
   - Port mappings (internal/external)
   - Volume mount configuration (where site files will live)
   - Container status verification

3. **Environment Verification:**
   ```bash
   # Need to confirm these are available:
   docker ps                    # Container status
   docker exec -it [container] bash
   stack --version             # Haskell Stack installation
   ghc --version              # GHC compiler version
   pandoc --version           # Pandoc availability
   ```

4. **Current Deployment Info:**
   - How does the Jekyll site currently deploy?
   - Git hooks? Manual process? CI/CD pipeline?
   - Domain configuration (davidglidden.eu)
   - SSL certificate setup

## Migration Architecture

### New Hakyll Site Structure:
```
site/
├── src/
│   ├── Main.hs              # Site generator
│   ├── Contexts.hs          # Template contexts
│   ├── Chamber/
│   │   ├── Types.hs         # Chamber data types
│   │   ├── Compiler.hs      # Chamber content processing
│   │   └── Auth.hs          # Authentication for protected content
│   └── Filters/
│       ├── Typography.hs    # Typography processing
│       └── Semantic.hs      # Semantic type handling
├── templates/               # Hakyll templates (converted from Liquid)
├── content/                 # All markdown content (migrated)
├── static/                  # CSS, JS, images
└── _site/                  # Generated output
```

### Enhanced Capabilities Post-Migration:
- **Native authentication** for Chamber session archives
- **Pandoc AST manipulation** for advanced typography
- **Compile-time processing** of Chamber canonical references
- **Type-safe content handling**
- **Custom markdown extensions** for Chamber notation
- **Semi-automated Chamber workflows**

## Migration Strategy

### Phase 1: Infrastructure Setup (Week 1)
- Server access and environment verification
- Hakyll project initialization
- Basic site structure creation
- Development/deployment pipeline setup

### Phase 2: Content Migration + Chamber Mode 1 (Week 1-2)
**Complete preservation of:**
- ✅ All URLs (SEO/bookmarks maintained)
- ✅ All content (posts, pages, Chamber entries)
- ✅ All styling (typography system, ornaments)
- ✅ All functionality (navigation, semantic types)
- ✅ All collections (chamber_canon, deliberations, etc.)
- ✅ **Chamber Mode 1 fully operational** (current workflow preserved)

**Technical tasks:**
- YAML frontmatter → Haskell data types
- Liquid templates → Hakyll templates
- Jekyll collections → Hakyll content organization
- CSS/SCSS preservation
- **Chamber protocols migration** (Standard, First Light, Shadow)
- **Session archiving system** functional in Hakyll
- **Manual paste-text workflow** preserved exactly

**Critical Chamber Requirements:**
- All current master prompts accessible in Hakyll documentation
- Session templates working for raw file processing
- Protocol documentation navigable and functional
- Proof-of-concept capability maintained without interruption

### Phase 3: Authentication System (Week 2)
```haskell
-- Protected routes for Chamber content
data SiteRoute 
  = PublicRoute Text
  | ProtectedRoute Text  
  | ChamberSession SessionId  -- Requires authentication

-- User roles
data UserRole = Public | ChamberAccess | Admin
```

**Features:**
- File-based user management (initially)
- Session-based authentication
- Protected Chamber session archives
- Role-based content access

### Phase 4: Source-Aware Development Preparation (Week 3-4)
- **Subdomain setup** for `chamber-dev` environment
- **Source-aware architecture foundation** (voices.yaml, context system)
- **Parallel development pipeline** for Chamber Mode 2
- Custom pandoc filters for Chamber notation
- Enhanced cross-reference generation
- Typography optimization via Haskell

**Note**: Mode 2 (source-aware) development occurs parallel to operational Mode 1, following specifications in `docs/chamber/SOURCE_AWARE_VISION.md` and `docs/chamber/CHAMBER_OPERATIONAL_MODES.md`

## Current Site Analysis

**Foundation**: Modified Klisé Jekyll theme (attribution preserved)
**Content Types**: 
- Standard posts with semantic types (essay, glimpse, encounter)
- Chamber system (canon, deliberations, sessions, voices)
- About pages with enfilade navigation

**Collections**:
- `_chamber_canon/` - Fictional works referenced by Chamber
- `_chamber_deliberations/` - Public Chamber discussions
- Standard posts with sophisticated frontmatter

**Key Features to Preserve**:
- Typography system (EB Garamond, IBM Plex Sans/Mono)
- Ornament system (❦, ⁂, ❧, ◊, etc.)
- Semantic post qualifiers (✦, ⟐)
- Chamber enfilade navigation
- Cross-referencing between Chamber content

## Questions for Server Administrator

1. **Is the Docker container already running and accessible?**
2. **What's the intended domain setup?** (davidglidden.eu pointing to new server)
3. **How should we handle the GitHub → private server transition?**
4. **Any firewall/security considerations for SSH access?**
5. **Backup strategy during migration?**
6. **Preferred deployment method?** (Git hooks, manual, CI/CD)

## Success Criteria

- [ ] Site loads identically to current version
- [ ] All URLs preserved (no broken links)
- [ ] All content migrated successfully
- [ ] Authentication system functional for protected content
- [ ] Enhanced Chamber capabilities operational
- [ ] Domain pointing to new server
- [ ] SSL certificate configured

## Risk Mitigation

- **Full site backup** before migration begins
- **Staged deployment** (test server first)
- **URL preservation testing**
- **Content integrity verification**
- **Rollback plan** if issues arise

## Post-Migration Audit Tasks

### Chamber Content Access Decisions
**Note**: Final decisions on public vs. protected content to be made post-migration based on authentication capabilities.

**Likely Public** (long-term):
- **Deliberations**: Showcase the process, maintain mystery and intrigue
- **Canon**: Already well-obfuscated fictional bibliography
- **Voices**: Pattern tracking without technical details

**Likely Protected** (internal only):
- **Sessions Archive**: Shows technical workings and methodology
- **Meta-Commentary**: AI analysis too revealing of process
- **Chamber Tools**: Operational documentation

### Documentation Hierarchy Review
- Audit all `/docs/` content for appropriate public/internal classification
- Review Chamber tools documentation accessibility
- Establish clear guidelines for what remains public vs. protected
- Consider graduated access levels:
  - Public: General visitors
  - Chamber-access: Trusted readers with login
  - Admin: Full technical access

### Implementation Considerations
- Use Hakyll's authentication to create nuanced access control
- Consider time-delayed public release of some content
- Maintain the balance: "Show the magic, hide the machinery"

### Future Enhancement: Voice Linking
- Link voice names to their canon entries and voice pattern pages
- Create comprehensive cross-referencing between voices and their works
- Generate automatic voice profile pages showing all appearances

---

**Ready to begin immediately upon server access confirmation.**

*Contact: Claude Code via David's session*  
*Created: 2025-01-15*  
*Updated: 2025-01-15 with post-migration audit notes*