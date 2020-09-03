import os
from telegram.ext import Updater, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from pytube import YouTube
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('TOKEN')


def download_stream(itag):
    url="https://youtu.be/2wcI10CNuxU"
    yt = YouTube(url)
    yt.streams.get_by_itag(itag).download(output_path = "downloads/")


def get_download_keyboard(url="https://youtu.be/2wcI10CNuxU"):
    yt = YouTube(url)

    keyboard = []

    for stream in yt.streams.filter(progressive=True).order_by('resolution'):
        # print(stream)
        mime_type = "{} {}".format(
            "🎵" if "audio" in stream.mime_type else "📺", stream.mime_type)
        quality = stream.resolution if stream.resolution != None else stream.abr
        quality = quality if quality != None else "❔"
        # print("{} {}".format(quality, mime_type), stream.itag)
        keyboard.append([InlineKeyboardButton("{} {}".format(
            quality, mime_type), callback_data=str(stream.itag))])

    return keyboard


def button(update, context):
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Selected option: {}".format(query.data))
    download_stream(query.data)


def hello(update, context):
    if (update.message.text.lower()) == "help":
        response = 'Hello {} you are asking for help.\nI will help you in a sec...'.format(
            update.message.from_user.first_name)
    elif (update.message.text[:2].lower()) == "dl":
        # ask user if they want audio or video
        # show them the various sizes of video/audio
        # download and upload to telegram the file they have requested
        keyboard = get_download_keyboard()
        reply_markup = InlineKeyboardMarkup(keyboard)

        update.message.reply_text(
            'Please choose an option:', reply_markup=reply_markup)
        response = "Your download will begin after you select an option."
    else:
        response = 'Hello {} you said {}'.format(
            update.message.from_user.first_name, update.message.text)

    update.message.reply_text(response)


updater = Updater(TOKEN, use_context=True)

updater.dispatcher.add_handler(MessageHandler(Filters.text, hello))
updater.dispatcher.add_handler(CallbackQueryHandler(button))

updater.start_polling()
updater.idle()
