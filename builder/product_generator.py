from pathlib import Path
from jinja2 import Template

from builder.specification import load
from builder.knowledge import workflows

ROOT = Path(__file__).resolve().parent.parent

PRODUCT = ROOT / "products" / "ai-workday-accelerator-kit" / "src"

MODULE_TEMPLATE = Template("""
# {{ title }}

## Overview

This system helps professionals accelerate repetitive business tasks using AI-driven workflows.

{% for wf in workflows %}

---

## Workflow {{ loop.index }} — {{ wf.name }}

### Problem

{{ wf.problem }}

### Objective

{{ wf.objective }}

### Audience

{{ wf.audience }}

### AI Prompt

You are a senior consultant specialized in **{{ wf.name }}**.

Help me solve the following task.

Business Context

[Describe your situation]

Requirements

- Produce a professional result.
- Explain your reasoning.
- Recommend improvements.
- Identify risks.
- Suggest best practices.

### Expected Output

- Professional deliverable
- Actionable recommendations
- Clear business language
- Practical next steps

### Example

Adapt your response to the supplied business context.

### Best Practices

- Include enough business context.
- Specify the desired outcome.
- Mention constraints.
- Review the generated result.

### Common Mistakes

- Missing business context.
- Ambiguous instructions.
- Undefined objectives.

### Pro Tip

Treat AI as a senior consultant instead of a search engine.

{% endfor %}
""")


def build(spec_name: str):

    spec = load(spec_name)

    knowledge = workflows()

    PRODUCT.mkdir(parents=True, exist_ok=True)

    for module in spec["modules"]:

        module_id = module["id"]

        content = MODULE_TEMPLATE.render(
            title=module["title"],
            workflows=knowledge[module_id]
        )

        file = PRODUCT / f"{module_id}.md"

        file.write_text(
            content,
            encoding="utf8"
        )

    print("Starter Edition generated successfully.")