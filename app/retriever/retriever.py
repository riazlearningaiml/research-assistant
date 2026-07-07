from app.models.document_chunk import DocumentChunk
import json
from app.embeddings.embedding_client import generate_embedding
from app.retriever.similarity import cosine_similarity

# def load_embeddings(path: str):

#     with open(
#         path,
#         "r",
#         encoding="utf-8"
#     ) as file:

#         return json.load(file)


def retrieve_chunks(
    question: str,
    chunks: list[DocumentChunk],
    top_k: int = 3
):

    question_embedding = generate_embedding(
        question
    )
    #print('Embedding Question:',question_embedding)
    for chunk in chunks:

        chunk.similarity_score = cosine_similarity(

            question_embedding,

            chunk.embedding

        )
        print("\n similarity_score : \n", chunk.similarity_score)

    chunks.sort(

        key=lambda chunk: chunk.similarity_score,

        reverse=True

    )

    print('retreived chunks', chunks[:top_k])
    return chunks[:top_k]