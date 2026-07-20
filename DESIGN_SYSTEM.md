# Profile design system

## Direction

Playful, high-energy, and terminal-native. The profile should feel like a neon arcade dashboard: dark canvas, glowing accents, ambient motion, and a bit of humor. Fun first — but still readable and factual.

## Palette

- Canvas: `#0A0E1A` → `#121026` (dark gradient)
- Surface: `#0B0F1A` / `#111827`
- Panel: `#0E1422`
- Line: `#1E293B`
- Text: `#ECFEFF` (bright) · `#94A3B8` (muted) · `#64748B` (dim)
- Neon cyan: `#22D3EE` / `#5EEAD4` / `#67E8F9`
- Neon violet: `#A78BFA` / `#C4B5FD`
- Neon pink: `#F472B6` / `#F9A8D4`
- Neon lime: `#A3E635` / `#BEF264`
- Neon amber: `#FBBF24` / `#FCD34D`

## Typography

- Display: Trebuchet MS / Verdana / sans-serif (bold, glowing headings)
- Mono: SFMono / Cascadia Code / JetBrains Code — the dominant voice (terminal feel)

## Visual language

1. Dark canvas with a subtle scrolling grid; reserve bright neon for accents and glows.
2. Each section owns one accent color (cyan → lime → pink → violet → amber).
3. Use `feGaussianBlur` glow filters sparingly on headings, stat numbers and status dots.
4. Motion is ambient: scanlines, blinking cursors, pulsing dots, drifting blobs, an equaliser — never fast or seizure-inducing.
5. Terminal metaphors everywhere: window dots, `~/path` labels, `$ command`, blinking cursors, `session.log`.
6. Emoji are welcome as small accents (🔥 ⚡ 🚀 🧠) — one per idea, not confetti.
7. All visuals are self-contained local SVGs with accessible `<title>`/`<desc>`.
8. The daily contribution snake mirrors the palette (cyan light / pink dark).

## Content hierarchy

```text
Hero (identity + status chips)
01 whoami    — terminal "about me" card
02 activity  — dashboard: streak, commits, grid, session log + real snake
03 projects  — flagship banner + 2×2 project cards with short summaries
04 stack     — languages/tech grid + principles ribbon
05 contact   — links
Footer
```

Each fact appears once. Project cards share one structure; content creates the distinction. Stats on the activity board are illustrative — swap for real numbers anytime.

## Repository structure

```text
README.md
DESIGN_SYSTEM.md
assets/
  hero.svg
  section-about.svg  section-activity.svg  section-projects.svg  section-stack.svg  section-contact.svg
  about.svg
  activity-board.svg
  project-water.svg  project-car-price.svg  project-track-learner.svg  project-nac.svg  project-auto-care.svg
  tech-stack.svg
  principles.svg
  divider.svg
  footer.svg
.github/
  workflows/
    contribution-snake.yml
```
