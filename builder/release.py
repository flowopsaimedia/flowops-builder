from pathlib import Path
import shutil
import zipfile


ROOT = Path(__file__).resolve().parent.parent

PRODUCT = ROOT / "products" / "ai-workday-accelerator-kit"

BUILD = PRODUCT / "build"

RELEASE = PRODUCT / "release"

VERSION = "v1.0"

ZIP_NAME = (
    f"AI_Workday_Accelerator_Kit_Starter_Edition_{VERSION}.zip"
)

ZIP_PATH = RELEASE / ZIP_NAME


# ============================================================
# CLEAN RELEASE DIRECTORY
# ============================================================

if RELEASE.exists():
    for item in RELEASE.iterdir():

        if item.is_dir():
            shutil.rmtree(item)

        else:
            item.unlink()

else:
    RELEASE.mkdir(parents=True)


# ============================================================
# CREATE PACKAGE STRUCTURE
# ============================================================

PACKAGE = RELEASE / "package"

PACKAGE.mkdir(parents=True, exist_ok=True)

MODULES = PACKAGE / "modules"
BONUS = PACKAGE / "bonus"

MODULES.mkdir(parents=True, exist_ok=True)
BONUS.mkdir(parents=True, exist_ok=True)


# ============================================================
# REQUIRED BUILD FILES
# ============================================================

required_files = [
    BUILD / "README.md",
    BUILD / "QUICK_START.md",
    BUILD / "RESULTS.md",
    BUILD / "AI_Workday_Accelerator_Kit.md",
    BUILD / "AI_Workday_Accelerator_Kit.pdf",
    BUILD / "BONUS_100_Enterprise_AI_Writing_Principles.md",
]


for file in required_files:

    if not file.exists():
        raise FileNotFoundError(
            f"Required release file not found: {file}"
        )


# ============================================================
# COPY CUSTOMER-FACING FILES
# ============================================================

shutil.copy2(
    BUILD / "README.md",
    PACKAGE / "README.md",
)

shutil.copy2(
    BUILD / "QUICK_START.md",
    PACKAGE / "QUICK_START.md",
)

shutil.copy2(
    BUILD / "RESULTS.md",
    PACKAGE / "RESULTS.md",
)

shutil.copy2(
    BUILD / "AI_Workday_Accelerator_Kit.pdf",
    PACKAGE / "AI_Workday_Accelerator_Kit.pdf",
)

shutil.copy2(
    BUILD / "AI_Workday_Accelerator_Kit.md",
    MODULES / "AI_Workday_Accelerator_Kit.md",
)

shutil.copy2(
    BUILD / "BONUS_100_Enterprise_AI_Writing_Principles.md",
    BONUS / "BONUS_100_Enterprise_AI_Writing_Principles.md",
)


# ============================================================
# CREATE ZIP
# ============================================================

with zipfile.ZipFile(
    ZIP_PATH,
    "w",
    compression=zipfile.ZIP_DEFLATED,
    compresslevel=9,
) as archive:

    for file in PACKAGE.rglob("*"):

        if not file.is_file():
            continue

        relative = file.relative_to(PACKAGE)

        archive.write(
            file,
            arcname=str(relative).replace("\\", "/"),
        )


# ============================================================
# VALIDATION
# ============================================================

required_archive_files = [
    "README.md",
    "QUICK_START.md",
    "RESULTS.md",
    "AI_Workday_Accelerator_Kit.pdf",
    "modules/AI_Workday_Accelerator_Kit.md",
    "bonus/BONUS_100_Enterprise_AI_Writing_Principles.md",
]


with zipfile.ZipFile(ZIP_PATH, "r") as archive:

    names = archive.namelist()

    for required in required_archive_files:

        if required not in names:
            raise RuntimeError(
                f"Release validation failed. Missing: {required}"
            )

    forbidden_terms = [
        "scratchpad",
        ".git/",
        "__pycache__/",
        ".venv/",
        ".pyc",
        "seo_keyword",
        "sales_page.md",
        "payhip.md",
    ]

    for name in names:

        normalized = name.lower()

        for forbidden in forbidden_terms:

            if forbidden.lower() in normalized:
                raise RuntimeError(
                    f"Forbidden release content detected: {name}"
                )


print()
print("=" * 60)
print("RELEASE COMPLETE")
print("=" * 60)
print()
print(f"Package: {ZIP_PATH}")
print(f"Size: {ZIP_PATH.stat().st_size:,} bytes")
print()
print("Included:")
print("  - README.md")
print("  - QUICK_START.md")
print("  - RESULTS.md")
print("  - AI_Workday_Accelerator_Kit.pdf")
print("  - AI_Workday_Accelerator_Kit.md")
print("  - 100 Enterprise AI Writing Principles")
print()
print("Excluded:")
print("  - sales_page.md")
print("  - payhip.md")
print("  - scratchpad")
print("  - source files")
print("  - development files")
print()
print("RELEASE VALIDATION PASSED")