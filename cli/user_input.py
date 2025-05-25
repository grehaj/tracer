"""
    Modul to collecting user data
"""


def input_from_choices(prompt: str, choices: list[str], default : str = None) -> str:
    choices_display = "/".join(choices)
    while True:
        value = input(f"{prompt} ({choices_display}): ").strip()
        if value in choices:
            return value
        if default is not None:
            return default
        print(f"Invalid input. Please choose one of: {', '.join(choices)}")