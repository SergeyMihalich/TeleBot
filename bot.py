import telebot
import os
from os.path import join, dirname
from dotenv import load_dotenv


def get_token(key):
    dotenv_path = join(dirname(__file__), 'token.env')
    load_dotenv(dotenv_path)
    return os.environ.get(key)


token = get_token('TOKEN')
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    _message = f'<b>Привет <u>{message.from_user.first_name.title()}</u></b>'
    bot.send_message(message.chat.id, _message, parse_mode='html')


bot.polling(none_stop=True)
