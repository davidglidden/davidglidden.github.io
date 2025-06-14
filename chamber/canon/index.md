---
title: "The Chamber Canon"
permalink: /chamber/canon/
layout: page
class: offering
---

## A Living Bibliography

<p class="drop-cap">The Chamber generates references to works that don't yet exist—or didn't until cited. Following Borges, we build libraries through reference rather than writing. This canon grows with each session.</p>

<div class="ornament philosophical"></div>

### Inventions° — Pure Chamber Creations

{% for work in site.chamber_canon %}
  {% if work.source_type == 'inventions' %}
- [*{{ work.title }}*{{ work.marker }}]({{ work.url }}) — {{ work.fictional_description }}
  {% endif %}
{% endfor %}

### Hybrid Works~ — Real Authors, Imagined Texts

{% for work in site.chamber_canon %}
  {% if work.source_type == 'hybrid' %}
- [*{{ work.title }}*{{ work.marker }}]({{ work.url }}) — {{ work.fictional_description }}
  {% endif %}
{% endfor %}

### Chamber Generated§ — Knowledge Through Dialogue

{% for work in site.chamber_canon %}
  {% if work.source_type == 'chamber-generated' %}
- [*{{ work.title }}*{{ work.marker }}]({{ work.url }}) — {{ work.fictional_description }}
  {% endif %}
{% endfor %}

### Hermetic Sources∞ — Ancient Wisdom Traditions

{% for work in site.chamber_canon %}
  {% if work.source_type == 'hermetic' %}
- [*{{ work.title }}*{{ work.marker }}]({{ work.url }}) — {{ work.fictional_description }}
  {% endif %}
{% endfor %}

<div class="ornament personal"></div>

Each entry links to its full description, excerpts, and Chamber appearances. The canon is searchable, browseable, and ever-growing.

<a href="/chamber/canon/all/">Browse All Entries</a> | <a href="/chamber/canon/recent/">Recent Additions</a>