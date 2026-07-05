import argparse

from builder.generator import create_prompt
from builder.specification import load
from builder.product_generator import build


def main():

    parser = argparse.ArgumentParser(
        prog="flowops",
        description="FlowOps Builder"
    )

    sub = parser.add_subparsers(dest="command")

    # --------------------------------------------------
    # new
    # --------------------------------------------------

    new = sub.add_parser(
        "new",
        help="Create new project assets"
    )

    new_sub = new.add_subparsers(dest="type")

    prompt = new_sub.add_parser(
        "prompt",
        help="Create a new prompt"
    )

    prompt.add_argument(
        "--category",
        required=True,
        help="Prompt category"
    )

    prompt.add_argument(
        "--name",
        required=True,
        help="File name"
    )

    prompt.add_argument(
        "--title",
        required=True,
        help="Prompt title"
    )

    # --------------------------------------------------
    # spec
    # --------------------------------------------------

    spec = sub.add_parser(
        "spec",
        help="Load a product specification"
    )

    spec.add_argument(
        "name",
        help="Specification name"
    )

    # --------------------------------------------------
    # generate
    # --------------------------------------------------

    generate = sub.add_parser(
        "generate",
        help="Generate product structure"
    )

    generate.add_argument(
        "name",
        help="Specification name"
    )

    # --------------------------------------------------
    # Parse
    # --------------------------------------------------

    args = parser.parse_args()

    # --------------------------------------------------
    # Commands
    # --------------------------------------------------

    if args.command == "new":

        if args.type == "prompt":

            create_prompt(
                args.category,
                args.name,
                args.title
            )

    elif args.command == "spec":

        data = load(args.name)

        print(data)

    elif args.command == "generate":

        build(args.name)

    else:

        parser.print_help()


if __name__ == "__main__":
    main()