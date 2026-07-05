from pathlib import Path
import shutil

from builder.specification import load

ROOT = Path(__file__).resolve().parent.parent

PRODUCT = ROOT / "products" / "ai-workday-accelerator-kit"

SRC = PRODUCT / "src"

RELEASE = PRODUCT / "release"


def copy_if_exists(source: Path, destination: Path):
    if source.exists():
        shutil.copy(source, destination)


def build_release(spec_name: str):

    spec = load(spec_name)

    product = spec["product"]

    version = str(product["version"])

    edition = product["edition"].replace(" ", "_")

    target = RELEASE / f"AI_Workday_Accelerator_Kit_{edition}_v{version}"

    if target.exists():
        shutil.rmtree(target)

    target.mkdir(parents=True)

    modules = target / "modules"
    templates = target / "templates"
    examples = target / "examples"
    bonus = target / "bonus"

    modules.mkdir()
    templates.mkdir()
    examples.mkdir()
    bonus.mkdir()

    # Copiar módulos
    for file in SRC.glob("*.md"):
        shutil.copy(file, modules / file.name)

    # Copiar documentos principales
    copy_if_exists(PRODUCT / "README.md", target)
    copy_if_exists(PRODUCT / "QUICK_START.md", target)
    copy_if_exists(PRODUCT / "CHANGELOG.md", target)
    copy_if_exists(PRODUCT / "LICENSE.md", target)

    archive = shutil.make_archive(
        str(target),
        "zip",
        target
    )

    print()
    print("Release created successfully")
    print(target)

    print()
    print("ZIP created")
    print(archive)

    archive = shutil.make_archive(
    str(target),
    "zip",
    target
    )

    print()
    print("ZIP created:")
    print(archive)