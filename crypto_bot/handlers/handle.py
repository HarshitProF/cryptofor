from telebot import TeleBot
from telebot.types import InputFile
from telebot.types import Message
def message_handle(message:Message,bot:TeleBot):
    text=message.text
    if message.chat.id==741728025:
        chats=db.db().get_chats()
        print(chats)
        i=0
        j=0
        k=0
        for chat in chats:
            print(chat[i])
            try:
                bot.send_message(chat[i],text)
                k=k+1
            except Exception as e:
                print(e)
            j=j+1
        resulted=f"message sent to{k+1} people out of {j+1} people"
        bot.send_message(message.chat.id, resulted)
from db import db
def send_message(ChatjoinRequest,bot:TeleBot):
    file=open('message.txt')
    message1=file.read()
    try:
        db.db().insert(ChatjoinRequest.user_chat_id)
    except Exception as e:
        print(e)
    bot.send_video(chat_id=ChatjoinRequest.user_chat_id,caption=message1,video=InputFile('images/VID_20230219_122105_301.mp4'))
