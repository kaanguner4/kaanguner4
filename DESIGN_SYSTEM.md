# Profile design system

## Direction

Recruiter-first, terminal-native, and evidence-led. The profile keeps its neon
engineering personality, but every screen should answer one of three questions:

1. Who is Kaan?
2. What can he contribute?
3. Where is the proof?

The page has exactly two numbered main sections. Contact is an unnumbered closing
step.

## Palette

- Canvas: `#080D17` → `#0C1320`
- Surface: `#0B111D` / `#0E1724`
- Line: `#1E293B` / `#2A3A4A`
- Text: `#EEF4FA` (bright) · `#94A3B8` (muted) · `#64748B` (dim)
- Cyan: `#38BDF8` / `#7DD3FC`
- Teal: `#34D399` / `#6EE7B7`
- Violet: `#A78BFA` / `#C4B5FD`
- Pink: `#F472B6` / `#F9A8D4`
- Amber: `#FBBF24` / `#FCD34D`

## Typography

- Display: Trebuchet MS / Verdana / sans-serif
- Technical detail: SFMono / Cascadia Code / JetBrains Mono / monospace
- Recruiter-critical positioning also appears as native text in `README.md`,
  so it remains searchable, selectable and readable if images do not load.

## Content hierarchy

```text
Hero
└── identity + role + outcome statement + build path

01 profile & contribution
├── concise native-text positioning statement
└── CV snapshot + three capability/evidence blocks

02 selected work
├── featured end-to-end project
├── four focused project cards
├── real GitHub activity generated daily
└── programming languages + technical toolkit + principles

Contact (unnumbered)
└── email + LinkedIn + GitHub
```

## Evidence rules

1. Projects appear before activity and tool lists.
2. Capability statements point to named project evidence.
3. Do not use illustrative streaks, commit totals, session logs, online states,
   or “last commit today” labels.
4. Time-sensitive activity must be generated from GitHub rather than hard-coded.
5. Project cards state the system, its useful behavior and its stack; they do not
   invent adoption numbers, performance metrics or production claims.
6. Every SVG has a descriptive `title` and `desc`; every README image has
   meaningful alt text unless it is purely decorative.

## Visual language

1. Dark canvas, quiet grid and restrained glow.
2. Cyan leads identity and data flow; pink marks selected work; teal marks real
   activity; violet marks the toolkit; amber marks contact.
3. Animation is ambient only: status pulses, moving dashed flow lines and slow
   background breathing.
4. Terminal metaphors support the message but never replace a clear heading.
5. Large type carries recruiter-critical information; smaller mono text is for
   technical proof.

## Repository structure

```text
README.md
DESIGN_SYSTEM.md
assets/
  hero.svg
  section-about.svg
  about.svg
  section-projects.svg
  project-water.svg
  project-car-price.svg
  project-nac.svg
  project-track-learner.svg
  project-auto-care.svg
  section-activity.svg
  activity-board.svg
  section-stack.svg
  tech-stack.svg
  principles.svg
  section-contact.svg
  divider.svg
  footer.svg
.github/
  workflows/
    contribution-snake.yml
```
