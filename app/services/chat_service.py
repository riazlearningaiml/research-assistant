
from app.storage.text_storage import load_text
from app.prompts.prompt_loader import load_prompt
from app.llm.client import generate_answer

def ask_question(filename:str, question:str)->str:
    
    document = load_text(filename)
    prompt_template = load_prompt("qa_prompt.txt")

    prompt = prompt_template.format(
        document=document,
        question=question
    )

    answer = generate_answer(prompt)

    return {
        "question": question,
        "answer": answer
    }