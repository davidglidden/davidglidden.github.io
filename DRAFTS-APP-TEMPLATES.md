# Drafts App YAML Templates for Jekyll Post Types

## How to Use These Templates in Drafts App

1. Create a new action in Drafts
2. Add a "Script" step
3. Copy the JavaScript code for each template
4. The script will create a new draft with the appropriate front matter

---

## Observation Template

**Action Name:** "New Observation"

```javascript
// New Observation Template
let today = new Date();
let dateStr = today.getFullYear() + "-" + 
              String(today.getMonth() + 1).padStart(2, '0') + "-" + 
              String(today.getDate()).padStart(2, '0');

let template = `---
title: ""
date: ${dateStr}
description: ""
tags: [en, observation]
class: observation
ornament: personal
location: 
---

`;

let d = Draft.create();
d.content = template;
d.update();
editor.load(d);
```

---

## Fragment Template

**Action Name:** "New Fragment"

```javascript
// New Fragment Template
let today = new Date();
let dateStr = today.getFullYear() + "-" + 
              String(today.getMonth() + 1).padStart(2, '0') + "-" + 
              String(today.getDate()).padStart(2, '0');

let template = `---
title: ""
date: ${dateStr}
description: ""
tags: [en, fragment]
class: fragment
layout: fragment
ornament: personal
---

`;

let d = Draft.create();
d.content = template;
d.update();
editor.load(d);
```

---

## Essay Template

**Action Name:** "New Essay"

```javascript
// New Essay Template
let today = new Date();
let dateStr = today.getFullYear() + "-" + 
              String(today.getMonth() + 1).padStart(2, '0') + "-" + 
              String(today.getDate()).padStart(2, '0');

let template = `---
title: ""
date: ${dateStr}
description: ""
tags: [en, essay]
class: essay
ornament: philosophical
---

`;

let d = Draft.create();
d.content = template;
d.update();
editor.load(d);
```

---

## Meditation Template

**Action Name:** "New Meditation"

```javascript
// New Meditation Template
let today = new Date();
let dateStr = today.getFullYear() + "-" + 
              String(today.getMonth() + 1).padStart(2, '0') + "-" + 
              String(today.getDate()).padStart(2, '0');

let template = `---
title: ""
date: ${dateStr}
description: ""
tags: [en, meditation]
class: meditation
ornament: philosophical
---

`;

let d = Draft.create();
d.content = template;
d.update();
editor.load(d);
```

---

## Pattern Template

**Action Name:** "New Pattern"

```javascript
// New Pattern Template
let today = new Date();
let dateStr = today.getFullYear() + "-" + 
              String(today.getMonth() + 1).padStart(2, '0') + "-" + 
              String(today.getDate()).padStart(2, '0');

let template = `---
title: ""
date: ${dateStr}
description: ""
tags: [en, pattern, teaching]
class: pattern
ornament: musical
---

`;

let d = Draft.create();
d.content = template;
d.update();
editor.load(d);
```

---

## Performance Template

**Action Name:** "New Performance Reflection"

```javascript
// New Performance Template
let today = new Date();
let dateStr = today.getFullYear() + "-" + 
              String(today.getMonth() + 1).padStart(2, '0') + "-" + 
              String(today.getDate()).padStart(2, '0');

let template = `---
title: ""
date: ${dateStr}
description: ""
tags: [en, performance, music]
class: performance
ornament: musical
---

`;

let d = Draft.create();
d.content = template;
d.update();
editor.load(d);
```

---

## Teaching Template

**Action Name:** "New Teaching Note"

```javascript
// New Teaching Template
let today = new Date();
let dateStr = today.getFullYear() + "-" + 
              String(today.getMonth() + 1).padStart(2, '0') + "-" + 
              String(today.getDate()).padStart(2, '0');

let template = `---
title: ""
date: ${dateStr}
description: ""
tags: [en, teaching, pedagogy]
class: teaching
ornament: musical
---

`;

let d = Draft.create();
d.content = template;
d.update();
editor.load(d);
```

---

## Gloss Template

**Action Name:** "New Gloss"

```javascript
// New Gloss Template
let today = new Date();
let dateStr = today.getFullYear() + "-" + 
              String(today.getMonth() + 1).padStart(2, '0') + "-" + 
              String(today.getDate()).padStart(2, '0');

let template = `---
title: ""
date: ${dateStr}
description: ""
tags: [en, gloss, commentary]
class: gloss
ornament: philosophical
---

`;

let d = Draft.create();
d.content = template;
d.update();
editor.load(d);
```

---

## Correspondence Template

**Action Name:** "New Correspondence"

```javascript
// New Correspondence Template
let today = new Date();
let dateStr = today.getFullYear() + "-" + 
              String(today.getMonth() + 1).padStart(2, '0') + "-" + 
              String(today.getDate()).padStart(2, '0');

let template = `---
title: ""
date: ${dateStr}
description: ""
tags: [en, correspondence, dialogue]
class: correspondence
ornament: personal
---

`;

let d = Draft.create();
d.content = template;
d.update();
editor.load(d);
```

---

## Offering Template

**Action Name:** "New Offering"

```javascript
// New Offering Template
let today = new Date();
let dateStr = today.getFullYear() + "-" + 
              String(today.getMonth() + 1).padStart(2, '0') + "-" + 
              String(today.getDate()).padStart(2, '0');

let template = `---
title: ""
date: ${dateStr}
description: ""
tags: [en, offering]
class: offering
ornament: personal
---

`;

let d = Draft.create();
d.content = template;
d.update();
editor.load(d);
```

---

## Interlude Template

**Action Name:** "New Interlude"

```javascript
// New Interlude Template
let today = new Date();
let dateStr = today.getFullYear() + "-" + 
              String(today.getMonth() + 1).padStart(2, '0') + "-" + 
              String(today.getDate()).padStart(2, '0');

let template = `---
title: ""
date: ${dateStr}
description: ""
tags: [en, interlude]
class: interlude
ornament: personal
---

`;

let d = Draft.create();
d.content = template;
d.update();
editor.load(d);
```

---

## Travel Observation Template

**Action Name:** "New Travel Observation"

```javascript
// New Travel Observation Template
let today = new Date();
let dateStr = today.getFullYear() + "-" + 
              String(today.getMonth() + 1).padStart(2, '0') + "-" + 
              String(today.getDate()).padStart(2, '0');

let template = `---
title: ""
date: ${dateStr}
description: ""
location: 
tags: [en, observation, travel, seen]
class: observation
ornament: travel
---

<figure>
<img src="/assets/img/">
<figcaption></figcaption>
</figure>

`;

let d = Draft.create();
d.content = template;
d.update();
editor.load(d);
```

---

## Encounter Template (Transformative Post)

**Action Name:** "New Encounter"

```javascript
// New Encounter Template
let today = new Date();
let dateStr = today.getFullYear() + "-" + 
              String(today.getMonth() + 1).padStart(2, '0') + "-" + 
              String(today.getDate()).padStart(2, '0');

let template = `---
title: ""
date: ${dateStr}
description: ""
tags: [en, observation]
class: observation
encounter: true
ornament: personal
---

`;

let d = Draft.create();
d.content = template;
d.update();
editor.load(d);
```

---

## Multi-language Essay Template

**Action Name:** "New Multi-language Essay"

```javascript
// New Multi-language Essay Template
let today = new Date();
let dateStr = today.getFullYear() + "-" + 
              String(today.getMonth() + 1).padStart(2, '0') + "-" + 
              String(today.getDate()).padStart(2, '0');

let template = `---
title: ""
date: ${dateStr}
description: ""
tags: [en, fr, es, essay]
class: essay
ornament: philosophical
languages:
  - code: en
    name: English
  - code: fr
    name: Français  
  - code: es
    name: Castellano
---

{% include language-toggle.html %}

`;

let d = Draft.create();
d.content = template;
d.update();
editor.load(d);
```

---

## Setup Instructions for Drafts App

1. **Create Action Group:** Create a new action group called "Jekyll Posts"

2. **For Each Template:**
   - Tap the "+" to create a new action
   - Give it the suggested name (e.g., "New Observation")
   - Add a Script step
   - Copy the JavaScript code into the script step
   - Set the script step to run "After Success"

3. **Optional Customizations:**
   - Add icons to each action for quick identification
   - Assign keyboard shortcuts for frequently used templates
   - Modify the default tags or ornaments to match your preferences

4. **Usage:**
   - Run the action to create a new draft with pre-filled front matter
   - Fill in the title, tags, and content
   - The cursor will be positioned after the front matter for immediate writing

## Front Matter Field Reference

### Required Fields
- `title:` - Post title
- `date:` - Publication date (YYYY-MM-DD)
- `class:` - Post type (observation, fragment, essay, etc.)

### Optional Fields
- `tags:` - Array of tags [en, theme, topic]
- `location:` - GPS coordinates for travel posts
- `ornament:` - Visual ornament type (personal, musical, philosophical, travel)
- `encounter: true` - Mark transformative posts
- `layout:` - Override default layout
- `description:` - SEO description
- `languages:` - For multi-language posts

### Ornament Options
- `personal` - Personal reflections (❦)
- `musical` - Musical discussions (⁂)  
- `philosophical` - Philosophical content (❧)
- `travel` - Travel/place descriptions (◊)