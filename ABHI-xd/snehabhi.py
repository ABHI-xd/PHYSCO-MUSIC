import requests
from pyrogram import Client as Bot

from callsmusic import run
from config import API_HASH, API_ID, AUD_IMG, BOT_TOKEN
from handlers import __version__

response = requests.get(AUD_IMG)
with open("./etc/foreground.png", "wb") as file:
    file.write(response.content)


bot = Bot(
    ":memory:",
    API_ID,
    API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="handlers"),
)

print(f"[INFO]: SNEHABHI MUSICS v{__version__} STARTED !")

bot.start()
run()
