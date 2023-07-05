import os
import aiohttp
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

if os.path.exists("Internal"):
   load_dotenv("Internal")

aiohttpsession = aiohttp.ClientSession()
que = {}
admins = {}

#------------------------ Important Stuff 🤎 -----------------------

API_ID = int(getenv("API_ID", "22151516"))
API_HASH = getenv("API_HASH", "2804a8f5ce03cdcd7ab46ce6df78f386")
BOT_TOKEN = getenv("BOT_TOKEN", "6340255282:AAGrEiDPyQ0zrV4UwK6g3cjW0rT4pcy9fKM")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "600"))
STRING_SESSION = getenv("STRING_SESSION", "AgCimgQ-c6-_KeepPcavFzet3lvZ1Y4e3g_7s9PUEdQv5M2GKlatogMwuXJrR5jPEHq55vRyozK6bFA_uOQ75tolUv4xF3emAyxrqu8Uf7wMvPki8WnirvcyjtXDjii800UrwT75AQdQPeB12usUktsKmxkA_BY_Sf08c0QDqpN497_ha-Ft3N7rZnsTt3YGuQOyiRH8L07y1yDvOqcUNyjHs67iGmhnDoF3uqcBppT0r-n2eYiduGdfh7r-KscdGgh48AGPRCRiGdzGqi5uf0xIlmsmSofzUFP33JhqjthXd7nBqzjBDVQnITzVWF-hDe-7ziISUtYYF-2CgySTeVwVVIOOVgA")
BOT_USERNAME = getenv("BOT_USERNAME", "yy63bot")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1854384004").split()))
OWNER_ID = list(
    map(int, getenv("OWNER_ID", "1417907798").split())
)  # Input type must be interger
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "30"))

#•••••••••••••••••••••••• Mongodb Url Stuff & Loggroupid •••••••••••
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001847569598")) 

MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
#________________________ Updates  & Music bot name________________
NETWORK = getenv("NETWORK", "xl444")
GROUP = getenv("GROUP", "yybot63")
BOT_NAME = getenv("BOT_NAME", "Music")
BANNED_USERS = filters.user()

#************************* Image Stuff  ****************************

IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/5fdd8da2461c05d893189.jpg") 
YOUTUBE_IMG_URL = getenv("YOUTUBE_IMG_URL", "https://te.legra.ph/file/5fdd8da2461c05d893189.png")

aiohttpsession = aiohttp.ClientSession()


