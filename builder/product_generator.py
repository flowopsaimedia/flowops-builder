from pathlib import Path
from jinja2 import Template

from builder.specification import load

ROOT = Path(__file__).resolve().parent.parent

PRODUCT = ROOT / "products" / "ai-workday-accelerator-kit" / "src"

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

MODULE_TEMPLATE = Template("""
# {{ title }}

## Overview

This system helps professionals accelerate repetitive business tasks using AI-driven workflows.

{% for wf in workflows %}

---

## Workflow {{ loop.index }} — {{ wf }}

### Problem

Professionals spend too much time performing repetitive work related to **{{ wf }}**.

### Objective

Use AI to reduce manual effort while improving quality and consistency.

### AI Prompt

You are a senior business consultant specialized in {{ wf }}.

Help me complete this task professionally.

Context:

[Describe the business scenario]

Requirements:

- Deliver a professional result.
- Explain your reasoning.
- Suggest improvements.
- Highlight possible risks.
- Recommend best practices.

### Expected Output

- Professional deliverable
- Actionable recommendations
- Clear structure
- Business language

### Example

Provide a realistic business example adapted to the supplied context.

### Best Practices

- Always provide business context.
- Explain the desired outcome.
- Include constraints.
- Review the generated result.

### Common Mistakes

- Missing context.
- Vague instructions.
- No business objective.

### Pro Tip

Treat AI like an experienced consultant instead of a search engine.

{% endfor %}
""")


def build(spec_name: str):

    spec = load(spec_name)

    PRODUCT.mkdir(parents=True, exist_ok=True)

    for module in spec["modules"]:

        content = MODULE_TEMPLATE.render(
            title=module["title"],
            workflows=WORKFLOW_NAMES[module["id"]]
        )

        file = PRODUCT / f"{module['id']}.md"

        file.write_text(
            content,
            encoding="utf8"
        )

    print("Starter Edition generated successfully.")