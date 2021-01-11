import telebot
from telebot import types
import json, io 

from loguru import logger
from mysqlLogic import *

with open('config.json', 'r', encoding='utf-8') as fh:
	config = json.load(fh)

bot = telebot.TeleBot(config['TOKEN'])

@bot.message_handler(commands=['start'])
def welcome(message):
	add_user(message.chat.id)
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
	item1 = types.KeyboardButton("How to use")
	item2 = types.KeyboardButton("Start learning")
	markup.add(item1, item2)
	bot.send_message(message.chat.id, 'Hello boy!', reply_markup=markup)

@bot.message_handler(commands=['createDB'])
def create_new_db(message):
  	create_table()
  	bot.send_message(message.chat.id, 'create ! ')

@bot.message_handler(commands=['add'])
def add(message):
    set_use_command(message.chat.id, '')
    add_new_value(message.chat.id, 3, message.text)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item1 = types.KeyboardButton("/back")
    markup.add(item1)
    bot.send_message(message.chat.id, 'Done !', reply_markup=markup)

@bot.message_handler(commands=['back'])
def back(message):
    add_new_value(message.chat.id, 1, '')
    add_new_value(message.chat.id, 2, '')
    set_use_command(message.chat.id, '')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item1 = types.KeyboardButton("/addNew")
    item2 = types.KeyboardButton("/handleCheck")
    item3 = types.KeyboardButton("/seeAll")
    item4 = types.KeyboardButton("/delete")
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'o((⊙﹏⊙))o.', reply_markup=markup)

@bot.message_handler(commands=['seeAll'])
def seeAll(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item1 = types.KeyboardButton("/back")
    markup.add(item1)
    bot.send_message(message.chat.id, f'{select_all_value(message.chat.id)}', reply_markup=markup)

@bot.message_handler(commands=['addNew'])
def add_new(message):
    set_use_command(message.chat.id, 'addNewFirstValue')		
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item1 = types.KeyboardButton("/back")
    markup.add(item1)
    bot.send_message(message.chat.id, 'write a word ＼(≧▽≦)／', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lisener(message):
    if message.chat.type == 'private':
        if message.text == 'How to use':
            bot.send_message(message.chat.id, 'First of all, click "Start learning" to start your learning process')
        if message.text == 'Start learning':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            item1 = types.KeyboardButton("/addNew")
            item2 = types.KeyboardButton("/handleCheck")
            item3 = types.KeyboardButton("/seeAll")
            item4 = types.KeyboardButton("/delete")
            markup.add(item1, item2, item3, item4)
            bot.send_message(message.chat.id, 'o((⊙﹏⊙))o.', reply_markup=markup)
        if message.text != ' ':

            if cheack_use_command(message.chat.id, 'addNewFirstValue'):
                set_use_command(message.chat.id, 'addNewSecondValue')
                add_new_value(message.chat.id, 1, message.text)
                bot.send_message(message.chat.id, 'now write a translation of this word （*゜ー゜*）')

            if cheack_use_command(message.chat.id, 'addNewSecondValue'):
                if check_value(message.chat.id, message.text):
                    set_use_command(message.chat.id, 'add?')
                    add_new_value(message.chat.id, 2, message.text)
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                    item1 = types.KeyboardButton("/add")
                    item2 = types.KeyboardButton("/back")
                    markup.add(item1, item2)
                    value = select_new_value(message.chat.id)
                    bot.send_message(message.chat.id, f'Σ(っ °Д °;)っ {value["first_value"]} - {value["second_value"]}', reply_markup=markup)
            
bot.polling(none_stop=True)

