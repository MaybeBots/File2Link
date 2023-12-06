import env

from plugins.helpers import get_message_id, encode

from pyrogram import filters, Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from pyromod.exceptions import ListenerTimeout


@Client.on_message(filters.private & filters.command('batch') & env.SUDOERS)
async def batch(app: Client, message: Message):
    while True:
        try:
            f_msg = await message.from_user.ask(
                "Please forward the first message from db channel or post link",
                filters=(filters.forwarded | (
                    filters.text & ~filters.forwarded)),
                timeout=60,
            )
        except ListenerTimeout:
            await message.reply("You took too long to reply")
            return
        f_msg = get_message_id(app, f_msg)

        if f_msg:
            break
        else:
            await message.reply("This message isnt forwarded from your db channel or post link is from other channel")

    while True:
        try:
            s_msg = await message.from_user.ask(
                "Please forward the second message from db channel or post link",
                filters=(filters.forwarded | (
                    filters.text & ~filters.forwarded)),
                timeout=60,
            )
        except ListenerTimeout:
            await message.reply("You took too long to reply")
            return
        s_msg = get_message_id(app, s_msg)

        if s_msg:
            break
        else:
            await message.reply("This message isnt forwarded from your db channel or post link is from other channel")

    string = f"get-{f_msg*6969}-{s_msg*6969}"
    link = encode(string)
    await message.reply(f"Here is your link:\n `https://t.me/{app.me.username}?start={link}`",
                        disable_web_page_preview=True,
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton(
                                "Share Link", url=f"https://t.me/{app.me.username}?start={link}")]]
                        )
                        )


@Client.on_message(filters.private & filters.command('get') & env.SUDOERS)
async def get(app: Client, message: Message):
    while True:
        try:
            msg = await message.from_user.ask(
                "Please forward the message from db channel or post link",
                filters=(filters.forwarded | (
                    filters.text & ~filters.forwarded)),
                timeout=60,
            )
        except ListenerTimeout:
            await message.reply("You took too long to reply")
            return
        msg = get_message_id(app, msg)

        if msg:
            break
        else:
            await message.reply("This msg isnt forwarded from your db channel or post link is from other channel")

    string = f"get-{msg*6969}"
    link = encode(string)
    await message.reply(f"Here is your link:\n `https://t.me/{app.me.username}?start={link}`",
                        disable_web_page_preview=True,
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton(
                                "Share Link", url=f"https://t.me/{app.me.username}?start={link}")]]
                        )
                        )


@Client.on_message(filters.private & env.SUDOERS)
async def get_link(app: Client, message: Message):
    send_msg = await message.copy(env.DB_CHANNEL)
    string = f"get-{send_msg.id*6969}"
    link = encode(string)
    await message.reply(f"Here is your link:\n `https://t.me/{app.me.username}?start={link}`",
                        disable_web_page_preview=True,
                        reply_markup=InlineKeyboardMarkup(
                            [[InlineKeyboardButton(
                                "Share Link", url=f"https://t.me/{app.me.username}?start={link}")]]
                        )
                        )
