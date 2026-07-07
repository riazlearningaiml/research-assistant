import json
import os
from pathlib import Path
from app.models.document_chunk import DocumentChunk

CHUNK_DIR = Path("data/chunks")
CHUNK_DIR.mkdir(parents=True, exist_ok=True)


def save_chunks(
    filename: str,
    chunks: list[DocumentChunk]
) -> str:

    base = Path(filename).stem

    save_path = CHUNK_DIR / f"{base}_chunks.json"

    with open(
        save_path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            [chunk.to_dict() for chunk in chunks],
            file,
            indent=4,
            ensure_ascii=False
        )

    return str(save_path)


def load_chunks(
    filename: str
) -> list[DocumentChunk]:

    base = os.path.splitext(filename)[0]

    path = os.path.join(
        CHUNK_DIR,
        f"{base}_chunks.json"
    )

    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)

    return [
        DocumentChunk.from_dict(item)
        for item in data
    ]