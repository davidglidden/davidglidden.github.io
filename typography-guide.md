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
- **Mobile**: 1.375rem base font size (22px) with 1.75 line height — optimized for comfortable mobile reading
- **Tablet**: 1.25rem base font size (20px)
- **Desktop**: 1.3125rem base font size (21px) with 1.65 line height — refined for optimal reading

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

Drop caps are automatically applied to the first paragraph of article content. To disable for a specific paragraph:

```markdown
<p class="no-drop-cap">This paragraph will not have a drop cap.</p>
```

To manually add a drop cap to any paragraph:

```html
<p class="drop-cap">This paragraph will have a beautiful drop cap.</p>
```

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

### 5. **Poetic Styling**

For quotes or personal fragments:

```html
<p class="poetic">
  There is a silence before meaning,<br>
  and a texture in the waiting.
</p>
```

---

## 📱 Mobile-Specific Features

### Responsive Padding System
- Content padding: **1.5rem** (24px) on all mobile devices — matches iA.net exactly
- Images can break out to full viewport width on mobile
- Consistent padding applied to navigation, content, and footer areas

### Navigation
- Sticky navigation header on mobile with blur effect
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

## 🪶 Future Enhancements Implemented

- ✅ **Drop caps** for article openings (auto-applied to first paragraph)
- ✅ **Mobile-first responsive system** with iA Writer-inspired padding
- ✅ **Enhanced mobile typography** with proper scaling and spacing

### Suggestions for Future Work
- Expand color utility classes (`.tint`, `.highlight`)
- Implement automatic callout conversion for blockquote types (note, warn, tip, etc.)
- Add `.verse` style for poetry with preserved line breaks