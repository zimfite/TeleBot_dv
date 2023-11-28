import telebot
import random
from telebot import types
from dotenv import load_dotenv
import os 

load_dotenv()
bot = telebot.TeleBot(os.getenv("TOKEN"))

@bot.message_handler(commands=["start"])
def start(massage):
    markut=types.InlineKeyboardMarkup()
    item_1 = types.InlineKeyboardButton(text='Рандомное число', callback_data='random')
    item_2 = types.InlineKeyboardButton(text='Рандомный напиток', callback_data='vodka')
    item_3 = types.InlineKeyboardButton(text='Рандомный стикер', callback_data='ctic')
    markut.add (item_1, item_2, item_3)
    
    bot.send_message(massage.chat.id, "Привет! Этот бот в будущем будет делать великие дела!!! Пока вы можете получить рандомное число до 100. \n Разработала Катюша 🥲", reply_markup=markut)

@bot.callback_query_handler(func=lambda call:True)

def callback(call):
    if call.message:
        if call.data =="random":
            num = random.randint(1, 100)
            bot.send_message(call.message.chat.id, str(num))
            bot.callback_query_handler(func=lambda call:True)
        elif call.data =='vodka':
            a = random.randint(1,5)
            if a == 1:
                photo_1 = open('байкал.jpg', 'rb')
                bot.send_photo(call.message.chat.id, photo_1)
            elif a == 2:
                photo_2 = open('драйв.jpeg', 'rb')
                bot.send_photo(call.message.chat.id, photo_2)
            elif a == 3:
                photo_3 = open('липтон.jpg', 'rb')
                bot.send_photo(call.message.chat.id, photo_3)
            elif a == 4:
                photo_4 = open('флешбар.jpg', 'rb')
                bot.send_photo(call.message.chat.id, photo_4)
            elif a == 5:
                photo_5 = open('шампусик.jpg', 'rb')
                bot.send_photo(call.message.chat.id, photo_5)
        elif call.data == 'ctic':
            b=random.randint(-2,0)
            if b == 0:
                photo_0 = open('стикер1.jpg', 'rb')
                bot.send_photo(call.message.chat.id, photo_0)
            elif b ==-1:
                photo__1 = open('стикер2.jpg', 'rb')
                bot.send_photo(call.message.chat.id, photo__1)
            elif b ==-2:
                photo__2 = open('стикер3.jpg', 'rb')
                bot.send_photo(call.message.chat.id, photo__2)

@bot.message_handler()
def start(massage):
    bot.send_message(massage.chat.id,"Что-то пошло не так")

bot.polling(non_stop=True)