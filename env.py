import os
from dotenv import load_dotenv
from pyrogram import filters 

load_dotenv()

API_ID = os.getenv("API_ID", "").strip()
API_HASH = os.getenv("API_HASH", "").strip()
BOT_TOKEN = os.getenv("BOT_TOKEN", "").strip()
MONGO_URL = os.getenv("MONGO_DB", "").strip()
CHANNEL= os.getenv('CHANNEL_USERNAME', "").strip()
LOG_ID = os.getenv('LOG_ID', "").strip()
SUDO_IDS = list(map(int, os.getenv("SUDO_IDS", "").split()))

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
  print("No MONGO_DB found. Exiting...")
  raise SystemExit
  
try:
  LOG_ID = int(LOG_ID)
  API_ID = int(API_ID)
except ValueError:
  print("API_ID/LOG_ID is not a valid integer. Exiting...")
  raise SystemExit

for id in SUDO_IDS:
  SUDOERS.add(id)
