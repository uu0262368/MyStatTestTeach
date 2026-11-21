import requests
from config import AI_KEY

def ask_ai(messages):
    res = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer {AI_KEY}"},
        json={
            "model": "anthropic/claude-haiku-5.5",
            "messages": messages
        }
    )
    return res.json()["choices"][0]["message"]["content"]
