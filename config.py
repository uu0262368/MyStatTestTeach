import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
AI_KEY = os.getenv("OPENROUTER_API_KEY")

commands = "Команды:/ai [вопрос] - задать вопрос ИИ /help        - помощь по командам /quiz [тема] - сделать мини тест по теме(может быть пустым) /clear       - очистить историю сообщений /formulas    - сводка по теме"
