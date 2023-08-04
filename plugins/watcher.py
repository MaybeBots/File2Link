import env
import asyncio
import logging

from database import DB
from pyrogram import filters, Client


@Client.on_message(filters.document & filters.private & env.SUDOERS )
async def watcher(app, msg):
    ids = []
    file_id = str(msg.document.file_id)[:64]
    group_media = msg.media_group_id

    if group_media:
        if group_media in DB.get_group_media():
            return

        DB.add_group_media(group_media)
        ok = await app.get_media_group(chat_id=msg.chat.id, message_id=msg.id)
        for i in ok:
            ids.append(i.id)
    else:
        ids.append(msg.id)

    try:
        ok = await msg.reply('Saving File...')
        msg_ids = await app.forward_messages(chat_id=env.LOG_ID,
                                             from_chat_id=msg.from_user.id,
                                             message_ids=ids)
        link = 'https://t.me/{}?start={}'.format(app.me.username, file_id)
        await asyncio.sleep(0.3)
        await ok.edit(f'File saved Successfully.\n\nAccess File by: {link}',
                      disable_web_page_preview=True)

    except Exception:
        logging.ERROR('Bot is not able to send message in log group please check.')
        await msg.reply('Failed to save the file')
        return

    await DB.add_file_id(file_id, [i.id for i in msg_ids])
