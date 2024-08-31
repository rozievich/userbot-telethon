import os
from dotenv import load_dotenv


load_dotenv(os.path.join(".env"))


api_id = str(os.getenv("API_ID"))
api_hash = str(os.getenv("API_HASH"))
bot_token = str(os.getenv("BOT_TOKEN"))
filter_words = ["salom", "assalomu alaykum", "qanday"]  # Bu yerga kerakli so'zlarni kiriting
main_group_id = -1002173502304
