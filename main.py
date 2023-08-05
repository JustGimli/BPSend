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

    if files != "" and files:
        await bot.send_document(int(user_id), document=files)

    if start_cons != "False" and start_cons:
        data = requests.post(f'{os.getenv("URL_PATH")}consultation/create/', {
            'scenario': os.getenv('SCENARIO'),
            'username': os.getenv('USERNAME'),
            'token': os.environ.get('TOKEN'),
            'end_time': os.environ.get('END_TIME'),

        })

        if data.status_code == 201:
            start_message = data.json().get("start_message")

            if start_message:
                await send_message(int(user_id), start_message)

    if (len(message)):
        await send_message(int(user_id), message)
    await bot.close()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
