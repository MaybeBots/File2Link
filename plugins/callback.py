from plugins import close_markup

from pyrogram import Client
from pyrogram.types import CallbackQuery

ABOUT_TEXT = """
-> DEVELOPER: @MaybeSuraj
-> LANGUAGE: Python3
-> LIBRARY: Pyrogram
-> CHANNEL: @MaybeBots
-> GROUP: @MaybeBotsSupport
"""

@Client.on_callback_query()
async def callback(app: Client, cb: CallbackQuery):
  data = cb.data
  if data == 'close':
    return await cb.message.delete()

  if data == 'about':
    await cb.message.edit(
      text = ABOUT_TEXT,
      reply_markup = close_markup
    )