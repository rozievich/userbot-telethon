from datetime import datetime
from config import block_list, filter_words


async def check_word(message: str) -> bool:
    if any(block in message for block in block_list):
        return False
    elif any(word in message for word in filter_words):
        return True
    else:
        return False


async def is_sleep_time():
    """02:00 dan 05:00 gacha botni to'xtatish."""
    now = datetime.now()
    if now.hour >= 1 and now.hour < 5:  # Agar hozir 01:00 dan 05:00 oralig'ida bo'lsa
        return True
    return False
