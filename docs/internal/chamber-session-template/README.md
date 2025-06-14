# Chamber Session Template

Copy this folder structure for each new session:

```
chamber-sessions/YYYY-MM-DD-title/
├── session-metadata.yml
├── submitted-text.md
├── gpt-standard-raw.md
├── claude-standard-raw.md  
├── gpt-shadow-raw.md
├── claude-shadow-raw.md
├── extracted-references.md
├── meta-commentary.md
└── session-notes.md
```

## Quick Start Process

1. **Create session folder**: `chamber-sessions/2025-06-14-my-title/`
2. **Copy prompts**: Use master prompts from `/chamber/prompts/`
3. **Run all four protocols**: Save raw outputs
4. **Extract references**: Hunt for all fictional works with notation
5. **Create meta-commentary**: Analyze AI differences
6. **Build deliberation**: Synthesize for public page
7. **Update canon**: Create/update fictional work entries
8. **Archive everything**: Complete documentation

See [workflow-manual.md](../workflow-manual.md) for detailed procedures.

## File Templates

### session-metadata.yml
```yaml
session_id: "2025-06-14-title"
date: 2025-06-14
submitted_text_type: "essay"
submitted_text_length: 500
protocols_completed:
  - gpt-standard: true
  - claude-standard: true
  - gpt-shadow: true
  - claude-shadow: true
text_survives_shadow: false
total_fictional_works: 0
```

### extracted-references.md
```markdown
# Fictional References from Session YYYY-MM-DD

## From GPT Standard:
- *Title*° - Author, Date - "Quote context"

## From Claude Standard:
- *Title*° - Author, Date - "Quote context"

## From GPT Shadow:
- *Title*° - Author, Date - "Quote context"

## From Claude Shadow:
- *Title*° - Author, Date - "Quote context"

## Canon Actions Required:
- [ ] Create: *New Work*°
- [ ] Update: *Existing Work*~
```

The Chamber transforms texts while documenting its own evolution.