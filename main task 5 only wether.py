from config import TOKEN
import telebot
import random
import logging
import requests

#____________________________________________________________________________#

# настрока логирования
logging.basicConfig(filename='bot_log.log',
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    encoding='utf-8')

#____________________________________________________________________________#
# Создание экземпляра класса TeleBot (создание нашего бота)
bot = telebot.TeleBot(TOKEN)


# команда для бота /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"добрый день, {message.from_user.username}")


# команда для бота /get_info
@bot.message_handler(commands=['get_info'])
def start(message):
    send = bot.send_message(message.chat.id, '''Что именно вы хотите узнать?
                                                    \n/file_name - Ваше имя
                                                    \n/user_name - Ваш ник
                                                    \n/last_name - Вашу фамилию''')
    bot.register_next_step_handler(send, info)


def info(message):
    if message.text == 'first_name':
        bot.send_message(message.chat.id, message.from_user.first_name)
    elif message.text == 'user_name':
        bot.send_message(message.chat.id, message.from_user.user_name)
    elif message.text == 'last_name':
        bot.send_message(message.chat.id, message.from_user.last_name)
    else:
        bot.send_message(message.chat.id, "Я такого не знаю")


@bot.message_handler(commands=['help'])
def help(message):
    text = '''
    Я поддерживаню следующие команды:
    /start - Вывод приветствия
    /get_info - Информация о пользователе
    /motivation - рандомная цитата
    /help - Помощь
    /photo - фоточки)
    /local_photo - локал фоточки)
    /music - музыка
    /venue - локация(заранее заданная)
    /dice - кости
    /game1 - Игра отгадай число (на данном релизе отключил)
    /game2  - Камень ножнецы бумага
    /weather_old - Погода
    /weather_new - Погода с локой
    /yeas_or_not - Случайный ДА или НЕТ
    '''
    bot.send_message(message.chat.id, text)


#____________________________________________________________________________#
# логика для погоды с локацией


'''def current_weather(lat, lon):
    url = f'https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,rain,showers,snowfall,weather_code,wind_speed_10m,wind_direction_10m,wind_gusts_10m&wind_speed_unit=ms&timezone=Europe%2FMoscow&forecast_days=1'
    r = requests.get(url).json()['current']

    text = ""
    text += f'Температура: {r["temperature_2m"]} °C\n'
    text += f'Влажность: {r["relative_humidity_2m"]} %\n'
    text += f'Ощущаемая температура: {r["apparent_temperature"]} °C\n'

    if r["precipitation"] == 0:
        text += "Осадков нет\n"
    else:
        if r["rain"] != 0:
            text += f'Дождь {r["rain"]} мм.\n'
        if r["showers"] != 0:
            text += f'Ливень {r["showers"]} мм.\n'
        if r["snowfall"] != 0:
            text += f'Снегопад {r["snowfall"]} мм.\n'

    return text
'''


def current_weather(lat, lon):
    '''requests запрос на json'''
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min,wind_speed_10m_max&timezone=Asia%2FBangkok&forecast_days=3"
    r = requests.get(url).json()['daily']
    return format_weather_forecast(r)


def format_weather_forecast(weather_data):
    '''формирование удобочитаемой даты'''
    forecast_text = ""
    for i in range(len(weather_data['time'])):
        forecast_text += f"Прогноз погоды на {weather_data['time'][i]}\n"
        forecast_text += f"Максимальная температура: {weather_data['temperature_2m_max'][i]}\n"
        forecast_text += f"Минимальная температура: {weather_data['temperature_2m_min'][i]}\n"
        forecast_text += f"Скорость ветра: {weather_data['wind_speed_10m_max'][i]}\n\n"
    return forecast_text


# Погода с локой
@bot.message_handler(commands=['weather_new'])
def send_keyboard(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = telebot.types.KeyboardButton('Поделитесь местоположением', request_location=True)
    keyboard.add(button)
    bot.send_message(message.chat.id, 'Привет! поделись местоположением', reply_markup=keyboard)


@bot.message_handler(content_types=['location'])
def send_weather(message):

    weatherZ = current_weather(message.location.latitude, message.location.longitude)

    a = telebot.types.ReplyKeyboardRemove()

    bot.send_message(message.chat.id, weatherZ, reply_markup=a)

    print(message.location.latitude, message.location.longitude, message.from_user.first_name)
    # Логирования сообщения в файл _________________________________________
    logging.info(f'GeoLoca {message.from_user.first_name, message.from_user.username}: {message.location.latitude, message.location.longitude}')


#____________________________________________________________________________#
# команда для бота /motivation


motivation_quotes = (
    'Сила – не в бабках. Ведь бабки – уже старые',
    'Из проведённых 64-х боёв у меня 64 победы. Все бои были с тенью',
    'Взял нож - режь, взял дошик - ешь',
    'Я живу, как карта ляжет. Ты живёшь, как мамка скажет',
    'Никогда не сдавайтесь, идите к своей цели! А если будет сложно – сдавайтесь.',
    'Если заблудился в лесу, иди домой.',
    'Запомни: всего одна ошибка – и ты ошибся.',
    'Я вообще делаю что хочу. Хочу импланты — звоню врачу.',
    'В жизни всегда есть две дороги: одна — первая, а другая — вторая',
    'Мы должны оставаться мыми, а они – оними',
    'Делай, как надо. Как не надо, не делай',
    'Сниму квартиру. Порядок на районе гарантирую',
    'Работа — это не волк. Работа — ворк. А волк — это ходить',
    'Не будьте эгоистами, в первую очередь думайте о себе!',
    'Марианскую впадину знаешь? Это я упал',
    'Как говорил мой дед, «Я твой дед»',
    'Без подошвы тапочки — это просто тряпочки',
    'Слово - не воробей. Вообще ничто не воробей, кроме самого воробья',
    'Жи - ши пиши от души.'
)


@bot.message_handler(commands=['motivation'])
def send_motivation(message):
    bot.send_message(message.chat.id, random.choice(motivation_quotes))


#____________________________________________________________________________#
# Фото по ссылке
pic_link = (
    'https://bugaga.ru/uploads/posts/2017-03/1489052030_kotik-hosiko-12.jpg',
    'https://cs14.pikabu.ru/post_img/2023/12/31/1/1703973860125993095.jpg',
    'https://cs14.pikabu.ru/post_img/big/2023/12/21/2/170311777011298346.png',
    'https://cs14.pikabu.ru/post_img/big/2023/12/15/5/1702627067114180148.png',
    'https://cs13.pikabu.ru/post_img/big/2023/12/05/9/170179187211421308.jpg',
    'https://cs14.pikabu.ru/post_img/big/2023/11/13/6/1699867796187852957.jpg',
    'https://cs14.pikabu.ru/post_img/big/2023/11/03/4/1698991096171453909.png',
    'https://cs13.pikabu.ru/post_img/big/2023/08/30/7/1693392423140685214.jpg',
    'https://cs13.pikabu.ru/post_img/2023/07/26/3/1690337224114874057.jpg',
    'https://cs14.pikabu.ru/post_img/2023/07/03/9/1688393540140866945.jpg'
)


@bot.message_handler(commands=['photo'])
def send_photo(message):
    bot.send_photo(message.chat.id, random.choice(pic_link))


# Фото с ПК
pic_lockal = (
    'pic (1).jpg',
    'pic (2).jpg',
    'pic (3).jpg',
    'pic (4).jpg',
    'pic (5).jpg',
    'pic (6).jpg',
    'pic (7).jpg',
    'pic (8).jpg'
)


@bot.message_handler(commands=['local_photo'])
def send_local_photo(message):
    bot.send_photo(message.chat.id, open(f'img/{random.choice(pic_lockal)}', 'rb'))


#____________________________________________________________________________#
# Игра отгадай число
'''
@bot.message_handler(commands=['game1'])
def send_game(message):
    #создаем клавиатуру
    keyboard = telebot.types.InlineKeyboardMarkup()

    lst = []
    for i in range(5):
        # добавление кнопки с вариантами ответов
        lst.append(telebot.types.InlineKeyboardButton(text="⭐",
                                                      callback_data=str(i)))
    keyboard.row(*lst)
    bot.send_message(message.chat.id, 'Что выберешь?', reply_markup=keyboard)


@bot.callback_query_handler(func= lambda call: True)
def callback_query(call):
    # Если случайное число от 0 до 4 равно выбранному значению
    if random.randint(0,4) == int(call.data):
        bot.send_photo(call.message.chat.id,
                       'https://proprikol.ru/wp-content/uploads/2020/07/ehidnaya-ulybka-prikolnye-kartinki-6.jpg',
                       'Поздравляю, ты победил')
    else:
        bot.send_photo(call.message.chat.id,
                       'https://krasivosti.pro/uploads/posts/2021-04/1617884613_13-p-pechalnii-kot-14.jpg',
                       'Увы, ты проиграл')
'''


#____________________________________________________________________________#
# Обработчик команды /game2
@bot.message_handler(commands=['game2'])
def send_game(message):
    # Создаем клавиатуру
    keyboard = telebot.types.InlineKeyboardMarkup()

    # Добавляем кнопки для камня, ножниц и бумаги
    keyboard.row(
        telebot.types.InlineKeyboardButton(text="Камень", callback_data="rock"),
        telebot.types.InlineKeyboardButton(text="Ножницы", callback_data="scissors"),
        telebot.types.InlineKeyboardButton(text="Бумага", callback_data="paper")
    )

    bot.send_message(message.chat.id, 'Выбери: камень, ножницы или бумага?', reply_markup=keyboard)


# Обработчик callback-запросов
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    # Список вариантов хода бота
    choices = ["rock", "scissors", "paper"]

    # Выбираем случайный ход бота
    bot_choice = random.choice(choices)

    # Определяем результат игры
    if bot_choice == call.data:
        result = "Ничья!"
    elif (call.data == "rock" and bot_choice == "scissors") or \
            (call.data == "scissors" and bot_choice == "paper") or \
            (call.data == "paper" and bot_choice == "rock"):
        result = "Поздравляю, вы победили!"
    else:
        result = "Увы, вы проиграли."

    bot.send_message(call.message.chat.id, f"Вы выбрали {call.data}. Я выбрал {bot_choice}. {result}")



#____________________________________________________________________________#
# Аудио
sound_lockal_link = (
    'FIZICA feat. VENERA - В области сердца.mp3',
    'FIZICA feat. Нуна - Я. Ты. Эксперимент.mp3'
)


@bot.message_handler(commands=['music'])
def send_music(message):
    bot.send_audio(message.chat.id, open(f'media/{random.choice(sound_lockal_link)}', 'rb'))
    # bot.send_audio(message.chat.id, open(f'media/{random.choice(sound_lockal_link)}', 'rb'),
    #                caption='caption text',
    #                title='title text')

#____________________________________________________________________________#
# Локация встречи


@bot.message_handler(commands=['venue'])
def send_ven(message):
    bot.send_venue(message.chat.id, 59.991830, 29.776847, 'Кронштадт', 'Санкт-Питербург')

#____________________________________________________________________________#
# кости


@bot.message_handler(commands=['dice'])
def dice(message):
    dice_result = random.randint(1, 6)
    bot.send_message(message.chat.id, f"Вы бросили кость и выпало число: {dice_result}")

#____________________________________________________________________________#
# Погода


@bot.message_handler(commands=['weather_old'])
def weather(message):
    city = 'Абакан'
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
    weather_data = requests.get(url).json()

    temperature = round(weather_data['main']['temp'])
    temperature_feel = round(weather_data['main']['feels_like'])
    description = weather_data['weather'][0]['description']

    response = f"Сейчас в городе {city}: {temperature}°C\n"
    response += f"Ощущается как: {temperature_feel}°C\n"
    response += f"Погодные условия: {description}"

    bot.send_message(message.chat.id, response)


#____________________________________________________________________________#
# yeas_or_not


@bot.message_handler(commands=['yeas_or_not'])
def send_rand_yeas_or_not(message):

    r = requests.get('https://yesno.wtf/api').json()

    url = r["image"]

    ans = r["answer"]

    bot.send_animation(message.chat.id, url, caption=ans)


#____________________________________________________________________________#
# обработка приветствия


@bot.message_handler(func=lambda x: x.text.lower() in ['привет', 'здравствуйте', 'добрый день'])
def say_hello(message):
    bot.send_message(message.chat.id, random.choice(['Привет😉', 'Здравствуйте😎', 'Добрый день 🤖']))

#____________________________________________________________________________#


# обработка событий (текст)
@bot.message_handler(content_types=['text'])
def echo(message):
    # Логирования сообщения в файл _________________________________________
    logging.info(f'Message from {message.from_user.username}: {message.text}')

    bot.send_message(message.chat.id, (message.text + ' - *** упс непредвиденное слово *** ') * 1)


# обработка событий (стикер)
@bot.message_handler(content_types=['sticker'])
def get_sticker(message):
    bot.send_message(message.chat.id, f'ID Твоего стикера - {message.sticker.file_id}')


# обработка событий (закреп сообщения)
@bot.message_handler(content_types=['pinned_message'])
def pin(message):
    bot.send_message(message.chat.id, f'{message.from_user.first_name} Опять что-то закрепил.')


# if __name__ == '__main__':
bot.infinity_polling()



# https://t.me/Sin_bot_Mike_bot



