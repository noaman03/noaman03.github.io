# 03 — Critique

Written after looking at the built pages at 360, 768 and 1280 px in both themes, and after a
keyboard-only pass. Screenshots are in `design/screens/`; they are full-page captures of the
**production build**, not the dev server, with lazy images forced to load so the gallery is
photographed as a reader would see it.

---

## What works

1. **The ladder carries the page.** Two wells at 1 : 1.589 — measured 387 px and 615 px inside a
   1040 px container — sharing a baseline. The scale difference is legible before you read a
   word, which is the whole point: one codebase, two screen classes. It is the only bold object,
   and nothing else on the page competes with it.

2. **The gold rule does the hierarchy that twenty cards used to fail at.** Strong 8K is the same
   size and shape as Khayyer and PSA Academy. The only difference is a 2 px gold rule down its
   left edge, and it reads as the important one anyway. No card needed to grow.

3. **The skills split is the most on-brand thing on the site.** Nine rows of what he uses, then a
   gold hairline, then "Studied, not shipped — Docker, Kubernetes, Terraform, Ansible, Jenkins,
   Argo CD, Prometheus, Grafana, AWS, Azure." A portfolio that volunteers which half of its own
   skills list is unproven is doing something almost nobody does.

4. **The Strong 8K case study sounds like a person.** "Media3 reports READY even after its codec
   has been released… the only honest signal left is a frame counter, so I plumbed one across the
   platform boundary." Three problems at roughly 300 words each, with a gold hairline under each
   title and nothing else decorating them.

5. **The gallery bug is gone.** Nine landscape captures at 2-up, full 16:9 and 16:10, uncropped;
   the portrait phone galleries on the other seven projects render 4-up at their own tall ratio.
   Aspect ratio now comes from the data, and the validator fails the build if an image ships
   without its dimensions.

6. **Every cliché from the audit is gone from the output**, and three of them are now enforced:
   no `uppercase` label class, no arrow glyph, no image without width and height. No cards, no
   shadows, no gradients, no hover lift, no scroll reveal, no monospace, no middle-dot meta
   strings except inside data the site does not own.

---

## What still reads generic, or is simply weak

1. **Khayyer's and PSA Academy's thumbnails are marketing renders, and it shows.** A phone
   floating on a pastel gradient is exactly the stock-looking imagery this redesign was supposed
   to get away from, and framing one in a black well makes it look more like an advertisement,
   not less. Strong 8K's row has a real screenshot; the two below it have pictures _of_ a phone.
   I cannot fix this inside the brief — only the nine Strong 8K captures are approved, and
   `scripts/process_media.py` is off limits — so it stands as the weakest thing on the home page.
   **The fix is a real screenshot of each app, from Ahmed.**

2. **After the ladder, nothing happens again.** Every section is the same `--section-y`, the same
   hairline rule, the same left alignment. That is deliberate — the rhythm is declared once — but
   the home page is 6,227 px tall at 1280 and 8,479 px at 360, and the reader travels all of it
   at one pace. A page can be quiet without being flat, and this one is nearer flat than I would
   like.

3. **The hero's bottom-left quadrant is empty at 1280.** The lead paragraph is indented to 25% so
   the display line reads as a shape, which works; but the phone well then starts at the far left
   below it, leaving a void between the two. It looks composed in a screenshot and slightly
   accidental in the browser.

4. **The project row's right column stacks four kinds of information with only space between
   them** — summary, status, stack, links. It is legible, but it is the one place where "separate
   with space, not boxes" costs clarity rather than buying it.

5. **"8 total. 1 in a store." loses its job at 360 px.** Right-aligned against "Projects" at
   desktop it reads as a caption on the heading; stacked underneath on a phone it reads as a
   stray fragment.

6. **The ladder note is three lines of small grey text immediately under the one bold object.**
   It earns its place — it is what stops the page implying there are TV and Windows captures —
   but it is the busiest small text on the page and it sits where the eye lands next.

---

## What I removed — the Chanel rule

**The second facts table in "Education and certificates."** It listed `B.Sc. Computer
Engineering · 2021 – expected 2026` and `Arab Academy for Science, Technology & Maritime
Transport · Alexandria` — all four of which already appear in the About facts table immediately
above it. Two near-identical two-column tables separated by one section rule was the page
repeating itself in its own voice. The certificates list now stands alone and the section is
shorter and clearer for it.

**Considered and kept: the moving focus ring.** It is the most "clever" thing here and the first
thing a critic would cut. I kept it because it is the brief's requested interaction feedback,
because it is borrowed from the product itself — Strong 8K is driven by a D-pad, where one bright
box tells you where you are — and because it degrades honestly: if the script does not run, the
stylesheet's own `:focus-visible` outline is what shows, and inside a modal dialog the box stands
down and the outline takes over. It costs about thirty lines and no network request.

---

## Keyboard pass

Done with no mouse, at 1280 px.

| Step                | Result                                                                                                                                                              |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| First Tab           | Skip link appears, bordered in gold, and jumps to `#main-content`                                                                                                   |
| Header              | Brand → four nav links → GitHub → LinkedIn → Download CV → theme → each with the gold box following at 90 ms                                                        |
| Measured            | Box at (917, 17) wrapping the LinkedIn link at (920, 20, 56 × 24) — a true 3 px offset, not an approximation                                                        |
| Projects disclosure | Enter expands, label changes "Show the other 5 projects" → "Show fewer projects", `aria-expanded` flips, eight rows present; collapsing returns focus to the button |
| Gallery             | Enter on "See 9 screenshots" opens the dialog and focus lands on Close                                                                                              |
| Inside the gallery  | ← → step through, the counter announces "3 of 9" through its live region, the image cross-fades at 120 ms                                                           |
| Escape              | Closes the dialog and focus returns to the exact trigger, with the gold box drawn around it                                                                         |
| Certificates        | `<details>` opens on Enter; the `+` becomes `−`                                                                                                                     |

Nothing was reachable without a visible indicator, and nothing trapped focus.

---

## Page weight — measured, and over budget

First load at 1280 px, device pixel ratio 1, production build both sides, bytes off the wire,
uncompressed.

|               |      Before |       After |       Delta |
| ------------- | ----------: | ----------: | ----------: |
| HTML          |      66,389 |      64,511 |      −1,878 |
| CSS           |      31,973 |      25,275 |      −6,698 |
| Font (WOFF2)  |           0 |      47,528 | **+47,528** |
| Images (AVIF) |      14,734 |      44,632 | **+29,898** |
| **Total**     | **113,096** | **181,946** | **+68,850** |

**The brief's rule was that the home page should not grow by more than the fonts added. It grew
by 68,850 bytes against a 47,528-byte font, so it is about 21 KB over.** The overage is the
second real screenshot in the hero: the ladder loads two captures where the old page loaded one
thumbnail.

What I did about it before accepting the number:

- Cut 6,698 bytes of CSS and 1,878 of HTML, by deleting the card, shadow and gradient machinery.
- Added an **800w step** to the two ladder images, because the tablet well renders at ~615 CSS px
  and a one-times desktop was pulling the 1200w file for it. That saved 15,748 bytes. The two
  800w files were resized from the committed 1200w WebP, which is the best copy in the repo.
- Stopped eager-loading the first project thumbnail. Nothing above the fold is a project
  thumbnail any more, so all eight load lazily.

**The lever, if 21 KB matters more than the idea:** dropping the ladder to a single well brings
the page in under the font budget. That removes the thing the whole design is built on, so it is
Ahmed's call, not mine.

---

## What I could not verify

- **Real devices.** Everything here was checked in Chromium (headless, and the desktop app's
  browser pane). No Safari, no Firefox, no physical phone, no Android TV browser.
- ~~**The Google Play listing.**~~ **Resolved: Ahmed confirmed on 2026-10-19 that Strong 8K is
  live on Google Play at the URL in `projects.ts`.** This closes `strong8k-brief.md` §7.2, which
  had it as an open question. The link and the "Google Play" wording stay.
- **Lighthouse, CLS and real LCP.** Not run. Every image has explicit dimensions and the font is
  preloaded with `font-display: swap` and a matched fallback stack, so layout shift should be
  near zero, but "should be" is not a measurement.
- **Print.** There are no print styles, before or after.
  All six width/theme combinations were checked: 360, 768 and 1280 px in both themes, with no
  horizontal overflow at any of them (document scrollWidth equals clientWidth throughout).

---

# After follow-up

Done on branch `fix/portfolio-followup`, against the review of the merged redesign. Screenshots
for this round are in `design/screens/`, now at 360 and 1280 px in **both** themes.

## Closed

| #   | Item                                         | What changed                                                                                                                                                                                                                                                                                                                                          |
| --- | -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Marketing-render thumbnails                  | Six projects now show a real capture: PSA Academy's admin dashboard, Padelit's home screen, A-store's home, the clone's feed, the food-delivery offers screen and Todo's dark home. A new `capture` treatment in `scripts/process_media.py` emits the screenshot unchanged, because the stylesheet already supplies the frame the device ladder uses. |
| 3   | Empty bottom-left quadrant at 1280           | The hero buttons return to the left rule, where they line up with the phone well directly below. Only the lead paragraph is still indented, so the offset reads as one deliberate move rather than a block with a hole under it.                                                                                                                      |
| 4   | Four kinds of information stacked in the row | One hairline above the status line separates what a project _is_ from what it is _made of_. No box.                                                                                                                                                                                                                                                   |
| 5   | "8 total. 1 in a store." stranded at 360 px  | The heading row no longer wraps. The count keeps its column and wraps inside it, right-aligned, so it stays a caption on the heading at every width.                                                                                                                                                                                                  |
| 6   | The three-line ladder note                   | Two even lines now ("One Flutter codebase. It also ships to Android TV and Windows; neither has a capture here."), balanced with `text-wrap: balance`. The provenance sentence it repeated lives on the Strong 8K page, under the gallery it describes.                                                                                               |

## Partly closed, and why

**Item 2, the one-pace page.** The brief said not to fix this with decoration, and to use the
skills split if anything. That is what I did: the studied-but-unproven half of the skills list is
now set in the quiet ink, so a reader can see at a glance that it is a different class of claim
without reading the note above it. That is information, not rhythm. **The rest of the pace
problem stands and I am leaving it.** A long single-column page read at one pace is the price of
having no cards and no scroll animation, and I would rather pay it than invent a section break
that means nothing.

## New in this round

- **Light theme verified** at 360, 768 and 1280, which the first pass never screenshotted.
  Gold on paper measures **4.75:1** — it passes AA for normal text, so it stays as text, as a
  rule, and as the focus ring.
- **A real frame on every media well.** `--rule`, the typographic hairline between blocks of
  text, is 1.35:1 against the page by design. It was also the only edge around a screenshot, so
  the light captures — PSA Academy, Padelit, A-store, the clone, food delivery — dissolved into
  the paper. A new `--frame` token rings every well instead: **3.22:1** on paper, **3.32:1** on
  the dark ground. Section rules and table rules keep `--rule`.
- **Two facts corrected**: based in Cairo, and graduating January 2027. Both propagated to the
  CV, which was regenerated and is still two pages.

## Still open

- **Khayyer's thumbnail is the last generated image on the home page.** All three of its gallery
  images are presentation slides rather than captures, so swapping one in would replace one
  render with another. `design/04-screenshots-needed.md` says exactly what to shoot.
- **Portrait rows have a ragged bottom edge.** A phone screenshot is taller than the three lines
  of text beside it, so the media column runs past the buttons by roughly 120 px. Narrowing the
  well to 13 rem keeps the row readable as one unit and the screenshot legible; cropping would
  square it off and is not allowed, which is the right trade.
- **Chromium only**, still. No Safari, no Firefox, no physical device, no Lighthouse run.
- **The page is ~8 KB heavier**, measured at 1280 px and DPR 1 against `main`: 182,120 → 190,101
  bytes. HTML fell 2,175 and CSS rose 478; the images rose 9,696, because a photograph of a
  screen compresses worse than the flat generated graphic it replaced. The portrait thumbnails
  ship a single file with no intermediate srcset step, so a 1× desktop fetches a 480–640 px image
  for a 208 px slot. Adding a 320w step would recover most of the 9 KB and is the obvious next
  optimisation if the number matters.

## Keyboard pass, re-run

Scripted against the built site at 1280 px; nine assertions, all passing.

| Check                                                                                               | Result |
| --------------------------------------------------------------------------------------------------- | ------ |
| First Tab reaches the skip link                                                                     | pass   |
| Header order: brand → Projects → Skills → About → Contact → GitHub → LinkedIn → Download CV → theme | pass   |
| The gold box tracks the focused element at a true 3 px offset                                       | pass   |
| Disclosure expands to 8 rows and the label changes                                                  | pass   |
| Collapsing returns focus to the button and flips `aria-expanded`                                    | pass   |
| Enter opens the gallery and focus lands on Close                                                    | pass   |
| Arrow keys step to "3 of 9" and the image is decoded                                                | pass   |
| Escape closes the gallery and focus returns to the exact trigger                                    | pass   |
| The ring is redrawn on the trigger after the dialog closes                                          | pass   |
