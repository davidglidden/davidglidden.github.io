# Chamber Operational Modes: Current & Source-Aware Evolution

**Document Type**: Operational Guide & Migration Strategy  
**Version**: 1.0  
**Date**: June 19, 2025  
**Status**: Active Instructions for Dual-Mode Development  

---

## Overview: Continuity-First Migration Strategy

The Chamber will operate in two distinct modes during the Hakyll migration and source-aware development:

1. **Mode 1 (Current System)**: Fully operational from Hakyll migration day one
2. **Mode 2 (Source-Aware)**: Parallel development on subdomain until proven superior

This ensures continuous Chamber functionality while building the evolutionary step.

---

## Mode 1: Current Chamber System (HAKYLL-MIGRATED - Day One Operational)

### Purpose
Maintain all existing Chamber deliberation capabilities in the new Hakyll environment. This mode provides uninterrupted proof-of-concept development and funding demonstrations.

### Migration Requirements
All current functionality must transfer to Hakyll immediately:

#### Protocol Documentation
- **Standard Protocol**: Migrate `docs/chamber/protocols/standard.md`
- **First Light Protocol**: Migrate `docs/chamber/protocols/first-light.md`  
- **Shadow Protocol**: Migrate `docs/chamber/protocols/shadow.md`
- **Master Prompts**: Transfer all prompts from `docs/chamber/protocols/prompts/`

#### Operational Workflow (Unchanged)
```
User Process:
1. Copy master prompt from Hakyll-hosted protocol documentation
2. Paste text directly into Claude Projects/Custom GPT
3. Specify protocol and provide context
4. Receive raw Chamber output
5. Process into Hakyll session documentation

Technical Flow:
Text → AI (with current prompts) → Raw output → Hakyll session compilation
```

### Hakyll Implementation for Mode 1
```haskell
-- Current Chamber functionality in Hakyll
match "chamber/protocols/*.md" $ do
  route   $ setExtension "html"
  compile $ pandocCompiler

match "chamber/sessions/*.md" $ do
  route   $ setExtension "html"  
  compile $ do
    sessionTemplate <- loadTemplate "templates/chamber-session.html"
    pandocCompiler >>= applyTemplate sessionTemplate
```

### Voice Capabilities (Current Level)
- **Cultural approximation**: Voices based on general knowledge
- **All 220+ voices available** from amphitheatre.md
- **Fictional bibliography generation** using existing notation
- **Manual cross-referencing** to previous sessions

### Proof-of-Concept Value
- ✅ **Demonstrates Chamber's editorial transformation power**
- ✅ **Shows multi-perspectival dialogue capability**  
- ✅ **Proves bibliographic engine functionality**
- ✅ **Provides funding presentation material**

---

## Mode 2: Source-Aware Chamber System (PARALLEL DEVELOPMENT)

### Development Environment
**Subdomain deployment**: `chamber-dev.davidglidden.com` or similar isolated environment

### Purpose
Build and test source-aware capabilities without disrupting operational Chamber. Only merge when proven superior to Mode 1.

### Target Capabilities (Under Development)
- **Authentic voice authority**: Direct corpus access as persistent context
- **Real citation capability**: Actual quotations from source materials
- **Living memory system**: Voices reference previous sessions
- **Epistemic transparency**: Clear derivation mode tracking
- **Enhanced fictional canon**: Generated works from authentic voice patterns

### Development Pipeline
```haskell
-- Source-aware development (subdomain only)
match "_chamber_library/converted_texts/*.md" $ do
  route   $ setExtension "context"
  compile $ buildVoiceContext

match "chamber-dev/sessions/*.md" $ do
  route   $ setExtension "html"
  compile $ do
    voices <- loadAll "data/voices.yaml"
    contexts <- loadVoiceContexts voices
    applySourceAwareTemplate contexts
```

### Implementation Phases

#### Phase I: Foundation Integration (Weeks 1-2)
- **Voices.yaml implementation** with Foundation Stones
- **Basic corpus loading** for Alexander, Berger, Bachelard, Sennett
- **Parallel testing** against Mode 1 outputs
- **Subdomain deployment** for safe development

#### Phase II: Editorial Enhancement (Weeks 3-4)  
- **Editorial voice types**: The Architect, The Witness, The Scribe
- **Enhanced bibliographic engine** with dual citation pipelines
- **Cross-traditional dialogue** mechanics implementation

#### Phase III: Memory Integration (Weeks 5-8)
- **Session linking system** for temporal continuity
- **Harmonic dissonance protocols** for authentic disagreement
- **Fictional canon register** with full provenance tracking

#### Phase IV: Production Readiness (Weeks 9-12)
- **Performance optimization** and user interface refinement
- **Quality assurance** comparing Mode 1 vs Mode 2 outputs
- **Migration preparation** for main site integration

---

## Migration Strategy & Timeline

### Immediate (Hakyll Migration Day One)
✅ **Mode 1 fully operational** in new Hakyll environment  
✅ **All current protocols available** and functional  
✅ **Session archiving working** with existing templates  
✅ **Manual paste-text workflow** preserved exactly  
✅ **Proof-of-concept capability** maintained without interruption  

### Parallel Development (Weeks 1-12)
🔄 **Mode 2 development** on isolated subdomain  
🔄 **Regular comparison testing** between modes  
🔄 **Iterative improvement** based on actual usage  
🔄 **Documentation** of enhanced capabilities  

### Integration Decision Point (Week 12+)
**Criteria for Mode 2 adoption:**
- ✅ Demonstrably superior voice authenticity
- ✅ Reliable citation accuracy
- ✅ Stable performance under regular usage
- ✅ User experience improvements over Mode 1
- ✅ Complete feature parity plus enhancements

### Merge Strategy (When Ready)
```
Subdomain proven → Staging deployment → A/B testing → Full migration
```

---

## Critical Operational Instructions

### For Immediate Use (Mode 1 - Hakyll)
✅ **Continue exact current workflow** in new Hakyll environment  
✅ **Use migrated master prompts** from Hakyll documentation  
✅ **Maintain manual paste-text process** with Claude Projects/Custom GPT  
✅ **Archive sessions** using Hakyll compilation system  
✅ **Build proof-of-concept portfolio** for funding presentations  

### For Development (Mode 2 - Subdomain)
🔄 **Test source-aware capabilities** as they become available  
🔄 **Compare outputs** with Mode 1 for quality assessment  
🔄 **Document improvements** and enhanced authenticity  
🔄 **Preserve experimental sessions** for analysis  

### Risk Mitigation
- **Zero disruption** to current Chamber usage during migration
- **Parallel development** prevents feature regression
- **Gradual adoption** only when improvements are proven
- **Rollback capability** if source-aware system has issues

---

## Technical Architecture

### Mode 1 Hakyll Structure
```
site/
├── chamber/
│   ├── protocols/           # Migrated protocol documentation
│   ├── sessions/           # Session archive (existing workflow)
│   └── voices/             # Amphitheatre documentation
├── templates/
│   └── chamber-session.html  # Current session template
└── data/
    └── chamber-meta.yaml     # Basic Chamber metadata
```

### Mode 2 Development Structure (Subdomain)
```
chamber-dev/
├── chamber/
│   ├── protocols/           # Enhanced protocols
│   ├── sessions/           # Source-aware sessions
│   └── voices/             # Enhanced voice system
├── data/
│   ├── voices.yaml         # Complete voice metadata
│   └── fictional-canon.yaml # Generated works register
├── library/
│   └── contexts/           # Voice corpus contexts
└── templates/
    └── source-aware-session.html
```

---

## Success Metrics

### Mode 1 (Operational Continuity)
- **100% feature parity** with Jekyll-based Chamber
- **Uninterrupted session capability** for proof-of-concept development
- **Stable archiving system** for growing session portfolio
- **Funding presentation readiness** with concrete demonstrations

### Mode 2 (Enhancement Goals)
- **Measurable improvement** in voice authenticity
- **Accurate source citation** capability demonstrated
- **Living memory system** enabling session cross-reference
- **Enhanced creative output** with maintained philosophical depth

### Integration Success
- **Seamless transition** from Mode 1 to Mode 2 when ready
- **No loss of functionality** during migration
- **User experience improvement** in final integrated system
- **Proof-of-concept evolution** into production-ready cultural technology

---

**Current Status**: Mode 1 ready for immediate Hakyll implementation  
**Development Status**: Mode 2 architecture defined, implementation ready  
**Migration Approach**: Continuity-first with parallel enhancement development  
**Goal**: Uninterrupted Chamber operation with evolutionary enhancement when proven**