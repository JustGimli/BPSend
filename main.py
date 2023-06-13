import asyncio
import os
from aiogram import Bot, Dispatcher

bot = Bot(token=os.getenv(
    "TOKEN", "5311611984:AAE49xLBcV5aa9AMdvnm46vna6VFpM3N92Q"))
dp = Dispatcher(bot=bot)


async def send_message(id, message):
    try:
        await bot.send_message(chat_id=id, text=message)
        print("Сообщение успешно отправлено!")
    except Exception as e:
        print(f"Ошибка при отправке сообщения: {str(e)}")


async def main():
    user_id = os.getenv("USER_ID", "1239134441")
    message = os.getenv("MESSAGE", "Asd")
    await send_message(user_id, message)
    await bot.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
