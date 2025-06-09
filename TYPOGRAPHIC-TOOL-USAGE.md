# Typographic Formatter Usage Guide

## Overview

The Typographic Formatter is a Python tool that automatically prepares Markdown documents with appropriate typographic markup for *Animal Rationis Capax*. It applies classical typography principles and integrates with the site's sophisticated ornament and class system.

## Usage

```bash
python typographic-formatter.py input.md [output.md]
```

If no output file is specified, the tool creates a new file with `_formatted` suffix.

## What the Tool Does

### 1. **Content Analysis**
- Analyzes text to determine content type: `musical`, `philosophical`, `personal`, or `travel`
- Detects if content qualifies as an "essay" (substantial pieces worthy of drop caps)

### 2. **YAML Front Matter**
- Creates proper Jekyll front matter with required fields:
  - `title` (extracted from first heading or generated)
  - `layout` (post for essays, page for others)
  - `date` (current date if missing)
  - `tags` (based on detected content type)
  - `class: essay` (for substantial pieces)

### 3. **Automatic Markup Application**

#### Small Caps
- Latin phrases: *ad astra*, *circa*, *et cetera*, *i.e.*, *e.g.*
- Abbreviations: *A.D.*, *B.C.*, *vs.*, *etc.*

#### Oldstyle Figures
- Years: 1607, 2025
- Ordinal numbers: 1st, 2nd, 3rd

#### Contextual Ornaments
Replaces `---` with appropriate ornaments:
- **Musical content**: ⁂ (asterism)
- **Philosophical content**: ❧ (fleuron)
- **Personal content**: ❦ (aldus leaf)
- **Travel content**: ◊ (diamond)

#### Typography Classes
- **Blockquotes**: Short quotes get `.poetic` class
- **Images**: Automatic size classification (`.image-small` for portraits)
- **Essay marker**: Adds comment showing where drop cap will appear

## Examples

### Input:
```markdown
# A Musical Reflection on Monteverdi

In 1607, Claudio Monteverdi premiered his opera L'Orfeo.

> "Music must touch the heart"

The composer's innovative use of harmony...

---

When I first encountered Monteverdi's music...
```

### Output:
```markdown
---
title: "A Musical Reflection on Monteverdi"
layout: post
date: 2025-06-09
tags: [musical]
class: essay
---

# A Musical Reflection on Monteverdi

<!-- Drop cap will be automatically applied to the first paragraph -->
In <span class="oldstyle">1607</span>, Claudio Monteverdi premiered his opera L'Orfeo.

<blockquote class="poetic">
  "Music must touch the heart"
</blockquote>

The composer's innovative use of harmony...

<div class="ornament musical"></div>
When I first encountered Monteverdi's music...
```

## Content Type Detection

The tool uses keyword analysis to determine content type:

- **Musical**: music, melody, composer names (Mozart, Bach), musical terms
- **Philosophical**: philosophy, wisdom, philosopher names (Aristotle, Kant)
- **Personal**: memory, family, emotional words, first-person narrative
- **Travel**: journey, city names (Paris, Rome), architectural terms

## Essay Classification

Content is classified as an "essay" if it has:
- 3+ substantial paragraphs, OR
- 300+ words

Essays automatically receive:
- `layout: post` (instead of `page`)
- `class: essay` in front matter
- Drop cap guidance comment

## Integration with Typography System

The tool creates markup that works seamlessly with:
- **Mobile-responsive typography** (iA Writer-inspired)
- **Classical proportions** (golden ratio, Aldine principles)  
- **Contextual ornament system** (content-aware decorations)
- **Hierarchical bullet system** (Renaissance-inspired symbols)
- **Drop cap system** (intentional application for essays)

## Manual Overrides

You can still manually add classes and markup:
- Use `<span class="small-caps">text</span>` for specific small caps
- Use `<div class="ornament personal"></div>` for specific ornaments
- Use `<p class="no-drop-cap">` to prevent drop caps
- Use `{:.image-large}` for specific image sizing

The tool preserves existing markup and works alongside manual formatting.