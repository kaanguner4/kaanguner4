# Profile design system

Minimal, monochrome, typography-first. Mirrors [gunerkaan.com](https://gunerkaan.com).

## Rules

1. One accent only: green, for "live" and "open" status chips. Everything else is ink, grey and hairlines.
2. Big uppercase headlines (weight 800, tight tracking), with one outlined word.
3. Small mono caps for labels, dates and chips.
4. Numbered sections: `01 / ABOUT`, `02 / EXPERIENCE`, `03 / SELECTED WORK`, `04 / TOOLKIT`, `05 / ACTIVITY`.
5. No decoration outside the hero. Only the hero has a panel, a glow and the pixel field.
6. Content follows the CV. No numbers that are not in the CV.

## Tokens

| | Dark | Light |
|---|---|---|
| Hero panel | `#0b0c10` | `#fdfdfd` |
| Ink | `#f1f3f6` | `#111111` |
| Muted | `#9ca3af` | `#4b5563` |
| Dim | `#7a808e` | `#6b7280` |
| Line | `#22252d` | `#e5e7eb` |
| Chip | `#15171d` / `#262a33` | `#f9fafb` / `#e5e7eb` |
| OK | `#86efac` | `#166534` |

Fonts: Inter with system sans fallback; system mono for labels.

## How to update

All text lives in the CONTENT block of `scripts/build.py`.

```bash
python3 scripts/build.py   # rewrites assets/dark and assets/light
```

`README.md` picks the theme with `<picture>` and `prefers-color-scheme`.
About text, links and contact are native Markdown so they stay selectable.
