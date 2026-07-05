import argparse

from builder.generator import create_prompt
from builder.product_generator import build
from builder.release import build_release
from builder.specification import load
from builder.pdf_generator import markdown_to_pdf


def main():

    parser = argparse.ArgumentParser(
        prog="flowops",
        description="FlowOps Builder"
    )

    sub = parser.add_subparsers(dest="command")

    # ==================================================
    # NEW
    # ==================================================

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
        help="Prompt file name"
    )

    prompt.add_argument(
        "--title",
        required=True,
        help="Prompt title"
    )

    # ==================================================
    # SPEC
    # ==================================================

    spec = sub.add_parser(
        "spec",
        help="Load product specification"
    )

    spec.add_argument(
        "name",
        help="Specification name"
    )

    # ==================================================
    # GENERATE
    # ==================================================

    generate = sub.add_parser(
        "generate",
        help="Generate product from specification"
    )

    generate.add_argument(
        "name",
        help="Specification name"
    )

    # ==================================================
    # RELEASE
    # ==================================================

    release = sub.add_parser(
        "release",
        help="Generate release package"
    )

    release.add_argument(
        "name",
        help="Specification name"
    )

    # ==================================================
    # PDF
    # ==================================================

    sub.add_parser(
        "pdf",
        help="Generate PDF from compiled Markdown"
    )

    # ==================================================
    # PARSE
    # ==================================================

    args = parser.parse_args()

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

    elif args.command == "release":

        build_release(args.name)

    elif args.command == "pdf":

        markdown_to_pdf()

    else:

        parser.print_help()


if __name__ == "__main__":
    main()