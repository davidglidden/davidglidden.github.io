# SEO-Optimized Post Template

## Ideal Front Matter Structure

```yaml
---
title: "Your Title Here"
date: 2024-01-15 10:00:00 +0100
description: "A compelling 150-160 character description that captures the essence and invites reading"
tags: [observation, pattern, barcelona, music]  # Use underscore_separated for multi-word concepts
class: observation  # or fragment, essay, meditation, pattern, etc.
layout: post  # Usually auto-applied
image: /assets/img/posts/specific-image.jpg  # Optional, falls back to social-default.jpg
encounter: true  # Only for transformative/significant posts
ornament: personal  # personal, musical, philosophical, travel
location: "41.3851,2.1734"  # GPS coordinates for travel posts (optional)
---
```

## SEO Description Guidelines

### Length: 150-160 characters (ideal for search results)
- Count includes spaces and punctuation
- Should be complete thoughts, not cut off mid-sentence
- Compelling enough to encourage clicks

### Content Types by Post Class:

#### **Observation** (50-70% of posts)
```yaml
description: "A contemplative observation on [specific moment/place/detail] that reveals [insight/pattern/meaning]"
```
Examples:
- "Morning light through Gothic glass reveals how attention transforms the ordinary into threshold moments"
- "A graffiti girl in locked-down Paris becomes a meditation on presence and the democracy of attention"

#### **Fragment** (20-30% of posts)
```yaml
description: "Brief reflections on [topic] - incomplete thoughts seeking their larger pattern"
```
Examples:
- "Brief reflections on the space between notes where music actually happens"
- "Incomplete thoughts on why the best teaching happens in the margins of what we planned to say"

#### **Essay** (10-15% of posts)
```yaml
description: "An extended inquiry into [central question/theme] through the lens of [approach/experience]"
```
Examples:
- "Extended inquiry into Monteverdi's Vespers as architecture made audible in Cremona's sacred spaces"
- "How Christopher Alexander's pattern language applies to the craft of musical interpretation"

#### **Pattern** (Teaching/Pedagogical posts)
```yaml
description: "A recognized pattern in [domain] that reveals deeper principles about [larger theme]"
```
Examples:
- "How the pattern of 'festina lente' in viola technique reveals universal principles of presence and craft"

#### **Meditation** (Rare, contemplative)
```yaml
description: "Deep contemplation on [existential theme] arising from [specific experience/observation]"
```

### Geographic/Travel Posts:
Always mention the specific location:
```yaml
description: "Observations from [Specific Place, City/Region] on [theme] - where [what was discovered]"
```

### Language-Specific Considerations:
- For posts with foreign phrases, hint at the linguistic element
- "A meditation on the untranslatable Spanish concept of 'duende' in musical performance"

## Technical SEO Elements

### Image Optimization:
```yaml
image: /assets/img/posts/2024-01-15-title-slug.jpg  # Specific to post
# Falls back to: /assets/img/social-default.jpg
```

### Tags Strategy:
1. **Language code**: en (always first)
2. **Post type**: observation, essay, fragment, pattern
3. **Primary theme**: music, teaching, travel, philosophy
4. **Secondary themes**: presence, attention, craft, barcelona
5. **Specific topics**: monteverdi, alexander, pedagogy

### URL Structure:
- Permalink: `/:title/` (set in _config.yml)
- Keep titles concise but descriptive
- Use hyphens for word separation
- Avoid stop words when possible

## Content Structure for SEO

### Opening Paragraph:
Should contain key terms naturally and hook the reader within first 50 words.

### Internal Linking:
- Link to related posts using descriptive anchor text
- Link to main pages: /about/, /archive/, /now/
- Use relative URLs: `[about this site](/about/)`

### Headings Hierarchy:
```markdown
# Main Title (H1 - automatic from front matter)
## Major Sections (H2)
### Subsections (H3)
```

### Schema Markup:
Handled automatically by jekyll-seo-tag plugin when properly configured.

## Example Complete Posts:

### Observation Post:
```yaml
---
title: "Light Through Gothic Glass"
date: 2024-01-15 08:30:00 +0100
description: "Morning light through Gothic glass at Santa Maria del Mar reveals how attention transforms ordinary moments"
tags: [en, observation, barcelona, sacred_spaces, attention]
class: observation
ornament: personal
---
```

### Essay Post:
```yaml
---
title: "The Architecture of Attention in Monteverdi's Vespers"
date: 2024-01-15 14:00:00 +0100
description: "How Monteverdi's 1610 Vespers creates spaces for contemplation through musical architecture and sacred time"
tags: [en, essay, monteverdi, sacred_music, architecture, performance]
class: essay
ornament: musical
---
```

### Fragment Post:
```yaml
---
title: "On the Democracy of Pencils"
date: 2024-01-15 16:45:00 +0100
description: "Brief thoughts on why the most democratic tool for thinking remains unchanged after centuries of innovation"
tags: [en, fragment, tools, craft, simplicity]
class: fragment
layout: fragment
ornament: philosophical
---
```

## SEO Checklist for Each Post:

- [ ] Description is 150-160 characters
- [ ] Description accurately represents content
- [ ] Description uses active voice and compelling language
- [ ] Tags follow underscore convention for multi-word concepts
- [ ] Class is specified and appropriate
- [ ] Title is descriptive but concise
- [ ] Date includes timezone (+0100 for Barcelona)
- [ ] Image specified if relevant, or falls back to default
- [ ] First paragraph contains key terms naturally
- [ ] Headings use proper hierarchy
- [ ] Internal links use descriptive anchor text
- [ ] Foreign phrases include language attributes when used in content

## Tools for Description Length:

**Character count bookmark:**
```javascript
javascript:alert('Length: ' + window.getSelection().toString().length + ' characters');
```

**Or use:** charactercounttool.com for quick checking

---

*Keep this template updated as SEO practices evolve and site needs change.*