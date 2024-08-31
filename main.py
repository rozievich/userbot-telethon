from telethon.sync import TelegramClient, events
from config import api_hash, api_id, filter_words, main_group_id



async def forward_message(client, target_group, message, user_name, user_telegram, user_phone):
    formatted_message = f"Xabar: {message.text}\nUserning ismi: {user_name}\nTelegram Username: {user_telegram}\nTelefon raqam: {user_phone or 'Noma’lum'}"
    await client.send_message(target_group, formatted_message)


async def main():
    client = TelegramClient('taxi_bot', api_id, api_hash)

    async with client:
        @client.on(events.NewMessage(chats=await client.get_dialogs()))
        async def handler(event):
            if event.is_group and event.chat_id != main_group_id:
                message_text = event.message.message.lower()  # Xabar matnini kichik harflarga aylantirish

                # Xabar ichida filter so'zlar mavjudligini tekshirish
                if any(word in message_text for word in filter_words):
                    # Foydalanuvchi haqida ma'lumot olish
                    sender = await event.get_sender()
                    user_name = sender.first_name
                    user_telegram = f"@{sender.username}" if sender.username else "Noma'lum"
                    user_phone = sender.phone

                    # Xabarni asosiy guruhga forward qilish
                    await forward_message(client, main_group_id, event.message, user_name, user_telegram, user_phone)

        print("Bot ishlamoqda...")
        await client.run_until_disconnected()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
