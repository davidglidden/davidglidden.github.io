---
title: "Type Specimens"
permalink: /specimens/
layout: page
class: essay
---

## Typography in Action

<blockquote class="poetic">
"Typography is what language looks like."<br>
—<span class="small-caps">Ellen Lupton</span>
</blockquote>

<p class="drop-cap">This page demonstrates the complete typographic system of *Animal Rationis Capax* in practical use. Not theory, but the actual forms and voices that shape reading across these pages. Consider it a testing ground—where every element proves its fitness for the contemplative life.</p>

<div class="ornament philosophical"></div>

## The Three Voices

### <span class="small-caps">EB Garamond</span> — Body Text & Storytelling

Our primary voice carries the weight of sustained reading. Notice how the letterforms breathe with classical proportions while remaining crisp on contemporary screens:

**Regular weight** provides the foundation for all body text, designed for durability across long passages. **Italic** offers emphasis without shouting—*like this phrase that asks for gentle attention*. **Bold** appears sparingly, **reserved for technical documentation** where weight truly serves meaning.

<span class="oldstyle">1234567890</span> — These oldstyle figures sit within the text line, having ascenders and descenders like letters. They feel more natural in running prose than the mechanical <span style="font-feature-settings: 'lnum';">1234567890</span> of lining figures.

#### True Small Capitals

<span class="small-caps">Christopher Alexander</span> and <span class="small-caps">Simone Weil</span> receive the honor of true small capitals—not scaled-down capitals but letterforms drawn specifically for this purpose. Notice the optical weight matches the surrounding text.

#### Ligatures in Action

The _fi_ and _fl_ ligatures happen automatically: field, flight, configuration, influence. These aren't decoration but collision avoidance—preventing letters from bumping into each other awkwardly.

### <span class="small-caps">IBM Plex Sans</span> — Interface & Guidance

Headings and navigational elements speak in Plex Sans, providing structure without rigidity. The **medium weight (500)** gives presence to navigation elements, while **regular (400)** handles metadata and breadcrumbs.

### <span class="small-caps">IBM Plex Mono</span> — Precision & Code

Technical elements require different breathing:

```
Date: 2025-01-13 14:32
Location: Carrer del Pi, Barcelona
Camera: Leica M6, Tri-X 400
```

Notice the monospace scaling: smaller than body text but optically matched to feel harmonious rather than intrusive.

<div class="ornament section"></div>

## Semantic Typography

Different post types receive different typographic treatments, each serving the content's particular needs:

### Essays — Classical Treatment

Essays receive **drop caps** for their opening paragraphs, signaling substantial content worthy of classical attention. The measure expands to full width, inviting sustained engagement.

### Fragments — Intimate Spacing

<div style="max-width: 85%; margin: 0 auto; font-size: 0.95em; line-height: 1.8;">
Fragments live in reduced measure, centered on the page. They speak more quietly, often about incomplete thoughts that honor their incompleteness. The narrower line length creates intimacy.
</div>

### Observations — Present-Tense Attention

Observations resist the classical signals of essays. No drop caps, but enhanced paragraph spacing encourages contemplative breathing between thoughts.

### Glimpses — Pure Image

Glimpses display no title—only full-bleed imagery that breaks all container bounds, followed by whisper-level metadata. The image speaks first and entirely, with location and camera details appearing below in subtle italics.

<div class="ornament musical"></div>

## Ornamental Punctuation

Where others place horizontal rules, we set ornaments—breathing marks that carry semantic meaning:

<div class="ornament"></div>

The default **aldus leaf (❦)** provides gentle pause between sections.

<div class="ornament philosophical"></div>

The **rotated fleuron (❧)** marks philosophical asides and turns in thought.

<div class="ornament asterism"></div>

The **asterism (⁂)** signals triple emphasis, often for musical discussions.

<div class="ornament travel"></div>

The **lozenge (◊)** accompanies travel writing and geographic positioning.

<div class="ornament section"></div>

**Section marks (§ § §)** create stronger divisions, particularly for pattern language.

<div class="ornament glimpse"></div>

The **aperture (◉)** marks photographic glimpses—the eye opening to light.

<div class="ornament photo-essay"></div>

**Triple viewfinders (⊙ ⊙ ⊙)** signal sequential visual narratives.

<div class="ornament chapter"></div>

**Triple aldus leaves (❦ ❦ ❦)** mark major transitions in substantial works.

<div class="ornament personal"></div>

## Scale & Rhythm

Typography breathes through an **8px rhythm**. Every margin, every space between elements follows this musical interval:

- **0.5rem** (8px) — Minimal breathing
- **1rem** (16px) — Comfortable spacing  
- **1.5rem** (24px) — Thoughtful separation
- **2rem** (32px) — Sectional divisions

Font sizes scale responsively but maintain optical harmony:

- **Desktop**: 21px base, 1.6 line height
- **Tablet**: 20px base, 1.55 line height  
- **Mobile**: 22px base, 1.55 line height

The larger mobile size compensates for intimate reading distances and ensures accessibility.

<div class="ornament thought"></div>

## Special Elements

### Whisper Text

<p class="whisper">
<em>Sometimes words need to speak more quietly, trailing off into suggestion rather than declaration. Whisper text provides this gentleness.</em>
</p>

### Callout Blocks

<div class="callout">
Important information that needs visual separation from body text receives this treatment—background tint and left border providing clear but gentle distinction.
</div>

### Post Qualifiers

Beyond body typography, certain posts carry qualifying symbols:

- **✦** — The encounter mark, appearing after titles where ordinary observation opened into transformative experience
- **⟐** — The chamber seal, marking texts that emerged transformed through collective review

These function like musical accidentals—they change how the following content should be approached.

<div class="ornament asterism"></div>

## Language Support

Foreign phrases receive proper language markup for accessibility:

- <span lang="la">Animal rationis capax</span> (Latin)
- <span lang="fr">L'écriture de soi</span> (French)
- <span lang="it">Sprezzatura</span> (Italian)
- <span lang="de">Gelassenheit</span> (German)

Screen readers pronounce these correctly, honoring both meaning and sound.

<div class="ornament lozenge"></div>

## Technical Implementation

The complete system loads as self-hosted WOFF2 files with `font-display: swap`, respecting slow connections. No external dependencies preserve both performance and privacy.

### Font Feature Settings

```scss
// Oldstyle numerals in text
.oldstyle {
  font-feature-settings: "onum";
}

// Enhanced ligatures
.ligatures {
  font-variant-ligatures: common-ligatures discretionary-ligatures;
}

// True small capitals
.small-caps {
  font-family: 'EB Garamond SC', $serif-family;
  letter-spacing: 0.03em;
  text-transform: lowercase;
}
```

### Responsive Scaling

```scss
// Visual compensation
$garamond-scale: 1;      // Baseline
$plex-sans-scale: 0.94;  // Sans appears larger
$plex-mono-scale: 0.88;  // Mono appears largest
```

Different typefaces have different optical weights. These scales ensure visual harmony across the complete system.

<div class="ornament philosophical"></div>

## Typography as Interface

Every typographic choice functions as interface design:

- **Drop caps** signal "this deserves sustained attention"
- **Centered fragments** whisper "approach intimately"  
- **Full-bleed glimpses** declare "look first, read second"
- **Ornamental breaks** provide "breathing space for thought"

The typography doesn't just carry content—it shapes how that content wants to be received.

<blockquote class="whisper">
The best typography feels inevitable. These letterforms want to arrange themselves this way, want to breathe at these intervals, want to invite this particular quality of attention.
</blockquote>

<div class="ornament section"></div>

<nav class="about-enfilade">
  <a href="/typography/">Typography</a>
  <span class="separator">·</span>
  <span class="current">Specimens <span class="arrow">←</span></span>
  <span class="separator">·</span>
  <a href="/typography-guide/">Technical Guide</a>
</nav>

<div class="ornament philosophical"></div>

*Specimens set in <span class="small-caps">EB Garamond</span>, <span class="small-caps">IBM Plex Sans</span>, and <span class="small-caps">IBM Plex Mono</span>. Every element tested for clarity and grace. Last refined: <span class="oldstyle">2025</span>.*