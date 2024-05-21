import requests
from random import choice, randint
import telebot


url = 'https://raw.githubusercontent.com/iuzhakov/English-Russian-vocabulary/master/words.json'
dictionary = requests.get(url).json()

# для хранения информации о пользователях
users = {}


def generate_question():
    word = choice(dictionary)
    question = f"Как переводится {word['en']}?"
    true_ans = word['ru'].replace('(TR!)', '')
    answers = [choice(dictionary)['ru'].replace('(TR!)', '') for i in range(3)]
    answers.insert(randint(0, 3), true_ans)
    keyboard = telebot.types.InlineKeyboardMarkup()
    for answer in answers:
        keyboard.add(telebot.types.InlineKeyboardButton(answer,
                                                        callback_data=('true' if answer == true_ans else 'false')))
    return question, keyboard
