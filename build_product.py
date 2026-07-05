from pathlib import Path
import shutil

ROOT = Path(__file__).parent

PRODUCT = ROOT / "products" / "ai-workday-accelerator-kit"
SRC = PRODUCT / "src"
BUILD = PRODUCT / "build"


def build_product():

    BUILD.mkdir(parents=True, exist_ok=True)

    master = BUILD / "AI_Workday_Accelerator_Kit.md"

    parts = []

    for file in sorted(SRC.glob("*.md")):

        parts.append(file.read_text(encoding="utf8"))
        parts.append("\n\n---\n\n")

    master.write_text(
        "".join(parts),
        encoding="utf8"
    )

    for file in PRODUCT.glob("*.md"):

        shutil.copy(file, BUILD / file.name)

    print()
    print("BUILD COMPLETE")
    print(master)


if __name__ == "__main__":
    build_product()