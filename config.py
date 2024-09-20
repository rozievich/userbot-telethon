import os
from dotenv import load_dotenv


load_dotenv(os.path.join(".env"))


api_id = str(os.getenv("API_ID"))
api_hash = str(os.getenv("API_HASH"))
bot_token = str(os.getenv("BOT_TOKEN"))
filter_words = ("kia", "hunday", "yuk", "isuzi", "gazel", "sprintir", "12 ta viloyat", "qoʻyasiz", "uzum", "shoftoli", "oʻrik", "mol", "qoʻy", "goʻsht", "marojna", "sitrus", "qoʻshimcha", "bosring", "ot", "toy", "oʻtin", "avareniy", "laseti", "koblt", "nexia", "katta", "isuzu", "jiguli", "olma")

main_group_id = -4546126791
