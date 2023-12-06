import env
import pyromod  # type:ignore
import logging

from client import MyClient
from pyrogram import idle

# logging things
logging.basicConfig(
    format='[%(asctime)s - %(levelname)s] - %(name)s : %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)


LOGGER('pyrogram').setLevel(logging.WARNING)

# Creating Pyro Client
app = MyClient(name='File2Link',
               api_id=env.API_ID,
               api_hash=env.API_HASH,
               bot_token=env.BOT_TOKEN,
               plugins=dict(root='plugins'),
               workers=4)


async def main():
    LOGGER(__name__).info('Starting Bot...')
    await app.start()
    LOGGER(__name__).info(f'{app.me.first_name} is started successfully')
    await idle()
    await app.stop()

if __name__ == '__main__':
    app.run(main())
