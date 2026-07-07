
from app.retriever.retriever import retrieve_chunks
from app.llm.client import generate_answer
from app.prompts.prompt_loader import load_prompt
from app.storage.embedding_storage import load_embeddings

def answer_question(filename: str, question: str):
    print(filename)
    print(question)
    chunks = load_embeddings(filename)
    print("\n records\n",chunks)
    chunks = retrieve_chunks(question, chunks, top_k=10)
    print("\n retrieve_chunks\n",chunks)

    context= '\n\n'.join(chunk.text for chunk in chunks)
    print(f'\n context\n',context)
    template = load_prompt('qa_prompt.txt')

    prompt = template.format(
        document=context,
        question=question
    )

    print(prompt)
    
    answer = generate_answer(prompt)
    print("\n answer\n",answer)
    return {
        "answer": answer,
        "retrieved_chunks": chunks
    }
