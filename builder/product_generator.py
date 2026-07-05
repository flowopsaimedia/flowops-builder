from pathlib import Path

from builder.specification import load

ROOT = Path(__file__).resolve().parent.parent

PRODUCT = ROOT / "products" / "ai-workday-accelerator-kit" / "src"


WORKFLOW_TEMPLATE = """
# {title}

## Overview

TODO

---

## Workflows

{workflows}
"""


WORKFLOW_BLOCK = """
### Workflow {number} — {workflow}

#### Problem

TODO

#### Objective

TODO

#### AI Prompt

TODO

#### Expected Output

TODO

#### Example

TODO

#### Best Practices

TODO

#### Common Mistakes

TODO

#### Pro Tip

TODO
"""


WORKFLOW_NAMES = {
    "excel-intelligence": [
        "Formula Builder",
        "Data Cleaning",
        "Dashboard Designer",
        "Executive Reports",
        "Business Insights",
    ],
    "technical-documentation": [
        "Technical Guide",
        "Procedure Builder",
        "Root Cause Analysis",
        "Integration Documentation",
        "Knowledge Transfer",
    ],
    "troubleshooting": [
        "Incident Diagnosis",
        "Log Analysis",
        "Error Investigation",
        "Performance Analysis",
        "Recovery Plan",
    ],
    "project-delivery": [
        "Project Planning",
        "Risk Assessment",
        "Status Reporting",
        "Meeting Summary",
        "Lessons Learned",
    ],
    "executive-productivity": [
        "Executive Email",
        "Meeting Brief",
        "Decision Memo",
        "Presentation Builder",
        "Weekly Executive Summary",
    ],
}


def build(spec_name: str):

    spec = load(spec_name)

    PRODUCT.mkdir(parents=True, exist_ok=True)

    for module in spec["modules"]:

        blocks = []

        names = WORKFLOW_NAMES[module["id"]]

        for i, workflow in enumerate(names, start=1):

            blocks.append(

                WORKFLOW_BLOCK.format(

                    number=i,

                    workflow=workflow

                )

            )

        content = WORKFLOW_TEMPLATE.format(

            title=module["title"],

            workflows="\n".join(blocks)

        )

        filename = PRODUCT / f"{module['id']}.md"

        filename.write_text(

            content,

            encoding="utf8"

        )

    print("Starter Edition generated successfully.")