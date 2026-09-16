import telebot
from telebot import apihelper

API_TOKEN = "YOUR BOT API"
bot = telebot.TeleBot(API_TOKEN)
apihelper.ENABLE_MIDDLEWARE = True

#==========================================================================

# @bot.message_handler(commands=['help', 'start'])
# def send_welcome(message):
#     bot.send_message(message.chat.id, """\
# Hi there, I am EchoBot.
# I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
# """)


#==========================================================================
# @bot.message_handler(content_types=['document', 'audio'])
# def handle_docs_audio(message):
# 	if message.content_type == "document":
# 		bot.reply_to(message, "Do not send a document files.")
# 		pass
# 	elif message.content_type == "audio":
# 		bot.reply_to(message, "file recived!")


#==========================================================================
# def check_hello(message):
#     return message.text == "Hello"

# @bot.message_handler(func= check_hello)
# def say_hello(message):
#     bot.reply_to(message, f"Hello @{message.from_user.username}")
	

#==========================================================================
# def check_type(message):
#     return message.document.mime_type == 'text/plain'


# @bot.message_handler(func= check_type, content_types=['document'])
# def say_result(message):
#     bot.reply_to(message, "file recived!")


# we can write up code, like the below codes:
#==========================================================================
# @bot.message_handler(content_types=['document'])
# def say_result(message):
#     if message.document.mime_type == "text/plain":
# 	    bot.reply_to(message, "file recived!")
#     else:
#         bot.reply_to(message, "Invalid Type")

    

#==========================================================================
# @bot.message_handler(commands=['poll'])
# def create_poll(message):
#     bot.send_poll(
#         chat_id=message.chat.id,
#         question="Which is your favorite song type?",
#         options=["Funk", "jazz", "pop", "metal", "rock"],
#         is_anonymous=False
#     )

# @bot.poll_answer_handler(func=lambda answer: True)
# def receive_answer(poll_answer):
#     user_name = poll_answer.user.first_name
#     bot.send_message(
#         poll_answer.user.id,
#         f"Thanks for your vote {user_name}!"
#     )


#==========================================================================
bot = telebot.TeleBot(API_TOKEN)

@bot.middleware_handler(update_types=['message'])
def modify_message(bot_instance, message):
    if message.text:  
        message.another_text = message.text + ':changed'
    else:
        pass

@bot.message_handler(func=lambda message: True)
def reply_modified(message):
    bot.reply_to(message, message.another_text)

bot.infinity_polling()
