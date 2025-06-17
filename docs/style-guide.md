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

## Semantic Post Types — Complete Reference

*Typology as topology: These are rooms to inhabit, not boxes to fill*

### Core Principles
- **Compound classes**: Enable nuance through combination (`class: essay meditation`)
- **Transformative flags**: Any type can become an `encounter` when threshold moments occur
- **Ornament alignment**: Each type has preferred ornamental breathing marks
- **Living taxonomy**: Types evolve as new forms of attention emerge

---

### Primary Types

#### **observation**
- **Rationale**: From Berger's "ways of seeing"—attention as encounter with the external
- **Tone**: Present-tense immediacy, sensory precision, quiet wonder
- **Typography**: No drop caps, `.observation` class for generous spacing
- **Ornament**: `.personal` (❦) 
- **Can become**: `encounter: true` when the world meets you back
- **Examples**: "Morning Light Through Catalan Shutters", "The Cellist's Breathing Before the Suite"

#### **fragment**
- **Rationale**: Incomplete thoughts that honor their incompleteness
- **Tone**: Tentative, elliptical, resistant to closure, often inward-facing
- **Typography**: `.fragment` class (85% width, special em styling)
- **Ornament**: `.thought` (❧)
- **Distinction**: Fragments are internal; observations external
- **Examples**: "Notes Toward a Theory of Musical Grief", "The Sentence I Cannot Complete"

#### **essay**
- **Rationale**: Substantial explorations deserving classical treatment
- **Tone**: Sustained inquiry, allowing complexity and contradiction
- **Typography**: `.essay` class triggers drop caps, full measure
- **Ornament**: `.chapter` (❦ ❦ ❦) for major works
- **Can combine**: Often `essay meditation` for contemplative depth
- **Examples**: "On Becoming Animal Rationis Capax", "The Ethics of Unfinished Work"

#### **meditation**
- **Rationale**: Discursive wanderings that resist essay's formality
- **Tone**: Circular rather than linear, contemplative, open-ended
- **Typography**: Can combine with `.essay` for drop caps or standalone
- **Ornament**: `.philosophical` (❧)
- **Can become**: `encounter: true` when insight arrives unbidden
- **Examples**: "What the Bow Teaches About Time", "Variations on Silence"

#### **pattern**
- **Rationale**: Alexander's pattern language applied across domains
- **Tone**: Analytical yet embodied, seeking the universal in the particular
- **Typography**: Pattern names in `.small-caps`, structured sections
- **Ornament**: `.section` (§ § §)
- **Examples**: "The Pause Before Teaching", "Bow Distribution as Breath Distribution"

#### **glimpse**
- **Rationale**: Cartier-Bresson's decisive moment—photography as immediate attention
- **Tone**: Visual fragments, caught rather than composed
- **Typography**: `.glimpse` class (full-bleed images, no title display, whisper metadata)
- **Ornament**: `.glimpse` (◉) — aperture/eye opening to light
- **Presentation**: No title shown—image speaks first, metadata whispers after
- **Philosophy**: *"A glimpse is an event that happens to you"* — pure interruption requiring no introduction
- **Layout**: Full-bleed breaks reading frame because interruption IS its nature
- **Metadata**: `location:` and `camera:` displayed below image in italicized gray
- **Distinction**: Glimpses are received; photo-essays are read
- **Technical note**: Title exists in frontmatter for URLs/archives but isn't displayed
- **Examples**: Pure image + "La Rochelle, France", "Carrer del Pi, Barcelona · Leica M6"

#### **photo-essay**
- **Rationale**: Mohr/Berger collaboration—images and text interrogating each other
- **Tone**: Sequential narrative, meaning through accumulation
- **Typography**: Images within text column, full essay treatment with drop caps, title displayed
- **Ornament**: `.photo-essay` (⊙ ⊙ ⊙) — triple viewfinder
- **Philosophy**: *"A photo essay is a journey you choose to begin"* — title as doorway into temporal sequence
- **Layout**: Contained within text column to maintain narrator-reader contract
- **Metadata**: `series:` and `images:` count fields
- **Distinction**: Photo-essays build meaning through sequence; glimpses capture singular moments
- **Key insight**: Multiple images need "a thread to string them upon" — language starting with title
- **Examples**: "Market Light" (morning markets series), "Barcelona Gothic: Stone Memory"

#### **gloss**
- **Rationale**: Close readings in the manuscript tradition
- **Tone**: Intimate attention, scholarly care, revelatory
- **Typography**: Quoted text in `.poetic`, commentary in `.whisper`
- **Ornament**: `.lozenge` (◊)
- **Future enhancement**: Consider margin layout for true marginalia effect
- **Examples**: "On 'Animal Rationis Capax': A Phrase Unfolds", "Reading Bachelard's Margins"

#### **correspondence** *(alias: letter)*
- **Rationale**: Epistolary form as thinking-toward-another
- **Tone**: Direct address, vulnerability, temporal awareness
- **Typography**: Standard essay format, perhaps `.poetic` salutation
- **Ornament**: `.personal` (❦)
- **Technical note**: Use `letter` in YAML for clarity
- **Examples**: "Letter to My Unborn Son", "Dear Student Who Cried During Bach"

#### **offering** *(formerly reference)*
- **Rationale**: Curatorial acts as gifts to readers
- **Tone**: Generous, connective, intellectually hospitable
- **Typography**: Lists with `.oldstyle` numerals, annotated links
- **Ornament**: `.triple` (• • •)
- **Name evolution**: From "reference" to honor gift-economy ethos
- **Examples**: "Essential Readings on Craft Time", "Barcelona Walks: An Annotated Map"

#### **performance**
- **Rationale**: Where musical work meets spiritual inquiry
- **Tone**: Technical precision wed to interpretive freedom
- **Typography**: May include musical examples, fingering notations
- **Ornament**: `.musical` (⁂)
- **Examples**: "Finding the Emotional Temperature of Prelude No. 1", "The Audience as Co-Performer"

#### **teaching**
- **Rationale**: Pedagogical stories as forms of knowledge
- **Tone**: Narrative, revealing, attentive to emergence
- **Typography**: Standard format, may use `.callout` for key moments
- **Ornament**: `.asterism` (⁂)
- **Can become**: `encounter: true` when student becomes teacher
- **Examples**: "The Student Who Taught Me About Silence", "When Technique Becomes Prayer"

#### **interlude**
- **Rationale**: Breathing spaces between major movements
- **Tone**: Seasonal, transitional, briefly personal
- **Typography**: Often shorter, may use `.poetic` throughout
- **Ornament**: Varies by season/mood
- **Examples**: "Spring Equinox: Site Notes", "Between Books", "The Desk, Revisited"

---

### Transformative Modifiers

#### **encounter: true**
Not a type but a quality that can emerge within any type:
- **Porosity**: Observer/observed boundary dissolves
- **Risk**: Something is at stake
- **Transformation**: You leave changed
- **Ethical weight**: Demands response, even if silence
- **Symbol**: ✦ (four-pointed star)
- **Display policy**: Show symbol only, not word (maintains elegant mystery)

#### **chamber: true**
Review process marking texts transformed through collective examination:
- **Witnessed**: Multiple perspectives have interrogated the work
- **Transformed**: Emerged different from review process
- **Sealed**: Bears the ⟐ mark of examination
- **Symbol**: ⟐ (chamber seal)
- **Display policy**: Show symbol only, not word (consistent with encounter marking)

---

## Chamber Source Citations

When citing works that emerge from Chamber sessions:

### Notation Usage
- Apply superscript markers immediately after work titles
- Include hover text for digital versions  
- Use existing gray color for unobtrusive presence
- Link to full canon entries when available

### Source Types & Markers
- **(unmarked)** - Real, verified sources
- **°** - Pure inventions from Chamber sessions  
- **~** - Hybrid works (real author, imagined text)
- **†** - Contested or apocryphal sources
- **§** - Chamber's own synthesis
- **∞** - Hermetic/esoteric traditions
- **※** - Miscellaneous works that resist other categories

### Examples in Practice
- The *Gutenberg Meditations*° explores printing as prayer
- Tschichold's *Letters to Future Typographers*~ (imagined correspondence)  
- According to the *Prague Alchemical Codex*†, text transforms reader
- The Chamber's synthesis§ reveals pattern languages in suffering
- The *Corpus Hermeticum*∞ connects above and below
- Alexander writes◊ about "unfolding wholeness" in ways the Chamber extends

### Integration with Existing Styles
Chamber citations follow our existing emphasis patterns but add ontological transparency. The goal is scholarly honesty about the constructed nature of authority while serving both contemplative and critical reading.

### Chamber Content Formatting Rules

**Names in Chamber content**: ALL significant names must use small caps across all Chamber deliberations, canon entries, and related content
- Standard: *Title*° (<span class="small-caps">Author Name</span>, date)
- Avoid HTML in YAML arrays—apply formatting in templates

**Language consistency**: Use active voice in Chamber contexts
- "Born from Chamber examination" not "Emerged through"
- "Summoned by deliberation" not "Generated from"
- Maintain ontological ambiguity following Borgesian tradition
- "Summoned" or "called forth" rather than "created" or "fictional"
- "Works within Chamber reality" rather than "fictional works"

**Canon generation policy**: Create canon entries for works that are:
- **Foundational** - could influence future Chamber thinking
- **Generative** - open rather than close inquiry
- **Substantial** - readers might want to investigate independently
- Leave ornamental/decorative citations as references until they prove necessary

**Title duplication**: Never include H1 headers when title exists in YAML frontmatter
- Layouts handle title display from metadata
- Content should begin with subtitle or opening text

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