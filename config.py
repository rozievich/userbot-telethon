import os
from dotenv import load_dotenv


load_dotenv(os.path.join(".env"))


api_id = str(os.getenv("API_ID"))
api_hash = str(os.getenv("API_HASH"))
bot_token = str(os.getenv("BOT_TOKEN"))
