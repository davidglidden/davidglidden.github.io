---
title: "Typography Guide"
permalink: /typography-guide/
layout: page
comments: false
---

# ✍️ Typographic Style Guide — Animal Rationis Capax

This guide outlines how to access the full expressive range of the typographic system implemented on *Animal Rationis Capax*. It balances elegant design with Markdown compatibility and GitHub Pages deployment.

---

## 📚 Font System Overview

- **Body Font**: EB Garamond (400 normal, 400 italic, 700 bold)
- **UI / Headings Font**: IBM Plex Sans (400, 500, 700)
- **Code**: IBM Plex Mono
- **Small Caps**: EB Garamond SC (Regular + Display variants)

All fonts are self-hosted (WOFF2) in `/fonts/` and declared via `@font-face` in `_fonts.scss`.

### Responsive Font Sizing
- **Mobile**: 1.375rem base font size (22px) with 1.55 line height
- **Tablet**: 1.25rem base font size (20px)
- **Desktop**: 1.3125rem base font size (21px) with 1.6 line height

---

## 🧰 Typographic Utilities (Defined in `_utilities.scss`)

These custom classes enable extended typographic expression in Markdown-rendered HTML:

| Class         | Effect                                                     | Mobile Behavior |
|---------------|------------------------------------------------------------|-----------------|
| `.small-caps` | Applies proper small caps using EB Garamond SC             | Slightly reduced size (0.95em) |
| `.oldstyle`   | Activates oldstyle figures (onum)                          | No change |
| `.ligatures`  | Enables discretionary and common ligatures                 | No change |
| `.no-ligatures` | Disables all ligatures                                  | No change |
| `.poetic`     | Adds spacing, italics, and soft coloring for epigraphs     | Reduced margins and font size (0.95em) |
| `.callout`    | Visual block quote with shaded background and border       | Extends to viewport edges, smaller font (0.9em) |
| `.whisper`    | Small italic, muted tone, used for asides or commentary    | Further reduced size (0.8rem) |
| `.drop-cap`   | Beautiful drop cap for first letter                        | Scales from 3.2em to 2.8em on mobile |

---

## 🏛️ Semantic Post Types & Typography

The site uses semantic post types that influence typographic treatment:

### Post Type Classes

Add to your post front matter:
```yaml
---
layout: post
class: observation  # or: pattern, essay, meditation, fragment, etc.
encounter: true     # optional flag for transformative moments
ornament: personal  # optional ornament override
---
```

#### Typography by Type:

| Type | Typography Treatment | Drop Caps | Special Features |
|------|---------------------|-----------|------------------|
| `observation` | Generous line spacing (1.65) | No | Present-tense immediacy |
| `fragment` | 85% width, italic emphasis | No | Honors incompleteness |
| `essay` | Full measure, classical proportions | Yes | Sustained reading |
| `meditation` | Can combine with essay | Optional | Contemplative pacing |
| `pattern` | Pattern names in `.small-caps` | No | Structured sections |
| `gloss` | `.whisper` for commentary | No | Marginalia styling |
| `correspondence` | Standard format | No | Direct address |
| `offering` | Lists with `.oldstyle` numerals | No | Curatorial tone |
| `performance` | May include musical notation | No | Technical + spiritual |
| `teaching` | Standard format | No | Narrative emergence |
| `interlude` | Often uses `.poetic` | No | Seasonal/transitional |

### Compound Classes

Combine types for nuanced treatment:
```yaml
class: essay meditation  # Gets drop cap + contemplative spacing
class: observation fragment  # External attention, incomplete
```

### The Encounter Modifier

When any post becomes transformative:
```yaml
class: observation
encounter: true
```

Displays a subtle ✦ marker and increases line height to 1.8 for breathing room.

---

## 📝 How to Use in Markdown (with GitHub Pages)

### 1. **Raw HTML Embedding in Markdown**

GitHub Pages supports inline HTML. You can use this to apply styles:

```markdown
<p class="small-caps">This sentence uses small caps.</p>

<p class="poetic">Where there is no vision, the people perish.</p>

<p class="whisper">*A quiet aside, noted softly.*</p>
```

Avoid mixing with fenced code blocks or indented Markdown blocks.

---

### 2. **Drop Caps**

Drop caps are now **intentionally applied** rather than automatic, following classical typography principles where drop caps mark significant beginnings.

#### For Essays and Substantial Pieces:
Add the `.essay` class to your layout or post front matter:
```yaml
---
layout: post
class: essay
---
```
This will automatically apply a drop cap to the first paragraph.

#### Manual Drop Cap Application:
```html
<p class="drop-cap">This paragraph will have a beautiful drop cap.</p>
```

#### To Disable Drop Caps:
```html
<p class="no-drop-cap">This paragraph will not have a drop cap.</p>
```

**Note**: Drop caps now require intentional application to preserve their semantic weight and classical meaning.

---

### 3. **Headings and Lists**

These are handled via your existing SCSS:

- Headings use IBM Plex Sans at defined scale ratios
- Lists inherit body typography (EB Garamond)
- Mobile heading sizes are optimized for readability

To apply variants (e.g. `.ligatures`, `.oldstyle`) to sections:

```html
<section class="oldstyle">
  <p>1759 was a fine year for numerals like these.</p>
</section>
```

---

### 4. **Code Blocks and Inline Code**

Styled by default with IBM Plex Mono:

```markdown
`inline code`
```

or

````markdown
```bash
zsh ./deploy.sh
```
````

On mobile, code blocks extend to viewport edges with horizontal scrolling when needed.

---

### 5. **Images and Classical Proportions**

The site uses Aldus Manutius-inspired proportional relationships for images:

#### Standard Images (85% width):
```markdown
![Description](image.jpg)
```
Creates harmonious proportions with text measure.

#### Small Images (Golden Ratio - 61.8% width):
```markdown
![Description](image.jpg){: .image-small}
```
Perfect for portraits or decorative elements using φ (phi) proportions.

#### Large/Full-width Images:
```markdown
![Description](image.jpg){: .image-large}
```
For architectural photography or landscape images requiring emphasis.

#### Image Captions (Aldine Style):
Captions automatically use:
- **EB Garamond** at 0.875rem (≈14px) — minore modulo principle
- **Soft grey** italic styling
- **80% max-width** with center alignment
- **Elegant spacing** (0.5rem top, 1.5rem bottom)

```markdown
![Architecture detail](building.jpg)
*Figure 1: Classical proportions in Renaissance architecture*
```

### 6. **Typographic Ornaments**

Classical ornaments replace standard horizontal rules (`<hr>`):

#### Automatic Ornament (replaces `<hr>`):
```markdown
---
```
Renders as: ❦ (Aldus leaf)

#### Custom Ornaments with Data Attributes:
```html
<hr data-ornament="asterism">   <!-- ⁂ -->
<hr data-ornament="fleuron">    <!-- ❧ -->
<hr data-ornament="triple">     <!-- • • • -->
```

#### Ornament Classes:
```html
<div class="ornament"></div>              <!-- ❦ (default) -->
<div class="ornament asterism"></div>     <!-- ⁂ -->
<div class="ornament fleuron"></div>      <!-- ❧ -->
<div class="ornament lozenge"></div>      <!-- ◊ -->
<div class="ornament triple"></div>       <!-- • • • -->
<div class="ornament section"></div>      <!-- § § § -->
```

#### Contextual Ornaments:
```html
<div class="ornament chapter"></div>      <!-- ❦ ❦ ❦ -->
<div class="ornament article"></div>      <!-- ⁂ -->
<div class="ornament thought"></div>      <!-- ❧ -->
```

#### Content-Aware Ornaments:
Based on the nature of your content, use these semantically meaningful ornaments:
```html
<div class="ornament personal"></div>     <!-- ❦ for personal reflections -->
<div class="ornament musical"></div>      <!-- ⁂ for musical discussions -->
<div class="ornament philosophical"></div><!-- ❧ for philosophical asides -->
<div class="ornament travel"></div>       <!-- ◊ for travel/place descriptions -->
```

#### Jekyll Include:
```liquid
{% include ornament.html type="asterism" %}
{% include ornament.html type="fleuron" %}
{% include ornament.html type="personal" %}
{% include ornament.html %}  <!-- default aldus -->
```

### 7. **Poetic Styling**

For quotes or personal fragments:

```html
<p class="poetic">
  There is a silence before meaning,<br>
  and a texture in the waiting.
</p>
```

---

## 🧭 Navigation Typography

Post types appear in breadcrumbs using IBM Plex Sans at 13px:
```
Observations → Morning Light Through Catalan Shutters
```

Navigation uses IBM Plex Sans Regular (400 weight) to distinguish from bold headings while maintaining readability at small sizes.

---

## 📱 Mobile-Specific Features

### Responsive Padding System
- Content padding: **1.5rem** (24px) on all mobile devices
- Images can break out to full viewport width on mobile
- Consistent padding applied to navigation, content, and footer areas

### Navigation
- Quiet header with avatar and theme toggle
- Quiet return navigation appears on 30% scroll
- Touch targets meet 44px minimum for accessibility

### Typography Enhancements
- Automatic hyphenation enabled for narrow screens
- Optimized paragraph spacing and margins
- Reduced animation durations for better performance

---

## 🔎 Debugging Notes

- **Use private browsing** or clear cache to verify font loads
- Ensure `.woff2` paths are correct and lowercase
- Small caps require separate `EB Garamond SC` face—ensure that's installed and called properly
- GitHub Pages will honor styles in your Jekyll theme as long as they compile cleanly from SCSS
- Test mobile layouts using browser dev tools at various breakpoints (375px, 768px, 1024px)

---

## 🪶 Implementation Notes

### SCSS Structure
- `main.scss` - Variable definitions and imports
- `_fonts.scss` - @font-face declarations only
- `_base.scss` - Foundation typography and layout
- `_typography.scss` - Core typography rules
- `_utilities.scss` - Expressive typography classes
- `_navigation.scss` - Navigation-specific typography
- `_post.scss` - Article-specific styles
- `_mobile-responsive.scss` - Mobile adjustments

### Visual Compensation
Different fonts appear different sizes even at the same point size. We compensate:
```scss
$garamond-scale: 1;      // Baseline
$plex-sans-scale: 0.94;  // Appears larger
$plex-mono-scale: 0.88;  // Appears larger still
```

### Future Enhancements
- Expand color utility classes (`.tint`, `.highlight`)
- Implement automatic callout conversion for blockquote types
- Add `.verse` style for poetry with preserved line breaks
- Consider margin notes for gloss post type

---

For the philosophy behind these choices, see "[Typography: The Shape of Thought](/typography/)"