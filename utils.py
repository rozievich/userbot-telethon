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


async def forward_message(client, target_group, message, user_name, user_telegram, user_phone, group):
    formatted_message = (
        f"<b>Xabar:</b> {message.text}\n\n"
        f"<b>Ismi:</b> {user_name}\n"
        f"<b>Username:</b> {user_telegram}\n"
        f"<b>Telefon raqam:</b> {f'+{user_phone}' if user_phone else 'Noma’lum'}\n"
        f"<b>Guruh:</b> {group}\n"
        f"<b>Vaqt:</b> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )
    try:
        await client.send_message(target_group, formatted_message, parse_mode='html')
    except Exception as e:
        print(e)
