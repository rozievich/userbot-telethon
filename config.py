import os
from dotenv import load_dotenv


load_dotenv(os.path.join(".env"))


API_ID = str(os.getenv("API_ID"))
API_HASH = str(os.getenv("API_HASH"))
TO_GROUP = str(os.getenv("TO_GROUP_ID"))
