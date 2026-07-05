import argparse
from builder.generator import create_prompt


def main():
    parser = argparse.ArgumentParser(
        prog="flowops",
        description="FlowOps Builder"
    )

    sub = parser.add_subparsers(dest="command")

    new = sub.add_parser("new")

    new_sub = new.add_subparsers(dest="type")

    prompt = new_sub.add_parser("prompt")

    prompt.add_argument("--category", required=True)
    prompt.add_argument("--name", required=True)
    prompt.add_argument("--title", required=True)

    args = parser.parse_args()

    if args.command == "new" and args.type == "prompt":
        create_prompt(
            args.category,
            args.name,
            args.title
        )