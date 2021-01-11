import telebot
from telebot import types
import json, io 

from loguru import logger
from mysqlLogic import *
from func import * 

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
    item5 = types.KeyboardButton("/learnNew")
    item2 = types.KeyboardButton("/handleCheck")
    item3 = types.KeyboardButton("/seeAll")
    item4 = types.KeyboardButton("/delete")
    markup.add(item1, item5, item2, item3, item4)
    bot.send_message(message.chat.id, 'o((⊙﹏⊙))o.', reply_markup=markup)

@bot.message_handler(commands=['handleCheck'])
def handleCheck(message):
    set_use_command(message.chat.id, 'check')
    value = generate_random_value(select_all_value(message.chat.id))
    add_new_value(message.chat.id, 1, value['first_value'])
    add_new_value(message.chat.id, 2, value['second_value'])
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item1 = types.KeyboardButton("/back")
    markup.add(item1)
    bot.send_message(message.chat.id, 'write the translation of the word')
    bot.send_message(message.chat.id, f'{value["first_value"]}', reply_markup=markup)

@bot.message_handler(commands=['learnNew'])
def learnNew(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item1 = types.KeyboardButton("/back")
    markup.add(item1)
    bot.send_message(message.chat.id, f'{unpucking_random_value(select_all_value(message.chat.id))}', reply_markup=markup)

@bot.message_handler(commands=['seeAll'])
def seeAll(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item1 = types.KeyboardButton("/back")
    markup.add(item1)
    bot.send_message(message.chat.id, f'{unpucking(select_all_value(message.chat.id))}', reply_markup=markup)

@bot.message_handler(commands=['delete'])
def delete(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    item1 = types.KeyboardButton("/back")
    markup.add(item1)
    set_use_command(message.chat.id, 'delete')
    bot.send_message(message.chat.id, 'what do you want to delete (write first value)', reply_markup=markup)

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
            item5 = types.KeyboardButton("/learnNew")
            item2 = types.KeyboardButton("/handleCheck")
            item3 = types.KeyboardButton("/seeAll")
            item4 = types.KeyboardButton("/delete")
            markup.add(item1, item5, item2, item3, item4)
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
            if cheack_use_command(message.chat.id, 'delete'):
                set_use_command(message.chat.id, '')
                delete_value(message.chat.id, message.text)
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                item1 = types.KeyboardButton("/back")
                markup.add(item1)
                bot.send_message(message.chat.id, 'Deleted! ㄟ( ▔, ▔ )ㄏ', reply_markup=markup)
            if cheack_use_command(message.chat.id, 'check'):
                set_use_command(message.chat.id, '')
                if message.text == select_new_value(message.chat.id)['second_value']:
                    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
                    item1 = types.KeyboardButton("/back")
                    markup.add(item1)
                    bot.send_message(message.chat.id, f'{select_new_value(message.chat.id)["first_value"]} - {select_new_value(message.chat.id)["second_value"]}')
                    bot.send_message(message.chat.id, 'smart girl 🔮', reply_markup=markup)



            
bot.polling(none_stop=True)

