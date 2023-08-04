import env
from pyrogram.types import InlineKeyboardMarkup as ikm, InlineKeyboardButton as ikb

reply_markup = ikm(
  [
    [
      ikb('⚡ Main Channel ⚡', url=f'https://t.me/{env.CHANNEL}')
    ]
  ]
)

close_markup = ikm(
  [
    [
      ikb('Close', 'close')
    ]
  ]
)

start_markup = ikm(
  [
    [
      ikb('About', 'about'),
      ikb('Close', 'close')
    ]
  ]
)