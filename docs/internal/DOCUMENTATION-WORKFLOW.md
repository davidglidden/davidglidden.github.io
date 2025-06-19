# Documentation Workflow & Session Guide
## How to Work with Claude Code on Animal Rationis Capax

*A practical guide for maintaining comprehensive documentation and effective collaboration*

---

## Starting Each Session

### What Claude AUTOMATICALLY Does
- ✅ Reads `CLAUDE.md` at the root of your repository
- ✅ Receives git status showing current branch and recent commits
- ✅ Gets working directory context

### What You SHOULD Ask Claude to Do
Claude does NOT automatically read the full documentation system. For best results, start sessions with:

```
"Please read the collaboration protocol and project memory to understand our current context"
```

Or more specifically:
```
"Please review:
- docs/internal/collaboration-protocol.md
- docs/internal/project-memory.md
- Any other relevant docs for what we're working on today"
```

### Quick Start Commands

**For general work:**
```
Read the collaboration protocol and recent project memory
```

**For design decisions:**
```
Read the collaboration protocol and DESIGN-DIALOGUES.md - we'll need our advisors today
```

**For typography work:**
```
Read the typography guide and style guide documentation
```

---

## Documentation Update Workflow

### During Our Sessions

#### 1. **Before Major Changes**
Ask Claude to:
- Document current state in PROJECT-MEMORY.md
- Note the problem/opportunity we're addressing
- Record any design consultations

Example: *"Before we implement this, please document our reasoning in project memory"*

#### 2. **After Implementations**
Remind Claude to:
- Update PROJECT-MEMORY.md with what was built
- Add technical details to relevant guides
- Update protocols if working patterns changed

Example: *"Please update the project memory with what we just implemented"*

#### 3. **When Patterns Emerge**
Point out:
- New working methods that should be captured
- Communication patterns that work well
- Technical patterns worth documenting

Example: *"This approach worked well - can you add it to our collaboration protocol?"*

---

## What Gets Documented Where

### PROJECT-MEMORY.md
- ✓ Chronological development history
- ✓ Major features implemented
- ✓ Design decisions and rationale
- ✓ Technical implementation notes
- ✓ Lessons learned

### CLAUDE-COLLABORATION-PROTOCOL.md
- ✓ Communication patterns
- ✓ Working methods that emerge
- ✓ Design advisor consultation process
- ✓ Technical preferences
- ✓ Quality standards

### Style Guide & Technical Docs
- ✓ New semantic types
- ✓ CSS/SCSS implementations
- ✓ Typography decisions
- ✓ Editorial guidelines
- ✓ Code patterns

### DESIGN-DIALOGUES.md
- ✓ Advisor consultations
- ✓ Design philosophy discussions
- ✓ Reasoning behind aesthetic choices
- ✓ Alternative approaches considered

---

## Best Practices

### 1. **Commit Code and Docs Together**
When making changes:
```bash
git add [code files] [documentation files]
git commit -m "Feature: X with comprehensive documentation"
```

### 2. **Use Explicit Instructions**
Instead of: *"Update the docs"*
Say: *"Please update PROJECT-MEMORY.md with our decision to use full-bleed images for glimpses and the reasoning from our advisor consultation"*

### 3. **Review Documentation Periodically**
- Check that memory is accurate
- Ensure protocols reflect current practice
- Verify technical docs match implementation

### 4. **Create New Docs as Needed**
As complexity grows, ask Claude to create:
- TECHNICAL-REFERENCE.md for deep implementation details
- API-PATTERNS.md for reusable code patterns
- MIGRATION-PLAN.md for Hakyll transition
- Any other focused documentation

---

## Session Templates

### Standard Development Session
```
1. "Please read the collaboration protocol and recent project memory"
2. Work on features/fixes
3. "Update project memory with what we implemented"
4. "Any protocols need updating based on how we worked today?"
5. Commit everything together
```

### Design Decision Session
```
1. "Please read the collaboration protocol and design dialogues"
2. "Let's consult our advisors on [specific question]"
3. Implement based on consultation
4. "Document this design dialogue and update relevant guides"
5. "Update project memory with our decision and rationale"
```

### Major Feature Session
```
1. "Read all relevant documentation for [feature area]"
2. Plan the implementation
3. Build the feature
4. "Create/update all relevant documentation"
5. "Add a comprehensive entry to project memory"
```

---

## Common Pitfalls & Solutions

### Pitfall: Forgetting to document decisions
**Solution**: Make it habit - "Before we move on, let's document why we made this choice"

### Pitfall: Documentation drift from reality
**Solution**: Regular reviews - "Does this protocol still match how we work?"

### Pitfall: Too much or too little detail
**Solution**: Focus on the "why" not just the "what" - future you needs context

### Pitfall: Not reading context at session start
**Solution**: Make it your opening ritual - context first, then work

---

## The Philosophy

Remember: Documentation is not overhead, it's investment. Every decision documented today saves time and confusion tomorrow. The goal is to create a living system that:

- **Captures wisdom** as it emerges
- **Preserves context** for future decisions
- **Enables continuity** across sessions
- **Supports growth** as complexity increases

---

## Quick Reference Card

### Session Start
```
"Read the collaboration protocol and project memory"
```

### After Decisions
```
"Document this decision and reasoning in project memory"
```

### After Implementation
```
"Update all relevant documentation with what we built"
```

### When Patterns Emerge
```
"Add this pattern to our collaboration protocol"
```

### Before Committing
```
"Have we documented everything from this session?"
```

---

*"The best documentation is written in the moment, when context is fresh and reasoning is clear."*

**Created**: June 2025  
**Purpose**: Ensure comprehensive documentation throughout development  
**Scope**: All Animal Rationis Capax development sessions