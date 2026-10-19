# 04 — Screenshots still needed

One project could not be fixed from material already in the repository. Everything else on this
page is done.

---

## What was fixed without you

Six projects now show the application itself instead of a generated cover. Each thumbnail is a
real capture already published in that project's gallery, shown whole, at its own aspect ratio,
on the page background with the site's one hairline border — the same framing the Strong 8K
device ladder uses.

| Project          | Thumbnail is now           | Source                |
| ---------------- | -------------------------- | --------------------- |
| PSA Academy      | the admin dashboard        | `psa-admin-analytics` |
| Padel System     | the Padelit home screen    | `padel-home`          |
| E-commerce       | the A-store home screen    | `ecommerce-home`      |
| Instagram clone  | the home feed              | `instagram-home-feed` |
| Food delivery    | the offers home screen     | `food-delivery-home`  |
| Todo and weather | the dark-theme home screen | `todo-home`           |

**Strong 8K keeps its gold wordmark graphic on purpose.** It is the product's own feature
graphic, not a stock render of a phone, and the two real captures sit directly above it in the
device ladder. Nothing to change there.

---

## Khayyer — three captures needed

**Why it was skipped.** All three images in Khayyer's published gallery are slides from a project
presentation, not screenshots: `khayyer-onboarding` and `khayyer-charity-scheduling` are four
phone mock-ups arranged on a green gradient under a title, and the third carries a slide number
in the corner. Swapping one of those in as the thumbnail would replace one render with another,
so Khayyer keeps its current cover until there is a real capture. It is now the only project on
the home page showing a generated image rather than the app.

**What to capture.** Three screens, in this order of usefulness:

| #   | Screen                                                                                                          | Why                                                                    |
| --- | --------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| 1   | **Donor home / dashboard** — the screen a signed-in donor lands on, with the welcome panel and active campaigns | This becomes the thumbnail. It should show the app doing its main job. |
| 2   | **Donation capture** — the form where a donation is photographed and described                                  | This is the feature the project is actually about.                     |
| 3   | **Organization view** — a charity's list of incoming donations with their statuses                              | Shows the second role, which the summary already claims.               |

**How to capture them:**

- **Portrait, at least 1080 px wide**, straight from the device or emulator. The screen only — no
  device frame, no drop shadow, no background, no title text, no slide number.
- **Light theme**, so the three sit together.
- **Arabic or English**, whichever you consider the primary interface; be consistent across all
  three. If Arabic, say so and the alt text will describe a right-to-left interface.
- **Demo data only.** No real donor names, no real charity names, no phone numbers, no email
  addresses, no photographs of real people, no location that identifies anyone. The same rule the
  Strong 8K captures follow, which is why those were safe to publish.
- PNG, unedited. Do not crop them to a square or a 16:9 box — the site takes the aspect ratio
  from the image.

**Where to put them:** drop them into `khayyer_assets/` and tell me the filenames. I will add
them to `scripts/process_media.py`, run it, and point the gallery and thumbnail at them. Nothing
else needs to change.

**Until then** Khayyer's thumbnail stays as it is, and this file stays in the repository as the
open item.
