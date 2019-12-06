import telebot
from datetime import datetime

_date = datetime.today()
bot = telebot.TeleBot("API KEY HERE") # Insert API key here
bot_info = bot.get_me()
print(_date, " [i] ", bot_info)


@bot.message_handler()
def log(message):
        out = ("{0} [{1}], {2} {3}, (id: {4} {5}), >> {6}".format(_date, message.chat.title, message.from_user.first_name, message.from_user.last_name, message.from_user.username, message.from_user.id, message.text))
        print(out)
        logtime = datetime.strftime(datetime.now(), '%Y-%m-%d')
        filename = (logtime + " [Messages] " + message.chat.title + ".log")
        logfile = open(filename, "a", encoding='utf-8', errors='replace')
        logfile.write(out + "\n")
        logfile.close()


@bot.message_handler(content_types=['new_chat_member', 'new_chat_members'])
def join(message):
        out = ("{0} [{1}], USER JOINED: {2} {3}, (id: {4} {5})".format(_date, message.chat.title, message.from_user.first_name, message.from_user.last_name, message.from_user.username, message.from_user.id))
        print(out)
        logtime = datetime.strftime(datetime.now(), '%Y')
        filename = (logtime + " [Events] " + message.chat.title + ".log")
        logfile = open(filename, "a", encoding='utf-8', errors='replace')
        logfile.write(out + "\n")
        logfile.close()


@bot.message_handler(content_types=['left_chat_member'])
def left(message):
        out = ("{0} [{1}], USER LEFT: {2} {3}, (id: {4} {5})".format(_date, message.chat.title, message.from_user.first_name, message.from_user.last_name, message.from_user.username, message.from_user.id))
        print(out)
        logtime = datetime.strftime(datetime.now(), '%Y')
        filename = (logtime + " [Events] " + message.chat.title + ".log")
        logfile = open(filename, "a", encoding='utf-8', errors='replace')
        logfile.write(out + "\n")
        logfile.close()


                                                                                                                                                                                                                                             print(_date, " [*] Bot started")
bot.polling()
