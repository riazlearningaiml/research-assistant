from pathlib import Path

EXTRACTED_DIR = Path("data/extracted")

# Create folder if it doesn't exist
EXTRACTED_DIR.mkdir(parents=True, exist_ok=True)



def save_text(filename: str, text: str) -> str:
    """
    Save extracted text as a .txt file.

    Example:
        report.pdf
            ↓
        report.txt
    """

    txt_filename = Path(filename).stem + ".txt"

    txt_path = EXTRACTED_DIR / txt_filename

    txt_path.write_text(text, encoding="utf-8")

    return str(txt_path)


def load_text(filename: str) -> str:
    """
    Load extracted text from disk.
    """

    txt_file = EXTRACTED_DIR / filename

    if not txt_file.exists():
        raise FileNotFoundError(f"{txt_file} does not exist.")

    return txt_file.read_text(encoding="utf-8")