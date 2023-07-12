import asyncio
import os

import requests
from aiogram import Bot, Dispatcher, types


bot = Bot(token=os.getenv(
    "TOKEN"))
dp = Dispatcher(bot=bot)


async def send_message(id, message):
    try:
        await bot.send_message(chat_id=id, text=message, reply_markup=types.ReplyKeyboardRemove())
    except Exception as e:
        await bot.send_message(chat_id=id, text="Ошибка при отправке сообщения", reply_markup=types.ReplyKeyboardRemove())


async def main():
    user_id = os.getenv("USER_ID")
    message = os.getenv("MESSAGE")
    files = os.getenv('FILES')
    start_cons = os.getenv('CONS', False)

    if files != "":
        for file in files:
            await bot.send_document(user_id, file)

    if start_cons != "False" and start_cons:
        requests.post(f'{os.getenv("URL_PATH")}consultation/create/', {
            'scenario': os.getenv('SCENARIO'),
            'username': os.getenv('USERNAME'),
            'token': os.environ.get('TOKEN'),

        })

        requests.post(f'{os.getenv("URL_PATH")}chats/create/', {
            'chat_id': user_id,
            'username': os.getenv('USERNAME'),
            'token': os.environ.get('TOKEN'),
        })

    await send_message(int(user_id), message)
    await bot.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
