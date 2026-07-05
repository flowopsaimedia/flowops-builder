from pathlib import Path
import shutil

ROOT = Path(__file__).parent

PRODUCT = ROOT / "products" / "ai-workday-accelerator-kit"

SRC = PRODUCT / "src"

BUILD = PRODUCT / "build"

BUILD.mkdir(exist_ok=True)

master = BUILD / "AI_Workday_Accelerator_Kit.md"

parts = []

for file in sorted(SRC.glob("*.md")):

    text = file.read_text(encoding="utf8")

    parts.append(text)

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