---
title: "Browse All Canon Entries"
permalink: /chamber/canon/all/
layout: page
class: offering
---

## Complete Chamber Canon

<p class="drop-cap">All works cited into existence through Chamber examinations, organized by source type and chronology.</p>

<div class="ornament philosophical"></div>

{% assign all_canon = site.pages | where_exp: "page", "page.path contains 'chamber/canon/' and page.path != 'chamber/canon/index.md' and page.path != 'chamber/canon/all.md' and page.path != 'chamber/canon/recent.md'" | sort: "date" %}

{% for work in all_canon %}
<div class="canon-entry">
  <h3><a href="{{ work.url }}"><em>{{ work.title }}</em>{{ work.notation }}</a></h3>
  <p class="canon-meta">
    <span class="small-caps">{{ work.author }}</span>, {{ work.date | date: "%Y" }}
    {% if work.emerged_from %}
    <br><em>Born from <a href="{{ work.emerged_from }}">Chamber examination</a></em>
    {% endif %}
  </p>
  {% if work.excerpt %}
  <blockquote class="canon-excerpt">{{ work.excerpt }}</blockquote>
  {% endif %}
</div>
{% endfor %}

<div class="ornament personal"></div>

<nav class="chamber-enfilade">
  <a href="/chamber/">Chamber</a>
  <span class="separator">·</span>
  <a href="/chamber/about/">About</a>
  <span class="separator">·</span>
  <a href="/chamber/canon/">Canon</a>
  <span class="separator">·</span>
  <a href="/chamber/deliberations/">Deliberations</a>
  <span class="separator">·</span>
  <a href="/chamber/voices/">Voices</a>
  <a href="/colophon/" class="back-to-about">Back to About pages</a>
</nav>