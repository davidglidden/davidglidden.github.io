---
title: "The Chamber Canon"
permalink: /chamber/canon/
layout: page
class: offering
---

## A Living Bibliography

<p class="drop-cap">The Chamber accumulates references to works that don't yet exist—or didn't until cited. Following Borges, we build libraries through reference rather than writing. This canon grows with each session.</p>

<div class="ornament philosophical"></div>

<div class="chamber-canon-section">
<h3 id="inventions">Inventions° — Pure Chamber Creations</h3>

{% assign inventions = site.chamber_canon | where: "source_type", "inventions" | sort: "first_cited" %}
{% if inventions.size > 0 %}
<ul>
{% for work in inventions %}
<li><a href="{{ work.url }}"><em>{{ work.title }}</em>{{ work.marker }}</a> — {{ work.fictional_description }}</li>
{% endfor %}
</ul>
{% else %}
<p><em>No inventions yet...</em></p>
{% endif %}
</div>

<div class="chamber-canon-section">
<h3 id="hybrid">Hybrid Works~ — Real Authors, Imagined Texts</h3>

{% assign hybrid = site.chamber_canon | where: "source_type", "hybrid" | sort: "first_cited" %}
{% if hybrid.size > 0 %}
<ul>
{% for work in hybrid %}
<li><a href="{{ work.url }}"><em>{{ work.title }}</em>{{ work.marker }}</a> — {{ work.fictional_description }}</li>
{% endfor %}
</ul>
{% else %}
<p><em>No hybrid works yet...</em></p>
{% endif %}
</div>

<div class="chamber-canon-section">
<h3 id="chamber-written">Chamber Written§ — Knowledge Through Dialogue</h3>

{% assign chamber_written = site.chamber_canon | where: "source_type", "chamber-generated" | sort: "first_cited" %}
{% if chamber_written.size > 0 %}
<ul>
{% for work in chamber_written %}
<li><a href="{{ work.url }}"><em>{{ work.title }}</em>{{ work.marker }}</a> — {{ work.fictional_description }}</li>
{% endfor %}
</ul>
{% else %}
<p><em>No chamber-written works yet...</em></p>
{% endif %}
</div>

<div class="chamber-canon-section">
<h3 id="hermetic">Hermetic Sources∞ — Ancient Wisdom Traditions</h3>

{% assign hermetic = site.chamber_canon | where: "source_type", "hermetic" | sort: "first_cited" %}
{% if hermetic.size > 0 %}
<ul>
{% for work in hermetic %}
<li><a href="{{ work.url }}"><em>{{ work.title }}</em>{{ work.marker }}</a> — {{ work.fictional_description }}</li>
{% endfor %}
</ul>
{% else %}
<p><em>No hermetic sources yet...</em></p>
{% endif %}
</div>

<div class="ornament personal"></div>

Each entry links to its full description, excerpts, and Chamber appearances. The canon is searchable, browseable, and ever-growing.

<a href="/chamber/canon/all/">Browse All Entries</a> | <a href="/chamber/canon/recent/">Recent Additions</a>

<nav class="chamber-enfilade">
  <a href="/chamber/">Chamber</a>
  <span class="separator">·</span>
  <a href="/chamber/about/">About</a>
  <span class="separator">·</span>
  <span class="current">Canon <span class="arrow">←</span></span>
  <span class="separator">·</span>
  <a href="/chamber/sessions/">Sessions</a>
  <span class="separator">·</span>
  <a href="/chamber/voices/">Voices</a>
</nav>