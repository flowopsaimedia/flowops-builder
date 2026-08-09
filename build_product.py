from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent

PRODUCT = ROOT / "products" / "ai-workday-accelerator-kit"

SRC = PRODUCT / "source"
BUILD = PRODUCT / "build"

BUILD.mkdir(parents=True, exist_ok=True)

MASTER = BUILD / "AI_Workday_Accelerator_Kit.md"

parts = []


def add_file(path: Path):
    if not path.exists():
        return

    text = path.read_text(encoding="utf8").strip()

    if text:
        parts.append(text)
        parts.append("\n\n---\n\n")


# ============================================================
# PRODUCT INTRODUCTION
# ============================================================

for filename in [
    "README.md",
    "QUICK_START.md",
    "RESULTS.md",
    "BONUS_100_Enterprise_AI_Writing_Principles.md",
]:

    add_file(PRODUCT / filename)


# ============================================================
# BUSINESS SYSTEMS
# ============================================================

module_order = [
    "excel",
    "technical-documentation",
    "troubleshooting",
    "project-delivery",
    "executive-productivity",
]


for module in module_order:

    module_dir = SRC / module

    if not module_dir.exists():
        continue

    files = sorted(module_dir.glob("*.md"))

    for file in files:
        add_file(file)


# ============================================================
# MASTER DOCUMENT
# ============================================================

MASTER.write_text(
    "".join(parts).rstrip() + "\n",
    encoding="utf8",
)


# ============================================================
# COPY COMMERCIAL FILES TO BUILD
# ============================================================

commercial_files = [
    PRODUCT / "README.md",
    PRODUCT / "QUICK_START.md",
    PRODUCT / "RESULTS.md",
    PRODUCT / "BONUS_100_Enterprise_AI_Writing_Principles.md",
    PRODUCT / "marketing" / "sales_page.md",
    PRODUCT / "marketing" / "payhip.md",
]


for source in commercial_files:

    if source.exists():
        shutil.copy2(
            source,
            BUILD / source.name,
        )


print()
print("=" * 60)
print("BUILD COMPLETE")
print("=" * 60)
print()
print(f"Master document: {MASTER}")
print()
print(f"Business Systems: {len(parts)} content sections")
print()