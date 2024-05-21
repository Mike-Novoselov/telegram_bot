from config import TOKEN

import telebot
import random

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=['text'])
def echo(message):
    if message.text.lower() in ['привет', 'здравствуй', 'добрый день']:
        bot.send_message(message.chat.id, random.choice(['Привет', 'Здравствуй', 'Добрый день']))

    elif message.text == 'Как дела?':
        bot.send_message(message.chat.id, 'Нормально, а твои как?')

    else:
        bot.send_message(message.chat.id, message.text)
        # bot.send_message(message.chat.id, (message.text + ' ') * 10)  # дубль *10


if __name__ == '__main__':
    bot.infinity_polling()


# https://t.me/Sin_bot_Mike_bot



"""
from config import TOKEN

import asyncio
import random
from aiogram import Bot, Dispatcher, types


API_TOKEN = TOKEN  #  API токен 

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


async def echo(message: types.Message):
    if message.text.lower() in ['привет', 'здравствуй', 'добрый день']:
        await message.answer(random.choice(['Привет', 'Здравствуй', 'Добрый день']))

    elif message.text == 'Как дела?':
        await message.answer('Нормально, а твои как?')

    else:
        await message.answer((message.text + ' ') * 10)


@dp.message_handler()
async def echo_message(message: types.Message):
    await echo(message)


async def main():
    # Start bot
    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
"""



