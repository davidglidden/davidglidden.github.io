---
title: "Editorial Style Guide"
permalink: /style-guide/
layout: page
class: essay
---

## Editorial Guidelines

<blockquote class="poetic">
"Style is not a display but a discipline."<br>
—<span class="small-caps">Jan Tschichold</span>
</blockquote>

<p class="drop-cap">This guide documents the editorial voice and stylistic choices that shape *Animal Rationis Capax*. It serves as both reference and philosophy—not rules to constrain but patterns to enable consistent, thoughtful expression. Like typography itself, these guidelines exist to serve meaning, not decorate it.</p>

<div class="ornament philosophical"></div>

## Voice & Tone

### Core Qualities

**Contemplative without being precious**  
We think deeply but speak clearly. Philosophy serves insight, not obfuscation.

**Precise but not pedantic**  
Every word chosen carefully, but not to show off vocabulary. Precision serves the reader.

**Personal without narcissism**  
The self appears as lens, not subject. Personal experience illuminates universal patterns.

**Questioning over declaring**  
End with invitations to think. Trust readers to complete thoughts we begin.

### The Shadow Principle

Beauty can hide violence. Craft can serve oppression. Our style must:
- Include uncomfortable truths
- Question its own premises
- Make space for refusal
- Acknowledge what it might exclude or harm

<div class="ornament section"></div>

## Language Patterns

### Names & References

**Small capitals** for significant figures when first mentioned or when carrying particular weight:
- <span class="small-caps">Christopher Alexander</span> (philosophical guides)
- <span class="small-caps">Jordi Savall</span> (mentors, collaborators)
- Not for every name, only those that anchor thought

**Attributions** in quotes:
- Em dash before name
- Small caps for author
- Example: —<span class="small-caps">Simone Weil</span>

### Numbers & Dates

**Oldstyle figures** in running text: <span class="oldstyle">2025</span>, not 2025  
**Lining figures** in technical contexts: Version 25.3  
**Spelled out** when beginning sentences or for small numbers under ten

### Emphasis & Weight

**Italics** for emphasis in body text: *this* matters  
**Bold** reserved for technical documentation and guides  
**"Scare quotes"** only when genuinely questioning a term  
**NEVER** use all caps for emphasis

### Foreign Language

**Always mark language** for accessibility:
```html
<span lang="la">festina lente</span>
<span lang="fr">joie de vivre</span>
<span lang="it">sprezzatura</span>
```

**Common language codes:**
- `la` - Latin
- `fr` - French  
- `es` - Spanish
- `it` - Italian
- `de` - German

### Lists & Structure

**Bullet points** only in guides and technical documents  
**In essays**, lists flow as natural language: "First this, then that, finally the other"  
**Numbered lists** only when sequence truly matters

<div class="ornament personal"></div>

## Semantic Post Types

Each piece declares its nature, determining both style and reader approach:

### Primary Types

**observation** - External attention, present tense, no interpretation  
**fragment** - Incomplete by design, often italic, honors the partial  
**essay** - Sustained thought, receives drop cap, builds argument  
**meditation** - Inward spiral, contemplative pacing  
**pattern** - Recognition pieces, pattern names in small caps  
**glimpse** - Photographic moments, full-bleed images, minimal commentary  
**photo-essay** - Sequential visual narrative, images and text in conversation  
**gloss** - Commentary, marginalia, uses whisper text  
**offering** - Curatorial, lists with oldstyle numerals  

### Modifiers

`encounter: true` - When world stops, marked with ✦  
`chamber: true` - Underwent Chamber review, marked with ⟐

<div class="ornament philosophical"></div>

## Structural Elements

### Critical Page Rule

**NEVER include an H1 (`#`) in markdown content.** The title belongs only in YAML frontmatter:

✓ **Correct:**
```markdown
---
title: "Navigation Philosophy"
---

<blockquote class="poetic">
Opening quote without H1...
</blockquote>
```

✗ **Incorrect:**
```markdown
---
title: "Navigation Philosophy"
---

# Navigation Philosophy

This creates duplicate titles...
```

### Opening Patterns

**Drop caps** only for essays and substantial meditations  
**Poetic blockquotes** to establish tone, not as decoration  
**Context-setting** through concrete detail before abstraction

### Transitions

**Ornamental breaks** using semantic classes:
- `<div class="ornament"></div>` - default (❦)
- `<div class="ornament philosophical"></div>` - for ideas (❧)
- `<div class="ornament personal"></div>` - for experience (❦)
- `<div class="ornament musical"></div>` - for sound/music (⁂)
- Never bare `<hr>` tags

### Closing Gestures

**Whisper text** for gentle conclusions:
```html
<p class="whisper">
<em>Text that trails off, suggests, wonders...</em>
</p>
```

**Questions** that open rather than answers that close  
**Invitations** to continue thinking  
**Never** heavy-handed summaries

<div class="ornament thought"></div>

## Technical Constraints as Style

### Privacy as Principle
- No tracking or analytics
- No comments (broadcast, don't discuss)
- Self-hosted fonts
- Local-first philosophy

### Presence Requirements
- No Zoom ("presence requires presence")
- Email for correspondence
- Slowness over immediacy

### Citation Practice
- Internal links where they illuminate
- External links sparingly (future: with popovers)
- Always credit sources
- Prefer primary to secondary

### Image Guidelines
**Always include descriptive alt text:**
```markdown
![Morning light through Gothic arches at Santa Maria del Mar](path/to/image.jpg)
```
Not just: `![Gothic arches](path/to/image.jpg)`

### Footer Philosophy

The footer provides gentle closure through:
- **Philosophical grounding** - Opens with <span lang="la">Animal Rationis Capax</span>
- **Contextual navigation** - Shows "Beginning" only when not on homepage
- **Temporal awareness** - Post dates when relevant, seasonal geometry always
- **Geographic presence** - Barcelona as place of making

**Seasonal Geometry** based on ancient associations:
- △ Spring (rising/air/growth)
- □ Summer (stable/earth/fullness)  
- ▽ Autumn (falling/water/harvest)
- ○ Winter (complete/enclosed/rest)

The footer speaks in whispers, using established typographic utilities. No copyright symbols, no defensive language—just quiet acknowledgment of time and place.

<div class="ornament section"></div>

## The Chamber Review

Certain pieces undergo Chamber review—a process too complex to detail here. These pieces:
- Bear the mark ⟐ (divided lozenge)
- Show `chamber: reviewed` in metadata
- Often exhibit particular depth or difficulty
- May have faced the shadow voices

The Chamber serves transformation, not validation.

<div class="ornament musical"></div>

## Forbidden Patterns

What we consciously avoid:

**Performative humility** - False modesty serves no one  
**Academic jargon** - Unless precision truly requires it  
**Conclusion paragraphs** - Trust readers to synthesize  
**Meta-commentary** - Don't explain what you're doing while doing it  
**Hedge words** - "Perhaps," "maybe," "it seems" (unless genuine uncertainty)  
**Promotional language** - The work speaks for itself

<div class="ornament philosophical"></div>

## Living Guidelines

This guide evolves. Language lives. What serves today may constrain tomorrow. The principles matter more than rules:

1. **Clarity serves complexity** - Deep thought needs clear expression
2. **Beauty carries responsibility** - Ask what it might hide
3. **Form follows function** - Every choice should serve meaning
4. **Slowness enables depth** - Resist internet urgency
5. **Questions honor readers** - Trust their intelligence

<blockquote class="whisper">
Style is ethics made visible. How we write reveals how we think, what we value, whom we serve. May these patterns enable expression while maintaining the struggle that creates meaning.
</blockquote>

<div class="ornament section"></div>

## Quick Reference

### YAML Frontmatter
```yaml
---
title: "Title Here"
date: 2025-01-20
class: essay meditation  # semantic type(s)
encounter: true         # optional modifier
chamber: true           # chamber reviewed
ornament: philosophical # override default
---
```

#### Visual Types
```yaml
# Glimpse
---
title: "Brief, evocative phrase"
class: glimpse
date: 2025-01-13 14:32
location: "Carrer del Pi, Barcelona"  
camera: "Leica M6, Tri-X 400"
---

# Photo Essay
---
title: "Market Light"
class: photo-essay
date: 2025-01-13
location: "Barri Gòtic, Barcelona"
series: "Morning Markets"
images: 8
---
```

### Common Patterns
- Drop cap: `<p class="drop-cap">`
- Small caps: `<span class="small-caps">Name</span>`
- Oldstyle: `<span class="oldstyle">2025</span>`
- Whisper: `<p class="whisper"><em>Text</em></p>`
- Ornament: `<div class="ornament"></div>`

### Chamber Marks
- ✦ = encounter (transformative moment)
- ⟐ = chamber reviewed (divided lozenge)

<div class="ornament philosophical"></div>

<p class="whisper">
<em>For technical typography details, see the internal Typography Guide. For philosophy, read the Colophon. For examples, read the site itself.</em>
</p>