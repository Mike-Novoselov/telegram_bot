import telebot


"""locations = {
    '1': {
        'text': 'Ты только что вышел из затемненного коридора и оказался внутри густого леса. Высокие деревья тянутся к небу, создавая густой зеленый потолок над твоей головой. Мягкий шум листьев под твоими ногами создает атмосферу спокойствия, но в то же время напоминает тебе о том, что ты не один в этом диком месте. Но за этой красотой лежит тайна и опасность, и ты должен быть осторожен, исследуя этот лес.',
        'items': [],
        'next_move': {
            'К приключениям': '2'
        },
        'exchange': {}
    },
    '2': {
        'text': 'Путешественник, перед тобой разветвление тропинок. Первая тропинка ведет к густому зарослю, из которого доносится загадочное шуршание. Вторая тропинка уводит в темный лес, где свет едва проникает сквозь густую листву. Третья тропинка ведет к подземелью. Теперь предстоит сделать выбор, путник. Куда ты направишься?',
        'items': [],
        'next_move': {
            'Первая тропинка': '3',
            'Вторая тропинка': '4',
            'Третья тропинка': '5'
        },
        'exchange': {}
    },
    '3': {
        'text': 'К сожалению, путник, если ты выбрал первую тропинку, тебе не повезло. Ты все глубже погружался в густой заросль, но, когда попытался развернуться, обнаружил, что потерял путь. Внезапно, шорох в кустах заставил тебя обернуться, и ты увидел враждебное существо, благодаря твоему любопытству, теперь твое приключение закончилось.',
        'items': [],
        'next_move': {},
        'exchange': {}
    },
    '4': {
        'text': 'Путник, идя по второй тропинке, ты выходишь на открытое поле, где тебя ждет торговец. Он предлагает разнообразные товары и снаряжение, которые могут быть полезны в твоем приключении. Улыбаясь, он ждет, чтобы ты обратил внимание на его товары. Это место представляет собой небольшую оазисную точку в твоем путешествии, где ты можешь пополнить запасы и обменяться информацией с этим таинственным торговцем.',
        'items': [],
        'next_move': {
            'Вернуться к развилке': '2'
        },
        'exchange': {
            'шкатулка': 'золото: 3'
        }
    },
    '5': {
        'text': 'Путник, когда ты подходишь к входу подземелья, ты видишь перед собой мрачный лес, где деревья склоняются к земле, словно приветствуя тебя своими древними ветвями. Таинственный туман покрывает окрестности, создавая атмосферу загадочности и опасности. Перед тобой лежит вход в подземелье, окруженный мрачной аурой, предвещающей множество опасностей и тайн, ждущих своего исследователя.',
        'items': [],
        'next_move': {
            'Осмотреться рядом': '6',
            'Войти в подземелье': '7',
            'Вернуться к развилке': '2'
        },
        'exchange': {}
    },
    '6': {
        'text': 'Путник, когда ты пытаешься найти что-то вокруг подземелья, ты обнаруживаешь следы древних руин, скрытые среди густой растительности. Эти развалины могут скрывать древние артефакты или секретные входы в подземелье. Ты побродил еще немного в надежде что-то найти...',
        'items': ['шкатулка'],
        'next_move': {
            'Вернуться к подземелью': '5'
        },
        'exchange': {}
    },
    '7': {
        'text': 'Путник, когда ты исследуешь лабиринты подземелья, за поворотом туннеля ты видишь мрачный коридор, освещенный лишь тусклым светом факелов. Стены усыпаны древними рунами, излучающими таинственную энергию. Вдалеке слышен шум водопада, а в воздухе витает запах земли и мха. Это место кажется наполненным древней магией и тайнами, приглашая тебя на дальнейшее исследование.',
        'items': ['золото: 2'],
        'next_move': {
            'Пойти к туннелю': '8',
            'Вернуться на улицу': '5'
        },
        'exchange': {}
    },
    '8': {
        'text': 'Путник, когда ты находишься внутри туннеля, впереди тебя простирается мрачная атмосфера, освещенная лишь тусклым светом факелов, бьющихся в стену. Стены покрыты влажными мхом и лишайником, а в воздухе пахнет землей и стариной. Звуки твоих шагов отдается от стен, создавая призрачные эхо, словно туннель наполнен загадками и тайнами, ждущими своего откровения. В дали виднеется тусклый свет, указывающий на возможный выход из этих забытых глубин.',
        'items': [],
        'next_move': {
            'Пойти к выходу': '9',
            'Вернуться назад': '7'
        },
        'exchange': {}
    },
    '9': {
        'text': 'Вы находитесь в темном туннеле, где тусклый свет факелов едва освещает окружающее. По мере продвижения вперед, вы замечаете фигуру стража, стоящего у выхода. Он строго смотрит на вас и говорит: "Для прохода через этот выход, вам нужно заплатить 5 монет". Ваше приключение зависит от вашего выбора - заплатить или найти другой путь.',
        'items': [],
        'next_move': {
            'Вернуться назад': '8'
        },
        'exchange': {
            'золото: 5': 'выход'
        }
    }
}
"""

locations = {
    '1': {
        'text': 'Ты находишься в темном подвале заброшенного особняка. Здесь витает атмосфера ужаса и таинственности. Звуки скрипящих дверей и шагов доносятся из темных углов, а холодный ветер заставляет тебя дрожать. Осторожно исследуй этот мрачный уголок.',
        'items': ['маска ужаса', 'книга некромантии'],
        'next_move': {
            'Пойти в темную комнату': '2',
            'Посмотреть в окно': '3',
            'Вернуться к лестнице': '4'
        },
        'exchange': {}
    },
    '2': {
        'text': 'Ты зашел в темную комнату, где тени играют с твоим разумом. Чувствуется присутствие зловещих сил, а воздух наполняется запахом гнили. Что-то ждет тебя в этой мрачной глубине...',
        'items': ['амулет проклятия', 'флакон с ядом'],
        'next_move': {
            'Исследовать дальше': '5',
            'Вернуться обратно': '1'
        },
        'exchange': {}
    },
    '3': {
        'text': 'Из окна виден старый кладбищенский двор, покрытый мертвыми листьями и окутанный туманом. Твои глаза не могут оторваться от темных фигур, бродящих между надгробиями. Что-то зловещее приближается...',
        'items': ['свеча с лиловым пламенем', 'кость скелета'],
        'next_move': {
            'Выйти на кладбище': '6',
            'Вернуться обратно': '1'
        },
        'exchange': {}
    },
    '4': {
        'text': 'Лестница скрипит под твоими ногами, когда ты поднимаешься наверх. Твое сердце бьется в унисон с каждым шагом, а холодный ветер не унимается. Не оглядывайся, пока не доберешься до вершины...',
        'items': [],
        'next_move': {
            'Открыть дверь': '7',
            'Вернуться обратно': '1'
        },
        'exchange': {}
    },
    '5': {
        'text': 'Ты оказался в забытом погребе, где темные силы тянут тебя в свою бездну. Воздух насыщен запахом гнили и смерти. Будь осторожен, ведь здесь скрываются мрачные тайны...',
        'items': ['кристалл тьмы', 'костяная фигура'],
        'next_move': {
            'Исследовать глубже': '8',
            'Вернуться обратно': '2'
        },
        'exchange': {}
    },
    '6': {
        'text': 'Ты оказался среди могил и надгробий, окруженных мрачным мраком. Зловещие силы поджидают тебя за каждым углом, готовые обрушить свой ужас на невинного путника. Будь начеку, ведь смерть следит за тобой...',
        'items': ['костяные черепа', 'гробничный ключ'],
        'next_move': {
            'Продолжить исследование': '9',
            'Вернуться обратно': '3'
        },
        'exchange': {}
    },
    '7': {
        'text': 'Дверь за тобой закрывается, оставляя тебя один на один с мрачной комнатой, наполненной зловещими тайнами. Тебя окутывает атмосфера страха и беспокойства. Что-то невидимое приближается, и ты чувствуешь, что время работает против тебя...',
        'items': ['черная рука', 'старый дневник'],
        'next_move': {
            'Исследовать дальше': '10',
            'Вернуться обратно': '4'
        },
        'exchange': {}
    },
    '8': {
        'text': 'Ты продвигаешься вглубь погреба, где тьма становится все плотнее, а зловещие голоса звучат в твоей голове. Мертвецы пробуждаются от своего вечного сна, готовые заполучить твою душу. Будь готов к битве за свою жизнь...',
        'items': ['паучьи ноги', 'черная свеча'],
        'next_move': {
            'Исследовать глубже': '11',
            'Вернуться обратно': '5'
        },
        'exchange': {}
    },
    '9': {
        'text': 'Ты оказался в центре мрачного лабиринта, где стены кажутся поджидающими тебя монстрами. Вокруг тебя витает аура смерти и разрушения. Остерегайся, ведь этот лабиринт полон ловушек и опасностей...',
        'items': ['мрачный артефакт', 'ржавый меч'],
        'next_move': {
            'Искать выход': '12',
            'Вернуться обратно': '6'
        },
        'exchange': {}
    },
    '10': {
        'text': 'Ты погружаешься еще глубже во мрак комнаты, где каждый шаг кажется последним. Видения и кошмары преследуют тебя, окутывая мир мрачной дымкой. Ничто не может спасти тебя от этой черной бездны...',
        'items': ['глаз ужаса', 'медальон проклятия'],
        'next_move': {
            'Искать выход': '13',
            'Вернуться обратно': '7'
        },
        'exchange': {}
    },
    '11': {
        'text': 'Ты в самой глубокой части погреба, где тьма обрушивается на тебя со всей своей силой. Здесь твои страхи становятся реальностью, а зловещие сущности поджидают свою добычу. Скорее всего, ты не выберешься отсюда живым...',
        'items': ['черный кристалл', 'кровавый свиток'],
        'next_move': {
            'Попытаться найти выход': '14',
            'Вернуться обратно': '8'
        },
        'exchange': {}
    },
    '12': {
        'text': 'Ты блуждаешь по лабиринту, теряясь в его запутанных коридорах. Тьма окутывает тебя со всех сторон, и каждый шаг кажется последним. Будь начеку, ведь тебе еще предстоит преодолеть множество испытаний...',
        'items': ['мрачный амулет', 'кровавая повязка'],
        'next_move': {
            'Продолжить поиски': '15',
            'Вернуться обратно': '9'
        },
        'exchange': {}
    },
    '13': {
        'text': 'Ты находишься в самой темной части лабиринта, где тьма проникает в самые глубины твоей души. В этом месте сосредоточена вся зловещая энергия, которая может поглотить тебя целиком. Будь готов к последней битве...',
        'items': ['темный артефакт', 'костяная маска'],
        'next_move': {
            'Искать последний выход': '14',
            'Вернуться обратно': '10'
        },
        'exchange': {}
    },
    '14': {
        'text': 'Ты стоишь перед последней дверью лабиринта, зная, что за ней тебя ждет либо спасение, либо вечная тьма. Твой выбор определит твою судьбу...',
        'items': ['ключ от свободы', 'кровавый амулет'],
        'next_move': {
            'Открыть дверь': '15',
            'Вернуться обратно': '11'
        },
        'exchange': {}
    },
    '15': {
        'text': 'Ты выбрался из лабиринта и оказался на свету дня, но зловещие тени следуют за тобой. Твоя борьба с темными силами только начинается, и ты уже знаешь, что ты - последний надежный барьер перед возвращением зла...',
        'items': ['подарок тьмы', 'черный флакон'],
        'next_move': {
            'Продолжить свой путь': '1',
            'Остаться и сразиться': '0'
        },
        'exchange': {}
    }
}



users_info = {}


def generate_story(user_id):
    # получаем текущую локацию игрока
    current_location = users_info[user_id]['cur_pos']
    # получаем текстовое описание локации
    text = locations[current_location]['text']


    keyboard = telebot.types.InlineKeyboardMarkup()
    # перебираем направления для следующего хода
    for i in locations[current_location]['next_move']:
        # добавляем кнопку, где тексом будет направление, а callback_data - название локации для перехода
        keyboard.add(telebot.types.InlineKeyboardButton(i, callback_data=locations[current_location]['next_move'][i]))
   
    # перебираем все предметы текущей локации
    for i in users_info[user_id]['loc'][current_location]['items']:
        # добавляем кнопку, текст которой будет - 'Взять предмет {название предмета}', пример, 'Взять предмет шкатулка'
        # callback_data - 'item {название предмета}', например, 'item шкатулка'
        keyboard.add(telebot.types.InlineKeyboardButton(f'Взять предмет {i}', callback_data=f'item {i}'))


    # перебираем ключи словаря предметов для обмена (i - предмет, который отдает пользователь)
    for i in users_info[user_id]['loc'][current_location]['exchange']:
        # если этот предмет есть у пользователя или название предмета начинается с 'золото: ' и у пользователя есть нужное кол-во монет
        if i in users_info[user_id]['items'] or i.startswith('золото: ') and users_info[user_id]['coins'] >= int(i.replace('золото: ', '')):
            # генерируем текст для кнопки, например, 'Обменять предмет шкатулка на золото: 3'
            text_key = f'Обменять предмет {i} на {users_info[user_id]["loc"][current_location]["exchange"][i]}'
            # генерируем строку для callback_data, например, 'exchange шкатулка'
            data_key = f'exchange {i}'
            # добавляем кнопку на клавиатуру
            keyboard.add(telebot.types.InlineKeyboardButton(text_key, callback_data=data_key))


    keyboard.add(
        telebot.types.InlineKeyboardButton('Рюкзак 🎒', callback_data='backpack'),
        telebot.types.InlineKeyboardButton('Баланс 💰', callback_data='balance')
    )
    return text, keyboard



   