#(©)CodeXBotz




import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7895883671:AAFSp7wa7-fMdoXzP38Hz8O724Pr3g191CE")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "21406615"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "d66b1900ea3a7438ee22dd389085949a")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002474765500"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "7974532619"))

#Port
PORT = os.environ.get("PORT", "8027")

#Database
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://tharkihoobooji:tharkihoobooji@cluster0.sje0k.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "tharkihoobooji")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "0"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#start message
START_MSG = os.environ.get("START_MESSAGE", "Hello {first} , Thanks for using Me 🍑\n\n")
try:
    ADMINS=[6376328008]
    for x in (os.environ.get("ADMINS", "6992533662 7846069816").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "HEY {first}🌺\n \nJoin our channel to use me.")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "🚫 Please Avoid Direct Messages. I'm Here merely for file sharing!"

ADMINS.append(OWNER_ID)
ADMINS.append(5191566338)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
