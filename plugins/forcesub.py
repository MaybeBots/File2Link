from env import CHANNEL, SUDOERS
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-2)
async def must_join_channel(bot: Client, msg: Message):
    if not CHANNEL:  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member(CHANNEL, msg.from_user.id)
        except UserNotParticipant:
            link = "https://t.me/" + CHANNEL
            try:
                await msg.reply(
                    f"Looks like you haven't join our chat yet! Please Join First",
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("⚡ Join Channel ⚡", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
      return

@Client.on_message(filters.private & filters.incoming & ~SUDOERS & ~filters.command('start'), group=-1)
async def ok(app, msg):
  await msg.reply('Please don\'t send me message directly! ❌')