from pathlib import Path
from jinja2 import Template

from builder.specification import load
from builder.knowledge import workflows

ROOT = Path(__file__).resolve().parent.parent

PRODUCT = ROOT / "products" / "ai-workday-accelerator-kit" / "src"

MODULE_TEMPLATE = Template("""
# {{ title }}

## Business Outcome

This Business System helps professionals reduce repetitive work while improving consistency, quality and decision-making.

### Expected Business Impact

- Reduce repetitive work
- Increase productivity
- Improve deliverable quality
- Standardize business processes
- Accelerate decision making

{% for wf in workflows %}

---

# {{ wf.name }}

## Business Problem

{{ wf.problem }}

## Business Objective

{{ wf.objective }}

## Target Audience

{{ wf.audience }}

## Professional AI Workflow

You are a Senior Enterprise Consultant with extensive experience in {{ wf.name }}.

Your objective is to help produce enterprise-grade deliverables.

### Business Context

Describe:

- Organization
- Industry
- Business process
- Current challenge
- Expected outcome

### Deliverables

Produce:

1. Executive Summary

2. Detailed Analysis

3. Recommended Actions

4. Risks

5. Best Practices

6. Implementation Roadmap

7. Executive Recommendations

### Quality Requirements

- Professional language
- Business oriented
- Actionable
- Structured
- Executive ready

## Expected Output

The response must include:

- Executive Summary

- Business Analysis

- Recommended Actions

- Risks

- Opportunities

- Implementation Plan

- Final Recommendations

## Real Business Scenario

Example:

Company:

Medium-sized manufacturing company.

Situation:

Monthly operational reporting requires approximately 8 hours every week.

Objective:

Reduce reporting time by using AI while improving report quality.

Expected Result:

AI generates a structured report ready for executive review.

## Implementation Notes

Always include:

- business context
- stakeholders
- constraints
- available information
- desired outcome

The more context provided, the better the results.

## Common Pitfalls

Avoid:

- Generic prompts
- Missing business objectives
- Lack of context
- Undefined audience
- Ambiguous requests

## Expert Recommendation

Treat AI as a Senior Enterprise Consultant.

Do not ask AI to "write something."

Instead, describe the business problem and the expected business outcome.

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

        output = PRODUCT / f"{module_id}.md"

        output.write_text(
            content,
            encoding="utf8"
        )

    print()
    print("=" * 60)
    print("STARTER EDITION GENERATED")
    print("=" * 60)
    print()

    for module in spec["modules"]:
        print(f"✓ {module['title']}")

    print()