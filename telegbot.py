
import telebot
# 5034856664:AAGB7X0fJRIj7TTJtxjdz6N0NxXSN3Kr1NE

bot = telebot.TeleBot("5034856664:AAGB7X0fJRIj7TTJtxjdz6N0NxXSN3Kr1NE", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if message.text == "Привет":
        bot.reply_to(message, "Привет владелец")
    elif message.text == "How are you?":
        bot.reply_to(message, "I am fine, thanks")
	# bot.reply_to(message, message.text)

bot.infinity_polling()


