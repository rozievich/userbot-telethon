from telethon import TelegramClient, events
from config import API_ID, API_HASH, TO_GROUP


# Filtr so'zlari ro'yxati
filter_words = ['odam olamiz', 'yuramiz', 'kishi kerak']

# Telegram klientini yaratish
client = TelegramClient('rozievich', API_ID, API_HASH)

@client.on(events.NewMessage)
async def handler(event):
    # Faqat guruhlardagi xabarlarni qabul qilish
    if event.is_group:
        message_text = event.message.message
        # Filtr so'zlarini tekshirish
        if any(word in message_text for word in filter_words):
            # Xabarni maqsad guruhiga forward qilish
            await client.forward_messages(TO_GROUP, event.message)

async def main():
    # Telegram klientini ishga tushirish
    await client.start()
    print("Bot ishga tushdi.")
    # Botni uzluksiz ishga tushirish
    await client.run_until_disconnected()

if __name__ == '__main__':
    # Asinxron funksiyani ishga tushirish
    client.loop.run_until_complete(main())
