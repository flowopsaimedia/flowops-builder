from pathlib import Path

ROOT = Path(__file__).parent

SRC = ROOT / "products" / "ai-workday-accelerator-kit" / "src"

BUILD = ROOT / "products" / "ai-workday-accelerator-kit" / "build"

BUILD.mkdir(parents=True, exist_ok=True)

content = []

for file in sorted(SRC.glob("*.md")):

    content.append(file.read_text(encoding="utf8"))

    content.append("\n\n---\n\n")

output = BUILD / "AI_Workday_Accelerator_Kit.md"

output.write_text(

    "".join(content),

    encoding="utf8"

)

print(output)