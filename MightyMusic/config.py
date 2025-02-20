import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "gabutimes")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/75734bc9ffa935a4bc1f8.jpg")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Wolf_Music Assistent")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "gabutimes")
PROJECT_NAME = getenv("PROJECT_NAME", "Wolf_MusicBot")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/BlitzSecret/Wolf_MusicBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())
PMPERMIT = getenv("PMPERMIT", None)
OWNER_USERNAME = getenv ("OWNER_USERNAME", "Bblitzzz")

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
