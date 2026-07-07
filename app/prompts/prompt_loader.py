from pathlib import Path

PROMPT_DIR = Path("app/prompts")


def load_prompt(name: str) -> str:
    prompt_file = PROMPT_DIR / name

    return prompt_file.read_text(encoding="utf-8")