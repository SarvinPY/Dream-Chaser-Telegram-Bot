import telebot
from telebot import apihelper

API_TOKEN = "<token_string>"
bot = telebot.TeleBot(API_TOKEN)


#option button
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

@bot.message_handler(commands=['start'])
def send_options(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder= "choose an option...")
    markup.add(KeyboardButton('Send me a song!'), KeyboardButton('A random song? OK'))
    markup.add(KeyboardButton('About'))
    markup.add(KeyboardButton('Next Page ➡️'))
    bot.send_message(message.chat.id, 'Make your mind:', reply_markup=markup)

def check_next_page(message):
    return message.text == 'Next Page ➡️'

@bot.message_handler(func= check_next_page)
def next_page_options(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True, input_field_placeholder= "choose an option...", one_time_keyboard=True)
    markup.add(KeyboardButton('test'))
    markup.add(KeyboardButton('Previous Page ⬅️'))
    bot.send_message(message.chat.id, 'Make your mind:', reply_markup=markup)


def check_previous_page(message):
    return message.text == 'Previous Page ⬅️'

@bot.message_handler(func=check_previous_page)
def previous_page_options(message):
    send_options(message)

#About
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def check_about(message):
    return message.text == 'About'

@bot.message_handler(func=check_about)
def send_about(message):
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton('Main Channel', url='https://t.me/+Ao7539SF26szM2Zk')
    button2 = InlineKeyboardButton('Playlist Channel', url='https://t.me/weirdness_universal')
    button3 = InlineKeyboardButton('GitHub', url='https://github.com/SarvinPY')
    button4 = InlineKeyboardButton('Linkedin', url='https://linkedin.com/in/sarvin-hosseini-b5b002396')
    button5 = InlineKeyboardButton('Next', callback_data = "page2")
    markup.add(button1, button2)
    markup.add(button3)
    markup.add(button4)
    markup.add(button5)
    bot.send_message(message.chat.id, 'test', reply_markup=markup)

@bot.callback_query_handler(func= lambda call: True)
def reply_call(call):
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton('button1', url='https://t.me/+Ao7539SF26szM2Zk')    
    button2 = InlineKeyboardButton('button2', url='https://t.me/+Ao7539SF26szM2Zk') 
    markup.add(button1)
    markup.add(button2)
    if call.data == "page2":
        bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.id, text = "test1:", reply_markup = markup)