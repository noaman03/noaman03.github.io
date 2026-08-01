"""Generate deterministic site icons and normalize the approved social card."""

from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps


ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"
SOCIAL_SOURCE = ROOT / "tmp" / "social-card-source.png"
FONT = Path(r"C:\Windows\Fonts\seguisb.ttf")


def create_icon(size: int, destination: Path) -> None:
    scale = 4
    canvas_size = size * scale
    image = Image.new("RGB", (canvas_size, canvas_size), "#07101f")
    draw = ImageDraw.Draw(image)
    for y in range(canvas_size):
        mix = y / max(canvas_size - 1, 1)
        color = (
            int(7 + 2 * mix),
            int(16 + 88 * mix),
            int(31 + 118 * mix),
        )
        draw.line((0, y, canvas_size, y), fill=color)
    inset = round(canvas_size * 0.08)
    radius = round(canvas_size * 0.22)
    draw.rounded_rectangle(
        (inset, inset, canvas_size - inset, canvas_size - inset),
        radius=radius,
        outline="#38bdf8",
        width=max(3, round(canvas_size * 0.025)),
    )
    text_font = ImageFont.truetype(str(FONT), round(canvas_size * 0.34))
    bbox = draw.textbbox((0, 0), "AN", font=text_font)
    x = (canvas_size - (bbox[2] - bbox[0])) / 2
    y = (canvas_size - (bbox[3] - bbox[1])) / 2 - bbox[1]
    draw.text((x, y), "AN", font=text_font, fill="#f8fbff")
    image.resize((size, size), Image.Resampling.LANCZOS).save(destination, "PNG", optimize=True)


def main() -> None:
    PUBLIC.mkdir(parents=True, exist_ok=True)
    if not SOCIAL_SOURCE.exists():
        raise FileNotFoundError(f"Missing generated social card: {SOCIAL_SOURCE}")
    with Image.open(SOCIAL_SOURCE) as source:
        card = ImageOps.fit(source.convert("RGB"), (1200, 630), method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))
        card.save(PUBLIC / "og.png", "PNG", optimize=True)
    create_icon(32, PUBLIC / "favicon-32.png")
    create_icon(192, PUBLIC / "favicon-192.png")
    create_icon(180, PUBLIC / "apple-touch-icon.png")
    create_icon(512, PUBLIC / "icon-512.png")


if __name__ == "__main__":
    main()
