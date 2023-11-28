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
    item_1 = types.InlineKeyboardButton(text='Сгенерировать рандомное число', callback_data='random')
    markut.add (item_1)
    
    bot.send_message(massage.chat.id, "Привет! Этот бот в будущем будет делать великие дела!!! Пока вы можете получить рандомное число до 100. \n Разработала Катюша 🥲", reply_markup=markut)

@bot.callback_query_handler(func=lambda call:True)

def callback(call):
    if call.message:
        if call.data =="random":
            num = random.randint(1, 100)
            bot.send_message(call.message.chat.id, str(num))
            markut_1=types.InlineKeyboardMarkup()
            item_2 = types.InlineKeyboardButton(text='Ещё', callback_data='random')
            markut_1.add(item_2)
            bot.callback_query_handler(func=lambda call:True)
            
@bot.message_handler()
def start(massage):
    bot.send_message(massage.chat.id,"Что-то пошло не так")

bot.polling(non_stop=True)