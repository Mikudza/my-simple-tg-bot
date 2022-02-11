import config   # use config.py to store your bot token in TOKEN var
import telebot  # Telegram Bot API


bot = telebot.TeleBot(config.TOKEN)
logger = telebot.logger


@bot.message_handler(commands=['start', 'id'])
def send_welcome(message):
    bot.send_message(message.chat.id, message.from_user.id)


# Run
bot.polling(non_stop=True)
