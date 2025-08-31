from pyrogram import filters, types

from anony import app, db


@app.on_message(filters.command(["stats", "users"]) & filters.user(app.OWNER))
async def get_stats(_, message: types.Message):
    users = len(await db.get_users())
    await message.reply_text(f"Current stats of {app.name} :\n\n {users} users")
