from ai import ask_ai

def register_handlers(bot):
    @bot.message_handler(commands=["start"])
    def start(message):
        bot.send_message(message.chat.id, "Привет! Я ИИ-репетитор. Задай любой вопрос по учебе.")

    @bot.message_handler()
    def reply(message):
        answer = ask_ai(message.text)
        bot.send_message(message.chat.id, answer)
