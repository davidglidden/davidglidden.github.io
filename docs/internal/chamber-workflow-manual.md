# Chamber Manual Workflow
## Complete Session Documentation Process

**Version**: 2.1  
**Purpose**: Manual workflow for Chamber sessions with collaborative publishing  
**Context**: David runs sessions → Claude Code processes for publication  
**Access**: Private - David Glidden only  

---

# DAVID'S WORKFLOW (Steps 1-2)

## Step 1: Choose Protocol and Execute Session
Create session folder: `chamber-sessions-private/YYYY-MM-DD-title/`

**Choose ONE protocol per session** using master prompts from `docs/internal/chamber-prompts/`:

### For First Light Protocol:
Use prompts from `docs/internal/chamber-prompts/first-light/`
1. **GPT First Light** → save as `[first-light]gpt-raw.txt`
2. **Claude First Light** → save as `[first-light]claude-raw.txt`
3. **Original text** → save as `[first-light]submitted-text.md`

### For Standard Protocol:
Use prompts from `docs/internal/chamber-prompts/standard/`
1. **GPT Standard** → save as `[standard]gpt-raw.txt`
2. **Claude Standard** → save as `[standard]claude-raw.txt`
3. **Original text** → save as `[standard]submitted-text.md`

### For Shadow Protocol:
Use prompts from `docs/internal/chamber-prompts/shadow/`
1. **GPT Shadow** → save as `[shadow]gpt-raw.txt`
2. **Claude Shadow** → save as `[shadow]claude-raw.txt`
3. **Original text** → save as `[shadow]submitted-text.md`

**Optional:**
- `session-notes.md` - Any observations about the process

## Step 2: Send to Claude Code
**Notify that there's a new session ready for processing.**

Include any notes about:
- Which voices surprised you
- Any fictional references that particularly stood out
- Overall impression of the session
- Reason for choosing this protocol

---

# CLAUDE CODE'S WORKFLOW (Steps 3-9)

## Step 3: Detect Protocol and Extract Fictional References
Auto-detect protocol from filename brackets: `[first-light]`, `[standard]`, or `[shadow]`

Hunt through both raw outputs for works marked with notation (°, ~, †, §, ∞, ◊).

Create comprehensive extraction document cataloging:
- All fictional works by voice (from both GPT and Claude outputs)
- Overlapping citations between engines
- Conflicts or variations
- Assessment of which works merit canon entries
- Protocol-specific patterns (First Light tends to be gentler, Shadow more accusatory)

## Step 4: Create Canon Entries
For each significant fictional work:
- Create proper Jekyll markdown file with YAML frontmatter
- Write description and context
- Include excerpts and Chamber appearances
- Set up cross-references and related works
- Place in appropriate canon subdirectory

## Step 5: Synthesize Deliberation Page
Synthesize both engine outputs for the chosen protocol into unified narrative:
- Opening observations from multiple voices
- Primary dialogue maintaining voice authenticity  
- Emergent patterns and tensions
- Synthesized recommendations
- Essential questions that emerged
- Links to generated canon entries

## Step 6: Write Meta-Commentary
Analyze differences between AI systems:
- Voice manifestation variations (How did Tschichold differ?)
- Protocol outcome divergences (Standard vs Shadow verdicts)
- Fictional generation patterns (GPT vs Claude tendencies)
- Implications for Chamber understanding

## Step 7: Jekyll Integration
- Create proper file paths and YAML frontmatter
- Set up cross-links between deliberations and canon
- Update session archive and navigation
- Ensure source markers display correctly
- Test all links and formatting

## Step 8: Present Drafts to David
**Send for review:**
- Draft deliberation page
- Draft canon entries  
- Draft meta-commentary
- Summary of Jekyll integration

**Request feedback on:**
- Editorial voice and emphasis
- Canon entry completeness
- Missing insights or patterns
- Publication approval

## Step 9: Publish After Approval
- Commit all files to repository
- Update chamber session registry
- Document any workflow improvements
- Archive complete session privately

---

# COLLABORATIVE WORKFLOW SUMMARY

**David's Responsibility**: 
- Choose appropriate protocol for each text
- Run 2-engine Chamber sessions (GPT + Claude for chosen protocol)
- Send session folder notification with notes
- Review and approve all drafts
- Maintain editorial control

**Claude Code's Responsibility**:
- Extract and structure all content
- Create Jekyll-ready publications
- Handle technical integration  
- Present drafts for approval
- Publish only after sign-off

This division maximizes the Chamber's transformative work while ensuring systematic documentation and proper technical implementation.

---

# ARCHIVE MANAGEMENT

## Permanent Preservation Policy
**All raw session files are kept indefinitely for research value.**

### Storage Structure
```
chamber-sessions-private/
├── 2024/
│   └── 2024-12-28-owl-emblem/
├── 2025/
│   ├── 2025-06-16-session-name/
│   └── 2025-06-20-another-session/
├── 2026/
└── README.md (archive organization notes)
```

### What We Preserve
- **All raw AI outputs**: `[protocol]gpt-raw.txt`, `[protocol]claude-raw.txt`
- **Original submitted texts**: `[protocol]submitted-text.md` 
- **Session notes**: `session-notes.md` with observations and reasoning
- **Processing documentation**: Any notes from synthesis work
- **Re-processing versions**: If sessions are re-analyzed with improved methods

### Research Value
This archive serves as primary source material for:
- **Chamber methodology research**: Systematic study of editorial transformation
- **AI collaboration studies**: Cross-engine comparison and voice consistency analysis
- **Longitudinal behavior tracking**: How AI systems evolve over time
- **Future system improvements**: Training data and methodology refinement
- **Academic documentation**: Complete record for scholarly analysis

### Storage Considerations
- **Capacity**: 3TB+ available, easily expandable
- **File sizes**: Text files are minimal storage impact
- **Compression**: Optional for older years if needed
- **Access**: David Glidden only, private working archive

The raw files constitute irreplaceable primary sources documenting the emergence of human-AI editorial collaboration.

---

# RECENT SESSIONS PROCESSED

## 2025-06-16: "Seeds of Activation" (First Light)
**Status**: ✅ Successfully processed and published
**Protocol**: First Light (inaugural session)
**Outcome**: Gentle recognition with three fictional works generated
**Notes**: Perfect demonstration of First Light methodology working as designed
**Canon additions**: 3 works (Alexander°, Martin~, Reciprocal Manual§)
**Obfuscation**: ✅ All AI references properly hermetic in public materials