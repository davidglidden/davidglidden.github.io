# Architecture Decision Records
## Animal Rationis Capax Decision Documentation

*Formal record of significant architectural and design decisions*

---

## Purpose

Architecture Decision Records (ADRs) capture the context, reasoning, and consequences of important decisions made during project development. They preserve not just **what** was decided, but **why** it was decided and **what alternatives were considered**.

---

## ADR Index

### **Chamber System Architecture**

- **[ADR-001: Four-Protocol Chamber System](2024-12-15-four-protocol-chamber-system.md)**  
  *Why use GPT + Claude with Standard + Shadow protocols rather than alternatives*

- **[ADR-002: Shadow Protocol as Essential](2024-12-15-shadow-protocol-as-essential.md)**  
  *Why every text undergoes ethical reckoning regardless of apparent content*

- **[ADR-003: Gray Source Markers Over Colors](2024-12-15-gray-source-markers-over-colors.md)**  
  *Why fictional work notation uses gray symbols rather than color-coded system*

- **[ADR-004: Manual Chamber Workflow](2024-12-15-manual-chamber-workflow.md)**  
  *Why human-controlled process rather than automated protocol execution*

### **Future Decisions**
*Additional ADRs will be added as significant architectural choices are made*

---

## ADR Template

When creating new ADRs, use this structure:

```markdown
# ADR-XXX: [Decision Title]

**Date**: YYYY-MM-DD  
**Status**: [Proposed | Accepted | Superseded]  
**Supersedes**: [Previous ADR if applicable]

## Context
[What forces led to this decision?]

## Decision  
[What we decided to do]

## Consequences
### Positive
[Benefits of this decision]

### Negative  
[Costs or limitations]

### Neutral
[Neither positive nor negative effects]

## Alternatives Considered
[What other options we evaluated and why they were rejected]

## References
[Links to related documents, implementations, or examples]
```

---

## Decision Categories

### **Architectural**: System structure and component relationships
### **Philosophical**: Value-based choices that shape project direction  
### **Technical**: Implementation approaches and tool choices
### **Process**: Workflow and collaboration methodology decisions
### **Design**: User experience and interface design choices

---

## Status Values

- **Proposed**: Decision suggested but not yet implemented
- **Accepted**: Decision made and being implemented  
- **Superseded**: Decision replaced by later ADR
- **Deprecated**: Decision no longer relevant to current system

---

## Integration with Project Memory

ADRs complement but differ from [Project Memory](../internal/project-memory.md):

**ADRs**: Formal decision documentation with alternatives and consequences  
**Project Memory**: Chronological development history with insights and patterns

Both preserve essential project knowledge but serve different purposes in maintaining context and enabling future decision-making.

---

*"Every significant decision shapes the project's future. ADRs ensure we remember not just what we chose, but why we chose it."*

**Created**: December 2024  
**Updated**: As new ADRs are added