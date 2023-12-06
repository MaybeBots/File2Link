import env
import base64
import asyncio

from pyrogram import Client
from pyrogram.types import Message
from pyrogram.errors import FloodWait


def get_message_id(client: Client, msg: Message):
    if msg.forward_from_chat:
        if msg.forward_from_chat.id == env.DB_CHANNEL:
            return msg.forward_from_message_id
        else:
            return False
    else:
        return False



def encode(string):
    string_bytes = string.encode("ascii")
    base64_bytes = base64.urlsafe_b64encode(string_bytes)
    base64_string = (base64_bytes.decode("ascii")).rstrip("=")
    return base64_string


def decode(base64_string):
    padding = '=' * (4 - (len(base64_string) % 4))
    base64_string = base64_string + padding

    base64_bytes = base64_string.encode("ascii")
    string_bytes = base64.urlsafe_b64decode(base64_bytes)
    string = string_bytes.decode("ascii")
    return string


async def get_messages(client: Client, msg: Message, ids: list):
    messages = []
    try:
        msg = await client.get_messages(env.DB_CHANNEL, ids)
        messages.extend(msg)
    except FloodWait as e:
        await asyncio.sleep(e.x)
        msg = await client.get_messages(env.DB_CHANNEL, ids)
        messages.extend(msg)
    except Exception as e:
        await msg.reply('Something went wrong\n\n{}'.format(e))

    
    return [msg for msg in messages if not msg.empty]
