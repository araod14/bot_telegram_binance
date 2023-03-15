from config import *
import telebot
import time
import threading

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

@bot.message_handler(content_types=["text"])
def bot_message_text(message):
    """
    Messages handler
    """
    if message.text and message.text.startswith("/"):
        bot.send_message(message.chat.id, "not find command")
    else:
        x_message = bot.send_message(message.chat.id, "Aprendiendo de a poco")
        #con parse_mode puedo añadir formato markdown o html
        bot.send_chat_action(message.chat.id, "typing")
        time.sleep(3)
        bot.edit_message_text("Chao", message.chat.id, x_message.message_id)
        time.sleep(3)
        bot.delete_message(message.chat.id, x_message.message_id)

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
    print('El Bot esta ccorriendo')