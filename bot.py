import telebot
from telebot import types
TOKEN = ''
CHANNEL_NAME = '@jayceon13'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('₽ Оплатить в рублях')
    item2 = types.KeyboardButton('₺ Pay in TL')
    item3 = types.KeyboardButton('$ Pay in USD')
    item4 = types.KeyboardButton('€ Pay in EUR')

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}, тут ты можешь оплатить мои видеоуроки по представленным реквизитам😊\n\n Hello, {0.first_name}, here you can pay for my video lessons using the details provided😊'.format(message.from_user), reply_markup = markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == '₽ Оплатить в рублях':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('⬅️ Назад/Back')
            markup.add(back)

            bot.send_message(message.chat.id, 'Номер карты: 2200 7001 4981 7693\n\n Имя получателя: Кристина А.\n\n Пожалуйста, после оплаты отправьте скриншот оплаты @k_alferuk', reply_markup=markup)

        elif message.text == '₺ Pay in TL':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('⬅️ Назад/Back')
            markup.add(back)

            bot.send_message(message.chat.id, 'IBAN: TR370006400000162210297358\n\n Name: Vitalii Alferuk\n\n Please send a screenshot of the payment to @k_alferuk after payment', reply_markup=markup)

        elif message.text == '$ Pay in USD':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('⬅️ Назад/Back')
            markup.add(back)

            bot.send_message(message.chat.id, 'IBAN: TR370006400000262210188131\n\n Name: Vitalii Alferuk\n\n SWIFT code: ISBKTRIS\n\n Adress: Mahmutlar, Zafer cad, Yigiter APT, B block, No: 5, D:19, Alanya Antalya\n\n Please send a screenshot of the payment to @k_alferuk after payment', reply_markup=markup)

        elif message.text == '€ Pay in EUR':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            back = types.KeyboardButton('⬅️ Назад/Back')
            markup.add(back)

            bot.send_message(message.chat.id, 'IBAN: TR470006400000262210188145\n\n Name: Vitalii Alferuk\n\n SWIFT code: ISBKTRIS\n\n Adress: Mahmutlar, Zafer cad, Yigiter APT, B block, No: 5, D:19, Alanya Antalya\n\n Please send a screenshot of the payment to @k_alferuk after payment', reply_markup=markup)

        elif message.text == '⬅️ Назад/Back':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            item1 = types.KeyboardButton('₽ Оплатить в рублях')
            item2 = types.KeyboardButton('₺ Pay in TL')
            item3 = types.KeyboardButton('$ Pay in USD')
            item4 = types.KeyboardButton('€ Pay in EUR')

            markup.add(item1, item2, item3, item4)

            bot.send_message(message.chat.id,'⬅️ Назад/Back', reply_markup=markup)

bot.polling(none_stop = True)
