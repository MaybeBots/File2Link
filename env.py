import os
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# REQUIRED VARS
API_ID = os.getenv("API_ID", "").strip()
API_HASH = os.getenv("API_HASH", "").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
DB_CHANNEL = os.getenv('DB_CHANNEL', "").strip()
SUDO_IDS = list(map(int, os.getenv("SUDO_IDS", "").split()))

# OPTIONAL VARS
MONGO_URL = os.getenv("MONGO_URL", "").strip()
FORCE_SUB = os.getenv('FORCE_SUB', "").strip()
DELAY_TIME = float(os.getenv('DELAY_TIME', 0.5))
HASH = int(os.getenv('HASH', 6969))


SUDOERS = filters.user()
if not API_ID:
    print("No API_ID found. Exiting...")
    raise SystemExit
if not API_HASH:
    print("No API_HASH found. Exiting...")
    raise SystemExit
if not BOT_TOKEN:
    print("No BOT_TOKEN found. Exiting...")
    raise SystemExit
if not SUDO_IDS:
    print('Please Add Sudo IDS. Exiting...')
    raise SystemExit

if not MONGO_URL:
    print("No MONGO_DB specified")

try:
    DB_CHANNEL = int(DB_CHANNEL)
    API_ID = int(API_ID)
except ValueError:
    print("API_ID/DB_CHANNEL is not a valid integer. Exiting...")
    raise SystemExit

for id in SUDO_IDS:
    SUDOERS.add(id)
