from pathlib import Path

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate

ROOT = Path(__file__).resolve().parent.parent

PRODUCT = ROOT / "products" / "ai-workday-accelerator-kit"

BUILD = PRODUCT / "build"


def markdown_to_pdf():

    source = BUILD / "AI_Workday_Accelerator_Kit.md"

    target = BUILD / "AI_Workday_Accelerator_Kit.pdf"

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(str(target))

    story = []

    for line in source.read_text(encoding="utf8").splitlines():

        line = line.strip()

        if not line:
            continue

        if line.startswith("# "):
            story.append(Paragraph(f"<b><font size=20>{line[2:]}</font></b>", styles["Title"]))

        elif line.startswith("## "):
            story.append(Paragraph(f"<b><font size=16>{line[3:]}</font></b>", styles["Heading2"]))

        elif line.startswith("### "):
            story.append(Paragraph(f"<b>{line[4:]}</b>", styles["Heading3"]))

        else:
            story.append(Paragraph(line, styles["BodyText"]))

    doc.build(story)

    print(f"PDF generated: {target}")