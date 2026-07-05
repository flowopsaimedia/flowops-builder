import argparse

from builder.generator import create_prompt
from builder.product_generator import build
from builder.release import build_release
from builder.specification import load


def main():

    parser = argparse.ArgumentParser(
        prog="flowops",
        description="FlowOps Builder"
    )

    sub = parser.add_subparsers(dest="command")

    # ----------------------------------------------------

    new = sub.add_parser("new")

    new_sub = new.add_subparsers(dest="type")

    prompt = new_sub.add_parser("prompt")

    prompt.add_argument("--category", required=True)
    prompt.add_argument("--name", required=True)
    prompt.add_argument("--title", required=True)

    # ----------------------------------------------------

    spec = sub.add_parser("spec")

    spec.add_argument("name")

    # ----------------------------------------------------

    generate = sub.add_parser("generate")

    generate.add_argument("name")

    # ----------------------------------------------------

    release = sub.add_parser("release")

    release.add_argument("name")

    # ----------------------------------------------------

    args = parser.parse_args()

    if args.command == "new":

        if args.type == "prompt":

            create_prompt(
                args.category,
                args.name,
                args.title
            )

    elif args.command == "spec":

        print(load(args.name))

    elif args.command == "generate":

        build(args.name)

    elif args.command == "release":

        build_release(args.name)

    else:

        parser.print_help()


if __name__ == "__main__":
    main()