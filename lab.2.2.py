import telebot

bot = telebot.TeleBot('7199619253:AAHgSTVM_835NHfuuKJ4eDeulF1xVdiWspU')

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.reply_to(message, "Привет! Я чат-бот 'Первокурсник' ОмГТУ. Я могу помочь вам, напиши мне 'расписание' , 'столовая' или 'библиотека'. ")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if 'расписание' in message.text.lower():
        bot.reply_to(message, "Расписание занятий можно посмотреть на официальном сайте ОмГТУ: https://rasp.omgtu.ru/ruz/.")
    elif 'столовая' in message.text.lower():
        bot.reply_to(message, "Столовая находится в шестом корпусе на первом этаже, ищи по запаху;)")
    elif 'библиотека' in message.text.lower():
        bot.reply_to(message, "Библиотека располагается в главном корпусе на первом этаже, в правом крыле.")
    else:
        bot.reply_to(message, "Простите, я не понимаю ваш вопрос. Попробуйте спросить что-то другое.")

bot.polling()
