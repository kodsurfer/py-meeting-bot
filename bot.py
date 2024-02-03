import telebot
from telebot import types

bot = telebot.TeleBot('BOT-TOKEN')

@bot.message_handler(commands=['start'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='crt works website', url='https://crt.works/')
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Click button to visit our website!", reply_markup=markup)
