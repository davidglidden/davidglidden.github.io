# Chamber Manual Workflow
## Complete Session Documentation Process

**Version**: 1.1  
**Purpose**: Manual workflow for Chamber sessions with collaborative publishing  
**Context**: David runs sessions → Claude Code processes for publication  
**Access**: Private - David Glidden only  

---

# DAVID'S WORKFLOW (Steps 1-2)

## Step 1: Session Execution
Create session folder: `chamber-sessions-private/YYYY-MM-DD-title/`

**Run all four protocols using master prompts from `docs/internal/chamber-prompts/`:**
1. **GPT Standard** → save as `gpt-standard-raw.txt` 
2. **Claude Standard** → save as `claude-standard-raw.txt`
3. **GPT Shadow** → save as `gpt-shadow-raw.txt`
4. **Claude Shadow** → save as `claude-shadow-raw.txt`

**Also save:**
- `submitted-text.md` - The original text you submitted
- `session-notes.md` - Any observations about the process

## Step 2: Send to Claude Code
**Zip/compress the complete session folder and send it.**

Include any notes about:
- Which protocol seemed most productive
- Any fictional references that particularly stood out
- Which voices surprised you
- Overall impression of the session

---

# CLAUDE CODE'S WORKFLOW (Steps 3-9)

## Step 3: Extract Fictional References
Hunt through all four raw outputs for works marked with notation (°, ~, †, §, ∞, ◊).

Create comprehensive extraction document cataloging:
- All fictional works by protocol and voice
- Overlapping citations between engines
- Conflicts or variations
- Assessment of which works merit canon entries

## Step 4: Create Canon Entries
For each significant fictional work:
- Create proper Jekyll markdown file with YAML frontmatter
- Write description and context
- Include excerpts and Chamber appearances
- Set up cross-references and related works
- Place in appropriate canon subdirectory

## Step 5: Synthesize Deliberation Page
Choose the most productive protocol outputs and create unified narrative:
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
- Run 4-protocol Chamber sessions
- Send raw outputs with notes
- Review and approve all drafts
- Maintain editorial control

**Claude Code's Responsibility**:
- Extract and structure all content
- Create Jekyll-ready publications
- Handle technical integration  
- Present drafts for approval
- Publish only after sign-off

This division maximizes the Chamber's transformative work while ensuring systematic documentation and proper technical implementation.