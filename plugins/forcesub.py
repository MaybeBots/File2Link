from env import FORCE_SUB, SUDOERS
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private & ~SUDOERS, group=-2)
async def must_join_channel(bot: Client, msg: Message):
    if not FORCE_SUB:  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member(FORCE_SUB, msg.from_user.id)
        except UserNotParticipant:
            if FORCE_SUB.startswith('-'):
                info = await bot.get_chat(FORCE_SUB)
                link = info.invite_link
            else:
                link = "https://t.me/" + FORCE_SUB
            try:
                markup = [
                    [InlineKeyboardButton("⚡ Join Channel ⚡", url=link)]
                ]
                if msg.text[0:6] == "/start" and len(msg.text) > 7:
                    markup.append([InlineKeyboardButton(
                        "🔄 Refresh 🔄", url=f"https://t.me/{bot.me.username}?start={msg.text[7:]}")])
                await msg.reply(
                    f"Looks like you haven't join our chat yet! Please Join First",
                    reply_markup=InlineKeyboardMarkup(markup)
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        return


@Client.on_message(filters.private & filters.incoming & ~SUDOERS & ~filters.command('start'), group=-1)
async def ok(app, msg):
    await msg.reply('Please don\'t send me message directly! ❌')
