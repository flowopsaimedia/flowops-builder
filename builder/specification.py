from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent

SPECIFICATIONS = ROOT / "automation" / "specifications"


def load(name: str):

    file = SPECIFICATIONS / f"{name}.yaml"

    with open(file, encoding="utf8") as f:

        return yaml.safe_load(f)