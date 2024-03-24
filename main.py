from telethon.sync import TelegramClient
from config import api_hash, api_id


async def send_message_to_user(client, user_id, message):
    await client.send_message(user_id, message)


async def send_message_to_all_users(client, users, message):
    for user in users:
        await client.send_message(user, message)


async def main():
    client = TelegramClient('send_message_data', api_id, api_hash)

    async with client:
        user_ids = [6066967779, -1002078072933]
        for user_id in user_ids:
            await send_message_to_user(client, user_id, "Assalomu alaykum!")
        await send_message_to_all_users(client, user_ids, "Hamma foydalanuvchilarga salom!")


if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
