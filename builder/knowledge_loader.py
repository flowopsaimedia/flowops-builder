from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parent.parent

KNOWLEDGE = ROOT / "automation" / "knowledge"


def load_yaml(path: Path):

    with open(path, encoding="utf8") as f:

        return yaml.safe_load(f)