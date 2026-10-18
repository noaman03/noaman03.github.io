"""Generate the public, two-page CV in PDF and editable HTML formats."""

from __future__ import annotations

import html
import json
import shutil
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, TextStringObject
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import (
    KeepTogether,
    PageBreak,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "cv" / "cv_data.json"
EDITABLE_HTML = ROOT / "cv" / "Ahmed-Mohamed-Noaman-CV-Updated.html"
OUTPUT_DIR = ROOT / "output" / "pdf"
PUBLIC_DIR = ROOT / "public" / "documents"
OUTPUT_PDF = OUTPUT_DIR / "Ahmed-Mohamed-Noaman-CV-Updated.pdf"
PUBLIC_PDF = PUBLIC_DIR / "Ahmed-Mohamed-Noaman-CV.pdf"
TEMP_PDF = ROOT / "tmp" / "pdfs" / "cv-build.pdf"

NAVY = colors.HexColor("#102D4F")
INK = colors.HexColor("#202A35")
MUTED = colors.HexColor("#4A5969")
LINE = colors.HexColor("#BDD1E3")
LINK = colors.HexColor("#0879D9")


def load_data() -> dict:
    return json.loads(DATA_PATH.read_text(encoding="utf-8"))


FONT_DIR = ROOT / "cv" / "fonts"
# Segoe UI is used when the CV is built on Windows. Elsewhere (CI, Linux, macOS)
# the bundled Selawik family (Microsoft's open-source, metric-compatible
# alternative, SIL OFL) keeps the layout and pagination identical.
FONT_CANDIDATES = {
    "Segoe": (Path(r"C:\Windows\Fonts\segoeui.ttf"), FONT_DIR / "Selawik-Regular.ttf"),
    "Segoe-Semibold": (Path(r"C:\Windows\Fonts\seguisb.ttf"), FONT_DIR / "Selawik-Bold.ttf"),
}


def register_fonts() -> None:
    for name, candidates in FONT_CANDIDATES.items():
        for candidate in candidates:
            if candidate.exists():
                pdfmetrics.registerFont(TTFont(name, str(candidate)))
                break
        else:
            raise FileNotFoundError(f"No font file found for {name}: {candidates}")


def make_styles() -> dict[str, ParagraphStyle]:
    register_fonts()
    base = getSampleStyleSheet()
    return {
        "name": ParagraphStyle(
            "Name",
            parent=base["Normal"],
            fontName="Segoe-Semibold",
            fontSize=21,
            leading=23,
            textColor=NAVY,
            alignment=TA_CENTER,
            spaceAfter=3,
        ),
        "title": ParagraphStyle(
            "Title",
            parent=base["Normal"],
            fontName="Segoe-Semibold",
            fontSize=10.5,
            leading=13,
            textColor=INK,
            alignment=TA_CENTER,
            spaceAfter=4,
        ),
        "contact": ParagraphStyle(
            "Contact",
            parent=base["Normal"],
            fontName="Segoe",
            fontSize=7.6,
            leading=10,
            textColor=MUTED,
            alignment=TA_CENTER,
            spaceAfter=7,
        ),
        "section": ParagraphStyle(
            "Section",
            parent=base["Heading2"],
            fontName="Segoe-Semibold",
            fontSize=11.5,
            leading=14,
            textColor=NAVY,
            spaceBefore=6,
            spaceAfter=4,
            keepWithNext=True,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["BodyText"],
            fontName="Segoe",
            fontSize=8.2,
            leading=11.2,
            textColor=INK,
            spaceAfter=3,
        ),
        "project": ParagraphStyle(
            "Project",
            parent=base["Heading3"],
            fontName="Segoe-Semibold",
            fontSize=9.5,
            leading=12,
            textColor=NAVY,
            spaceBefore=3,
            spaceAfter=2,
            keepWithNext=True,
        ),
        "meta": ParagraphStyle(
            "Meta",
            parent=base["BodyText"],
            fontName="Segoe-Semibold",
            fontSize=7.6,
            leading=10.2,
            textColor=MUTED,
            spaceAfter=2,
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            parent=base["BodyText"],
            fontName="Segoe",
            fontSize=7.9,
            leading=10.6,
            textColor=INK,
            leftIndent=10,
            firstLineIndent=-6,
            bulletIndent=2,
            spaceAfter=1.3,
        ),
        "small": ParagraphStyle(
            "Small",
            parent=base["BodyText"],
            fontName="Segoe",
            fontSize=7.7,
            leading=10.5,
            textColor=INK,
            spaceAfter=2,
        ),
        "period": ParagraphStyle(
            "Period",
            parent=base["BodyText"],
            fontName="Segoe-Semibold",
            fontSize=7.6,
            leading=12,
            textColor=MUTED,
            alignment=TA_RIGHT,
        ),
    }


def section_heading(text: str, styles: dict[str, ParagraphStyle]) -> list:
    return [
        Paragraph(text.upper(), styles["section"]),
        Table([[""]], colWidths=[174 * mm], rowHeights=[0.45 * mm], style=TableStyle([("BACKGROUND", (0, 0), (-1, -1), LINE)])),
        Spacer(1, 1.5 * mm),
    ]


def project_block(project: dict, styles: dict[str, ParagraphStyle]) -> KeepTogether:
    flow = [
        Paragraph(f"{html.escape(project['name'])} - {html.escape(project['category'])}", styles["project"]),
        Paragraph(html.escape(project["description"]), styles["body"]),
        Paragraph(f"<b>Stack:</b> {html.escape(project['stack'])}", styles["meta"]),
    ]
    for bullet in project["bullets"]:
        flow.append(Paragraph(f"• {html.escape(bullet)}", styles["bullet"]))
    flow.append(Spacer(1, 1.3 * mm))
    return KeepTogether(flow)


def experience_block(entry: dict, styles: dict[str, ParagraphStyle]) -> KeepTogether:
    heading = Table(
        [
            [
                Paragraph(f"{html.escape(entry['role'])} - {html.escape(entry['organisation'])}", styles["project"]),
                Paragraph(html.escape(entry["period"]), styles["period"]),
            ]
        ],
        colWidths=[134 * mm, 40 * mm],
        hAlign="LEFT",
    )
    heading.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 0),
                ("TOPPADDING", (0, 0), (-1, -1), 0),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 0),
            ]
        )
    )
    flow = [
        heading,
        Paragraph(html.escape(entry["description"]), styles["body"]),
        Paragraph(f"<b>Stack:</b> {html.escape(entry['stack'])}", styles["meta"]),
    ]
    for bullet in entry["bullets"]:
        flow.append(Paragraph(f"• {html.escape(bullet)}", styles["bullet"]))
    if entry.get("links"):
        links = " | ".join(
            f"<link href='{html.escape(link['url'])}' color='{LINK.hexval()}'>{html.escape(link['label'])}</link>"
            for link in entry["links"]
        )
        flow.append(Paragraph(links, styles["meta"]))
    flow.append(Spacer(1, 1.3 * mm))
    return KeepTogether(flow)


def build_pdf(data: dict) -> None:
    styles = make_styles()
    TEMP_PDF.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    PUBLIC_DIR.mkdir(parents=True, exist_ok=True)

    doc = SimpleDocTemplate(
        str(TEMP_PDF),
        pagesize=A4,
        rightMargin=18 * mm,
        leftMargin=18 * mm,
        topMargin=13 * mm,
        bottomMargin=13 * mm,
        title="Ahmed Mohamed Noaman - Flutter Developer CV",
        author=data["name"],
        subject="Flutter Developer and Mobile Application Engineer curriculum vitae",
        creator="Ahmed Mohamed Noaman portfolio",
    )

    story = [
        Paragraph(data["name"].upper(), styles["name"]),
        Paragraph(data["title"], styles["title"]),
        Paragraph(
            f"{html.escape(data['location'])} | "
            f"<link href='mailto:{html.escape(data['email'])}' color='{LINK.hexval()}'>{html.escape(data['email'])}</link> | "
            f"<link href='https://{html.escape(data['github'])}' color='{LINK.hexval()}'>{html.escape(data['github'])}</link> | "
            f"<link href='{html.escape(data['portfolio'])}' color='{LINK.hexval()}'>{html.escape(data['portfolio'])}</link> | "
            f"<link href='https://www.{html.escape(data['linkedin'])}' color='{LINK.hexval()}'>LinkedIn</link>",
            styles["contact"],
        ),
    ]

    story.extend(section_heading("Professional Summary", styles))
    story.append(Paragraph(html.escape(data["summary"]), styles["body"]))

    if data.get("experience"):
        story.extend(section_heading("Freelance Experience", styles))
        for entry in data["experience"]:
            story.append(experience_block(entry, styles))

    story.extend(section_heading("Technical Skills", styles))
    for skill in data["skills"]:
        story.append(Paragraph(f"<b>{html.escape(skill['category'])}:</b> {html.escape(skill['items'])}", styles["small"]))

    story.extend(section_heading("Selected Projects", styles))
    for index, project in enumerate(data["projects"]):
        if index == data.get("page_break_before_project", -1):
            story.append(PageBreak())
        story.append(project_block(project, styles))

    story.extend(section_heading("Education & Training", styles))
    for education in data["education"]:
        period = f" | {html.escape(education['period'])}" if education["period"] else ""
        story.append(
            Paragraph(
                f"<b>{html.escape(education['degree'])}</b> | {html.escape(education['school'])}{period}",
                styles["small"],
            )
        )
    for course in data.get("training", []):
        period = f" | {html.escape(course['period'])}" if course.get("period") else ""
        story.append(
            Paragraph(
                f"<b>{html.escape(course['name'])}</b> | {html.escape(course['provider'])}{period}"
                + (f" - {html.escape(course['details'])}" if course.get("details") else ""),
                styles["small"],
            )
        )

    story.extend(section_heading("Selected Certifications", styles))
    cert_rows = []
    for index in range(0, len(data["certifications"]), 2):
        row = []
        for item in data["certifications"][index : index + 2]:
            row.append(Paragraph(f"• {html.escape(item)}", styles["small"]))
        while len(row) < 2:
            row.append("")
        cert_rows.append(row)
    cert_table = Table(cert_rows, colWidths=[86 * mm, 86 * mm], hAlign="LEFT")
    cert_table.setStyle(
        TableStyle(
            [
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 0),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 1),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
            ]
        )
    )
    story.append(cert_table)

    story.extend(section_heading("Languages", styles))
    story.append(Paragraph(" | ".join(html.escape(item) for item in data["languages"]), styles["small"]))

    def page_number(canvas, document):
        canvas.saveState()
        canvas.setFont("Segoe", 7)
        canvas.setFillColor(MUTED)
        canvas.drawRightString(A4[0] - 18 * mm, 7 * mm, f"Page {document.page}")
        canvas.restoreState()

    doc.build(story, onFirstPage=page_number, onLaterPages=page_number)

    reader = PdfReader(str(TEMP_PDF))
    writer = PdfWriter()
    writer.clone_document_from_reader(reader)
    writer.add_metadata(
        {
            "/Title": "Ahmed Mohamed Noaman - Flutter Developer CV",
            "/Author": data["name"],
            "/Subject": "Flutter Developer and Mobile Application Engineer curriculum vitae",
            "/Keywords": "Flutter, Dart, mobile application engineer, Firebase, Riverpod, BLoC",
        }
    )
    writer.root_object[NameObject("/Lang")] = TextStringObject("en-US")
    with OUTPUT_PDF.open("wb") as stream:
        writer.write(stream)
    shutil.copyfile(OUTPUT_PDF, PUBLIC_PDF)


def build_html(data: dict) -> None:
    experience_html = []
    for entry in data.get("experience", []):
        bullets = "".join(f"<li>{html.escape(item)}</li>" for item in entry["bullets"])
        links = " | ".join(
            f'<a href="{html.escape(link["url"])}">{html.escape(link["label"])}</a>' for link in entry.get("links", [])
        )
        experience_html.append(
            f"""
            <article class="project">
              <h3>{html.escape(entry['role'])} <span>- {html.escape(entry['organisation'])}</span> <em class="period">{html.escape(entry['period'])}</em></h3>
              <p>{html.escape(entry['description'])}</p>
              <p class="stack"><strong>Stack:</strong> {html.escape(entry['stack'])}</p>
              <ul>{bullets}</ul>
              {f'<p class="stack">{links}</p>' if links else ''}
            </article>
            """
        )
    training_html = "".join(
        f"<p><strong>{html.escape(item['name'])}</strong> | {html.escape(item['provider'])}"
        + (f" | {html.escape(item['period'])}" if item.get("period") else "")
        + (f" - {html.escape(item['details'])}" if item.get("details") else "")
        + "</p>"
        for item in data.get("training", [])
    )
    project_html = []
    for project in data["projects"]:
        bullets = "".join(f"<li>{html.escape(item)}</li>" for item in project["bullets"])
        project_html.append(
            f"""
            <article class="project">
              <h3>{html.escape(project['name'])} <span>- {html.escape(project['category'])}</span></h3>
              <p>{html.escape(project['description'])}</p>
              <p class="stack"><strong>Stack:</strong> {html.escape(project['stack'])}</p>
              <ul>{bullets}</ul>
            </article>
            """
        )
    education_html = "".join(
        f"<p><strong>{html.escape(item['degree'])}</strong> | {html.escape(item['school'])}"
        + (f" | {html.escape(item['period'])}" if item["period"] else "")
        + "</p>"
        for item in data["education"]
    )
    skills_html = "".join(
        f"<p><strong>{html.escape(item['category'])}:</strong> {html.escape(item['items'])}</p>"
        for item in data["skills"]
    )
    certifications_html = "".join(f"<li>{html.escape(item)}</li>" for item in data["certifications"])
    languages_html = " | ".join(html.escape(item) for item in data["languages"])
    document = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Ahmed Mohamed Noaman - Flutter Developer CV</title>
  <style>
    @page {{ size: A4; margin: 15mm 18mm; }}
    * {{ box-sizing: border-box; }}
    body {{ max-width: 850px; margin: 0 auto; color: #202a35; font: 14px/1.48 "Segoe UI", Arial, sans-serif; }}
    header {{ text-align: center; }}
    h1 {{ margin: 0; color: #102d4f; font-size: 30px; letter-spacing: .02em; }}
    header h2 {{ margin: 2px 0 5px; color: #202a35; font-size: 16px; }}
    .contact {{ margin: 0 0 14px; color: #4a5969; font-size: 12px; }}
    a {{ color: #0879d9; }}
    section > h2 {{ margin: 14px 0 7px; padding-bottom: 4px; border-bottom: 2px solid #bdd1e3; color: #102d4f; font-size: 16px; text-transform: uppercase; }}
    p {{ margin: 4px 0; }}
    .project {{ break-inside: avoid; margin-bottom: 10px; }}
    .project h3 {{ margin: 7px 0 3px; color: #102d4f; font-size: 14px; }}
    .project h3 span {{ color: #4a5969; font-weight: 600; }}
    .project h3 .period {{ float: right; color: #4a5969; font-size: 12px; font-style: normal; font-weight: 600; }}
    .stack {{ color: #4a5969; font-size: 12px; }}
    ul {{ margin: 4px 0; padding-left: 20px; }}
    li {{ margin: 2px 0; }}
    .certifications {{ columns: 2; column-gap: 28px; }}
    @media print {{ a {{ color: #0879d9; text-decoration: none; }} .page-break {{ break-before: page; }} }}
  </style>
</head>
<body>
  <header>
    <h1>{html.escape(data['name']).upper()}</h1>
    <h2>{html.escape(data['title'])}</h2>
    <p class="contact">{html.escape(data['location'])} | <a href="mailto:{html.escape(data['email'])}">{html.escape(data['email'])}</a> | <a href="https://{html.escape(data['github'])}">{html.escape(data['github'])}</a> | <a href="{html.escape(data['portfolio'])}">{html.escape(data['portfolio'])}</a> | <a href="https://www.{html.escape(data['linkedin'])}">LinkedIn</a></p>
  </header>
  <section><h2>Professional Summary</h2><p>{html.escape(data['summary'])}</p></section>
  {f"<section><h2>Freelance Experience</h2>{''.join(experience_html)}</section>" if experience_html else ''}
  <section><h2>Technical Skills</h2>{skills_html}</section>
  <section><h2>Selected Projects</h2>{''.join(project_html)}</section>
  <section><h2>Education &amp; Training</h2>{education_html}{training_html}</section>
  <section><h2>Selected Certifications</h2><ul class="certifications">{certifications_html}</ul></section>
  <section><h2>Languages</h2><p>{languages_html}</p></section>
</body>
</html>
"""
    EDITABLE_HTML.write_text(document, encoding="utf-8")
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(EDITABLE_HTML, OUTPUT_DIR / EDITABLE_HTML.name)


def main() -> None:
    data = load_data()
    build_html(data)
    build_pdf(data)


if __name__ == "__main__":
    main()
