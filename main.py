import os
from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('TOKEN')

def hello(update, context):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))

def help(update, context):
    update.message.reply_text(
        'Helping {}'.format(update.message.from_user.first_name))

updater = Updater(TOKEN, use_context=True)

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('help', help))

updater.start_polling()
updater.idle()