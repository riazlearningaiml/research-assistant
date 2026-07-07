import os
import requests
from dotenv import load_dotenv

#Load dot env
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found in .env")

MODEL = "gemini-embedding-2"

URL = (
    f"https://generativelanguage.googleapis.com/v1beta/models/"
    f"{MODEL}:embedContent?key={API_KEY}"
)

def generate_embedding(text: str) -> list[float]:

    """
    Generates an embedding vector for a piece of text using the Gemini API.
    """

    headers = {
        "Content-Type": "application/json"
    }

    body = {
        "model": f"models/{MODEL}",
        "content": 
            {
                "parts": [
                    {
                        "text": text
                    }
                ]
            }
    }

    response = requests.post(
        URL,
        headers=headers,
        json=body,
        timeout=30
    )

    if response.status_code != 200:
        print("Status Code:", response.status_code)
        print(response.text)
        return None

    data = response.json()

    vec = data["embedding"]["values"]

    return vec
