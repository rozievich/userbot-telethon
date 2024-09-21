import sys
import asyncio
import logging
from telethon.sync import TelegramClient, events
from config import api_hash, api_id, filter_words, main_group_id, block_list



async def check_word(message: str) -> bool:
    if any(block in message for block in block_list):
        return False
    elif any(word in message for word in filter_words):
        return True
    else:
        return False


async def forward_message(client, target_group, message, user_name, user_telegram, user_phone, group):
    formatted_message = f"<b>Xabar:</b> {message.text}\n\n<b>Ismi:</b> {user_name}\n<b>Username:</b> {user_telegram}\n<b>Telefon raqam:</b> {f'+{user_phone}' if user_phone else 'Noma’lum'}\n<b>Guruh:</b> {group}"
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
                        await asyncio.sleep(0.033)
            except Exception as e:
                print("Main function error: ", e)


        await client.run_until_disconnected()

if __name__ == '__main__':
    # Barcha loglarni chiqarib borish uchun
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    # Asinxron funksiyani ishga tushirish
    asyncio.run(main())
