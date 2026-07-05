from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def templates():

    return ROOT / "automation" / "templates"


def prompts():

    return ROOT / "prompts"