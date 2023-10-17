import os
from os import getenv


API_ID = int(getenv("API_ID", "27367626"))
API_HASH = getenv("API_HASH", "a291c4806cab38bc22b27c12ed456413")
BOT_USERNAME = getenv("BOT_USERNAME", "MrSatoruGojo_Bot")
COMMAND_HANDLER = ["/", "!"]
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = int(getenv("OWNER_ID", "1138802391"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "").split()))
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Hiroko:Hiroko@cluster0.1hztkgz.mongodb.net/?retryWrites=true&w=majority")
SESSION_STRING = getenv("SESSION_STRING", "")
