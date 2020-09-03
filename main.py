import os
from telegram.ext import Updater, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Bot
from pytube import YouTube
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('TOKEN')


class Bot:
    url = ""
    current_streams = []

    def __init__(self, TOKEN):
        updater = Updater(TOKEN, use_context=True)

        updater.dispatcher.add_handler(
            MessageHandler(Filters.text, self.main_handler))
        updater.dispatcher.add_handler(CallbackQueryHandler(self.button))

        updater.start_polling()
        updater.idle()

    def send_video(self, path, update, context):
        update.callback_query.message.reply_video(
            video=open(path, 'rb'), supports_streaming=True)

    def download_stream(self, itag, url):
        path_to_download = self.current_streams.get_by_itag(
            itag).download(output_path="downloads/")
        return path_to_download

    def get_download_keyboard(self, url):
        yt = YouTube(url)
        keyboard = []
        self.current_streams = yt.streams.filter(progressive=True).order_by('resolution')
        for stream in self.current_streams:
            # print(stream)
            mime_type = "{} {}".format(
                "🎵" if "audio" in stream.mime_type else "📺", stream.mime_type)
            quality = stream.resolution if stream.resolution != None else stream.abr
            quality = quality if quality != None else "❔"
            description = "{} {}".format(quality, mime_type)
            data = "{} | {}".format(stream.itag, description)
            keyboard.append([InlineKeyboardButton(
                description, callback_data=data)])

        return keyboard

    def button(self, update, context):
        query = update.callback_query
        query.answer()
        itag, description = query.data.split("|")
        query.edit_message_text(
            text="Selected option: {}".format(description))
        path = self.download_stream(itag, self.url)
        self.send_video(path, update, context)

    def main_handler(self, update, context):
        if (update.message.text.lower()) == "help":
            response = 'Hello {} you are asking for help.\nI will help you in a sec...'.format(
                update.message.from_user.first_name)
        elif (update.message.text[:2].lower()) == "dl":
            # download and upload to telegram the file they have requested
            url = update.message.text[3:]
            keyboard = self.get_download_keyboard(url)
            self.url = url
            reply_markup = InlineKeyboardMarkup(keyboard)

            update.message.reply_text(
                'Please choose an option:', reply_markup=reply_markup)
            response = "Your download will begin after you select an option."
            # try:
            #     keyboard = get_download_keyboard(url)
            #     reply_markup = InlineKeyboardMarkup(keyboard)

            #     update.message.reply_text(
            #         'Please choose an option:', reply_markup=reply_markup)
            #     response = "Your download will begin after you select an option."
            # except:
            #     response = "You have not entered a valid YouTube URL"

        else:
            response = 'Hello {} you said {}'.format(
                update.message.from_user.first_name, update.message.text)

        update.message.reply_text(response)


b = Bot(TOKEN)
