import json
import os
from pathlib import Path
from app.models.document_chunk import DocumentChunk

EMBEDDING_DIR = Path("data/embeddings")
EMBEDDING_DIR.mkdir(parents=True, exist_ok=True)



def save_embeddings(
    filename: str,
    chunks: list[DocumentChunk]
) -> Path:

    emb_filename = Path(filename).stem + ".json"

    path = EMBEDDING_DIR / emb_filename

    with open(
        path,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            [chunk.to_dict() for chunk in chunks],
            file,
            indent=4,
            ensure_ascii=False
        )

    return path



def load_embeddings(
    filename: str
) -> list[DocumentChunk]:

    path = EMBEDDING_DIR / filename
    print(f'load Embedding path: {EMBEDDING_DIR}')
    print(f'load Embedding filename: {filename}')

    if not path.exists():
        raise FileNotFoundError(f"{path} does not exist.")
    
    with open(
        path,
        "r",
        encoding="utf-8"
    ) as file:

        data = json.load(file)
        #print(f'embedding data')
        

    return [

        DocumentChunk.from_dict(item)

        for item in data

    ]