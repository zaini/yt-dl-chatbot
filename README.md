# yt-dl-chatbot
Simple chatbot to download YouTube videos for Telegram (and maybe WhatsApp soon)

# Features
* Download any YouTube video quickly and easily
* Videos are sent directly on Telegram
* Select any quality using an inline keyboard (No need to remember any extra commands)
* Easy to use, just send the YouTube link to the bot and select the quality to get your video

# Installation & Setup
This project uses python-telegram-bot and pytube to interact with Telegram and download YouTube videos.

dotenv is also used for loading environment variables, although you can just pass your Telegram bot secret token directly to the Bot class.

You can use pip to install everything you need:

```
pip install python-telegram-bot pytube python-dotenv
```

# Usage
1. Create a Telegram account and go through [BotFather](https://t.me/botfather) to create a bot.

2. Copy the given API token.

3. Create a ```.env``` file where you have ```main.py``` and create a variable called ```TOKEN``` and set it to your API token. e.g. ```TOKEN = YOUR_LONG_TOKEN_THAT_THE_BOTFATHER_GAVE_YOU```

4. Run main.py

# Other
Made this because I'd heard that Telegram is really open to people creating bots, which it very much was. They support a ton of features and I'll probably use it for more projects in the future.

The reason why I made a YouTube downloader in particular is that I've had requests to make one before. Still have to check that this meets the requirements of those who want to use it. I'll probably also expand it to work with Twitter videos.

You may need to apply this fix to pytude: https://github.com/nficano/pytube/issues/642#issuecomment-637671478

## Some of the libraries used

* https://github.com/python-telegram-bot/python-telegram-bot
* https://pypi.org/project/python-dotenv/
* https://github.com/nficano/pytube