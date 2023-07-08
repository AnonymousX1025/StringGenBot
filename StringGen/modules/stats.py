from pyrogram import filters
from pyrogram.types import Message

from config import OWNER_ID
from StringGen import Anony
from StringGen.utils import get_served_users


@Anony.on_message(filters.command(["stats", "users"]) & filters.user(OWNER_ID))
async def get_stats(_, message: Message):
    users = len(await get_served_users())
    await message.reply_text(f"» ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛs ᴏғ {Anony.name} :\n\n {users} ᴜsᴇʀs")
