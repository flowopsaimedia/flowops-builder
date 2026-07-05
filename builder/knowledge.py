from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent

FILE = ROOT / "automation" / "knowledge" / "workflows.yaml"


def workflows():

    with open(FILE, encoding="utf8") as f:

        return yaml.safe_load(f)