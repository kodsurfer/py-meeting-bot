import random
import aiogram
from aiogram import types,Bot
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token="BOT-TOKEN")
dp = Dispatcher(bot)

@dp.message_handler(commands=['all'])
async def process_show_users(message: types.Message):
    users_id = [random.randint(1000000,2000000) for i in range (10)]
    mesg_id = ""
    for index, id in enumerate(users_id):
        msg += f"[User {index+1}](tg://user?id={id})\n"
    
    await message.answer(text=msg, parse_mode="MarkdownV2")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


'''
   import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import random
import sqlite3
import time
API_TOKEN = '....'
logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

def db():
    con = sqlite3.connect('zazivala.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS db (users INTEGER, chats INTEGER)')
    con.commit()

@dp.message_handler(text='/add')
async def new_commands(message: types.Message):
    con = sqlite3.connect('zazivala.db')
    cur = con.cursor()
    result = cur.execute('SELECT users FROM db WHERE users = ? AND chats = ?', (message.from_user.id, message.chat.id)).fetchone()
    if len(str(result)) == 4:
        cur.execute('INSERT INTO db (users, chats) VALUES(?, ?)', (message.from_user.id, message.chat.id))
        con.commit()
        await message.reply(text='Добавил тебя в базу данных этого чата')
    else:
        await message.reply(text='Ты уже в базе данных этого чата')


@dp.message_handler(content_types=["left_chat_member"])
async def left_members(message):
    con = sqlite3.connect('zazivala.db')
    cur = con.cursor()
    cur.execute('DELETE FROM db WHERE users = ?', (message.from_user.id,))
    con.commit()

@dp.message_handler(text='/all')
async def call_all_users(message: types.Message):
    con = sqlite3.connect('zazivala.db')
    cur = con.cursor()
    alls = cur.execute('SELECT users FROM db WHERE chats = ?', (message.chat.id,))
    alls = alls.fetchall()
    for user in alls:
        text = ""
        text += f'{user}'.replace('(', '').replace(',','').replace(')','').replace(' ','')
        await message.answer(text=f'<a href="https://tg://user?id={text}">Общий сбор</a>', parse_mode=types.ParseMode.HTML)
    await message.answer('Общий сбор проведён успешно')

@dp.message_handler(text='/remove')
async def remove_user(message: types.Message):
    con = sqlite3.connect('zazivala.db')
    cur = con.cursor()
    await message.answer('✅ Ваш профиль был обновлен')
    cur.execute(f'UPDATE db SET users  = ? WHERE chats = ? AND users = ?', (message.from_user.id, message.chat.id, message.from_user.id))
    con.commit()



if __name__ == "__main__":
    db()
    executor.start_polling(dp, skip_updates=True)```

'''