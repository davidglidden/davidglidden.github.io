# Chamber Canon Generation Workflow

## When Processing New Deliberations

### 1. Identify All Cited Works
Extract all works marked with °, ~, †, §, ∞, ※ from protocol responses

### 2. Assess for Canon Development
Ask for each work:
- **Foundational**: Could this influence future Chamber thinking?
- **Generative**: Does this open rather than close inquiry?
- **Substantial**: Would readers want to investigate this independently?
- **Ornamental**: Is this mainly decorative/supporting citation?

### 3. Create Canon Entries for Substantial Works
Use standard format:
```yaml
---
layout: chamber_canon
title: "Work Title"
author: "Author Name"
date: YYYY-MM-DD
marker: "°|~|†|§|∞|※"
tags: [relevant, tags]
emerged_from: "/chamber/deliberations/path-to-deliberation/"
---
```

### 4. Link from Deliberation
Ensure deliberation links to canon entries where they exist:
```markdown
- [*Work Title*](/chamber/canon/slug/)° (<span class="small-caps">Author</span>, date)
```

### 5. Leave Ornamental Citations
Don't create canon entries for:
- Decorative supporting quotes
- Brief illustrative references  
- Works that feel complete as single citations
- References that close rather than open inquiry

## Advisory Consensus
*"Create entries for works that feel alive—works that generate questions rather than close them."* - Christopher Alexander

*"Ask: would a reader want to know more about this work?"* - Aldus Manutius

## Cross-Reference Development
As Chamber matures, works may earn canon development through:
- Multiple citations across different sessions
- Reader questions/interest
- Proven influence on subsequent thinking
- Evolution from ornamental to foundational status

## Policy Review Schedule
**NOTE**: This canon generation policy should be reviewed when:
- Canon reaches 50+ substantial entries
- Cross-referencing between works becomes common
- Multiple citations of individual works emerge regularly
- The Chamber develops sufficient maturity for different selection criteria

*Current policy appropriate for early Chamber development (fewer than 25 canon entries). May need adjustment as system matures and cross-referencing patterns emerge.*