import telebot
from telebot import custom_filters
from telebot import StateMemoryStorage
from telebot.handler_backends import StatesGroup, State

state_storage = StateMemoryStorage()
# Вставить свой токет или оставить как есть, тогда мы создадим его сами
bot = telebot.TeleBot("6630447854:AAFr-NjivHyywGzJanOQ8qdV_u3KowPiD1s",
                      state_storage=state_storage, parse_mode='Markdown')


class PollState(StatesGroup):
    v1 = State()
    v2 = State()
    v3 = State()
    v4 = State()


class HelpState(StatesGroup):
    wait_text = State()


text_poll = "опрос"  # Можно менять текст
text_button_1 = "Факт №1"  # Можно менять текст
text_button_2 = "Факт №2"  # Можно менять текст
text_button_3 = "Факт №3"  # Можно менять текст

menu_keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_poll,
    )
)
menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_button_1,
    )
)

menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_button_2,
    ),
    telebot.types.KeyboardButton(
        text_button_3,
    )
)


@bot.message_handler(state="*", commands=['start'])
def start_ex(message):
    bot.send_message(
        message.chat.id,
        'Привет! Что будем делать? Может пройдешь тест? Или узнаешь интересный факт о телеграмм?',  # Можно менять текст
        reply_markup=menu_keyboard)


@bot.message_handler(func=lambda message: text_poll == message.text)
def first(message):
    bot.send_message(message.chat.id,
                     'Супер! \n Правила: Будет всего 4 вопроса, после каждого вопроса будет выводится правильный ответ. Если ты ответил правильно то ставь себе 1 балл:) \n *Первый вопрос* Что такое социальные сети? \n а)  веб-сайт \n б) книга \n в) общение с друзьями')  # Можно менять текст
    bot.set_state(message.from_user.id, PollState.v1, message.chat.id)


@bot.message_handler(state=PollState.v1)
def name(message):
    # with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
    # data['name'] = message.text
    bot.send_message(message.chat.id,
                     'Правильный ответ А \n *Второй вопрос*  Выбрать определение социальной сети: \n а) сайт для общения с друзьями \n б) веб-сайт, предназначенные для построения, отражения и организации социальных взаимоотношений, визуализацией которых являются социальные графы \n в) онлайн-сервис или веб-сайт')  # Можно менять текст
    bot.set_state(message.from_user.id, PollState.v2, message.chat.id)


@bot.message_handler(state=PollState.v2)
def age(message):
    # with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
    #  data['age'] = message.text
    bot.send_message(message.chat.id,
                     'Правильный ответ Б \n *Третий вопрос* Какой из проектов был запущен вперед: \n а) ВКонтакте \n б) Facebook  \n в) Telegram')  # Можно менять текст
    bot.set_state(message.from_user.id, PollState.v3, message.chat.id)


@bot.message_handler(state=PollState.v3)
def age(message):
    # with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
    #  data['age'] = message.text
    bot.send_message(message.chat.id,
                     'Правильный ответ Б \n *Четвертый вопрос *Ведущая социальная сеть России: \n а) ВKонтакте \n б) Мой мир@mail \n в) Одноклассники')  # Можно менять текст
    bot.set_state(message.from_user.id, PollState.v4, message.chat.id)


@bot.message_handler(state=PollState.v4)
def age(message):
    # with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
    #  data['age'] = message.text
    bot.send_message(message.chat.id,
                     'Правильный ответ А \n Давай проверим на какую оценку ты выполнил тест! \n *4 балла* Молодец твоя оценка 5!!! \n *3-2 балла* Ты хорошо справился с тестом! Можешь поставить твердую четверку! \n *0-1 балл* Тебе нужно подтянуть знания',
                     reply_markup=menu_keyboard)  # Можно менять текст
    bot.delete_state(message.from_user.id, message.chat.id)


@bot.message_handler(func=lambda message: text_button_1 == message.text)
def help_command(message):
    bot.send_message(message.chat.id,
                     "*Факт 1* На самом деле русскоязычная аудитория в телеграм всего 7% от пользователей",
                     reply_markup=menu_keyboard)  # Можно менять текст


@bot.message_handler(func=lambda message: text_button_2 == message.text)
def help_command(message):
    bot.send_message(message.chat.id,
                     "*Факт 2* Идея и код телеграма и Вконтакте созданы Николаем Дуровым, братом Павла Дурова",
                     reply_markup=menu_keyboard)  # Можно менять текст


@bot.message_handler(func=lambda message: text_button_3 == message.text)
def help_command(message):
    bot.send_message(message.chat.id,
                     "*Факт 3* Бразилия, Индонезия, Индия, Иран - самые популярные страны для телеграм, куда летал лично Дуров для переговоров",
                     reply_markup=menu_keyboard)  # Можно менять текст


bot.add_custom_filter(custom_filters.StateFilter(bot))
bot.add_custom_filter(custom_filters.TextMatchFilter())

bot.infinity_polling()