# Documentation Reorganization Plan

**Created**: June 19, 2025  
**Purpose**: Optimize repository documentation structure for clarity, discoverability, and maintenance  
**Triggered by**: Chamber Amphitheatre placement decision and overall documentation review

---

## Current State Analysis

### **Strengths**
- Clear separation between public docs (`docs/`) and internal docs (`docs/internal/`)
- Comprehensive Chamber protocol documentation
- Strong technical documentation for migrations
- Robust IP protection and notarization materials

### **Issues Identified**

1. **Fragmented Chamber Documentation**
   - Chamber files scattered across multiple locations: `docs/internal/`, `_chamber_library/`, `docs/decisions/`
   - Core amphitheatre document now correctly placed in `docs/internal/`
   - Protocol files duplicated and inconsistently named

2. **Migration Documentation Overload**
   - Multiple overlapping Hakyll migration documents
   - Some files may be outdated post-migration completion

3. **Naming Inconsistencies**
   - Mixed case and dash conventions
   - Some files use underscore, others use dash

4. **Missing Organization**
   - No clear documentation hierarchy
   - Related files not grouped logically

---

## Proposed Reorganization

### **Core Structure**

```
docs/
├── README.md                           # Documentation index
├── CLAUDE.md                          # Essential instructions for Claude Code
├── style-guide.md                     # Style and editorial guidelines
├── typography-guide.md                # Typography system documentation
├── DESIGN-DIALOGUES.md               # Preserved advisor conversations
│
├── chamber/                           # 🆕 Chamber-specific documentation
│   ├── README.md                      # Chamber system overview
│   ├── amphitheatre.md               # Complete living amphitheatre (V2.1)
│   ├── protocols/                    # Protocol documentation
│   │   ├── README.md
│   │   ├── first-light.md
│   │   ├── standard.md
│   │   ├── shadow.md
│   │   └── prompts/                  # AI prompts for each protocol
│   │       ├── README.md
│   │       ├── claude/
│   │       └── gpt/
│   ├── workflow/                     # Chamber workflow documentation
│   │   ├── canon-workflow.md
│   │   ├── session-template/
│   │   └── bibliographic-engine.md
│   └── archive/                      # Historical Chamber documents
│       ├── email-exchanges/
│       ├── opentimestamps/
│       └── hashes/
│
├── migration/                         # 🆕 Migration documentation
│   ├── README.md                      # Migration overview
│   ├── hakyll/                       # Hakyll-specific docs
│   │   ├── plan.md
│   │   ├── requirements.md
│   │   ├── notes.md
│   │   └── handoff.md
│   ├── jekyll-final-state.md         # Final Jekyll state
│   └── archive/                      # Historical migration docs
│
├── ip-protection/                     # 🆕 Intellectual property documentation
│   ├── README.md                      # IP strategy overview
│   ├── checklist.md
│   ├── complete-guide.md
│   └── notary-package/               # Notarization materials
│       ├── README.md
│       ├── cover-letter.md
│       ├── executive-summary.md
│       ├── technical-documentation.md
│       ├── evidence-of-creation.md
│       ├── sample-outputs.md
│       └── declarations.md
│
├── internal/                          # Internal working documents
│   ├── README.md                      # Internal docs overview
│   ├── collaboration-protocol.md     # Claude collaboration guidelines
│   ├── project-memory.md             # Development history
│   ├── david-glidden-profile.md      # Context profile
│   ├── documentation-strategy.md     # Documentation approach
│   ├── documentation-workflow.md     # Documentation processes
│   ├── daily-update-routine.md       # Maintenance routines
│   ├── foundation-roadmap.md         # Strategic roadmap
│   └── advisory-deliberations/       # Advisory conversations
│       └── licensing-framework.md
│
└── decisions/                         # Architecture decision records
    ├── README.md
    ├── 2024-12-15-four-protocol-chamber-system.md
    ├── 2024-12-15-gray-source-markers-over-colors.md
    ├── 2024-12-15-manual-chamber-workflow.md
    └── 2024-12-15-shadow-protocol-as-essential.md
```

---

## Key Changes

### **1. New Top-Level Categories**

- **`chamber/`**: Consolidates all Chamber-related documentation
- **`migration/`**: Groups all migration documentation  
- **`ip-protection/`**: Dedicated IP and legal documentation

### **2. File Relocations**

**From `docs/internal/` to `docs/chamber/`**:
- `THE_CHAMBER_COMPLETE_LIVING_AMPHITHEATRE.md` → `amphitheatre.md`
- `chamber-first-light-protocol.md` → `protocols/first-light.md`
- `chamber-standard-protocol.md` → `protocols/standard.md`
- `chamber-shadow-protocol.md` → `protocols/shadow.md`
- `chamber-prompts/` → `protocols/prompts/`
- `chamber-canon-workflow.md` → `workflow/canon-workflow.md`
- `chamber-session-template/` → `workflow/session-template/`
- `chamber-bibliographic-engine.md` → `workflow/bibliographic-engine.md`

**From `docs/internal/` to `docs/migration/`**:
- `HAKYLL-MIGRATION-*` files → `hakyll/`
- `JEKYLL-FINAL-STATE.md` → `jekyll-final-state.md`
- `MIGRATION-HANDOFF.md` → `hakyll/handoff.md`

**From `docs/internal/` to `docs/ip-protection/`**:
- `ip-protection-*` files → root of category
- `NOTARY-PACKAGE/` → `notary-package/`

### **3. File Renamings**

- `THE_CHAMBER_COMPLETE_LIVING_AMPHITHEATRE.md` → `amphitheatre.md`
- `CLAUDE-COLLABORATION-PROTOCOL.md` → `collaboration-protocol.md`
- All SCREAMING_CASE files → kebab-case equivalents

### **4. Archive Strategy**

- Historical documents moved to `archive/` subdirectories
- Timestamped materials (hashes, screenshots) preserved in `chamber/archive/`
- Migration artifacts preserved but organized

---

## Implementation Plan

### **Phase 1: Structure Creation** ✅
- [x] Move amphitheatre document to correct location
- [ ] Create new directory structure
- [ ] Create README files for each major section

### **Phase 2: File Migration**
- [ ] Move Chamber documents to `docs/chamber/`
- [ ] Move migration documents to `docs/migration/`
- [ ] Move IP documents to `docs/ip-protection/`
- [ ] Rename files to consistent conventions

### **Phase 3: Content Updates**
- [ ] Update internal cross-references
- [ ] Create navigation README files
- [ ] Update CLAUDE.md with new structure references
- [ ] Verify all links work correctly

### **Phase 4: Archive Organization**
- [ ] Move historical files to archive subdirectories
- [ ] Ensure important materials remain discoverable
- [ ] Clean up outdated documentation

---

## Benefits

1. **Logical Grouping**: Related documents are co-located
2. **Clear Navigation**: Each major area has its own section
3. **Reduced Clutter**: `docs/internal/` becomes focused on working documents
4. **Better Discoverability**: README files guide users to relevant content
5. **Consistent Naming**: All files follow kebab-case convention
6. **Future-Proof**: Structure accommodates growth in each area
7. **Archive Strategy**: Historical materials preserved but not cluttering active docs

---

## Next Steps

1. Review this plan with David for approval
2. Begin Phase 1 implementation
3. Execute file migrations systematically
4. Update cross-references and navigation
5. Test structure with actual usage patterns

---

*This reorganization serves the Chamber's principle that "form follows question" - the documentation structure should serve the questions users need to answer when working with the repository.*