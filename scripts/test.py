
from app.services.embedding_service import generate_document_embeddings
from app.chunking.text_chunker import chunk_text
from app.storage.chunk_storage import save_chunks
from app.storage.text_storage import load_text

# document = load_text("data/pdfs/Raffann Term 1 Report Card.txt")

# chunks = chunk_text(
#     document,
#     chunk_size=50,
#     overlap=15
# )

# save_chunks(filename="Raffann Term 1 ReportCard_2.txt",chunks=chunks)

# generate_document_embeddings(filename="Raffann Term 1 ReportCard_2.txt",chunks=chunks)

from app.retriever.retriever import (
    load_embeddings,
    retrieve_chunks
)

records = load_embeddings(

    "data/embeddings/Raffann Term 1 ReportCard_2_embeddings.json"

)

chunks = retrieve_chunks(

    question="What are the student's strengths?",

    embedding_records=records,

    top_k=5

)

for chunk in chunks:

    print()

    print(chunk["score"])

    print(chunk["text"][:300])