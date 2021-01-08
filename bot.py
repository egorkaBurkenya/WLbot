import telebot
from telebot import types
import json, io 

from loguru import logger
# from MySQL_fn import *

with open('config.json', 'r', encoding='utf-8') as fh:
  config = json.load(fh)

bot = telebot.TeleBot(config['TOKEN'])

@bot.message_handler(commands=['start'])
def welcome(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
  item1 = types.KeyboardButton("How to use")
  item2 = types.KeyboardButton("Start learning")
  markup.add(item1, item2)
  bot.send_message(message.chat.id, 'Hello boy!', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def lisener(message):
	if message.chat.type == 'private':
		if message.text == 'How to use':
			bot.send_message(message.chat.id, 'First of all, click "Start learning" to start your learning process')
		if message.text == 'Start learning':
			bot.send_message(message.chat.id, 'Тут ты будешь учится')

bot.polling(none_stop=True)

