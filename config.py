import os
from dotenv import load_dotenv


load_dotenv(os.path.join(".env"))


api_id = str(os.getenv("API_ID"))
api_hash = str(os.getenv("API_HASH"))
filter_words = ("kia", "hunday", "yuk", "isuzi", "gazel", "sprintir", "12 ta viloyat", "qoʻyasiz", "uzum", "shoftoli", "oʻrik", "mol", "qoʻy", "goʻsht", "marojna", "sitrus", "qoʻshimcha", "bosring", "ot", "toy", "oʻtin", "avareniy", "laseti", "koblt", "nexia", "katta", "isuzu", "jiguli", "olma", "Юк", "юк", "Anor", "Olma", "Узум")
block_list = ("fura", "Фура", "фура", "yuk olamiz", "юк оламиз", "Юк оламиз")

main_group_id = -1002431469752
