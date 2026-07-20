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
2. Keep the black origami crane, rose, and computer as the profile's signature visual motif.
3. Prefer rules, spacing, and alignment over badges or decorative cards.
4. Use motion as ambient background behavior, never as fast or flashing UI.
5. Keep project cards structurally identical and let the content create distinction.
6. Avoid external statistic services so the profile remains stable and factual.
7. Use local SVG assets with accessible titles and descriptions.
8. Pair the local animated marquee with a daily-generated, real contribution-grid animation.

## Content hierarchy

```text
Identity
Profile
Activity board
Selected projects
Languages & technologies
Contact
```

Each piece of information should appear once. The activity board shows present focus, the featured card owns the flagship-system detail, and the languages-and-technologies panel holds the complete working set.

## Repository structure

```text
README.md
DESIGN_SYSTEM.md
assets/
  hero.svg
  activity-board.svg
  divider.svg
  pipeline.svg
  tech-stack.svg
  project-car-price.svg
  project-track-learner.svg
  project-nac.svg
  project-auto-care.svg
  footer.svg
.github/
  workflows/
    contribution-snake.yml
```
