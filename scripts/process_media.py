"""Create reviewed, optimized public media without altering supplied originals."""

from __future__ import annotations

import hashlib
import json
import math
import shutil
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public" / "assets" / "projects"
MASTERS = ROOT / "tmp" / "media-masters"
FONT_REGULAR = Path(r"C:\Windows\Fonts\segoeui.ttf")
FONT_SEMIBOLD = Path(r"C:\Windows\Fonts\seguisb.ttf")


@dataclass(frozen=True)
class GalleryItem:
    source: str
    output: str
    max_width: int


@dataclass(frozen=True)
class ProjectMedia:
    slug: str
    title: str
    category: str
    accent: tuple[int, int, int]
    thumbnail_source: str
    gallery: tuple[GalleryItem, ...]
    thumbnail_treatment: str = "branded"
    thumbnail_backdrop: tuple[int, int, int] = (7, 16, 31)
    thumbnail_tint_strength: float = 0.48
    funding_label: str | None = None
    video_source: str | None = None
    video_output: str | None = None


PROJECTS = (
    ProjectMedia(
        slug="strong-8k",
        title="Strong 8K",
        category="IPTV & Media Player · Freelance",
        accent=(214, 170, 60),
        thumbnail_source="strong8k_assets/feature-graphic.png",
        thumbnail_treatment="supplied",
        thumbnail_backdrop=(8, 8, 10),
        thumbnail_tint_strength=0.6,
        gallery=(
            GalleryItem("strong8k_assets/01-home.png", "strong8k-home", 1200),
            GalleryItem("strong8k_assets/02-live-tv.png", "strong8k-live-tv", 1200),
            GalleryItem("strong8k_assets/03-movies.png", "strong8k-movies", 1200),
            GalleryItem("strong8k_assets/04-movie-details.png", "strong8k-movie-details", 1200),
            GalleryItem("strong8k_assets/05-movie-player.png", "strong8k-player", 1200),
            GalleryItem("strong8k_assets/06-series.png", "strong8k-series", 1200),
            GalleryItem("strong8k_assets/07-tablet-home.png", "strong8k-tablet-home", 1200),
            GalleryItem("strong8k_assets/08-tablet-live-channel.png", "strong8k-tablet-live", 1200),
            GalleryItem("strong8k_assets/09-tablet-series-details.png", "strong8k-tablet-series", 1200),
        ),
    ),
    ProjectMedia(
        slug="khayyer",
        title="Khayyer",
        category="Graduation Project · AI & Food Donation",
        accent=(27, 208, 143),
        thumbnail_source="khayyer_assets/portfolio-thumbnail.png",
        thumbnail_treatment="supplied",
        thumbnail_backdrop=(239, 241, 238),
        thumbnail_tint_strength=0.34,
        funding_label="Funded by ITIDA",
        video_source="khayyer_assets/Khayyer_Portfolio_Demo.mp4",
        video_output="khayyer-demo.mp4",
        gallery=(
            GalleryItem("khayyer_assets/1784253528995.jpeg", "khayyer-onboarding", 1200),
            GalleryItem("khayyer_assets/1784253536107.jpeg", "khayyer-donation-flow", 1200),
            GalleryItem("khayyer_assets/1784253531081.jpeg", "khayyer-charity-scheduling", 1200),
        ),
    ),
    ProjectMedia(
        slug="psa-academy",
        title="PSA Academy",
        category="Sports Management & Analytics",
        accent=(34, 211, 238),
        thumbnail_source="psa_academy_assets/portfolio-thumbnail.png",
        thumbnail_treatment="supplied",
        thumbnail_backdrop=(10, 136, 139),
        thumbnail_tint_strength=0.18,
        gallery=(
            GalleryItem("psa_academy_assets/1781978020545.jpeg", "psa-athlete-workout", 480),
            GalleryItem("psa_academy_assets/1781978020699.jpeg", "psa-qr-attendance", 480),
            GalleryItem("psa_academy_assets/1781978022287.jpeg", "psa-admin-analytics", 480),
            GalleryItem("psa_academy_assets/1781978021402.jpeg", "psa-finance-overview", 480),
        ),
    ),
    ProjectMedia(
        slug="padel-system",
        title="Padel System",
        category="Booking & Club Management",
        accent=(61, 225, 170),
        thumbnail_source="padel_system_assets/portfolio-thumbnail.png",
        thumbnail_treatment="supplied",
        thumbnail_backdrop=(3, 27, 20),
        thumbnail_tint_strength=0.58,
        video_source="padel_system_assets/padelit-demo.mp4",
        video_output="padel-demo.mp4",
        gallery=(
            GalleryItem("padel_system_assets/02-light-home.png", "padel-home", 828),
            GalleryItem("padel_system_assets/02-dark-home.png", "padel-home-dark", 828),
            GalleryItem("padel_system_assets/04-light-courts.png", "padel-courts", 828),
            GalleryItem("padel_system_assets/08-light-tournaments.png", "padel-tournaments", 828),
            GalleryItem("padel_system_assets/10-light-tournament-details.png", "padel-tournament-details", 828),
            GalleryItem("padel_system_assets/13-light-matches.png", "padel-matches", 828),
            GalleryItem("padel_system_assets/15-light-match-details.png", "padel-match-details", 828),
            GalleryItem("padel_system_assets/18-dark-chat.png", "padel-chat-dark", 828),
            GalleryItem("padel_system_assets/19-light-owner-dashboard.png", "padel-owner-dashboard", 828),
            GalleryItem("padel_system_assets/20-light-owner-courts.png", "padel-owner-courts", 828),
            GalleryItem("padel_system_assets/22-light-admin.png", "padel-admin-dashboard", 828),
        ),
    ),
    ProjectMedia(
        slug="ecommerce",
        title="E-commerce",
        category="Shopping Application",
        accent=(96, 165, 250),
        thumbnail_source="ecommerce-assets/home.png",
        video_source="ecommerce-assets/A-store-portfolio-demo.mp4",
        video_output="ecommerce-demo.mp4",
        gallery=(
            GalleryItem("ecommerce-assets/home.png", "ecommerce-home", 960),
            GalleryItem("ecommerce-assets/product-detail.png", "ecommerce-product-detail", 960),
            GalleryItem("ecommerce-assets/products-grid-dark.png", "ecommerce-products-grid", 960),
            GalleryItem("ecommerce-assets/admin-dashboard.png", "ecommerce-admin-dashboard", 960),
            GalleryItem("ecommerce-assets/admin-products.png", "ecommerce-admin-products", 960),
        ),
    ),
    ProjectMedia(
        slug="instagram-clone",
        title="Instagram Clone",
        category="Social Media Application",
        accent=(244, 114, 182),
        thumbnail_source="instgram_clone_assets/home-feed.png",
        gallery=(
            GalleryItem("instgram_clone_assets/splash.png", "instagram-splash", 960),
            GalleryItem("instgram_clone_assets/login.png", "instagram-login", 960),
            GalleryItem("instgram_clone_assets/signup.png", "instagram-signup", 960),
            GalleryItem("instgram_clone_assets/home-feed.png", "instagram-home-feed", 960),
        ),
    ),
    ProjectMedia(
        slug="food-delivery-ui",
        title="Food Delivery",
        category="Flutter UI Concept",
        accent=(251, 146, 60),
        thumbnail_source="food_delivery_assets/1781115770250.jpeg",
        gallery=(
            GalleryItem("food_delivery_assets/1781115770250.jpeg", "food-delivery-home", 480),
            GalleryItem("food_delivery_assets/1781115766231.jpeg", "food-delivery-basket", 480),
            GalleryItem("food_delivery_assets/1781115765957.jpeg", "food-delivery-checkout", 480),
            GalleryItem("food_delivery_assets/1781115769285.jpeg", "food-delivery-orders", 480),
        ),
    ),
    ProjectMedia(
        slug="todo",
        title="Todo + Weather",
        category="Productivity Application",
        accent=(167, 139, 250),
        thumbnail_source="todo_assets/1781116072510.jpeg",
        gallery=(
            GalleryItem("todo_assets/1781116072510.jpeg", "todo-home", 480),
            GalleryItem("todo_assets/1781116072403.jpeg", "todo-due-date", 480),
            GalleryItem("todo_assets/1781116072559.jpeg", "todo-time", 480),
            GalleryItem("todo_assets/1781116072613.jpeg", "todo-calendar", 480),
        ),
    ),
)


def font(path: Path, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(path), size)


def gradient_background(size: tuple[int, int], accent: tuple[int, int, int]) -> Image.Image:
    width, height = size
    image = Image.new("RGB", size)
    pixels = image.load()
    for y in range(height):
        y_mix = y / max(height - 1, 1)
        for x in range(width):
            x_mix = x / max(width - 1, 1)
            glow = max(0.0, 1.0 - math.dist((x_mix, y_mix), (0.88, 0.18)) / 0.75)
            pixels[x, y] = (
                int(7 + 5 * y_mix + accent[0] * glow * 0.16),
                int(16 + 8 * x_mix + accent[1] * glow * 0.16),
                int(31 + 13 * x_mix + accent[2] * glow * 0.16),
            )
    return image


def rounded_mask(size: tuple[int, int], radius: int) -> Image.Image:
    mask = Image.new("L", size, 0)
    ImageDraw.Draw(mask).rounded_rectangle((0, 0, size[0] - 1, size[1] - 1), radius=radius, fill=255)
    return mask


def paste_rounded(canvas: Image.Image, source: Image.Image, box: tuple[int, int, int, int], radius: int) -> None:
    fitted = ImageOps.fit(source.convert("RGB"), (box[2], box[3]), method=Image.Resampling.LANCZOS)
    canvas.paste(fitted, (box[0], box[1]), rounded_mask((box[2], box[3]), radius))


def fit_contain(source: Image.Image, max_size: tuple[int, int]) -> Image.Image:
    copy = source.convert("RGB")
    copy.thumbnail(max_size, Image.Resampling.LANCZOS)
    return copy


def supplied_thumbnail(project: ProjectMedia) -> Image.Image:
    """Place a supplied portrait/square cover intact on a derived 16:9 backdrop."""
    with Image.open(ROOT / project.thumbnail_source) as opened:
        source_rgba = ImageOps.exif_transpose(opened).convert("RGBA")

    flattened = Image.new("RGBA", source_rgba.size, (*project.thumbnail_backdrop, 255))
    flattened.alpha_composite(source_rgba)
    source = flattened.convert("RGB")
    backdrop = ImageOps.fit(source, (1600, 900), method=Image.Resampling.LANCZOS)
    backdrop = backdrop.filter(ImageFilter.GaussianBlur(radius=54))
    tint = Image.new("RGB", backdrop.size, project.thumbnail_backdrop)
    canvas = Image.blend(backdrop, tint, project.thumbnail_tint_strength)

    has_transparency = source_rgba.getchannel("A").getextrema()[0] < 255
    if has_transparency:
        foreground = source_rgba.copy()
        foreground.thumbnail((1240, 840), Image.Resampling.LANCZOS)
        x = (canvas.width - foreground.width) // 2
        y = (canvas.height - foreground.height) // 2

        alpha = foreground.getchannel("A")
        shadow_alpha = alpha.filter(ImageFilter.GaussianBlur(radius=20)).point(
            lambda value: round(value * 0.34)
        )
        shadow = Image.new("RGBA", foreground.size, (0, 0, 0, 0))
        shadow.putalpha(shadow_alpha)

        composed = canvas.convert("RGBA")
        composed.alpha_composite(shadow, (x + 8, y + 18))
        composed.alpha_composite(foreground, (x, y))
        return composed.convert("RGB")

    foreground = fit_contain(source, (1240, 820))
    x = (canvas.width - foreground.width) // 2
    y = (canvas.height - foreground.height) // 2
    pad = 18
    draw = ImageDraw.Draw(canvas, "RGBA")
    draw.rounded_rectangle(
        (
            x - pad + 7,
            y - pad + 18,
            x + foreground.width + pad + 7,
            y + foreground.height + pad + 18,
        ),
        radius=38,
        fill=(0, 0, 0, 74),
    )
    canvas.paste(foreground, (x, y), rounded_mask(foreground.size, 24))
    draw.rounded_rectangle(
        (x - 1, y - 1, x + foreground.width, y + foreground.height),
        radius=24,
        outline=(255, 255, 255, 54),
        width=2,
    )
    return canvas


def wrap_title(draw: ImageDraw.ImageDraw, title: str, title_font: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    words = title.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = f"{current} {word}".strip()
        if draw.textbbox((0, 0), candidate, font=title_font)[2] <= max_width or not current:
            current = candidate
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines[:2]


def thumbnail(project: ProjectMedia) -> Image.Image:
    if project.thumbnail_treatment == "supplied":
        return supplied_thumbnail(project)

    canvas = gradient_background((1600, 900), project.accent)
    draw = ImageDraw.Draw(canvas, "RGBA")

    # Restrained interface-inspired geometry.
    draw.ellipse((1120, -300, 1850, 430), fill=(*project.accent, 22))
    draw.ellipse((-240, 610, 360, 1210), fill=(*project.accent, 13))
    for x in (90, 134, 178):
        draw.rounded_rectangle((x, 118, x + 22, 140), radius=11, fill=(*project.accent, 175))
    draw.line((90, 166, 460, 166), fill=(255, 255, 255, 32), width=2)

    title_font = font(FONT_SEMIBOLD, 84)
    category_font = font(FONT_REGULAR, 31)
    label_font = font(FONT_SEMIBOLD, 23)
    lines = wrap_title(draw, project.title, title_font, 650)
    title_y = 300 if len(lines) == 1 else 250
    for line in lines:
        draw.text((90, title_y), line, font=title_font, fill=(247, 250, 255, 255))
        title_y += 96

    category_y = title_y + 22
    category_lines = wrap_title(draw, project.category, category_font, 545)
    for category_line in category_lines:
        draw.text((93, category_y), category_line, font=category_font, fill=(*project.accent, 255))
        category_y += 42
    if project.funding_label:
        label_box = draw.textbbox((0, 0), project.funding_label, font=label_font)
        label_width = label_box[2] - label_box[0] + 40
        draw.rounded_rectangle((92, category_y + 32, 92 + label_width, category_y + 82), radius=25, fill=(*project.accent, 42), outline=(*project.accent, 150), width=2)
        draw.text((112, category_y + 41), project.funding_label, font=label_font, fill=(236, 253, 250, 255))

    source = ImageOps.exif_transpose(Image.open(ROOT / project.thumbnail_source))
    if source.width / source.height > 1.3:
        box = (650, 170, 860, 484)
        shadow = (box[0] - 18, box[1] + 20, box[0] + box[2] + 18, box[1] + box[3] + 48)
        draw.rounded_rectangle(shadow, radius=44, fill=(0, 0, 0, 76))
        paste_rounded(canvas, source, box, 34)
        draw.rounded_rectangle((box[0] - 1, box[1] - 1, box[0] + box[2], box[1] + box[3]), radius=34, outline=(255, 255, 255, 38), width=2)
    else:
        device = fit_contain(source, (460, 716))
        x = 1110 - device.width // 2
        y = 92
        pad = 18
        draw.rounded_rectangle((x - pad + 4, y - pad + 22, x + device.width + pad + 4, y + device.height + pad + 22), radius=58, fill=(0, 0, 0, 86))
        draw.rounded_rectangle((x - pad, y - pad, x + device.width + pad, y + device.height + pad), radius=58, fill=(13, 23, 41, 255), outline=(255, 255, 255, 50), width=2)
        canvas.paste(device, (x, y), rounded_mask(device.size, 40))

    return canvas


def save_modern(image: Image.Image, base: Path, width: int | None = None) -> tuple[int, int]:
    output = ImageOps.exif_transpose(image).convert("RGB")
    if width and output.width > width:
        height = round(output.height * width / output.width)
        output = output.resize((width, height), Image.Resampling.LANCZOS)
    base.parent.mkdir(parents=True, exist_ok=True)
    output.save(base.with_suffix(".webp"), "WEBP", quality=83, method=6)
    output.save(base.with_suffix(".avif"), "AVIF", quality=58, speed=6)
    return output.size


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            hasher.update(block)
    return hasher.hexdigest()


def main() -> None:
    PUBLIC.mkdir(parents=True, exist_ok=True)
    MASTERS.mkdir(parents=True, exist_ok=True)
    report: dict[str, object] = {"projects": {}, "source_hashes": {}}

    for project in PROJECTS:
        destination = PUBLIC / project.slug
        destination.mkdir(parents=True, exist_ok=True)
        master = thumbnail(project)
        master_path = MASTERS / f"{project.slug}-thumbnail-master.png"
        master.save(master_path, "PNG", optimize=True)
        save_modern(master, destination / "thumbnail", 1200)
        save_modern(master, destination / "thumbnail-640", 640)

        gallery_report = []
        for item in project.gallery:
            source_path = ROOT / item.source
            report["source_hashes"][item.source] = digest(source_path)
            with Image.open(source_path) as opened:
                source = ImageOps.exif_transpose(opened).convert("RGB")
                size = save_modern(source, destination / item.output, item.max_width)
                if item.max_width > 480 and source.width > 480:
                    save_modern(source, destination / f"{item.output}-480", 480)
            gallery_report.append({"source": item.source, "output": item.output, "size": size})

        report["source_hashes"][project.thumbnail_source] = digest(ROOT / project.thumbnail_source)
        if project.video_source and project.video_output:
            source_video = ROOT / project.video_source
            report["source_hashes"][project.video_source] = digest(source_video)
            shutil.copyfile(source_video, destination / project.video_output)

        report["projects"][project.slug] = {
            "thumbnail_source": project.thumbnail_source,
            "thumbnail_master": str(master_path.relative_to(ROOT)),
            "gallery": gallery_report,
            "video": project.video_output,
        }

    (ROOT / "tmp" / "media-processing-report.json").write_text(
        json.dumps(report, indent=2), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
