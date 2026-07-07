
from app.services.embedding_service import generate_document_embeddings
from app.embeddings.embedding_client import generate_embedding
from app.storage.chunk_storage import save_chunks
from app.chunking.text_chunker import chunk_text
from app.storage.text_storage import load_text


def chunk_service(filename: str):

    document_text = load_text(filename)

    chunks = chunk_text(filename,document_text)

    embedding_file = generate_document_embeddings(filename, chunks)
    
    chunks_file_path = save_chunks(filename, chunks)

    print(f'Embedding Service: {embedding_file['embedding_file']}')
    return {
        "total_chunks": len(chunks),
        "embedding_file": embedding_file['embedding_file']
    }