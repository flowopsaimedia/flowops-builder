from pathlib import Path

from builder.specification import load

ROOT = Path(__file__).resolve().parent.parent

PRODUCT = ROOT / "products" / "ai-workday-accelerator-kit" / "src"


def build(spec_name: str):

    spec = load(spec_name)

    PRODUCT.mkdir(parents=True, exist_ok=True)

    for module in spec["modules"]:

        filename = (
            PRODUCT /
            f"{module['id']}.md"
        )

        if filename.exists():
            continue

        text = f"""# {module['title']}

## Overview

TODO

"""

        filename.write_text(
            text,
            encoding="utf8"
        )

    print("Product structure generated.")