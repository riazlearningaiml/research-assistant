from app.embeddings.embedding_client import generate_embedding
from app.storage.embedding_storage import save_embeddings
from app.models.document_chunk import DocumentChunk


def generate_document_embeddings(
    filename: str,
    chunks: list[DocumentChunk]
)-> dict:

    for chunk in chunks:

        print(
            f"Embedding Chunk {chunk.chunk_id}"
        )

        chunk.embedding = generate_embedding(chunk.text)

    path = save_embeddings(
        filename,
        chunks
    )
    return {

        "total_chunks": len(chunks),

        "embedding_file": path.name

    }