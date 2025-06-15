# Daily Update Routine
## Documentation Maintenance for Continuous Context

*Protocol for maintaining project memory and collaborative context*

---

## Overview

To prevent context loss and maintain collaborative effectiveness, certain documents need regular updates after significant work sessions. This routine ensures that project memory, working patterns, and decision rationale remain current and accessible.

---

## Documents to Update Daily

### 1. **PROJECT-MEMORY.md** *(Critical)*
**Location**: `docs/internal/PROJECT-MEMORY.md`  
**Update after**: Any significant implementation, design decision, or new functionality

**What to add**:
- New major developments with technical details
- Key design decisions and their rationale  
- Insights about what worked well or revealed new patterns
- Failed approaches and why they didn't work
- Emerging collaborative patterns

**Format**: Chronological entries with clear section headers

### 2. **CLAUDE-COLLABORATION-PROTOCOL.md** *(High Priority)*
**Location**: `docs/internal/CLAUDE-COLLABORATION-PROTOCOL.md`  
**Update after**: Changes in working patterns, communication style, or collaborative approach

**What to update**:
- New working patterns in "Claude's Optimal Response Pattern"
- Updated technical context in "Recent Major Developments" 
- Evolved decision-making processes
- New advisor patterns or consultation methods
- Success/failure patterns in collaboration

**Format**: Replace relevant sections, update timestamps

### 3. **CHANGELOG.md** *(Public Record)*
**Location**: `CHANGELOG.md` (root level)  
**Update after**: Major feature implementations, public-facing changes

**What to add**:
- New features with user-facing descriptions
- Technical implementations that affect site functionality
- Breaking changes or significant modifications
- Version numbers and release dates

**Format**: Chronological with semantic versioning approach

### 4. **CLAUDE.md** *(As Needed)*
**Location**: `CLAUDE.md` (root level)  
**Update after**: Changes to essential commands, architecture, or working requirements

**What to update**:
- New essential commands or workflows
- Updated architecture descriptions
- Changed directory structures
- New plugins or dependencies

**Format**: Replace outdated sections

---

## Update Triggers

### **End of Session** (Every significant work period)
- [ ] Update PROJECT-MEMORY.md with session outcomes
- [ ] Note any changed working patterns in COLLABORATION-PROTOCOL.md
- [ ] Add completed work to CHANGELOG.md if public-facing

### **Major Implementation Complete**
- [ ] Full update to PROJECT-MEMORY.md with technical details and insights
- [ ] Update COLLABORATION-PROTOCOL.md with new patterns discovered
- [ ] Create CHANGELOG.md entry with complete feature description
- [ ] Update CLAUDE.md if architecture or commands changed

### **Working Pattern Evolution**
- [ ] Document in COLLABORATION-PROTOCOL.md
- [ ] Add insights to PROJECT-MEMORY.md lessons learned section
- [ ] Note process improvements for future reference

### **Context Resumption** (Start of new session)
- [ ] Review all documentation for current state
- [ ] Check for any needed updates from previous session
- [ ] Ensure all documents reflect actual working state

---

## Content Guidelines

### **PROJECT-MEMORY.md Focus**
- **Technical decisions**: What was implemented and why
- **Design insights**: What we learned about the problem space
- **Collaboration patterns**: How the working relationship evolved
- **Future implications**: What this enables or prevents

### **COLLABORATION-PROTOCOL.md Focus**  
- **Communication patterns**: How we talk and decide together
- **Process improvements**: What works better than before
- **Role clarifications**: Who does what and when
- **Context preservation**: How to maintain shared understanding

### **CHANGELOG.md Focus**
- **User-facing changes**: What someone using the site would notice
- **Feature descriptions**: What new capabilities exist
- **Technical overview**: How it works (high level)
- **Impact**: Why this matters for the site's purpose

---

## Quality Checks

### Before Committing Documentation Updates
- [ ] **Accuracy**: All technical details correct and current
- [ ] **Completeness**: No major decisions or insights missing
- [ ] **Clarity**: Future readers (including ourselves) can understand context
- [ ] **Integration**: Documents reference each other appropriately
- [ ] **Currency**: Timestamps and version information updated

### Periodic Review (Weekly/Monthly)
- [ ] **Consistency**: All documents tell the same story
- [ ] **Relevance**: Outdated information removed or marked historical
- [ ] **Accessibility**: Organization supports quick reference and lookup
- [ ] **Evolution**: Documents grow organically without becoming unwieldy

---

## Emergency Context Recovery

If context is lost or documentation falls behind:

1. **Read git commit messages** for recent technical changes
2. **Review PROJECT-MEMORY.md** for last known state
3. **Check COLLABORATION-PROTOCOL.md** for working patterns
4. **Scan recent file changes** for implementation details
5. **Update all documents** before proceeding with new work

---

## Integration with Chamber System

Since The Chamber generates its own documentation through session processing, ensure:

- **Chamber sessions documented** in PROJECT-MEMORY.md as they complete
- **Voice patterns and insights** added to project memory
- **Technical improvements** from Chamber work integrated into protocols
- **Fictional canon evolution** noted in development history

---

*"Documentation is not overhead—it is the practice of not forgetting."*

**Last updated**: December 2024  
**Next review**: After establishing routine in practice