import requests
from config import AI_KEY

def ask_ai(question):
    res = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer {AI_KEY}"},
        json={
            "model": "qwen/qwen3-14b",
            "messages": [
                {"role": "system", "content": "Ты ИИ-репетитор. Объясняй темы просто."},
                {"role": "user", "content": question}
            ]
        }
    )
    return res.json()["choices"][0]["message"]["content"]
