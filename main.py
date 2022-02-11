import config   # use config.py to store your bot token in TOKEN var
import telebot  # Telegram Bot API


bot = telebot.TeleBot(config.TOKEN)

# Run
if __name__ == "__main__":
    @bot.message_handler(commands=['start', 'id'])
    def send_id(message):
        bot.send_message(message.chat.id, message.from_user.id)
    bot.polling(non_stop=True)