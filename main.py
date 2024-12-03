import sys
import asyncio
import logging
from datetime import datetime
from random import uniform
from telethon.sync import TelegramClient, events

from config import api_hash, api_id, main_group_id
from utils import check_word, is_sleep_time



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


async def main():
    client = TelegramClient('user_bot', api_id, api_hash)

    async with client:
        @client.on(events.NewMessage(chats=await client.get_dialogs()))
        async def handler(event):
            try:
                if await is_sleep_time():
                    logging.info("Bot 01:00 dan 05:00 gacha to'xtatildi...")
                    await asyncio.sleep(60)  # Har 1 daqiqada vaqtni qayta tekshirish
                    return

                if event.is_group and event.chat_id != main_group_id:
                    message_text = event.message.message.lower()  # Xabar matnini kichik harflarga aylantirish

                    # Xabar ichida filter so'zlar mavjudligini tekshirish
                    if await check_word(message_text):
                        # Foydalanuvchi haqida ma'lumot olish
                        sender = await event.get_sender()
                        user_name = f'<a href="tg://user?id={sender.id}">{sender.first_name}</a>'
                        user_telegram = f"@{sender.username}" if sender.username else "Noma'lum"
                        user_phone = sender.phone
                        group = f"@{event.chat.username}"

                        # Xabarni asosiy guruhga forward qilish
                        await forward_message(client, main_group_id, event.message, user_name, user_telegram, user_phone, group)
                        await asyncio.sleep(uniform(0.033, 1))
            except Exception as e:
                print("Main function error: ", e)
        await client.run_until_disconnected()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
