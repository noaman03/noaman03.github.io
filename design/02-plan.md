# 02 — Design plan

Built from `design/01-audit.md`. Every fact quoted here already exists in `src/data/projects.ts`,
`src/data/profile.ts`, `strong8k-brief.md` or the public CV; nothing new is invented.

---

## 1. Subject

This is the site of someone who writes software for **screens people watch from a distance** —
a phone held sideways, a ten-inch tablet, a TV box driven by a remote from across a room, a
Windows desktop. The flagship is Strong 8K: a gold-on-black television application that went
from an empty repository to Google Play and the Microsoft Store in three months, carrying 73,576
lines of Dart, 51 screens and 2,603 passing tests, written by one person in Alexandria who also
stood up the Ubuntu box, the nginx vhosts and the build driver that produces fifteen brands from
one codebase. The interesting thing about him is not that he "crafts digital experiences"; it is
that he can tell you why a 403 from a streaming host means two different things, and what he did
about it.

So the site should look like what it is about: **black screens, read at distance, in a room.**
Big quiet type, a lot of air, one warm ink taken from the product, and the real screenshots given
the full width they were exported at. Not "developer portfolio" as a genre.

### The one memorable thing — the device ladder

> **Two black wells carrying real screenshots, side by side at true relative scale: the phone
> capture at 16:9 and the ten-inch tablet capture at 16:10, sharing a baseline, with the scale
> relationship between them preserved exactly.**

It is one composed object, not a picture — the point is the _relationship_ between the two, and
the relationship is the claim: the same Flutter codebase, drawn for two different screen shapes.
It replaces the hero code-window mock, which was a drawing of a file that does not exist.

**What the evidence actually supports, and the constraint that follows.** Of the nine approved
screenshots, six are phone landscape at 1200×675 (16:9) and three are ten-inch tablet at 1200×750
(16:10). **There is no Android TV capture and no Windows capture.** So the ladder has two wells,
not four. Android TV and Windows are stated in words on the rule beneath it — they are in
`projects.ts:92` as platforms, and the brief evidences both — but they are never drawn as frames
with someone else's screenshot inside. An empty outlined well labelled "TV" would read as a
missing image; a phone capture in a TV frame would be a lie. Two honest wells beat four dishonest
ones, and the aspect-ratio difference between them is the real evidence anyway.

```
desktop ≥768px — side by side, shared baseline, true relative scale

   ┌────────────────┐     ┌──────────────────────────┐
   │ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓ │     │ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ │
   │ ▓   phone    ▓ │     │ ▓    ten-inch tablet   ▓ │
   └────────────────┘     └──────────────────────────┘
    16:9                   16:10                        ← tablet ≈1.55× wider
   ──────────────────────────────────────────────────   ← gold hairline
    One Flutter codebase. Also ships to Android TV and Windows.

phone <768px — stacked, tablet first at full width, phone below at 62%,
left-aligned, so the size relationship survives the stack

   ┌──────────────────────────┐
   │ ▓   ten-inch tablet    ▓ │
   └──────────────────────────┘
   ┌───────────────┐
   │ ▓   phone   ▓ │
   └───────────────┘
   ───────────────────────────
   One Flutter codebase. Also
   ships to Android TV and Windows.
```

Everything else on the site gets quieter so the ladder lands. The wells are the only black
surfaces in the light theme and the only objects with no radius at all.

**Decisions taken by Ahmed, 2026-10-19:** this visual idea over the full-bleed band and over the
two alternatives offered (a moving D-pad selection; a full-viewport type poster); the DevOps
skills group **is** split into shipped versus diploma (§8.1); the hero sentence **is** used as
written (§8.3).

---

## 2. Palette

Six roles. The gold is taken from the Strong 8K icon and wordmark (`public/assets/projects/
strong-8k/thumbnail.webp`) and is used as **ink** — hairlines, small numerals, the focus ring —
never as a glow, a gradient or a fill. There are no gradients, no washes and no shadows in this
design; separation is done with rules and space.

| Token         | Light     | Dark      | Role                                                                                  |
| ------------- | --------- | --------- | ------------------------------------------------------------------------------------- |
| `--ground`    | `#F3F2EF` | `#0D0C0A` | page. Warm neutral, not cream and not blue-black                                      |
| `--ink`       | `#17150F` | `#EDEBE4` | body and headlines                                                                    |
| `--ink-quiet` | `#5C584C` | `#A8A294` | captions, row meta, secondary prose                                                   |
| `--rule`      | `#D6D2C7` | `#2E2A22` | hairlines, borders, table rules                                                       |
| `--gold`      | `#8A6512` | `#D7A33F` | accent ink: the rule beside shipped work, the focus ring, link underlines             |
| `--screen`    | `#0B0A08` | `#0B0A08` | **the same in both themes** — every media well is black, because a screen is a screen |

`--screen` being theme-independent is the idea that holds the whole thing together: the
gold-on-black screenshots always sit on black, so they never look orphaned on paper, and the
light theme gets its structure from black bands rather than from more boxes.

**Contrast, measured:**

| Pair                   | Ratio        | Verdict                |
| ---------------------- | ------------ | ---------------------- |
| `#17150F` on `#F3F2EF` | 16.3 : 1     | AAA                    |
| `#5C584C` on `#F3F2EF` | 7.5 : 1      | AAA                    |
| `#8A6512` on `#F3F2EF` | **4.70 : 1** | AA for text, AA for UI |
| `#EDEBE4` on `#0D0C0A` | 16.9 : 1     | AAA                    |
| `#A8A294` on `#0D0C0A` | 7.7 : 1      | AAA                    |
| `#D7A33F` on `#0D0C0A` | **8.58 : 1** | AAA                    |

Gold on light paper is the tightest pair at 4.70:1, so it is never used below 15px and never for
long prose — only for rules, the focus ring, link underlines and short labels.

Both themes ship as `@media (prefers-color-scheme)` blocks **as well as** `html[data-theme]`
overrides, so the site respects the system setting with JavaScript disabled. Today it does not
(`BaseLayout.astro:58-70` is the only thing choosing a theme).

---

## 3. Type

### One family: Archivo, self-hosted, variable

Archivo (Omnibus-Type, SIL OFL) was drawn for **highlights, headlines and signage** — type meant
to be read quickly from further away than a book. That is the literal subject of this site. Its
expanded widths give a display voice with real presence without reaching for a second typeface,
and its text widths are a plain, high-x-height grotesque that stays quiet under long prose.

It is explicitly **not** Inter (the current stack's first choice and the default of this genre),
not a monospace, and not a serif display paired with cream.

**Weight, verified, not estimated.** One variable WOFF2 carrying `wght 400–700` and
`wdth 100–125`, subset to Latin-1 plus the punctuation actually used, with `kern`, `liga`,
`calt` and `tnum` retained:

```
source Archivo[wdth,wght].ttf          658,596 bytes
instanced to wght 400:700 wdth 100:125 438,460 bytes
subset + WOFF2                          47,316 bytes   ← what ships
```

**47 KB, one file, one request**, against a budget of ~120 KB. `font-display: swap`, preloaded,
with a matched system fallback (`ui-sans-serif, Segoe UI, system-ui`) so the layout does not
shift. Subsetting is done by `fonttools` + `brotli` (Python, already present), committed as a
script under `scripts/`; no new npm dependency.

If the font cannot be fetched at build time the site falls back to the system stack and nothing
breaks — the design does not depend on the font to be legible, only to be itself.

### Scale

Base 17px / 1.6. Prose measure capped at **66 characters**; the lead paragraph at 58.

| Token         | Size                             | Weight | Width | Leading | Tracking | Use                                        |
| ------------- | -------------------------------- | ------ | ----- | ------- | -------- | ------------------------------------------ |
| `--t-display` | `clamp(2.6rem, 7.2vw, 5.6rem)`   | 700    | 118   | 0.94    | −0.02em  | the opening statement — **one per page**   |
| `--t-h2`      | `clamp(1.7rem, 3.4vw, 2.5rem)`   | 600    | 112   | 1.08    | −0.012em | section heads                              |
| `--t-h3`      | `clamp(1.2rem, 2vw, 1.5rem)`     | 600    | 100   | 1.2     | −0.006em | project names, case-study subheads         |
| `--t-lead`    | `clamp(1.08rem, 1.5vw, 1.25rem)` | 400    | 100   | 1.5     | 0        | the paragraph under a display line         |
| `--t-body`    | `1.0625rem`                      | 400    | 100   | 1.6     | 0        | prose                                      |
| `--t-small`   | `0.9375rem`                      | 400    | 100   | 1.5     | 0        | captions, notes, disclaimers               |
| `--t-meta`    | `0.8125rem`                      | 600    | 100   | 1.4     | +0.01em  | row labels and figures — **sentence case** |

**There is no uppercase token and no letter-spaced small-caps token.** The eyebrow cliché is
removed at the level of the design system, so it cannot come back by accident.

Numerals use `font-variant-numeric: tabular-nums` wherever figures are stacked (the shipped-facts
table, project years), so columns align.

### Headlines do visual work

The display line is set at up to 5.6rem in the expanded width, breaks where the _sense_ breaks
(hard `<br>` at author-chosen points, not wherever the box ends), and sits **against the left
rule with the lead paragraph indented to the second column** — so the headline is a shape on the
page, not a label above a paragraph. One display line per page, never two.

---

## 4. Layout

A 12-column grid, 1120px max, 24px gutters at phone and 40px at desktop. Nothing is full-bleed;
the ladder is the widest object and it still sits inside the container, because its whole point
is the proportion between its two wells and a bleed would break that. Rules appear in exactly
four places and each one means something:

1. A **gold left rule** beside a project row marks _shipped to a store_ (today only Strong 8K).
2. A **hairline rule between project rows** — these are a list, and a list has rules.
3. A **hairline under the header** — it separates chrome from content.
4. A **gold hairline under the device ladder**, carrying the one line of platform fact.

Everything else is separated by space. No card borders, no card shadows, no card radii. Radius is
`0` for media wells (a screen has square corners) and `2px` for buttons; nothing else is rounded.

### Home — desktop (1280)

```
┌────────────────────────────────────────────────────────────────────────────┐
│  Ahmed Noaman          projects  skills  about  contact      CV   ◐        │
├────────────────────────────────────────────────────────────────────────────┤  ← hairline
│                                                                            │
│  I build software for                                                      │  display,
│  screens people watch                                                      │  left-aligned,
│  from across the room.                                                     │  3 hard breaks
│                                                                            │
│              Flutter developer in Alexandria. For three months this        │  lead, indented
│              year I built Strong 8K — a live TV and on-demand client       │  to col 4, 58ch
│              for Android, Android TV and Windows. 73,576 lines of          │
│              Dart, 2,603 passing tests, now on Google Play and the         │
│              Microsoft Store.                                              │
│                                                                            │
│              Read the Strong 8K case study    Download CV                  │  2 buttons only
│                                                                            │
│                                                                            │
│   ┌──────────────────┐      ┌────────────────────────────────┐             │  THE LADDER
│   │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│      │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│             │  --screen,
│   │▓   phone 16:9   ▓│      │▓     ten-inch tablet 16:10    ▓│             │  radius 0,
│   └──────────────────┘      └────────────────────────────────┘             │  shared
│    Strong 8K on a phone      Strong 8K on a ten-inch tablet                 │  baseline,
│ ───────────────────────────────────────────────────────────────────────────│  true scale
│  One Flutter codebase. Also ships to Android TV and Windows.                │  ← gold rule
│  Captured against the reviewer demo line, so the catalogue is Blender       │  caption,
│  open movies.                                                               │  --ink-quiet
│                                                                            │
│  Projects                                           Eight. One shipped.    │  h2 left,
│ ───────────────────────────────────────────────────────────────────────────│  count right
│ ┃ 2026   Strong 8K                     Android · Android TV · Windows      │  ← GOLD RULE
│ ┃                                                                          │    = shipped
│ ┃  ┌──────────────────────┐   A live TV and on-demand client. Two playback │
│ ┃  │   16:9 still         │   engines behind one UI; failover that can     │
│ ┃  └──────────────────────┘   tell a blocked host from an expired line.    │
│ ┃                             Flutter  Kotlin  Node.js  nginx              │
│ ┃                             Case study    Google Play    Microsoft Store │
│ ───────────────────────────────────────────────────────────────────────────│
│   2026   Khayyer                                  Android · Firebase       │
│         ┌──────────────────────┐  Food donation platform, Arabic and       │
│         │   16:9 still         │  English. Graduation project, funded by   │
│         └──────────────────────┘  ITIDA.                                   │
│                                   Details   Demo   Screenshots   Source    │
│ ───────────────────────────────────────────────────────────────────────────│
│   2026   PSA Academy                                           Web         │
│                        …same row shape…                                    │
│ ───────────────────────────────────────────────────────────────────────────│
│   Five more projects                                                   ⌄   │  ← disclosure
├────────────────────────────────────────────────────────────────────────────┤
│  What I work with                                                          │
│                                                                            │
│  Mobile         Flutter · Dart · Kotlin platform views · Swift ·           │  two columns:
│                 Android TV and D-pad navigation · Media3/ExoPlayer         │  label | list,
│  Architecture   Layered UI, domain and data design · SOLID · …             │  no cards,
│  State          Riverpod · BLoC · Cubit · Provider · GetX                  │  hairlines
│  Backend        Firebase · Supabase · SQLite · MySQL · Node.js · Express   │  between rows
│  Delivery       Linux (Ubuntu, systemd, nginx) · Codemagic · GitHub        │
│                 Actions · Google Play and Microsoft Store releases         │
│  ─────────────────────────────────────────────────────────────────────────│
│  From the DevOps diploma, not yet used in shipped work                     │  ← the split
│                 Docker · Kubernetes · Terraform · Ansible · Jenkins ·      │    (see §7)
│                 Argo CD · Prometheus · Grafana · AWS · Azure               │
├────────────────────────────────────────────────────────────────────────────┤
│  About                          │  Computer Engineering   AASTMT           │
│  three short paragraphs,        │  Expected               2026             │  figures right,
│  66ch, first person             │  Flutter diploma        AMIT, 95%        │  tabular nums
│                                 │  DevOps diploma         Andalusia, 2026  │
│                                 │  Languages              Arabic, English  │
│                                 │  Based                  Alexandria       │
├────────────────────────────────────────────────────────────────────────────┤
│  I'm open to Flutter roles, internships and freelance work.                │  h2 = the fact
│  noamana455@gmail.com      GitHub      LinkedIn                            │  no card
├────────────────────────────────────────────────────────────────────────────┤
│  © 2026 Ahmed Mohamed Noaman.        Built with Astro, TypeScript, Tailwind │
└────────────────────────────────────────────────────────────────────────────┘
```

**What is left-aligned, what is not, where the grid breaks.** Everything is left-aligned to the
same rule — there is no centred text anywhere on the site. One thing breaks the grid on purpose:
the **lead paragraph**, which starts at column 4 while the display line starts at column 1, so the
opening reads as a shape rather than a stack. The ladder's two wells are set from the _left_ rule
and run out to whatever width true scale gives them, so the right edge is ragged on purpose —
the proportion is the content, not the alignment. The project count ("Eight. One shipped.") and the
figures in the about table are the only right-aligned elements, because they are a column of
numbers and numbers align right.

### Home — phone (360)

```
┌────────────────────────┐
│ Ahmed Noaman    ◐   ≡  │
├────────────────────────┤
│                        │
│ I build                │   display drops to
│ software for           │   2.6rem, 5 lines,
│ screens people         │   breaks re-flowed
│ watch from             │   for the narrow
│ across the room.       │   measure
│                        │
│ Flutter developer in   │   lead is NOT
│ Alexandria. For three  │   indented at phone
│ months this year I     │   — the indent is a
│ built Strong 8K …      │   desktop device
│                        │
│ Strong 8K case study → │   buttons full width,
│ Download CV            │   stacked, 2 only
│                        │
│┌──────────────────────┐│   ladder STACKS:
││▓ tablet 16:10      ▓ ││   tablet first,
│└──────────────────────┘│   full width
│┌─────────────┐         │
││▓ phone 16:9▓│         │   phone at 62% —
│└─────────────┘         │   the size ratio
│────────────────────────│   survives the
│ One Flutter codebase.  │   stack
│ Also ships to Android  │
│ TV and Windows.        │
├────────────────────────┤
│ Strong 8K on a ten-    │
│ inch tablet. Reviewer  │
│ demo line.             │
│                        │
│ Projects               │
│ Eight. One shipped.    │   count drops below
│ ───────────────────────│
│ ┃ 2026                 │   gold rule survives
│ ┃ Strong 8K            │   at phone — it is
│ ┃ Android · TV · Win   │   the one signal
│ ┃ ┌──────────────────┐ │   worth keeping
│ ┃ │   16:9 still     │ │
│ ┃ └──────────────────┘ │
│ ┃ A live TV and on-    │
│ ┃ demand client…       │
│ ┃ Flutter Kotlin Node  │
│ ┃ Case study           │
│ ┃ Google Play          │
│ ───────────────────────│
│   2026                 │
│   Khayyer              │
│        …               │
└────────────────────────┘
```

Rule for the phone: the hero must not exceed one screen before the ladder appears. Today it takes
roughly two.

### Project page — Strong 8K as a case study

```
┌────────────────────────────────────────────────────────────────────────────┐
│  Ahmed Noaman          projects  skills  about  contact      CV   ◐        │
├────────────────────────────────────────────────────────────────────────────┤
│  ← Projects                                                                │
│                                                                            │
│  Strong 8K                                                                 │  display
│                                                                            │
│              A live TV and on-demand streaming client for Android,         │  lead
│              Android TV and Windows. Freelance, July to October 2026.      │
│                                                                            │
│              Google Play    Microsoft Store    Nine screenshots            │
│                                                                            │
│   ┌──────────────────┐      ┌────────────────────────────────┐             │  the ladder
│   │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│      │▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓│             │  again, this
│   │▓  phone 16:9    ▓│      │▓    ten-inch tablet 16:10     ▓│             │  time from
│   └──────────────────┘      └────────────────────────────────┘             │  THIS
│ ───────────────────────────────────────────────────────────────────────────│  project's
│  One Flutter codebase. Also ships to Android TV and Windows.                │  own gallery
├────────────────────────────────────────────────────────────────────────────┤
│  What it is                                  │  Shipped                    │
│                                              │ ────────────────────────────│
│  Two paragraphs from projects.ts,            │  Google Play         1.0.9  │  tabular
│  66ch, first person.                         │  Microsoft Store     1.0.1  │  figures,
│                                              │  Dart in lib        73,576  │  gold
│                                              │  Screens                51  │  hairlines
│                                              │  Tests passing       2,603  │
│                                              │  Commits               195  │
│                                              │  Brands from one repo   15  │
│                                              │  Developers              1  │
├────────────────────────────────────────────────────────────────────────────┤
│  Three problems worth describing                                           │  h2
│                                                                            │
│  A 403 that means two different things                                     │  h3
│  ──────────────────────────────────────────                                │  gold hairline
│  Four short paragraphs, first person, 66ch. The reseller gives one         │
│  subscription several hosts; a finished subscription refuses a stream      │
│  with the same 403 a blocked host uses…                                    │
│                                                                            │
│  The picture freezes, the audio keeps playing                              │
│  ──────────────────────────────────────────                                │
│  …Media3 reports READY after its codec is released, so playback state,     │
│  isPlaying and position all say healthy. The only honest signal is a       │
│  frame counter, so I plumbed one across the platform boundary…             │
│                                                                            │
│  Twenty-seven megabytes of catalogue on a weak TV box                      │
│  ──────────────────────────────────────────                                │
│  …                                                                         │
├────────────────────────────────────────────────────────────────────────────┤
│  Nine screenshots                                                          │
│  Open any image for a full-screen gallery. Arrow keys move; Escape closes. │
│                                                                            │
│  ┌───────────────────────────┐  ┌───────────────────────────┐              │  2-up at
│  │      16:9 — UNCROPPED     │  │      16:9 — UNCROPPED     │              │  desktop,
│  └───────────────────────────┘  └───────────────────────────┘              │  1-up at
│  Home screen with the active     Live TV channel list with live            │  phone.
│  subscription badge.             indicators and a preview pane.            │  Never
│                                                                            │  cropped.
│  ┌───────────────────────────┐  ┌───────────────────────────┐              │
│  …                                                                         │
├────────────────────────────────────────────────────────────────────────────┤
│  Implementation boundary                                                   │
│  The note from projects.ts, in full, with a gold rule beside it.           │
└────────────────────────────────────────────────────────────────────────────┘
```

**The gallery fix.** Aspect ratio comes from the data, per image, never from CSS. The gallery
chooses its own shape: images where `width > height` (Strong 8K's 1200×675 and 1200×750, Khayyer's
1200×675) render **1-up at phone, 2-up from 768px**, at their true ratio. Portrait images
(PSA Academy 480×874, Padel 828×1792, E-commerce and Instagram 960×2137, Food delivery 480×1015,
Todo) render 2-up at phone and 4-up at desktop, also at their true ratio. Nothing is ever
`object-fit: cover`-ed into a box it does not fit. This deletes `aspect-ratio: 4 / 5` at
`global.css:1360` — the bug from the audit.

**The ladder is a Strong 8K device, not a site-wide one.** It needs two captures of the same
application at two genuine screen classes, and only Strong 8K has them (six phone-landscape, three
ten-inch tablet). Khayyer's gallery is landscape but single-class; the other six projects are
portrait phone captures only. So the other seven project pages open with **one well** carrying
their 1200×675 thumbnail — the same black, the same zero radius, the same caption treatment, just
one of it. They keep saying what they are — "Portfolio prototype", "UI-only project",
"Independent educational project" — in the status line directly under the name, not in a pill.
A one-well opening on a prototype and a two-well ladder on the shipped product is itself a
hierarchy the reader can see without being told.

---

## 5. Motion

**No load animation. No scroll-triggered reveals. No hover lift. No image zoom.**

Two moments of interaction feedback, both showing what actually changed:

1. **The focus ring moves like a remote.** Strong 8K is driven by a D-pad: the thing that tells
   you where you are is a bright box that snaps between targets. The site's focus ring is
   `2px solid var(--gold)` at a 3px offset, and it _moves_ — a 90ms position transition, nothing
   else. Tabbing through the project list reads like stepping through a channel guide. This is
   the only borrowed behaviour on the site and it doubles as the accessibility requirement.
2. **The gallery cross-fades**, 120ms on the stage image only, so stepping through nine stills
   with the arrow keys reads as a sequence instead of a flicker.

The projects disclosure does not animate. It appears, the button label changes, and the count
changes from "Five more projects" to "Show fewer" — the state change is told in words.

Under `prefers-reduced-motion: reduce`, both transitions become instant, and `scroll-behavior:
smooth` is turned off — which the current stylesheet forgets to do (`global.css:53` is never
reset at `:1553`).

---

## 6. Copy voice

First person, plain, specific, sentence case. Every sentence carries a fact. No emoji, no
exclamation marks, no Title Case on buttons, no arrows glued to links — external links keep their
existing `aria-label` "(opens in a new tab)" and are marked by a gold underline instead of a `↗`.

### Hero

> # I build software for screens people watch from across the room.
>
> Flutter developer in Alexandria. For three months this year I built Strong 8K — a live TV and
> on-demand client for Android, Android TV and Windows. 73,576 lines of Dart, 2,603 passing
> tests, now on Google Play and the Microsoft Store.
>
> `Read the Strong 8K case study` `Download CV`

Was: "I build secure, scalable cross-platform applications with Flutter, thoughtful architecture,
and modern state management. My work turns complex product requirements into maintainable mobile
experiences." — three adjectives and no facts.

### Section headings

| Was                                                                                             | Becomes                                                        |
| ----------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| eyebrow `SELECTED WORK` + "Built applications, not generic claims."                             | **Projects** · right-aligned: "Eight. One shipped."            |
| eyebrow `TECHNICAL EXPERTISE` + "Flutter first. Full application thinking throughout."          | **What I work with**                                           |
| eyebrow `ABOUT ME` + "Engineering mobile products with a broader systems perspective."          | **About**                                                      |
| eyebrow `EDUCATION & CREDENTIALS` + "Continuous learning across mobile, backend, and security." | **Education and certificates**                                 |
| eyebrow `CONTACT` + "Let's build a thoughtful mobile experience."                               | **I'm open to Flutter roles, internships and freelance work.** |
| eyebrow `SELECTED APPLICATION MEDIA` + "Screens chosen for clarity, variety, and privacy."      | **Nine screenshots** (the count comes from the data)           |
| "Verified engineering highlights"                                                               | **Three problems worth describing**                            |
| "Technical snapshot"                                                                            | **Shipped**                                                    |
| "Implementation boundary"                                                                       | kept — it is the most honest heading on the site               |

### About

> I'm in my final year of Computer Engineering at the Arab Academy for Science, Technology and
> Maritime Transport, in Alexandria. I finished AMIT Learning's Flutter diploma with 95%.
>
> From July to October 2026 I took Strong 8K from an empty repository to two stores as the only
> developer: the Flutter client, the Kotlin playback view, a Node.js service on Ubuntu behind
> nginx, a build driver that produces fifteen branded builds from one codebase, and the store
> submissions. The test suite grew with the code — 153 commits touched `lib`, 150 touched `test`.
>
> I've since finished a DevOps Engineering diploma at Andalusia covering Docker, Kubernetes,
> Terraform, Ansible, Jenkins, Argo CD, Prometheus and Grafana. None of it is in Strong 8K; that
> project runs on plain Linux, systemd and nginx, and the site says so below.

### Project summaries — shorter, and each says what it is

| Project          | Summary                                                                                                                                                                                                                             |
| ---------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Strong 8K        | A live TV and on-demand client for Android, Android TV and Windows. Two playback engines behind one UI, and failover that can tell a blocked host from an expired subscription. **Shipped to Google Play and the Microsoft Store.** |
| Khayyer          | A food donation platform in Arabic and English, connecting donors with charities. My graduation project; funded by ITIDA. The YOLOv8 and blockchain work is research scope, not in the repository.                                  |
| PSA Academy      | A Flutter Web and Firebase platform for an academy: roles, attendance, training plans, payments and QR check-in. Hosted, so you can open it.                                                                                        |
| Padel System     | A booking and club-management prototype. Not a shipped product.                                                                                                                                                                     |
| E-commerce       | An offline shopping application. Portfolio build.                                                                                                                                                                                   |
| Instagram clone  | A social app built to learn Firebase. Independent educational project; not affiliated with Instagram or Meta.                                                                                                                       |
| Food delivery    | Interface only — no backend, no orders.                                                                                                                                                                                             |
| Todo and weather | Offline tasks with SQLite, reminders and a weather API.                                                                                                                                                                             |

### Strong 8K case study — the three problems, in Ahmed's voice

Written from `strong8k-brief.md` §2. First person, the numbers that are verified, nothing
invented. Sketch of the first one, to set the register:

> **A 403 that means two different things**
>
> A reseller gives one subscription several interchangeable hosts. Any of them can be blocked or
> geo-fenced — and a host that is blocked refuses a stream with exactly the same HTTP 403 that a
> finished or over-limit subscription uses. The app used to read every 403 as a dead host and walk
> the whole list, collecting 403s, while the user watched a stuttering player and was never told
> their subscription had ended.
>
> I made the classification a pure function. It buckets a failure as transport, account, or
> ambiguous, and it has to dig the status code back out of raw message strings, because the layer
> below throws bare strings and erases the exception type. It deliberately does not treat 403 as
> an account status; what stops the dangerous case is checking the provider's own verdict on the
> line first.
>
> Walking the list authenticates every candidate concurrently — a couple of dozen hosts at a 20
> second timeout would take minutes in sequence — and then picks the first success in the
> operator's priority order rather than whoever answered fastest. The bound is structural rather
> than a magic number: each attempt adds hosts to a set the next enumeration filters on, so the
> untried pool strictly shrinks and A→B→A cannot happen.
>
> Because a walk can take twenty or thirty seconds, I split discovery from commitment. The probe
> promotes nothing and hands back a hop, so the caller can re-check whether it still matters, and
> a late loser is dropped by comparing a generation counter captured before discovery started.

A reader should be able to tell that the person who wrote that had the bug open in front of them.

---

## 7. Cliché review — every axis, before any code

> For each: _is this the default I would produce for any developer portfolio, or a choice made for
> this brief?_

| Axis        | The default (what is there now)                                                                                                                                                            | Replacement                                                                                                                                                                              | Why this, for this brief                                                                                                                                                                     |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Hero**    | Big name, job title, three buttons, floating `mobile-engineering.dart` code window, four-stat row, pulsing availability dot                                                                | One sentence about what he does, two buttons, then a full-bleed 16:9 screenshot of the real product                                                                                      | The work is pictures of screens. Show one instead of drawing a fake file. The name is in the header and the `<title>`; it does not need to be 7rem tall.                                     |
| **Palette** | Tailwind sky/cyan on blue-tinted off-white and blue-tinted near-black                                                                                                                      | Warm paper / warm near-black, gold **ink** at 4.7:1 and 8.6:1, plus one theme-independent black for every media well                                                                     | Gold-on-black is real material from the flagship. Used as ink, not glow: no gradient text, no glow shadow, no gold fills. The black wells give the light theme structure without more boxes. |
| **Type**    | Inter (named, never loaded), `clamp()` to 4.35rem, `-0.055em`, uppercase 0.15em eyebrows, monospace for non-code labels                                                                    | One self-hosted variable Archivo, 47 KB; display in the expanded width breaking on sense; **no uppercase token and no monospace at all**                                                 | Archivo was drawn for signage and highlights — reading at distance, which is the subject. Deleting the uppercase token stops the eyebrow returning by habit.                                 |
| **Cards**   | 20+ identical rounded boxes, radius 1.1–1.6rem, same border, same soft shadow, regardless of hierarchy                                                                                     | No cards. Projects are **rules-and-rows**, skills are a two-column label/list table, credentials are a figure table. Radius 0 on media, 2px on buttons, nothing else                     | Structure should encode information. A list of eight projects is a list; nine skill groups are a table; one shipped product gets a gold rule the others do not.                              |
| **Labels**  | Seven tracked ALL-CAPS eyebrows, `·`-joined meta strings, 17 arrow glyphs, `View 1…9` numbering on an unordered gallery                                                                    | Headings alone; meta as **table rows with their own column**, not strings joined by dots; external links marked by a gold underline and the existing `aria-label`; no numbering anywhere | Every eyebrow restated the heading below it. A middle dot is a table that lost its columns — so give it back its columns. The screenshots have no order, so they get captions, not numbers.  |
| **Motion**  | Fade-and-slide-up reveal, hover lift on cards and buttons, two image zooms, smooth scroll not reset under reduced motion                                                                   | Zero load/scroll animation. A **focus ring that moves like a D-pad selection** (90ms), and a 120ms gallery cross-fade. Reduced motion kills both and smooth scroll                       | The one borrowed behaviour comes from the product itself — Strong 8K is driven by a remote. It is also the accessibility requirement, so it earns its place twice.                           |
| **Copy**    | "secure, scalable", "thoughtful architecture", "turns complex product requirements into maintainable mobile experiences", "Let's build a thoughtful mobile experience", Title Case buttons | First person, sentence case, a fact per sentence; buttons say what they do; the Strong 8K page carries the three real engineering problems at length                                     | The brief's most convincing material is a frozen video frame and an ambiguous 403. Nothing written in marketing voice can compete with that, so stop trying.                                 |

---

## 8. Decisions — asked and answered (2026-10-19)

1. **Splitting the DevOps skills group — APPROVED, split it.** `src/data/profile.ts:80-92`
   listed Docker, Kubernetes, Terraform, Ansible, Jenkins, Argo CD, Prometheus, Grafana, AWS and
   Azure beside Linux, Codemagic and GitHub Actions with no distinction. `strong8k-brief.md` §4 is
   blunt: _"None of those is used in this project, with the single exception of Linux."_ The group
   renders in two parts — **used in shipped work** (Linux/Ubuntu/systemd/nginx, Codemagic, GitHub
   Actions, Play and Microsoft Store releases) and **from the DevOps diploma, not yet used in
   shipped work** (the rest). Same list, boundary drawn, as the site already does for Khayyer's
   YOLOv8 and blockchain scope. Needs a flag in `profile.ts`; invents no fact.
2. **The hero sentence — APPROVED as written.** "I build software for screens people watch from
   across the room."
3. **The visual idea — the device ladder**, chosen over the full-bleed screen band and over two
   alternatives offered (a gold D-pad selection that moves between targets; a full-viewport type
   poster with no hero image). See §1.
4. **"Eight. One shipped."** as the project count — kept. True today: Strong 8K is the only store
   release; PSA Academy is hosted but is not a store product. It will need editing when something
   else ships.
5. **Which captures go in the home ladder** — my call, not asked: `strong8k-home` (1200×675) in
   the phone well and `strong8k-tablet-home` (1200×750) in the tablet well. They are the same
   screen of the same app at two device classes, which is the only pairing that makes the ladder
   mean what it says.

### Still open — flagged, not blocking

- **No Android TV or Windows capture exists** among the nine approved screenshots, so both
  platforms appear only as words. If you have a TV or desktop screenshot that is safe to publish
  (demo line, no customer data), the ladder would carry four wells instead of two and would be a
  materially stronger object. I am not inventing one.

---

## 9. Validator rules this plan touches

| Rule                                                                                               | Change                                                                                              | Why                                                                                                  |
| -------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `validate-site.mjs:131-136` — exactly three `<article class="project-card">` before the disclosure | **unchanged** — the row component keeps the `project-card` class                                    | The three-then-disclosure structure is right; only its appearance changes.                           |
| `:88-93` banned terms, `:84` phone number                                                          | **untouched**, as instructed                                                                        | —                                                                                                    |
| `:40-43` exactly 10 HTML pages                                                                     | unchanged                                                                                           | No new routes; URL structure is fixed.                                                               |
| new                                                                                                | **add**: the home page must contain no `text-transform: uppercase` eyebrow and no `↗`/`→`/`↓` glyph | Encodes the two clichés most likely to creep back in a later edit. One-line comment explaining each. |
| new                                                                                                | **add**: every `<img>` under a gallery must carry `width`/`height` matching its data entry          | Encodes the no-cropping rule so the 4:5 bug cannot return.                                           |

---

## 10. Build order

1. Tokens and the font pipeline (`global.css` `:root`, `scripts/build_fonts.py`, `public/fonts/`).
2. Type scale and base elements; delete the uppercase and monospace label styles.
3. Header, footer, the device-ladder component.
4. Home: hero, band, project rows, skills table, about table, contact.
5. Project pages: shared template, then the Strong 8K case study prose.
6. Gallery: per-image aspect ratio, 2-up/4-up by orientation; dialog cross-fade.
7. Copy pass across all ten pages.
8. Validator rules + comments; `npm test`; screenshots; `design/03-critique.md`.
