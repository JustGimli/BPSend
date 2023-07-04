import asyncio
import os
from aiogram import Bot, Dispatcher

bot = Bot(token=os.getenv(
    "TOKEN"))
dp = Dispatcher(bot=bot)


async def send_message(id, message):
    try:
        await bot.send_message(chat_id=id, text=message)
        print("Сообщение успешно отправлено!")
    except Exception as e:
        print(f"Ошибка при отправке сообщения: {str(e)}")


async def main():
    user_id = os.getenv("USER_ID")
    message = os.getenv("MESSAGE")
    files = os.getenv('FILES')

    if files:
        for file in files:
            await bot.send_document(user_id, file)

    await send_message(user_id, message)
    await bot.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
