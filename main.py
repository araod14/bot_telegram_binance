from config import *
from telebot import types
import telebot
import threading
from binanceconnector import connector as conn

#Instanciar el bot
bot = telebot.TeleBot(TELEGRAM_TOKEN)

#Responde al comando /start
@bot.message_handler(commands=["start", "help"])
def cmd_start(message):
    """
    Welcome to User
    """
    bot.reply_to(message, "Welocome to your cryptobot")
    print(message.chat.id)

    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('Saldo')
    itembtn2 = types.KeyboardButton('Precios')
    itembtn3 = types.KeyboardButton('Señales')
    markup.add(itembtn1, itembtn2, itembtn3)
    bot.send_message(message.chat.id, "Choose one letter:", reply_markup=markup)


def reciving_messages():
    """
    infinity loop
    """
    bot.infinity_polling()

if __name__ == '__main__':
    bot.set_my_commands([
        telebot.types.BotCommand("/start", "Welcome to user")
    ])
    print("iniciando el bot")
    thread_bot= threading.Thread(name="hilo_bot", target=reciving_messages)
    thread_bot.start()
    print('El Bot esta corriendo')