import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
AI_KEY = os.getenv("OPENROUTER_API_KEY")
