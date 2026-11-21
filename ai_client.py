user_histories = {}

system_prompt = {
    "role": "system",
    "conteny": "Ты - опытный репититор. Объясняй темы понятно. если видишь /ai просто ответь на вопро. Если видишь /quiz составь мини тест на тему. Если пустота,то возьми с контекста. Елси /formulas то составь сводку о теме"
}


def get_user_history(user_id):
    if user_id not in user_histories:
        user_histories[user_id] = [system_prompt.copy()]
    return user_histories[user_id]
def add_user_messages(user_id, role, text):
    history = get_user_history(user_id)
    history.append({"role": role, "content": text})
    if len(history) > 16:
        user_histories[user_id] = [history[0] + history[-15]]

def clear_history(user_id):
    user_histories[user_id] = [system_prompt.copy()]
