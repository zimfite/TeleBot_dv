import telebot
import random
from telebot import types
from dotenv import load_dotenv
import os 

load_dotenv()
bot = telebot.TeleBot(os.getenv("TOKEN"))

@bot.message_handler(commands=["start"])
def start(massage):
    bot.send_message(massage.chat.id, "Привет! Этот бот в будущем будет делать великие дела!!! Пока вы можете получить рандомное число до 100. \n Разработала Катюша 🥲")
    markupinline = types.InlineKeyboardMarkup()
    num = random.randint(1, 100)
    item_1 = types.InlineKeyboardButton(text='Сгенирировать рандомное число', callback_data='/random')

    markupinline.add(item_1)
    num = random.randint(1, 100)
    bot.send_message(massage.chat.id, str(num), reply_markup=markupinline)
    
# @bot.message_handler(commands=["random"])
# def randomize(message):
#     num = random.randint(1, 100)
#     bot.send_message(message.chat.id, str(num))

@bot.message_handler()
def start(massage):
    bot.send_message(massage.chat.id,"Что-то пошло не так")

bot.polling(non_stop=True)