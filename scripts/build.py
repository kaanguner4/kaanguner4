#!/usr/bin/env python3
"""Generates every profile SVG in dark + light variants.

Run:  python3 scripts/build.py     (from the repo root)
Edit the CONTENT section below, re-run, commit.
"""
import os, random, textwrap
from xml.sax.saxutils import escape as esc

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
W = 880
SANS = "Inter,-apple-system,BlinkMacSystemFont,'Segoe UI','Helvetica Neue',Arial,sans-serif"
MONO = "ui-monospace,SFMono-Regular,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace"

THEMES = {
    "dark": dict(
        panel="#0b0c10", panel_bd="#1d2027", ink="#f1f3f6", muted="#9ca3af", dim="#7a808e",
        line="#22252d", card="#ffffff", card_op="0.025", card_bd="#23262e",
        chip_bg="#15171d", chip_bd="#262a33", chip_ink="#b0b6c3",
        ok_bg="#102218", ok_bd="#1d4a2e", ok_ink="#86efac",
        outline="#8b90a0", grad_a="#6b7080", grad_b="#e5e7eb",
        glow1="#5b3fa8", glow2="#2f4fa8", glow_op="0.38", px="#8b6cf0",
    ),
    "light": dict(
        panel="#fdfdfd", panel_bd="#e5e7eb", ink="#111111", muted="#4b5563", dim="#6b7280",
        line="#e5e7eb", card="#000000", card_op="0.012", card_bd="#e5e7eb",
        chip_bg="#f9fafb", chip_bd="#e5e7eb", chip_ink="#4b5563",
        ok_bg="#dcfce7", ok_bd="#bbf7d0", ok_ink="#166534",
        outline="#6b7280", grad_a="#aaaaaa", grad_b="#333333",
        glow1="#c9bdf2", glow2="#bccdf5", glow_op="0.55", px="#7c5ce0",
    ),
}

# ───────────────────────── CONTENT ─────────────────────────
ROLE = "KAAN GÜNER — SOFTWARE DEVELOPER & AI ENGINEER"
STATUS = "OPEN TO OPPORTUNITIES"

GLANCE = [
    ("FOCUS", "AI systems, end to end"),
    ("EDUCATION", "Computer Eng. · 01/2027"),
    ("RESEARCH", "TÜBİTAK 1002 · LDP for EEG"),
    ("BASE", "Antalya, Türkiye · UTC+3"),
]

EXPERIENCE = [
    ("Antalya Bilim University", "09/2026 — PRESENT", "STUDENT RESEARCHER · TÜBİTAK 1002",
     "Research on Local Differential Privacy for EEG data: how much utility each feature keeps, "
     "and how to choose the privacy budget (ε) per feature. Built the feature pipeline on the STEW "
     "workload dataset (48 participants, 22 EEG features) and delivered the utility stage as a "
     "reproducible 108-file package.",
     ["PYTHON", "SCIKIT-LEARN", "SCIPY", "LIGHTGBM"]),
    ("Enelsa", "06/2026 — 07/2026", "MACHINE LEARNING ENGINEER INTERN · R&D / IOT TEAM",
     "Designed and built, alone and end to end, the Water Anomaly Detection System for an industrial "
     "water treatment line, and took it live as an MVP with a real-time monitoring dashboard. Rare "
     "critical events had too little data for automated alerts, so that part moved to explainable "
     "rules and the limit was documented in the final report.",
     ["PYTHON", "LIGHTGBM", "XGBOOST", "FASTAPI", "POSTGRESQL", "REDIS", "DOCKER"]),
    ("i2i Systems", "06/2025 — 07/2025", "COMPUTER ENGINEER INTERN",
     "Built working components on 6 enterprise platforms in the intern engineering program: a "
     "Java/JDBC data loader, a 10,000-object Hazelcast map and a 5-endpoint REST API with Selenium "
     "end-to-end tests. Tested the team's telecom Online Charging System.",
     ["JAVA", "SPRING BOOT", "ORACLE XE", "VOLTDB", "HAZELCAST", "KAFKA", "SELENIUM"]),
    ("Masomo Gaming", "08/2024 — 10/2024", "GAME DEVELOPER INTERN",
     "Learned Unity and C# from zero and shipped 2 games: a 2D action platformer with 20 scripts "
     "across 6 systems, and JustDrift, a 3D mobile driving game with an online REST leaderboard.",
     ["UNITY", "C#", "REST API"]),
]
EDUCATION = ("Antalya Bilim University", "2022 — 01/2027 (EXPECTED)",
             "B.SC. COMPUTER ENGINEERING · GPA 3.13 / 4.00")

# file, category, status, ok?, title, description, chips, footer label, github?
PROJECTS = [
    ("project-sqlbuddy", "LLM · SAAS · GRADUATION PROJECT", "IN DEVELOPMENT", False, "SQLBuddy",
     "Text-to-SQL for non-technical teams, in Turkish or English. A multi-LLM router writes the SQL, "
     "and authorization is code, not a prompt. 2,600+ automated tests.",
     ["FASTAPI", "POSTGRESQL", "REDIS", "REACT", "TYPESCRIPT", "DOCKER"], "CODE PRIVATE", False),
    ("project-water", "INDUSTRIAL IOT · HYBRID ML AND RULES", "LIVE MVP AT ENELSA", True,
     "Water Anomaly Detection System",
     "Monitors an industrial water treatment line in real time: 5 sensor channels, about 60,000 "
     "records over 9 months. Per-channel tree models, explainable rules for the critical class and "
     "a model registry with hot-swap. 79.6% on an independent, human-labeled test set.",
     ["PYTHON", "LIGHTGBM", "XGBOOST", "SCIKIT-LEARN", "FASTAPI", "POSTGRESQL", "REDIS"], "PROPRIETARY", False),
    ("project-claude-island", "MACOS · OPEN SOURCE", "V0.9.0 · 10+ USERS", True, "Claude Island",
     "Native Swift app that turns Claude Code hook events into Dynamic Island style cards. "
     "Answer permission prompts from the card, even with many sessions in parallel.",
     ["SWIFT", "SWIFTUI", "APPKIT"], "VIEW ON GITHUB", True),
    ("project-ruvin", "CAFÉ OPERATIONS · INVOICE AND STOCK TRACKING", "LIVE IN PRODUCTION", True, "Ruvin Coffee",
     "Invoice and stock tracking system for a working café, with Supabase (PostgreSQL) as the "
     "backend database. Runs live in daily operations.",
     ["SUPABASE", "POSTGRESQL"], "CODE PRIVATE", False),
    ("project-tracklearner", "NEUROEVOLUTION · SIMULATION", "SHIPPED", False, "TrackLearnerAI",
     "60 cars learn to drive over up to 150 generations with NEAT. A 5-beam radar feeds a network "
     "that evolves its own topology, shown live at 60 FPS.",
     ["PYTHON", "NEAT", "OPENCV"], "VIEW ON GITHUB", True),
    ("project-nac", "NETWORK SECURITY · AAA", "SHIPPED", False, "NAC System",
     "RADIUS access control on 4 Docker services. FreeRADIUS sends every decision to a FastAPI "
     "policy engine: PAP and MAC authentication, VLAN assignment and rate limiting.",
     ["FREERADIUS", "FASTAPI", "POSTGRESQL", "REDIS", "DOCKER"], "VIEW ON GITHUB", True),
    ("project-car-tag", "WEB · REAL-TIME MULTIPLAYER", "LIVE ON GUNERKAAN.COM", True, "Car Tag Arena",
     "Real-time multiplayer browser game for 2 to 6 players over WebSockets, running on "
     "Cloudflare Workers and Durable Objects.",
     ["WEBSOCKETS", "CLOUDFLARE WORKERS", "DURABLE OBJECTS"], "VIEW ON GITHUB", True),
]

TOOLKIT = [
    ("PROGRAMMING", ["PYTHON", "SQL", "JAVA", "C / C++", "C#", "TYPESCRIPT", "SWIFT"]),
    ("MACHINE LEARNING", ["SCIKIT-LEARN", "LIGHTGBM", "XGBOOST", "PANDAS", "NUMPY", "SCIPY",
                          "ANOMALY DETECTION", "TIME-SERIES", "NEAT"]),
    ("RESEARCH", ["STATISTICAL TESTING", "DIFFERENTIAL PRIVACY", "TOPSIS", "MNE-PYTHON",
                  "REPRODUCIBLE PIPELINES"]),
    ("LLM ENGINEERING", ["MULTI-MODEL ROUTING", "LLM EVALUATION", "TEXT-TO-SQL", "GROQ", "GEMINI",
                         "CLAUDE API", "CLAUDE CODE", "CODEX"]),
    ("BACKEND & INFRA", ["FASTAPI", "SQLALCHEMY", "POSTGRESQL", "REDIS", "WEBSOCKETS", "JWT · RBAC",
                         "DOCKER", "GITHUB ACTIONS", "LINUX", "CLOUDFLARE WORKERS", "SUPABASE"]),
    ("TESTING", ["PYTEST", "SELENIUM", "INTEGRATION & E2E", "CI COVERAGE GATES"]),
]

SECTIONS = [("section-about", "01", "ABOUT"), ("section-experience", "02", "EXPERIENCE"),
            ("section-work", "03", "SELECTED WORK"), ("section-toolkit", "04", "TOOLKIT"),
            ("section-activity", "05", "ACTIVITY")]

# ───────────────────────── HELPERS ─────────────────────────
CH_FS, CH_LS, CH_H, CH_PAD = 10.5, 0.9, 24, 11


def mono_w(s, fs=CH_FS, ls=CH_LS):
    return len(s) * (fs * 0.6 + ls)


def chip(x, y, label, t, ok=False, dot=False):
    w = mono_w(label) + CH_PAD * 2 - CH_LS + (12 if dot else 0)
    bg, bd, ink = (t["ok_bg"], t["ok_bd"], t["ok_ink"]) if ok else (t["chip_bg"], t["chip_bd"], t["chip_ink"])
    tx = x + CH_PAD + (12 if dot else 0)
    d = (f'<circle class="pulse" cx="{x + CH_PAD + 3:.1f}" cy="{y + CH_H / 2}" r="3" fill="{ink}"/>' if dot else "")
    return (f'<rect x="{x:.1f}" y="{y}" width="{w:.1f}" height="{CH_H}" rx="{CH_H / 2}" fill="{bg}" stroke="{bd}"/>'
            f'{d}<text x="{tx:.1f}" y="{y + 16}" class="m" fill="{ink}" font-size="{CH_FS}" '
            f'letter-spacing="{CH_LS}">{esc(label)}</text>'), w


def chip_row(x, y, labels, t, max_x=W, gap=7, row_gap=8):
    out, cx, cy = [], x, y
    for lb in labels:
        w = mono_w(lb) + CH_PAD * 2 - CH_LS
        if cx + w > max_x and cx > x:
            cx, cy = x, cy + CH_H + row_gap
        s, w = chip(cx, cy, lb, t)
        out.append(s)
        cx += w + gap
    return "".join(out), cy + CH_H


def arrow(x, y, color, s=8):
    return (f'<path d="M{x} {y + s}L{x + s} {y}M{x + 2} {y}H{x + s}V{y + s - 2}" fill="none" '
            f'stroke="{color}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>')


def para(x, y, text, t, width, fs=14, lh=22, color=None):
    lines = textwrap.wrap(text, width)
    out = "".join(f'<text x="{x}" y="{y + i * lh}" font-size="{fs}" fill="{color or t["muted"]}">{esc(l)}</text>'
                  for i, l in enumerate(lines))
    return out, y + (len(lines) - 1) * lh


def svg(h, body, title, desc, extra_defs=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}" '
            f'role="img" aria-labelledby="t d"><title id="t">{esc(title)}</title><desc id="d">{esc(desc)}</desc>'
            f'<defs><style>text{{font-family:{SANS}}}.m{{font-family:{MONO};font-weight:500}}'
            f'.pulse{{animation:p 2.4s ease-in-out infinite}}@keyframes p{{50%{{opacity:.35}}}}'
            f'@media (prefers-reduced-motion:reduce){{.pulse{{animation:none}}}}</style>{extra_defs}</defs>'
            f'{body}</svg>\n')


# ───────────────────────── COMPONENTS ─────────────────────────
def hero(t):
    h = 404
    rnd = random.Random(7)
    px = "".join(
        f'<rect x="{360 + rnd.randrange(0, 34) * 15}" y="{40 + rnd.randrange(0, 22) * 15}" width="9" height="9" '
        f'rx="1.5" fill="{t["px"]}" opacity="{rnd.choice([0.05, 0.08, 0.12, 0.2])}"/>' for _ in range(46))
    defs = (f'<clipPath id="c"><rect width="{W}" height="{h}" rx="22"/></clipPath>'
            f'<radialGradient id="g1"><stop offset="0" stop-color="{t["glow1"]}" stop-opacity="{t["glow_op"]}"/>'
            f'<stop offset="1" stop-color="{t["glow1"]}" stop-opacity="0"/></radialGradient>'
            f'<radialGradient id="g2"><stop offset="0" stop-color="{t["glow2"]}" stop-opacity="{t["glow_op"]}"/>'
            f'<stop offset="1" stop-color="{t["glow2"]}" stop-opacity="0"/></radialGradient>'
            f'<linearGradient id="tg" x1="0" x2="1"><stop offset="0" stop-color="{t["grad_a"]}"/>'
            f'<stop offset="1" stop-color="{t["grad_b"]}"/></linearGradient>')
    st, _ = chip(48 + mono_w(ROLE, 11, 1.4) + 14, 44, STATUS, t, ok=True, dot=True)
    big = 'font-size="80" font-weight="800" letter-spacing="-3.6"'
    body = (f'<g clip-path="url(#c)"><rect width="{W}" height="{h}" fill="{t["panel"]}"/>'
            f'<circle cx="90" cy="20" r="330" fill="url(#g1)"/><circle cx="800" cy="330" r="300" fill="url(#g2)"/>'
            f'{px}</g><rect x=".5" y=".5" width="{W - 1}" height="{h - 1}" rx="22" fill="none" stroke="{t["panel_bd"]}"/>'
            f'<text x="48" y="60" class="m" font-size="11" letter-spacing="1.4" fill="{t["muted"]}">{esc(ROLE)}</text>{st}'
            f'<text x="44" y="168" {big} fill="{t["ink"]}">BUILDING <tspan fill="url(#tg)">AI</tspan></text>'
            f'<text x="44" y="252" {big} fill="{t["ink"]}">THAT SHIPS TO</text>'
            f'<text x="44" y="336" {big} fill="none" stroke="{t["outline"]}" stroke-width="1.4">PRODUCTION.</text>'
            f'<text x="48" y="374" class="m" font-size="11" letter-spacing="1.4" fill="{t["dim"]}">'
            f'STUDENT RESEARCHER · ANTALYA, TÜRKİYE · GUNERKAAN.COM</text>')
    return svg(h, body, "Kaan Güner — Software Developer and AI Engineer",
               "Building AI that ships to production. Student researcher, open to opportunities.", defs)


def section(num, name, t):
    label = f"{num} / {name}"
    x2 = mono_w(label, 12, 1.8) + 18
    body = (f'<text x="0" y="30" class="m" font-size="12" letter-spacing="1.8" fill="{t["ink"]}">'
            f'<tspan fill="{t["dim"]}">{num} /</tspan> {esc(name)}</text>'
            f'<line x1="{x2:.0f}" y1="26" x2="{W}" y2="26" stroke="{t["line"]}"/>')
    return svg(48, body, f"Section {num}: {name.title()}", name.title())


def glance(t):
    col = W / len(GLANCE)
    body = f'<line x1="0" y1=".5" x2="{W}" y2=".5" stroke="{t["line"]}"/><line x1="0" y1="83.5" x2="{W}" y2="83.5" stroke="{t["line"]}"/>'
    for i, (k, v) in enumerate(GLANCE):
        x = i * col + (0 if i == 0 else 18)
        if i:
            body += f'<line x1="{i * col:.0f}" y1="18" x2="{i * col:.0f}" y2="66" stroke="{t["line"]}"/>'
        body += (f'<text x="{x:.0f}" y="34" class="m" font-size="10.5" letter-spacing="1.4" fill="{t["dim"]}">{k}</text>'
                 f'<text x="{x:.0f}" y="58" font-size="14" font-weight="600" fill="{t["ink"]}">{esc(v)}</text>')
    return svg(84, body, "At a glance", "; ".join(f"{k.title()}: {v}" for k, v in GLANCE))


def experience(t):
    y, body, LX, RX = 0, "", 0, 250
    for i, (org, date, role, text, chips) in enumerate(EXPERIENCE):
        if i:
            body += f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="{t["line"]}"/>'
        top = y + 30
        body += (f'<text x="{LX}" y="{top + 4}" font-size="19" font-weight="700" letter-spacing="-.3" fill="{t["ink"]}">{esc(org)}</text>'
                 f'<text x="{LX}" y="{top + 28}" class="m" font-size="10.5" letter-spacing="1.2" fill="{t["dim"]}">{date}</text>'
                 f'<text x="{RX}" y="{top}" class="m" font-size="10.5" letter-spacing="1.3" fill="{t["ink"]}">{esc(role)}</text>')
        p, py = para(RX, top + 26, text, t, 84)
        c, cy = chip_row(RX, py + 16, chips, t)
        body += p + c
        y = cy + 26
    org, date, role = EDUCATION
    body += (f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="{t["line"]}"/>'
             f'<text x="{LX}" y="{y + 34}" font-size="19" font-weight="700" letter-spacing="-.3" fill="{t["ink"]}">{esc(org)}</text>'
             f'<text x="{LX}" y="{y + 58}" class="m" font-size="10.5" letter-spacing="1.2" fill="{t["dim"]}">{date}</text>'
             f'<text x="{RX}" y="{y + 30}" class="m" font-size="10.5" letter-spacing="1.3" fill="{t["ink"]}">{esc(role)}</text>'
             f'<text x="{RX}" y="{y + 56}" font-size="14" fill="{t["muted"]}">Graduation project: SQLBuddy. Research project: EEG face perception with MNE-Python.</text>')
    y += 78
    return svg(y, body, "Experience and education",
               " ".join(f"{role.title()} at {org}, {date}. {text}" for org, date, role, text, _ in EXPERIENCE))


def project(idx, p, t):
    _, cat, status, ok, title, text, chips, foot, gh = p
    body = ""
    sw = mono_w(status) + CH_PAD * 2 - CH_LS
    s, _ = chip(W - 28 - sw, 22, status, t, ok=ok)
    body += (f'<text x="28" y="39" class="m" font-size="10.5" letter-spacing="1.4" fill="{t["dim"]}">'
             f'{idx:02d} / {esc(cat)}</text>{s}'
             f'<text x="28" y="80" font-size="25" font-weight="700" letter-spacing="-.6" fill="{t["ink"]}">{esc(title)}</text>')
    ptxt, py = para(28, 108, text, t, 108)
    fw = mono_w(foot, 10.5, 1.4) + (16 if gh else 0)
    c, cy = chip_row(28, py + 18, chips, t, max_x=W - 28 - fw - 20)
    fx = W - 28 - fw
    body += ptxt + c + (f'<text x="{fx:.1f}" y="{cy - 8}" class="m" font-size="10.5" letter-spacing="1.4" '
                        f'fill="{t["ink"] if gh else t["dim"]}">{foot}</text>')
    if gh:
        body += arrow(W - 28 - 9, cy - 17, t["ink"])
    h = cy + 24
    frame = (f'<rect x=".5" y=".5" width="{W - 1}" height="{h - 1}" rx="16" fill="{t["card"]}" fill-opacity="{t["card_op"]}" '
             f'stroke="{t["card_bd"]}"/>')
    return svg(h, frame + body, f"{title} — {cat.title()}", f"{text} Status: {status.title()}.")


def toolkit(t):
    y, body = 0, ""
    for i, (label, items) in enumerate(TOOLKIT):
        if i:
            body += f'<line x1="0" y1="{y}" x2="{W}" y2="{y}" stroke="{t["line"]}"/>'
        body += f'<text x="0" y="{y + 34}" class="m" font-size="10.5" letter-spacing="1.4" fill="{t["dim"]}">{esc(label)}</text>'
        c, cy = chip_row(250, y + 18, items, t)
        body += c
        y = cy + 18
    return svg(y, body, "Toolkit", ". ".join(f"{k.title()}: {', '.join(v)}" for k, v in TOOLKIT))


def contact(t):
    big = 'font-size="68" font-weight="800" letter-spacing="-3"'
    body = (f'<text x="0" y="78" {big} fill="{t["ink"]}">LET’S BUILD</text>'
            f'<text x="0" y="150" {big} fill="none" stroke="{t["outline"]}" stroke-width="1.3">TOGETHER.</text>')
    return svg(172, body, "Let's build together", "Internships, projects, or a good engineering conversation.")


# ───────────────────────── BUILD ─────────────────────────
def main():
    for name, t in THEMES.items():
        out = os.path.join(ROOT, "assets", name)
        os.makedirs(out, exist_ok=True)
        files = {"hero": hero(t), "glance": glance(t), "experience": experience(t),
                 "toolkit": toolkit(t), "contact": contact(t)}
        for f, num, label in SECTIONS:
            files[f] = section(num, label, t)
        for i, p in enumerate(PROJECTS, 1):
            files[p[0]] = project(i, p, t)
        for f, s in files.items():
            with open(os.path.join(out, f + ".svg"), "w", encoding="utf-8") as fh:
                fh.write(s)
    print("built", len(files), "svgs x", len(THEMES), "themes")


if __name__ == "__main__":
    main()
