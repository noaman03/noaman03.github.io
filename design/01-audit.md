# 01 — Audit

Site as it stands on `feat/strong8k-devops` after the three prepared patches, viewed at 360,
768 and 1280 px in both themes. Every claim below cites the file and line it came from.

---

## What the site already does well — keep all of it

These are not neutral. They are the reason this is worth redesigning rather than replacing.

1. **The facts are real and the boundaries are drawn.** `src/data/projects.ts` separates what the
   code does from what the CV claims, in public, on the page: Khayyer's YOLOv8 and blockchain
   scope is explicitly marked "project scope rather than shipped repository features"
   (`src/data/projects.ts:176`), the Instagram clone carries an unaffiliated disclaimer
   (`:527`), the food-delivery app is labelled UI-only (`:544`). The Strong 8K note says the
   screenshots come from a reviewer demo line and the client code is private (`:165`). No other
   portfolio I would be asked to redesign says what it _cannot_ prove. This is the site's only
   real differentiator and the redesign must make it louder, not quieter.

2. **The validator enforces the brand.** `scripts/validate-site.mjs` fails the build on a leaked
   phone number (`:84`), on either banned term (`:21-24`, `:88-93`), on a missing skip link
   (`:76`), on `autoplay` (`:80`), on any broken asset reference (`:95-110`), and on a committed
   APK (`:155`). The disclaimer and the UI-only label are asserted as _strings that must be
   present on the home page_ (`:131-139`). Content rules that can fail CI are rare; these stay.

3. **Accessibility is actually built, not claimed.** Skip link (`BaseLayout.astro:82`), native
   `<dialog>` for gallery and video with arrow-key navigation, Escape, backdrop click and focus
   returned to the trigger (`MediaDialogs.astro:187-198`, `:239-255`), `aria-expanded` +
   `aria-controls` on both disclosures (`index.astro:173-175`, `Header.astro:66-70`), a live
   region on the gallery counter (`MediaDialogs.astro:43-45`), `prefers-reduced-motion`
   honoured (`global.css:1553-1565`), and a 3px focus ring at a 4px offset that is visible on
   every surface (`global.css:108-111`).

4. **Performance discipline.** Zero client framework; three small inline scripts. AVIF + WebP
   with explicit `width`/`height` and real `sizes` (`OptimizedPicture.astro`), lazy below the
   fold, video `src` attached only when the dialog opens (`MediaDialogs.astro`). The built site
   is 25 MB of which 24.5 MB is imagery; `dist/index.html` is 66 KB and there is exactly one
   stylesheet and no web font request.

5. **Two honest themes with a persisted manual toggle** (`Header.astro:146-160`, inline
   no-flash script at `BaseLayout.astro:58-70`).

**One real bug found while auditing, not a taste issue:** the project gallery crops the nine
landscape Strong 8K screenshots into portrait tiles — `aspect-ratio: 4 / 5; object-fit: cover;
object-position: top` (`global.css:1360-1364`). A 16:9 frame rendered at 4:5 loses 56% of its
width. On the Strong 8K page the film stills, the EPG grid and the tablet layouts — the actual
evidence — are sliced into vertical slivers. This is the single most damaging thing on the site.

---

## Why it reads as machine-made

Checked against the brief's cliché list. Found: **every category except particles and the
typewriter effect.**

### Hero — the full kit, all six parts

`index.astro:57-124` is the 2026 template almost line for line.

| Cliché                                              | Where                                                                                                                                |
| --------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Big name                                            | `Ahmed Noaman` at `clamp(3rem, 9.7vw, 7.25rem)` (`global.css:454`)                                                                   |
| One-line title under it                             | "Flutter Developer & Mobile Application Engineer" (`index.astro:64`)                                                                 |
| Two buttons (here, three)                           | View My Projects / Download CV / Contact Me (`index.astro:74-85`)                                                                    |
| **Floating code-window mock with a fake file name** | `.hero-proof` with three traffic-light dots and `<code>mobile-engineering.dart</code>` (`index.astro:107-112`, `global.css:499-530`) |
| Stats row                                           | `focus / work / method / based` definition list (`index.astro:113-121`)                                                              |
| Availability pill with a pulsing dot                | `index.astro:59-61`, `global.css:440-447`                                                                                            |

The code window is the worst offender. It is a picture of a file that does not exist, in a
monospace face, decorated with macOS window chrome, on the site of a person whose actual
repository contains 73,576 lines of real Dart. It claims craft instead of showing it.

### The SaaS card kit

Nine skill cards (`index.astro:195-206`), two credential cards, one contact card, eight project
cards, one hero aside — all the same rounded rectangle with the same border, the same soft
shadow and near-identical radii: `1.4rem` (`global.css:500`, `:610`), `1.2rem` (`:894`,
`:1296`), `1.25rem` (`:1047`, `:1275`), `1.6rem` (`:939`), `1.1rem` (`:813`). Hierarchy is
carried by _nothing_: a nine-item skills taxonomy and the single flagship product are rendered
in the same container at the same elevation. The skills grid at 1280 is the giveaway — nine
boxes of unequal content in a ragged grid, each one a little island.

**Gradient washes as decoration**, three of them: a radial bloom on `body` at 83% 8%
(`global.css:60-66`), a 34rem circle behind the hero (`:413-419`), a second inside the contact
card (`:939-946`). **Glassmorphism**, three times: the header (`backdrop-filter: blur(18px)
saturate(140%)`, `:145`), project labels (`blur(12px)`, `:675`), dialog backdrops (`:1055`).

### Labels, meta strings and arrows

- **Tracked-out ALL-CAPS eyebrows above every heading.** `.eyebrow` is
  `font-size: .76rem; font-weight: 800; letter-spacing: .15em; text-transform: uppercase`
  (`global.css:309-317`), used seven times on the home page — "SELECTED WORK", "TECHNICAL
  EXPERTISE", "ABOUT ME", "EDUCATION & CREDENTIALS", "CONTACT" — plus "SELECTED APPLICATION
  MEDIA" and "PROJECT GALLERY" elsewhere. Every one restates the heading below it.
- **Middle-dot meta strings.** `Flutter · Dart · Clean Architecture · Riverpod · BLoC · Firebase
· Supabase` (`index.astro:104-106`); `Freelance · Streaming & Media Player`
  (`projects.ts:56`); `Graduation Project · Food Donation` (`:171`); `AMIT Learning · Grade 95%`
  (`index.astro:291`); `Arabic — Native · English — C1+` (`:294`).
- **An arrow glued to every link.** 17 instances of `↗`, `↓` or `→` across five files
  (`Header.astro:90,93`; `index.astro:76,94,102,179,262,349,362,372`;
  `ProjectCard.astro:112,125,138,151`; `[slug].astro:87,99,112,124`).
- **Monospace for small labels** in three places that are not code: the hero stat keys
  (`global.css:523`), the hero file name (`:557`), the stack chips (`:732`).
- **Numbered markers on a non-sequence.** Every gallery thumbnail carries a `View 1 … View 9`
  badge (`[slug].astro:207`). The screenshots have no order; the numbers are decoration.

### One accent colour on one word of the headline

`.hero-title span` is painted `linear-gradient(100deg, var(--brand), var(--accent))` and clipped
to the text (`global.css:461-465`) — a blue-to-cyan gradient on the job title, the exact move.
`.section-heading` sets a `-0.055em` tracking at up to `4.35rem` (`:323-326`); headlines are
tight, large, and always in the default position directly above their paragraph.

### Palette

Not the near-black/acid-green combination and not the cream/terracotta one, but the third
default: **generic SaaS blue.** `--brand: #0879d9`, `--brand-bright: #0ea5e9`, `--accent:
#0891b2` (`global.css:15-17`) are Tailwind's sky/cyan ramp; the dark theme's `#38bdf8` /
`#22d3ee` / `#67e8f9` (`:36-38`) are the same ramp lightened. The page sits on `#f5f8fc` /
`#07101f` — blue-tinted off-white and blue-tinted near-black. Nothing here comes from the work.
Strong 8K is a **gold-on-black** television product and its thumbnail is the only warm object on
the entire site; the site frames it in cyan.

### Motion

- **Fade-and-slide-up reveal** on the disclosure: `@keyframes reveal-projects` translating
  0.75rem with opacity (`global.css:590-601`).
- **Hover lift on every card**: `.project-card:hover { transform: translateY(-4px) }` plus a
  shadow swap (`:619-622`), `.button:hover { translateY(-2px) }` (`:367-369`),
  `.button-small:hover { translateY(-1px) }` (`:1162-1163`).
- **Image zoom on hover**, twice: `scale(1.018)` on card media (`:651-652`), `scale(1.025)` on
  gallery thumbnails (`:1367-1368`).

No particles, no typewriter. Everything else on the list is present.

### Copy

The brief's banned words appear almost verbatim.

| On the page                                                                                  | Where                 |
| -------------------------------------------------------------------------------------------- | --------------------- |
| "secure, **scalable** cross-platform applications with Flutter, **thoughtful** architecture" | `index.astro:68-71`   |
| "turns complex product requirements into maintainable mobile experiences"                    | `index.astro:71-72`   |
| "Let's build a thoughtful mobile experience."                                                | `index.astro:316-318` |
| "Built applications, not generic claims."                                                    | `index.astro:137`     |
| "Screens chosen for clarity, variety, and privacy."                                          | `[slug].astro:188`    |
| "Flutter first. Full application thinking throughout."                                       | `index.astro:187`     |
| "Evidence-led architecture and UI"                                                           | `index.astro:118`     |
| "secure, scalable cross-platform applications" (again)                                       | `index.astro:244-245` |

Three further problems with the voice:

- **It is third-person marketing written in the first person.** "My work turns complex product
  requirements into maintainable mobile experiences" is a sentence with no facts in it. The
  Strong 8K brief, by contrast, contains "the app was _structurally_ incapable of noticing"
  a frozen picture because "Media3 reports READY even after its codec is released." One of those
  two was written by someone who was there.
- **Title Case on buttons and labels**: "View My Projects", "Download CV", "Watch Demo", "View
  Screenshots", "Source Code", "Open Live App", "Email Me", "Show More Projects", "Featured
  Project", "Portfolio Prototype". The brief asks for sentence case.
- **"Built applications, not generic claims."** is a claim, and a generic one.

### Structure that does not encode information

- Five of the six home sections are identical: `.section-block .section-divider` → eyebrow →
  heading → intro → grid of cards. Rules appear between every section whether or not the break
  matters (`global.css:300-307`).
- The flagship — a product shipped to two stores, with 2,603 tests, three genuinely hard
  engineering problems and nine screenshots — is **one card in a grid of three**, given a
  `grid-column: 1 / -1` (`global.css:1423-1425`) and 4 highlight bullets instead of 3. That is
  the entire difference between the published product and a UI-only concept.
- The Strong 8K page lists its three hardest problems as six interchangeable bullet points
  under "Verified engineering highlights" (`[slug].astro:146-149`), in a box beside a second box
  called "Technical snapshot". The failover story, the frozen-frame watchdog and the 27 MB
  delta-sync catalogue — the best material on this site — are compressed to one line each.

### Smaller things

- 360 px: the hero occupies roughly two full screens before any content; three stacked
  full-width buttons; the decorative arc crosses the body text in light theme.
- `scroll-behavior: smooth` is set globally (`global.css:53`) and _not_ disabled under
  `prefers-reduced-motion`; the media query at `:1553` only neutralises `transition-duration`
  and `animation-duration`.
- The theme is chosen by inline JS from `prefers-color-scheme` (`BaseLayout.astro:58-70`); the
  CSS itself has no `@media (prefers-color-scheme)` block, so with JS disabled the site is dark
  regardless of system preference.
- `html[data-theme='dark']` (0,1,1) beats `:root` (0,1,0), which works, but section spacing is
  set in four places — `.section-block` (`:300`), `.hero-section` (`:407`), `.project-detail-hero`
  (`:1235`) and `.section-shell` — so vertical rhythm is negotiated rather than declared.

---

## Verdict

The site is honest, fast and accessible, and it looks like it was assembled from a parts bin. The
material it is hiding — a gold-on-black television app, a 403 that means two different things, a
video that freezes while the audio keeps playing, 2,603 tests — is more interesting than anything
currently on the page. The redesign does not need new facts. It needs to stop decorating and
start **showing the evidence it already has**, starting with the nine screenshots it is currently
cropping in half.
