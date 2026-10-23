import requests

from config import OLLAMA_URL, MODEL


def chat(messages):

    data = {
        "model": MODEL,
        "messages": messages,
        "stream": False
    }

    response = requests.post(
        OLLAMA_URL,
        json=data,
        timeout=120
    )

    response.raise_for_status()

    result = response.json()

    return result["message"]["content"]