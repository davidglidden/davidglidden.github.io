---
title: "Recent Canon Additions"
permalink: /chamber/canon/recent/
layout: page
class: offering
---

## Recently Added Works

<p class="drop-cap">The latest works born from Chamber examinations, showing how the canon grows through dialogue.</p>

<div class="ornament philosophical"></div>

{% assign recent_canon = site.chamber_canon | sort: "date" | reverse | limit: 20 %}

{% for work in recent_canon %}
<div class="canon-entry recent">
  <h3><a href="{{ work.url }}"><em>{{ work.title }}</em>{{ work.marker }}</a></h3>
  <p class="canon-meta">
    <span class="small-caps">{{ work.author }}</span>, {{ work.date | date: "%Y" }}
    {% if work.emerged_from %}
    <br><em>Born from <a href="{{ work.emerged_from }}">Chamber examination</a></em>
    {% endif %}
  </p>
  {% if work.excerpt %}
  <blockquote class="canon-excerpt">{{ work.excerpt }}</blockquote>
  {% endif %}
  <div class="canon-tags">
    {% for tag in work.tags %}
    <span class="tag">{{ tag }}</span>
    {% endfor %}
  </div>
</div>
{% endfor %}

<div class="ornament personal"></div>

<p><a href="/chamber/canon/all/">Browse all {{ site.chamber_canon.size }} canon entries</a></p>

<nav class="chamber-enfilade">
  <a href="/chamber/">Chamber</a>
  <span class="separator">·</span>
  <a href="/chamber/about/">About</a>
  <span class="separator">·</span>
  <a href="/chamber/first-light/">First Light</a>
  <span class="separator">·</span>
  <a href="/chamber/canon/">Canon</a>
  <span class="separator">·</span>
  <a href="/chamber/deliberations/">Deliberations</a>
  <span class="separator">·</span>
  <a href="/chamber/voices/">Voices</a>
  <a href="/colophon/" class="back-to-about">Back to About pages</a>
</nav>