import sys
import asyncio
import logging
from random import uniform
from telethon.sync import TelegramClient, events

from config import api_hash, api_id, main_group_id
from utils import check_word, is_sleep_time, forward_message



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
                        if event.chat:
                            group = f"@{event.chat.username}"
                        else:
                            group = f"Maxfiy Guruh"

                        # Xabarni asosiy guruhga forward qilish
                        await forward_message(client, main_group_id, event.message, user_name, user_telegram, user_phone, group, sender.id)
                        await asyncio.sleep(uniform(0.033, 1))
            except Exception as e:
                print("Main function error: ", e)
        await client.run_until_disconnected()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
