# Chamber Technical Requirements

## Current Jekyll Implementation

The Chamber system is now fully operational in Jekyll with:

### Collections Structure
```
_chamber_canon/
  ├── hermetic/
  ├── hybrid/
  ├── inventions/
  └── chamber-generated/

_chamber_deliberations/
  └── standard/

_chamber_meta/
```

### Configuration
- Jekyll collections configured in `_config.yml`
- Default layouts and classes assigned
- Dynamic canon index using Liquid templates
- Navigation integration complete

### Content Types
- **Canon entries**: YAML frontmatter with source_type, marker, attribution
- **Deliberations**: Complete session syntheses with voice tracking
- **Meta-commentaries**: AI divergence analysis and protocol evaluation

## Future Hakyll Migration Requirements

### Core Functional Requirements
1. **Preserve all Chamber content and structure**
2. **Maintain dynamic canon generation**
3. **Support source notation markers**
4. **Enable Chamber-specific CSS classes**
5. **Handle fictional bibliography cross-references**

### Hakyll-Specific Implementation Needs

#### Metadata Handling
- Custom metadata parsers for Chamber content types
- Source type categorization (`hermetic`, `hybrid`, `inventions`, `chamber-generated`)
- Marker symbol preservation (`°`, `~`, `†`, `§`, `∞`, `◊`)
- Voice tracking and session correlation

#### Template System
- Chamber-specific page templates
- Dynamic canon listing by source type
- Cross-reference link generation
- Session archive organization

#### Content Processing
- Markdown with Chamber notation support
- YAML frontmatter parsing for complex session metadata
- Multi-protocol session synthesis
- Fictional work extraction and cataloging

#### Navigation Integration
- Chamber section in main navigation
- Canon browsing interface
- Session archive access
- Meta-commentary linking

### Data Structures

#### Canon Entry
```haskell
data CanonEntry = CanonEntry
  { title :: String
  , sourceType :: SourceType
  , marker :: Char
  , attributedTo :: String
  , dateClaimed :: String
  , firstCited :: String
  , createdBy :: String
  , fictionalDescription :: String
  , chambersAppearedIn :: [SessionReference]
  , excerpts :: [String]
  , relatedRealSources :: [String]
  }

data SourceType = Hermetic | Hybrid | Inventions | ChamberGenerated
```

#### Session Data
```haskell
data ChamberSession = ChamberSession
  { sessionId :: String
  , date :: String
  , protocol :: Protocol
  , engines :: [String]
  , leadVoice :: String
  , emergentVoices :: [String]
  , refusals :: [String]
  , canonicalRefs :: [CanonRef]
  , workSurvivessShadow :: Bool
  , sessionSummary :: String
  }

data Protocol = StandardOnly | ShadowOnly | StandardAndShadow
```

### Migration Strategy

1. **Content preservation**: Export all Chamber content from Jekyll collections
2. **Metadata mapping**: Convert YAML frontmatter to Hakyll context
3. **Template translation**: Convert Liquid templates to Hakyll templates
4. **Collection logic**: Implement dynamic canon generation in Hakyll
5. **URL preservation**: Maintain existing Chamber URLs for continuity
6. **CSS integration**: Ensure Chamber-specific styles carry over

### Testing Requirements

- All Chamber pages render correctly
- Canon index generates dynamically
- Session archive functions properly
- Cross-references resolve correctly
- Source notation displays properly
- Navigation integration works

### Performance Considerations

- Efficient canon generation (don't rebuild on every page)
- Session data caching for meta-commentary
- Minimal build time impact for large canon
- Scalable for future sessions

## Current Status

✅ **Jekyll implementation complete and functional**  
⏳ **Hakyll migration requirements documented**  
🔄 **Ready for future migration when needed**

---

*Technical requirements prepared for seamless Jekyll→Hakyll transition while preserving complete Chamber functionality.*