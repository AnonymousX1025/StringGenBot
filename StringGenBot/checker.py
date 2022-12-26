import time

import psutil
from pyrogram import filters, Client
from pyrogram.types import Message

from main import StartTime


def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "ᴍ", "ʜ", "ᴅᴀʏs"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return 

@Client.on_message(filters.command("respondtostatuschecker"))
async def st_father(_, message: Message):
    upt = int(time.time() - StartTime)
    cpu = psutil.cpu_percent(interval=0.5)
    uptime = get_readable_time((upt))
    await message.reply_text(f"{uptime}~{cpu}%~💤")
