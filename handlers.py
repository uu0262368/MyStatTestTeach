from ai import ask_ai
from config import commands
from ai_client import get_user_history, add_user_messages, clear_history
prompt_quiz = ""
prompt_formulas = ""

def register_handlers(bot):
    @bot.message_handler(commands=["start"])
    def start(message):
        bot.send_message(message.chat.id, "Привет! Я ИИ-репетитор. Задай любой вопрос по учебе. Для задачи вопроса используйте: /ai [вопрос] Для помощи по командам используйте /help /n")
    @bot.message_handler(commands=["help"])
    def start(message):
        bot.send_message(message.chat.id, commands)
    @bot.message_handler(commands=["ai"])
    def reply(message):
        user_id = message.from_user.id
        user_text = message.text
        add_user_messages(user_id, "user", user_text)
        messages_to_send = get_user_history(user_id)
        answer = ask_ai(messages_to_send)
        bot.send_message(message.chat.id, answer)
        add_user_messages(user_id, "assistant", answer)
    @bot.message_handler(commands=["quiz"])
    def reply(message):
        user_id = message.from_user.id
        user_text = message.text
        add_user_messages(user_id, "user", user_text)
        messages_to_send = get_user_history(user_id)
        answer = ask_ai(messages_to_send)
        bot.send_message(message.chat.id, answer)
        add_user_messages(user_id, "assistant", answer)
    @bot.message_handler(commands=["clear"])
    def reply(message):
        user_id = message.from_user.id
        clear_history(user_id)
    @bot.message_handler(commands=["formulas"])
    def reply(message):
        user_id = message.from_user.id
        user_text = message.text
        add_user_messages(user_id, "user", user_text)
        messages_to_send = get_user_history(user_id)
        answer = ask_ai(messages_to_send)
        bot.send_message(message.chat.id, answer)
        add_user_messages(user_id, "assistant", answer)




