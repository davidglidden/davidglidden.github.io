---
title: Writing Style Guide
permalink: /style-guide/
layout: page
class: pattern
published: false  # Internal use only
---

# Writing Style Guide

## Foreign Language Phrases

When using non-English phrases, always include language attributes for accessibility:

### Common Languages:
- Latin: `<span lang="la">animal rationis capax</span>`
- French: `<span lang="fr">joie de vivre</span>`
- Spanish: `<span lang="es">duende</span>`
- Italian: `<span lang="it">sprezzatura</span>`
- German: `<span lang="de">Zeitgeist</span>`

### Using the Include:
For frequently used phrases:
```liquid
{% include lang.html lang="la" text="festina lente" %}
```

### In Front Matter:
When titles contain foreign phrases:
```yaml
title: "On <span lang='it'>Sprezzatura</span> in Performance"
```

## Semantic Post Types

Always specify the post type in front matter:
- `observation` - momentary attention
- `fragment` - incomplete thoughts
- `pattern` - recognized connections
- `essay` - sustained inquiry
- `meditation` - contemplative depth
- Others as defined in `/attention/`

## Typography Conventions

- Small caps: Names of thinkers `<span class="small-caps">Christopher Alexander</span>`
- Drop caps: Add `class: essay` to front matter for automatic drop caps
- Ornaments: Use `<div class="ornament philosophical"></div>` for section breaks
- Whispers: `<p class="whisper">Quiet concluding thoughts</p>`

## Image Accessibility

Always include alt text:
```markdown
![Morning light through Gothic arches at Santa Maria del Mar](path/to/image.jpg)
```

---

*This guide is for internal reference. Update as conventions evolve.*