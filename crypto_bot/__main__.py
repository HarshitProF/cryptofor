from . import bot
from .handlers import handle
def connect():
    bot.register_message_handler(handle.message_handle,pass_bot=True)
    bot.infinity_polling()
connect()