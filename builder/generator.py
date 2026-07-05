from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent


def next_number(folder: Path) -> str:
    """
    Returns the next available 2-digit prompt number.
    Example:
    01
    02
    03
    """

    pattern = re.compile(r"^(\d+)-")

    numbers = []

    if folder.exists():
        for file in folder.glob("*.md"):
            match = pattern.match(file.stem)
            if match:
                numbers.append(int(match.group(1)))

    return f"{(max(numbers) + 1) if numbers else 1:02}"


def create_prompt(category, filename, title):

    template_path = (
        ROOT /
        "automation" /
        "templates" /
        "prompt.md"
    )

    template = template_path.read_text(
        encoding="utf8"
    )

    target = (
        ROOT /
        "prompts" /
        category
    )

    target.mkdir(
        parents=True,
        exist_ok=True
    )

    number = next_number(target)

    final_name = f"{number}-{filename}.md"

    destination = target / final_name

    if destination.exists():
        raise FileExistsError(
            f"{final_name} already exists."
        )

    content = (
        template
        .replace("{{TITLE}}", title)
        .replace(
            "{{USE_CASE}}",
            "Describe when this prompt should be used."
        )
        .replace(
            "{{PROMPT}}",
            "Write your prompt here."
        )
        .replace(
            "{{OUTPUT}}",
            "Describe the expected output."
        )
        .replace(
            "{{TIP}}",
            "Provide a practical recommendation."
        )
    )

    destination.write_text(
        content,
        encoding="utf8"
    )

    print()
    print("SUCCESS")
    print("------------------------------")
    print(destination)
    print()