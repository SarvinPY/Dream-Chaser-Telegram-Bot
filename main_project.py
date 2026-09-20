import telebot
from telebot import apihelper

API_TOKEN = "<token_string>"
bot = telebot.TeleBot(API_TOKEN)


#options button
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

@bot.message_handler(commands=['start'])
def send_options(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True, input_field_placeholder= "choose an option...")
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

#About(1. page) - Button
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def check_about(message):
    return message.text == 'About'

def about_P1_buttons():
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton('Main Channel', url='https://t.me/+Ao7539SF26szM2Zk')
    button2 = InlineKeyboardButton('Playlist Channel', url='https://t.me/weirdness_universal')
    button3 = InlineKeyboardButton('Spotify Playlist', url='https://open.spotify.com/playlist/1AjOUSzlKh4T44XWcAQMCJ?si=_8IkIAV7TCeQacg51JwKmQ&utm_source=copy-link')
    button4 = InlineKeyboardButton('Next', callback_data = "page2")
    markup.add(button1, button2)
    markup.add(button3)
    markup.add(button4)
    return markup

@bot.message_handler(func=check_about)
def send_about_P1(message):
    bot.send_message(message.chat.id, 'about me:', reply_markup = about_P1_buttons())


#About(2. page) - Button
@bot.callback_query_handler(func= lambda call: True)
def send_about_P2(call):
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton('GitHub', url='https://github.com/SarvinPY')
    button2 = InlineKeyboardButton('Linkdin', url='https://linkedin.com/in/sarvin-hosseini-b5b002396')
    button3 = InlineKeyboardButton('Back', callback_data = "page1")
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    if call.data == "page2":
        bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.id, text = "About my skills:", reply_markup = markup)
    elif call.data == "page1":
        bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.id, text = "about me:", reply_markup = about_P1_buttons())
    

# Send song - Button
import random
@bot.message_handler(content_types=['audio'])
def check_id(message):
    file_id = message.audio.file_id
    print(f"'{file_id}'")

Songs = ['CQACAgQAAxkBAAIBNWqvrkI_osfDsy0RIUe90GqEUjQ7AAISIgACWzB5UdsfIJTj5g4MPQQ',
        'CQACAgQAAxkDAAIBG2qu_pdMXjqIOQUL6rHo-mPdRihcAAKNIQACWzB5Uc6mNdhpLIitPQQ',
        'CQACAgEAAxkBAAIBPGqvry_jIGdXgzfDiY0fjff8xGjuAAKDIQACdMfyCNSOjMDjo3TsPQQ',
        'CQACAgEAAxkBAAIBPWqvr4Krn4JmdymdFI-QxmkzPwVlAALCRgACdMfyCDSCs9hWETefPQQ']


def check_Send_Song(message):
    return message.text == 'A random song? OK!'

@bot.message_handler(func=check_Send_Song)
def send_song(message):
    bot.send_chat_action(message.chat.id, action = 'upload_document')
    Random_song = random.choice(Songs)
    bot.send_audio(message.chat.id, Random_song)