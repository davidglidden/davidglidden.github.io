# ADR-003: Gray Source Markers Over Colored Notation System

**Date**: 2024-12-15  
**Status**: Accepted  
**Supersedes**: N/A

## Context

The Chamber's fictional bibliography requires visual notation to distinguish different types of sources:
- °, ~, †, §, ∞, ◊ for different fictional work categories
- Need for visual distinction without overwhelming the typography
- Integration with existing Animal Rationis Capax design system
- Balance between functionality and aesthetic coherence

Initial design included colored markers (red, blue, etc.) to enhance categorical distinction, but this raised concerns about visual consistency with the site's established minimal color palette.

## Decision

**Use gray source markers (#6b7886) exclusively instead of color-coded notation system.**

All fictional work source markers (°, ~, †, §, ∞, ◊) use the existing gray color from the site's design system rather than introducing new colors for categorical distinction.

## Consequences

### Positive
- **Visual consistency**: Maintains site's minimal, contemplative design philosophy
- **Typography focus**: Keeps attention on content rather than notation system
- **Accessibility**: No color-dependent information encoding
- **Design coherence**: Uses established color vocabulary rather than expanding it
- **Subtle integration**: Source markers provide information without dominating text

### Negative
- **Reduced categorical distinction**: Harder to quickly identify source types at a glance
- **Learning curve**: Users must memorize symbol meanings rather than relying on color cues
- **Potential confusion**: Similar symbols in gray may be harder to distinguish

### Neutral
- **Symbol system priority**: Places meaning in symbol choice rather than color choice
- **Scalability**: System can grow without color palette expansion
- **Print compatibility**: Works equally well in digital and print formats

## Alternatives Considered

### **Full Color-Coded System**
*Rejected*: Would break visual consistency with site's minimal aesthetic approach

**Proposed scheme**:
- ° Red for pure inventions
- ~ Blue for hybrid works  
- † Brown for contested attributions
- § Green for chamber-generated
- ∞ Purple for hermetic sources
- ◊ Orange for marginalia

*Rejection reasoning*: Animal Rationis Capax uses color sparingly (red accent only), and this would introduce visual noise inconsistent with contemplative reading focus.

### **Subtle Color Variations**
*Rejected*: Would require users to distinguish between similar gray tones

### **No Visual Distinction**
*Rejected*: Would lose categorical information entirely

### **Typography-Based Distinction**
*Rejected*: Would require different fonts or weights, creating visual hierarchy issues

## Implementation Details

- **Color value**: #6b7886 (existing gray from design system)
- **CSS class**: `.source-marker` with shared styling
- **Hover behavior**: Tooltips or other interaction to provide categorical information
- **Future enhancement**: Possible categorical organization on canon index pages

## Design Philosophy Alignment

This decision reflects core site values:
- **Contemplative reading**: Visual elements support rather than distract from content
- **Typographic primacy**: Text and its meaning take precedence over visual decoration
- **Minimal intervention**: Design serves content without drawing attention to itself
- **Consistency**: Every design choice reflects established site philosophy

## User Experience Considerations

- **Learning curve**: Users develop familiarity with symbol meanings through use
- **Contextual help**: Canon index and other pages provide symbol legend/explanation
- **Progressive disclosure**: Symbol meaning revealed when relevant rather than always visible
- **Cognitive load**: Single color reduces visual processing while preserving information

## Future Considerations

- **Symbol evolution**: May add new markers as fictional categories develop
- **Interaction design**: Hover states, tooltips, or other feedback to aid comprehension
- **Print versions**: Gray markers work across all output formats
- **Accessibility**: Ensure symbol meanings available through non-visual means

## Technical Implementation

```scss
.source-marker {
  vertical-align: super;
  font-size: 0.8em;
  color: #6b7886; // Existing gray from design system
  cursor: help;
  font-family: $serif-family;
  margin-left: 0.1em;
}
```

## Validation Through Use

First Chamber session (Khunrath owl emblem) validated this approach:
- Gray markers integrated seamlessly with text flow
- No visual distraction from content
- Categorical information preserved through symbol choice
- Consistent with site's contemplative design philosophy

## References

- Site color system: [Typography Guide](../typography-guide.md)
- First implementation: [Owl emblem deliberation](/chamber/deliberations/standard/2024-12-28-owl-emblem/)
- CSS implementation: `_sass/klise/_utilities.scss`