from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("22600695"))
API_HASH = getenv("23081df16fad795e9cf1ebeb6ffb94dd")

BOT_TOKEN = getenv("BOT_TOKEN")
MONGO_DB_URI = getenv("6609270965:AAHHa7yBoUDBB9ke7EqPYfDTPCGiHjU-oAA", None)

OWNER_ID = int(getenv("OWNER_ID", 6628968449))
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/TheBotSupportChat")
