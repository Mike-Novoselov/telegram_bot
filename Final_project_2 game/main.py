from config import TOKEN
from copy import deepcopy

from quiz_eng_ru import *
from game import *


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id, "Привет! что бы узнать, что я умею введи /help")


@bot.message_handler(commands=['help'])
def help(msg):
    text = "Доступные команды: \n"
    text += "/quiz - запуск викторины \n"
    text += "/game - запуск игры \n"
    text += "/help - помощь \n"
    bot.send_message(msg.chat.id, text)


@bot.message_handler(commands=['quiz'])
def start_quiz(msg):
    users[msg.from_user.id] = {"current_que": 1, "score": 0, "id_msg": None}
    question, keyboard = generate_question()
    bot_msg = bot.send_message(msg.chat.id, question, reply_markup=keyboard)
    users[msg.from_user.id]['id_msg'] = bot_msg.message_id


@bot.callback_query_handler(func=lambda call: call.data in ['true', 'false'])
def next_question(call):
    if call.data == 'true':
        text = 'Верно\n'
        # увеличиваем счет
        users[call.from_user.id]['score'] += 1
    else:
        text = 'Неверно\n'
    if users[call.from_user.id]['current_que'] < 5:
        users[call.from_user.id]['current_que'] += 1
        question, keyboard = generate_question()
        bot.edit_message_text(text + question, call.message.chat.id, users[call.from_user.id]['id_msg'], reply_markup=keyboard)
    else:
        bot.edit_message_text(text + f'Ты набрал {users[call.from_user.id]["score"]} из 5 баллов',
                              call.message.chat.id, users[call.from_user.id]["id_msg"])


@bot.message_handler(commands=['game'])
def start_game(msg):
    # 'cur_pos' - текущая позиция игрока (название локации)
    # 'coins' - баланс монет
    # 'items' - предметы в арсенале у игрока
    # 'loc' - глубокая копия словаря локаций
    # 'msg_id' - id сообщения ботка (для изменения сообщений)
    users_info[msg.from_user.id] = {'cur_pos': '1', 'coins': 0, 'items': [], 'loc': deepcopy(locations), 'msg_id': None}
    text, keyboard = generate_story(msg.from_user.id)
    msg_bot = bot.send_message(msg.chat.id, text, reply_markup=keyboard)
    users_info[msg.from_user.id]['msg_id'] = msg_bot.message_id


@bot.callback_query_handler(func=lambda call: call.data in locations)
def next_move(call):
    users_info[call.from_user.id]['cur_pos'] = call.data
    text, keyboard = generate_story(call.from_user.id)
    bot.edit_message_text(text, call.message.chat.id, users_info[call.from_user.id]['msg_id'], reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data.startswith('item '))
def get_item(call):
    # берем название предмета
    item = call.data.replace('item ', '')
    # если название предмета начинается с подстроки 'золото: '
    if item.startswith('золото: '):
        # добавляем на баланс пользователю монеты
        users_info[call.from_user.id]['coins'] += int(item.replace('золото: ', ''))
    else:
        # добавляем предмет в список предметов пользователя
        users_info[call.from_user.id]['items'].append(item)
    # берем название текущей локации пользователя
    current_pos = users_info[call.from_user.id]['cur_pos']
    # удаляем собранный предмет из локации
    users_info[call.from_user.id]['loc'][current_pos]['items'].remove(item)
    text, keyboard = generate_story(call.from_user.id)
    bot.edit_message_text(text, call.message.chat.id, users_info[call.from_user.id]['msg_id'], reply_markup=keyboard)
    # показываем уведомление о взятии предмета
    bot.answer_callback_query(call.id, f'Вы взяли предмет - {item}')


@bot.callback_query_handler(func=lambda call: call.data.startswith('exchange '))
def change_items(call):
    # берем название текущей локации пользователя
    current_pos = users_info[call.from_user.id]['cur_pos']
    # берем название первого предмета (который отдает пользователь)
    item_1 = call.data.replace('exchange ', '')
    # берем название второго предмета (который получает пользоваетль)
    item_2 = users_info[call.from_user.id]['loc'][current_pos]['exchange'][item_1]

    # если название предмета (который отдает пользователь) начинается с 'золото: '
    if item_1.startswith('золото: '):
        # отнимаем нужное кол-во монет у пользователя
        users_info[call.from_user.id]['coins'] -= int(item_1.replace('золото: ', ''))
    else:
        # удаляем предмет из списка предметов пользователя
        users_info[call.from_user.id]['items'].remove(item_1)

    # если название предмета (который получает пользователь) начинается с 'золото: '
    if item_2.startswith('золото: '):
        # прибавляем нужное кол-во монет пользователю
        users_info[call.from_user.id]['coins'] += int(item_2.replace('золото: ', ''))
    else:
        # добавляем предмет в список предметов пользователя
        users_info[call.from_user.id]['items'].append(item_2)

    if item_2 == 'выход':
        bot.edit_message_text('Ура, ты победил!', call.message.chat.id, users_info[call.from_user.id]['msg_id'])
    else:
        text, keyboard = generate_story(call.from_user.id)
        bot.edit_message_text(text, call.message.chat.id, users_info[call.from_user.id]['msg_id'],
                              reply_markup=keyboard)
        # показываем уведомление о взятии предмета
        bot.answer_callback_query(call.id, f'Вы обменяли предмет {item_1} на {item_2}')


@bot.callback_query_handler(func=lambda call: call.data == 'backpack')
def show_items(call):
    # берем все предметы пользователя (список)
    items = users_info[call.from_user.id]['items']
    # если список не пуст
    if items:
        # генерируем текст с названиями предметов
        text = 'Ваши предметы: ' + ', '.join(items)
        # показываем список предметов пользователя в уведомлении
        bot.answer_callback_query(call.id, text, show_alert=True)
    else:
        bot.answer_callback_query(call.id, 'Ваш рюкзак пуст', show_alert=True)


@bot.callback_query_handler(func=lambda call: call.data == 'balance')
def show_balance(call):
    bot.answer_callback_query(call.id, f'Ваш баланс: {users_info[call.from_user.id]["coins"]} монет', show_alert=True)


if __name__ == '__main__':
    bot.infinity_polling()
