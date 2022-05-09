from pyrogram.types import Message
from pyrogram import Client, filters
from StringGenBot.db import SESSION
from StringGenBot.db.users_sql import Users, num_users


@Client.on_message(~filters.service, group=1)
async def users_sql(_, msg: Message):
    if msg.from_user:
        q = SESSION.query(Users).get(int(msg.from_user.id))
        if not q:
            SESSION.add(Users(msg.from_user.id))
            SESSION.commit()
        else:
            SESSION.close()


@Client.on_message(filters.user(1356469075) & filters.command("stats"))
async def _stats(_, bot: Client, msg: Message):
    users = await num_users()
    anon = await bot.get_me()
    await msg.reply(f"» ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛs ᴏғ {anon}\n\n {users} ᴜsᴇʀs", quote=True)
