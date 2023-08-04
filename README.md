<h1 align=center>A File to Link Telegram Bot</h1>
<h2 align=center>A File2Link Bot that can stores documents in private channel and instantly provide a accessible link</h2>
<p align="center">
<a href="https://python.org"><img src="http://forthebadge.com/images/badges/made-with-python.svg" alt="made-with-python"></a>
<br>
    <img src="https://img.shields.io/github/stars/MaybeBots/File2Link?style=for-the-badge" alt="Stars">
    <img src="https://img.shields.io/github/forks/MaybeBots/File2Link?style=for-the-badge" alt="Forks">
    <img src="https://img.shields.io/github/watchers/MaybeBots/File2Link?style=for-the-badge" alt="Watchers"> 
<br>
    <img src="https://img.shields.io/github/repo-size/MaybeBots/File2Link?style=for-the-badge" alt="Repository Size">
    <img src="https://img.shields.io/github/contributors/MaybeBots/File2Link?style=for-the-badge" alt="Contributors">
    <img src="https://img.shields.io/github/issues/MaybeBots/File2Link?style=for-the-badge" alt="Issues">
</p>  

## Config Vars
1. `API_ID` : Telegram API_ID, get it from my.telegram.org/apps
2. `API_HASH` : Telegram API_ID, get it from my.telegram.org/apps
3. `MONGO_DB` : A valid Mongo Db url to store msg_ids and userids
4. `BOT_TOKEN` : A valid bot token, get it from [@BotFather](https://t.me/BotFather)
5. `LOG_ID` : Your Private Telegram channel's id (Example: -1001246808642)
6. `SUDO_IDS` : Owner id (Example: 1357907531 2468097531 3579864213)
7. `CHANNEL_USERNAME` : Your public channel username (without @) to enable force sub
## Deployment Methods

### Vps

To deploy on a VPS, follow these steps

1. Update and upgrade your system packages:
```
sudo apt-get update && sudo apt-get upgrade -y
```

2. Clone the repository and navigate to the project directory:
```
git clone https://github.com/maybebots/File2Link && cd File2Link
```

3. Install the required packages:
```
pip3 install -U -r requirements.txt
```
4. Create .env using example.env
```
cp example.env .env
```
5. Now open the .env file using **vi .env**
6. Edit the vars, by pressing **I**  on the keyboard
7. After editing save the file using **ctrl + c** then **:wq**
8. Run the script using Python 3:
```
python3 bot.py
```
## How to Save Files?

1. Make sure to make the bot an admin in your private log channel. This will allow the bot to save files there.
2. You can send your files directly to the bot's private message (PM). Just make sure to send them as document files. The bot won't be able to accept direct photos or videos etc. (This is only for sudo users)
3. After the bot saves your file, it will provide you with a special link. When someone clicks on that link, the bot will send them the file you uploaded, as long as it hasn't been deleted.
4. Additional Command `/broadcast [message]` or `/broadcast (reply to a message` (only for sudo ids)

<h3>Still Having problem feel free to ask in our support group. We're here to help!</h3>

## Support
- [Channel](https://t.me/Maybebots)
- [Group](https://t.me/MaybeBotsSupport)

## Credits
- [Pyrogram](https://github.com/pyrogram/pyrogram)
