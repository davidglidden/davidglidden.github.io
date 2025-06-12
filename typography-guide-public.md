---
title: "Typography"
permalink: /typography/
layout: page
class: essay
---

## The Shape of Thought

<blockquote class="poetic">
"The page is a unit of space and time."<br>
—<span class="small-caps">Robert Bringhurst</span>
</blockquote>

<p class="drop-cap">Typography is not decoration. It is epistemology made visible—a belief that form shapes thought, that the vessel changes the water. This site's typography emerges from a simple question: what would reading feel like if every choice served presence rather than efficiency?</p>

The answer lives somewhere between a <span class="oldstyle">16th</span>-century Aldine edition and tomorrow's screen. Between the manuscript's breathing room and the terminal's clarity. Between slowness and precision.

<div class="ornament philosophical"></div>

## The Voices

Three typographic voices converse across these pages:

### <span class="small-caps">EB Garamond</span> — The Storyteller
Our body text speaks in Claude Garamont's voice, as interpreted by Georg Duffner. This isn't nostalgia—it's recognition that <span class="oldstyle">450</span> years of readers have found home in these letterforms. Garamond carries time differently than sans serifs. It knows that reading is durational, not instantaneous.

*Technical notes for the curious: We use the full family at text sizes—regular, italic, and bold. True small caps come from EB Garamond SC. Everything self-hosted as WOFF2, because consistency matters.*

### <span class="small-caps">IBM Plex Sans</span> — The Guide  
Headings and interface elements speak in Plex Sans—IBM's gift to the commons, designed by Bold Monday. It provides wayfinding without shouting, structure without rigidity. Where Garamond whispers history, Plex Sans states the present.

*The medium weight (500) adds just enough presence for navigation. Regular (400) for breadcrumbs. Bold (700) for emphasis.*

### <span class="small-caps">IBM Plex Mono</span> — The Precision
Code and metadata require different breathing. Monospace isn't just for terminals—it's for any text that needs to declare its construction. Dates, times, technical notes. The grid made visible.

*Scaled to 0.88× to match Garamond's visual weight. Typography is about optical harmony, not mathematical equality.*

<div class="ornament section"></div>

## The Measure

Reading happens in the body. These measurements honor that:

- **Line length**: <span class="oldstyle">68</span> characters—about fourteen words. Long enough for thought to develop, short enough to return.
- **Line height**: <span class="oldstyle">1.6</span> on desktop, <span class="oldstyle">1.55</span> on mobile. Air between lines is thinking space.
- **Font size**: <span class="oldstyle">21</span>px base on desktop, <span class="oldstyle">22</span>px on mobile. Large enough to invite sustained reading.

The page breathes through an <span class="oldstyle">8</span>px rhythm. Every margin, every space between elements follows this musical interval. Not because grids are sacred, but because rhythm aids comprehension.

<div class="ornament musical"></div>

## Responsive Attention

Your distance from the screen changes everything:

### In Hand (<span class="oldstyle">22</span>px)
Mobile reading is intimate—often in bed, in transit, in stolen moments. The type swells slightly, line height opens. Paragraphs align left (never justified on narrow measures). The page becomes a private conversation.

### At Lap (<span class="oldstyle">20</span>px)
Tablets occupy a middle distance. Still personal but less immediate. The bridge between lean-in and lean-back reading.

### At Desk (<span class="oldstyle">21</span>px)
Full attention at arm's length. Here the classical proportions emerge. Margins frame thought. The full typographic system comes alive.

<div class="ornament travel"></div>

## Ornaments & Flourishes

Where others place horizontal rules, we set ornaments—breathing marks borrowed from manuscript tradition:

- **❦** — The Aldus leaf, our default pause
- **⁂** — The asterism, for triple emphasis
- **❧** — The rotated fleuron, marking turns in thought
- **◊** — The lozenge, for journeys and positions
- **⟐** — The divided lozenge, marking texts transformed through council review

These aren't mere decoration. They're semantic punctuation, each carrying its own quality of pause. The divided lozenge specifically marks work that has undergone collective examination and emerged transformed.

### Small Capitals & Other Graces

<span class="small-caps">Small capitals</span> mark proper names and concepts requiring gentle emphasis. Not the fake scaling that word processors offer, but true small caps drawn for this purpose.

<span class="oldstyle">Oldstyle figures</span> (notice these numerals: <span class="oldstyle">1234567890</span>) sit within text rather than upon it. They have ascenders and descenders like letters, because numbers are part of language, not above it.

Ligatures—the _fi_ and _fl_ connections—happen automatically. They're the typographic equivalent of smooth bowing, preventing the collision of letters that want to touch.

<div class="ornament personal"></div>

## The Technical Garden

For those who like to peek behind curtains:

```scss
// Visual compensation - making different fonts feel equal
$garamond-scale: 1;      // Our baseline
$plex-sans-scale: 0.94;  // Sans appears larger
$plex-mono-scale: 0.88;  // Mono larger still

// The 8px grid that undergirds everything
$space-unit: 0.5rem;
$space-sm: 1rem;    // Breathing
$space-md: 1.5rem;  // Thinking  
$space-lg: 2rem;    // Sectioning
```

Every font loads with `font-display: swap`, respecting slow connections. No external dependencies—your privacy matters more than my convenience.

### For the Especially Curious

View the complete technical implementation:
- [Internal typography documentation](/typography-guide/) 
- [SCSS source files](https://github.com/yourusername/yourrepo)
- [Type specimen tests](/specimens/) *(future page)*

<div class="ornament philosophical"></div>

## Typography as Ethics

Matthew Butterick writes that "typography is the visual component of the written word." But it's more—it's the tempo of thought, the gesture of meaning, the breath between ideas.

This site's typography makes commitments:

1. **Reading is not scanning**. These pages resist the quick extract. They invite dwelling.

2. **Beauty is not superficial**. Careful form honors both writer and reader.

3. **Tradition and innovation converse**. Garamond meets system fonts meets variable viewports.

4. **Every choice has meaning**. From the kerning of small caps to the rhythm of margins—nothing is arbitrary.

<blockquote class="whisper">
The best typography, like the best teaching, is invisible until you need it. Then it holds you like a trusted friend.
</blockquote>

<div class="ornament philosophical"></div>

## Use & Reuse

This typographic system is open for adaptation. Take what serves, leave what doesn't. The only request: maintain the spirit of craft. Don't just copy—understand, then transform.

For implementation details, see the [technical guide](/typography-guide/). For philosophy, you're already here.

<div class="ornament section"></div>

*Typography set in <span class="small-caps">EB Garamond</span>, <span class="small-caps">IBM Plex Sans</span>, and <span class="small-caps">IBM Plex Mono</span>. Designed in Barcelona, <span class="oldstyle">2024</span>–<span class="oldstyle">2025</span>. Last refined: today, probably.*