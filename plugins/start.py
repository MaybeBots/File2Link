import env
import sys
import logging 
import asyncio

from database import DB
from plugins import reply_markup, start_markup

from pyrogram import filters, Client
from pyrogram.errors.exceptions.bad_request_400 import ChannelInvalid


@Client.on_message(filters.command('start') & filters.private)
async def start(app, msg):
    await DB.add_user(msg.from_user.id) 
    if len(msg.command) < 2:
        TEXT = 'Hello there {},\nI can store files in Specified Channel and other users can access it from special link.'
        await msg.reply(TEXT.format(msg.from_user.mention), reply_markup=start_markup)
        return 
        

    file_id = msg.command[1]
    msg_ids = DB.get_msg_ids(file_id)

    if not msg_ids:
        return await msg.reply('Invalid Link')
    
    ok = await msg.reply('Processing...')
    await asyncio.sleep(0.4)
    await ok.delete()
    
    for i in msg_ids:
        try:
            message = await app.get_messages(env.LOG_ID, i)
            if message.empty:
                await msg.reply('That file has been deleted by the owner')
                continue 
            await message.copy(chat_id = msg.chat.id, reply_markup=reply_markup if env.CHANNEL else None) 
            await asyncio.sleep(1)
        except ChannelInvalid:
            logging.ERROR('Failed to access log channel. Exiting....')
            sys.exit(0)
