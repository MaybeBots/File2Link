import env
import asyncio

from database import DB

from pyrogram.types import Message
from pyrogram import filters, Client
from pyrogram.errors import FloodWait

from plugins.helpers import decode, get_messages
from plugins import start_markup, reply_markup


@Client.on_message(filters.command('start') & filters.private)
async def start(app: Client, msg: Message):
    await DB.add_user(msg.from_user.id)
    if len(msg.command) < 2:
        TEXT = 'Hello there {},\nI can store files in Specified Channel and other users can access it from special link.'
        await msg.reply(TEXT.format(msg.from_user.mention), reply_markup=start_markup)
        return

    ids = None
    try:
        link = decode(msg.command[1]).split('-')

        if len(link) == 2:
            f_msg = int(link[1])
            ids = [int(f_msg/6969)]

        elif len(link) == 3:
            _, f_msg, s_msg = link

            start = int(int(f_msg) / 6969)
            end = int(int(s_msg) / 6969)

            if start > end:
                start, end = end, start

            ids = range(start, end + 1)

        else:
            await msg.reply('Invalid Link')
            return
    except:
        await msg.reply('Invalid Link')
        return

    temp = await msg.reply('Processing...')
    messages: list[Message] = await get_messages(app, msg, ids)

    if not messages:
        await temp.edit('No messages found')
        return

    for message in messages:
        await temp.delete()
        try:
            await message.copy(msg.chat.id, reply_markup=reply_markup if env.FORCE_SUB else None)
            await asyncio.sleep(env.DELAY_TIME)
        except FloodWait as e:
            await asyncio.sleep(e.x + 5)
            await message.copy(msg.chat.id, reply_markup=reply_markup if env.FORCE_SUB else None)
            await asyncio.sleep(env.DELAY_TIME)
        except Exception as e:
            await msg.reply('Something went wrong\n\n{}'.format(e))

