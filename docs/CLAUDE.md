# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Essential Commands

### Development
```bash
bundle exec jekyll serve       # Start local development server at http://localhost:4000
bundle exec jekyll build       # Build site for production to _site/
bundle install                 # Install Ruby dependencies from Gemfile
```

### Git Workflow
The site is deployed via GitHub Pages on the `master` branch. Any commits to master will automatically deploy.

## Architecture Overview

This is David Glidden's personal website built with Jekyll 3.8.3, featuring a thoughtfully crafted typography system and content focused on music, pedagogy, and philosophy.

### Core Structure
- **Theme**: Modified Klisé theme with extensive customizations
- **Content Management**: Posts use jekyll-postfiles plugin allowing organized post assets in subdirectories
- **Typography**: Custom font stack (EB Garamond, IBM Plex Sans/Mono) with sophisticated SCSS utilities
- **Deployment**: GitHub Pages from master branch

### Key Directories
- `_posts/`: Blog posts with many containing photography and location-based titles
- `_sass/klise/`: Custom SCSS modules for the theme
- `assets/img/`: Image assets for posts
- `fonts/`: Self-hosted web fonts (EB Garamond, IBM Plex families)

### Jekyll Plugins in Use
- jekyll-postfiles: Allows organizing post-specific assets in subdirectories
- jekyll-seo-tag: SEO optimization
- jekyll-compress-html: HTML compression for production
- jekyll-paginate-v2: Pagination support
- jekyll-sitemap: Sitemap generation
- jekyll-feed: RSS feed generation

### Writing Workflow
- Posts are written in Markdown using iA Writer
- Images are stored in `assets/img/` with consistent naming convention
- Post files can have associated directories for multi-asset posts (using jekyll-postfiles)

### Typography System
The site implements a sophisticated typography system with:
- Base font size: 20px, line height: 1.6
- Custom utility classes for typographic variation (.small-caps, .oldstyle, .ligatures, etc.)
- True small caps support via EB Garamond SC

## Important Notes

1. **No Build Scripts**: This is a pure Jekyll setup without Node.js tooling
2. **Direct Deployment**: Changes to master branch auto-deploy to GitHub Pages
3. **Image Organization**: Many posts are photo essays; maintain consistent image naming
4. **Typography Focus**: The site prioritizes readability and typographic excellence
5. **Content Philosophy**: Site embodies "Animal Rationis Capax" - focused on art, work, and becoming