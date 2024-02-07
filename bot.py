import sqlite3
import telebot
from telebot import types

bot = telebot.TeleBot('BOT-TOKEN')


@bot.message_handler(commands=['start'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='website', url='https://ya.ru/')
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Click button to visit our website!", reply_markup=markup)


# TODO:
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    pass


def db():
    con = sqlite3.connect("meetings.db")
    cr = con.cursor()
    cr.execute("create table if not exists meetings(id integer, time_period text, user_id integer)")
    cr.commit()

@bot.message_handler(content_types=['add'])
def add_reserve(reserve):
    pass


bot.polling(non_stop=True, interval=0)
