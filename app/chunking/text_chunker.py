from app.models.document_chunk import DocumentChunk


def chunk_text(
    filename: str,
    text: str,
    chunk_size: int = 50,
    overlap: int = 10
) -> list[DocumentChunk]:

    if overlap >= chunk_size:
        raise ValueError(
            "overlap must be smaller than chunk_size."
        )

    words = text.split()

    step = chunk_size - overlap

    chunks = []

    chunk_id = 1

    for i in range(0, len(words), step):

        chunk_words = words[i:i + chunk_size]

        if not chunk_words:
            break

        chunk = DocumentChunk(
            chunk_id=chunk_id,
            document=filename,
            text=" ".join(chunk_words),
            word_count=len(chunk_words)
        )

        chunks.append(chunk)

        chunk_id += 1

    return chunks