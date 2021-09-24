import telebot
from telebot import types
from random import randint

bot = telebot.TeleBot('2032037778:AAEOTMrtQLn4gHzDS3JP4VAsglj-HNbXuU0')

name = ''
surname = ''
age = 0


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    bot.message_handler(content_types=['text', 'document', 'audio'])

    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь? Я умею:")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши 'Привет'")
    elif message.text == '/reg':
        bot.send_message(message.from_user.id, "Как тебя зовут?")
        bot.register_next_step_handler(message, get_name)
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help для помощи или /reg для регистрации.")


def get_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Какая у тебя фамилия?')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Сколько тебе лет?')
    bot.register_next_step_handler(message, get_age)


def get_age(message):
    global age
    while age == 0:
        try:
            age = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста')
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    question = 'Тебе ' + str(age) + ' лет, тебя зовут ' + name + ' ' + surname + '?'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "yes":
        ...
        bot.send_message(call.message.chat.id, 'Запомню : )')
    elif call.data == "no":
        ...
        bot.send_message(call.message.chat.id, 'Напиши еще раз /reg')


def talk(message):
    random = randint(1, 3)
    if message.text == "Как дела?":
        if random == 1:
            bot.send_message(message.from_user.id, 'Все хорошо, спасибо)')
        elif random == 2:
            bot.send_message(message.from_user.id, 'Все хорошо, а у тебя как дела, ' + name + '?')
        keyboard = types.InlineKeyboardMarkup()
        key_ok = types.InlineKeyboardButton(text='У меня тоже все хорошо', callback_data='ok')
        keyboard.add(key_ok)
        key_not = types.InlineKeyboardButton(text='Могло быть и лучше...', callback_data='not')
        keyboard.add(key_not)
        if keyboard == key_not:
            bot.send_message(message.from_user.id,
                             'Не переживай! https://ru.wikihow.com/%D1%81%D0%BF%D1%80%D0%B0%D0%B2%D0%B8%D1%82%D1%8C%D1%81%D1%8F-%D1%81-%D0%B3%D1%80%D1%83%D1%81%D1%82%D1%8C%D1%8E')
        elif keyboard == key_ok:
            bot.send_message(message.from_user.id, 'Это прекрасно,' + name + ', что у вас все хорошо!')


bot.polling(none_stop=True, interval=0)
