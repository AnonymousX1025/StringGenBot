import logging
from pyrogram import Client, enums, types

import config

logging.basicConfig(
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt="%d-%b-%y %H:%M:%S",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("telethon").setLevel(logging.ERROR)
logger = logging.getLogger(__name__)


class Pyro(Client):
    def __init__(self):
        super().__init__(
            name="StringSession",
            api_id=6,
            api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e",
            lang_code="en",
            bot_token=config.BOT_TOKEN,
            parse_mode=enums.ParseMode.HTML,
            link_preview_options=types.LinkPreviewOptions(is_disabled=True)
        )
        self.OWNER = config.OWNER_ID

    async def _start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name
        self.username = self.me.username
        self.mention = self.me.mention
        logger.info(f"@{self.username} started.")

    async def _stop(self):
        await super().stop()
        logger.info("Bot stopped.")


app = Pyro()

from convopyro import Conversation
Conversation(app)

from anony.database import Database
db = Database()

from anony.utils import Inline
buttons = Inline()
