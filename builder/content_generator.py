from pathlib import Path
from jinja2 import Template

ROOT = Path(__file__).resolve().parent.parent

PROMPTS = ROOT / "automation" / "prompts"


def load_prompt(name: str) -> str:

    return (PROMPTS / f"{name}.md").read_text(
        encoding="utf8"
    )


def build_business_system(context: dict):

    system = Template(
        load_prompt("business_system_generator")
    ).render(**context)

    module = Template(
        load_prompt("module_generator")
    ).render(**context)

    return f"{system}\n\n{module}"