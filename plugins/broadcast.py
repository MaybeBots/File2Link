import env
import asyncio

from database import DB
from pyrogram import filters, Client
from pyrogram.errors import FloodWait


@Client.on_message(filters.command("broadcast") & env.SUDOERS)
async def broadcast(app, msg):
    if not DB:
        await msg.reply_text("Mongo db is not configured!")
        return
    if msg.reply_to_message:
        x = msg.reply_to_message.id
        y = msg.chat.id
    else:
        if len(msg.command) < 2:
            return await msg.reply_text(
                "**Usage**:\n/broadcast [MESSAGE] or [Reply to a Message]")
        query = msg.text.split(None, 1)[1]
    sent = 0
    users = await DB.get_users()
    if not users:
        return
    for i in users:
        try:
            await app.forward_messages(
                i, y, x) if msg.reply_to_message else await app.send_message(
                    i, text=query)
            sent += 1
            await asyncio.sleep(0.8)
        except FloodWait as e:
            flood_time = int(e.value)
            await asyncio.sleep(flood_time + 10)
        except Exception:
            continue
    try:
        await msg.reply_text(f"**Broadcasted Message In {sent} Users.**")
    except:
        pass