import env
import sys
import asyncio
import logging

from pyrogram import Client
from pyrogram.errors import FloodWait


class MyClient(Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def start(self):
        await super().start()

        try:
            self.db_channel = await self.get_chat(env.DB_CHANNEL)
            test_msg = await self.send_message(self.db_channel.id, "Testing")
            await asyncio.sleep(1)
            await test_msg.delete()
        except Exception as e:
            logging.warning(e)
            logging.warning(
                "Bot isn't able to send message to DB Channel. Please recheck and run again.")
            logging.warning("Bot is quiting now.")
            sys.exit(1)

    async def stop(self):
        await super().stop()
        logging.warning("Bot stopped. GoodBye!")

    async def send_message(self, *args, **kwargs):
        try:
            return await super().send_message(*args, **kwargs)
        except FloodWait as e:
            await asyncio.sleep(e.x + 5)
            return await self.send_message(*args, **kwargs)