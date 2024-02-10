import sqlite3

from aiogram import types, Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token="BOT-TOKEN")
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
def url(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text='website', url='https://ya.ru/')
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Click button to visit our website!", reply_markup=markup)


# TODO:
@dp.message_handler(content_types=['text'])
def get_text_messages(message):
    pass


def db():
    con = sqlite3.connect("meetings.db")
    cr = con.cursor()
    cr.execute("create table if not exists meetings(id integer, time_period text, user_id integer)")
    con.commit()


@dp.message_handler(content_types=['add'])
def add_reserve(message):
    con = sqlite3.connect('meetings.db')
    cur = con.cursor()
    cur.execute('INSERT INTO meetings(time_period text, user_id integer) VALUES(?, ?)',
                (message.chat.id, message.from_user.id))
    con.commit()
    await message.reply(text='Добавил reserve')


@dp.message_handler(content_types=['free'])
def free_reserve(message):
    con = sqlite3.connect('meetings.db')
    cur = con.cursor()
    cur.execute('DELETE FROM meetings(time_period text, user_id integer) WHERE time_period=? AND  user_id=?)',
                (message.chat.id, message.from_user.id))
    con.commit()
    await message.reply(text='Free reserve')


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
