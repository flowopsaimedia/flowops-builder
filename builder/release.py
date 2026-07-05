from pathlib import Path
import shutil

from build_product import build_product
from builder.pdf_generator import markdown_to_pdf
from builder.product_generator import build
from builder.specification import load

ROOT = Path(__file__).resolve().parent.parent

PRODUCT = ROOT / "products" / "ai-workday-accelerator-kit"

BUILD = PRODUCT / "build"

RELEASE = PRODUCT / "release"


def build_release(spec_name: str):

    # 1. Generar módulos
    build(spec_name)

    # 2. Compilar producto
    build_product()

    # 3. Generar PDF
    markdown_to_pdf()

    spec = load(spec_name)

    version = spec["product"]["version"]
    edition = spec["product"]["edition"].replace(" ", "_")

    target = RELEASE / f"AI_Workday_Accelerator_Kit_{edition}_v{version}"

    if target.exists():
        shutil.rmtree(target)

    target.mkdir(parents=True)

    (target / "modules").mkdir()
    (target / "templates").mkdir()
    (target / "examples").mkdir()
    (target / "bonus").mkdir()

    # Copiar módulos Markdown

    for file in BUILD.glob("*.md"):

        shutil.copy(
            file,
            target / "modules" / file.name
        )

    # Copiar PDF

    pdf = BUILD / "AI_Workday_Accelerator_Kit.pdf"

    if pdf.exists():

        shutil.copy(
            pdf,
            target / pdf.name
        )

    # Copiar README / QUICK_START

    for file in PRODUCT.glob("*.md"):

        shutil.copy(
            file,
            target / file.name
        )

    archive = shutil.make_archive(
        str(target),
        "zip",
        target
    )

    print()
    print("======================================")
    print(" RELEASE SUCCESSFULLY GENERATED")
    print("======================================")
    print(target)
    print()
    print("ZIP")
    print(archive)