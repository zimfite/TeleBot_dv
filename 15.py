import telebot
import random
from telebot import types

bot = telebot.TeleBot("6540683955:AAEei9lScXByAPY_1UI2mtsR12K1SmwP4_Y")
@bot.message_handler(commands=["start"])
def start(massage):
    bot.send_message(massage.chat.id, "Привет! Этот бот в будущем будет делать великие дела!!! Пока вы можете получить рандомное число до 10. \n Разработала Катюша 🥲")
@bot.message_handler(commands=["random"])

def  random (massage):
    num = random.randint(1,10)
    bot.send_message(massage.chat.id, str(num))
@bot.message_handler(commands=["site"])

def site(massage):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Перейти на сайт", url="https://chat.geekgpt.org/"))
@bot.message_handler()

def start(massage):
    bot.send_message(massage.chat.id,"Что-то пошло не так")
bot.polling(non_stop=True)