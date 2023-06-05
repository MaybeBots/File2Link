import env
import logging

from pyrogram import Client, idle

# logging things
logging.basicConfig(
    format='[%(asctime)s - %(levelname)s] - %(name)s : %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    level=logging.INFO)

logging.getLogger('pyrogram').setLevel(logging.WARNING)

# Creating Pyro Client
app = Client(name='File2Link',
             api_id=env.API_ID,
             api_hash=env.API_HASH,
             bot_token=env.BOT_TOKEN,
             plugins=dict(root='plugins'))

if __name__ == '__main__':
    logging.info('Starting Bot...')
    app.start()
    me = app.me
    logging.info(f'{me.first_name} is started successfully')
    idle()
    app.stop()
    logging.info('GoodBye!')
