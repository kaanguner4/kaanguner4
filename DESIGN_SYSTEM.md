# Profile design system

## Direction

Quiet, editorial, and technically precise. The profile should feel considered before it feels decorative.

## Palette

- Canvas: `#F4F1EA`
- Surface: `#F8F6F1`
- Ink: `#191815`
- Secondary ink: `#393630`
- Muted: `#746F66`
- Line: `#D7D1C6`
- Accent: `#7D6C5D`
- Dark surface: `#1B1A18`

## Typography

- Display: Georgia / system serif
- Interface: SFMono / Cascadia Code / monospace
- Body: Inter / Segoe UI / Arial / sans-serif

## Visual language

1. Use warm neutrals and graphite; reserve the accent for small navigational details.
2. Use one quiet fold motif instead of literal origami illustrations.
3. Prefer rules, spacing, and alignment over badges or decorative cards.
4. Keep all motion out of the profile header.
5. Keep project cards structurally identical and let the content create distinction.
6. Avoid external statistic services so the profile remains stable and factual.
7. Use local SVG assets with accessible titles and descriptions.

## Content hierarchy

```text
Identity
Profile
Current work
Selected work
Engineering practice
Contact
```

Each piece of information should appear once. Technology lists belong in the engineering-practice panel; project cards only show the tools relevant to that project.

## Repository structure

```text
README.md
DESIGN_SYSTEM.md
assets/
  hero.svg
  divider.svg
  pipeline.svg
  tech-stack.svg
  project-car-price.svg
  project-track-learner.svg
  project-nac.svg
  project-auto-care.svg
  footer.svg
```
