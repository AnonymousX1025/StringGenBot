import io
import os
import re
import sys
import uuid
import asyncio
import traceback

from meval import meval
from html import escape
from pyrogram import filters, types
from typing import Any, List, Optional, Tuple

from anony import app

def format_exception(exc: BaseException, tb: Optional[List[traceback.FrameSummary]] = None) -> str:
    """Format an exception's traceback as a string."""
    tb = tb or traceback.extract_tb(exc.__traceback__)
    cwd = os.getcwd()
    for frame in tb:
        if cwd in frame.filename:
            frame.filename = os.path.relpath(frame.filename)
    stack = "".join(traceback.format_list(tb))
    return f"Traceback (most recent call last):\n{stack}{type(exc).__name__}: {exc}"


async def run_eval(message: types.Message, code: str) -> Tuple[str, str]:
    out_buf = io.StringIO()

    async def send(*args: Any, **kwargs: Any) -> types.Message:
        return await message.reply_text(*args, **kwargs)

    def _print(*args: Any, **kwargs: Any) -> None:
        kwargs.setdefault("file", out_buf)
        print(*args, **kwargs)

    eval_vars = {
        "m": message,
        "app": app,
        "client": app,
        "reply": message.reply_to_message,
        "chat": message.chat,
        "user": message.from_user,
        "ikb": types.InlineKeyboardButton,
        "ikm": types.InlineKeyboardMarkup,
        "asyncio": asyncio,
        "pyrogram": sys.modules["pyrogram"],
        "send": send,
        "print": _print,
        "os": os,
        "re": re,
        "sys": sys,
        "traceback": traceback,
    }

    try:
        result = await meval(code, globals(), **eval_vars)
        return "", str(result)
    except Exception as exc:
        tb = traceback.extract_tb(exc.__traceback__)
        tb = tb[next((i for i, f in enumerate(tb) if f.filename == "<string>"), 0):]
        return "⚠️ Error executing snippet\n\n", format_exception(exc, tb)


@app.on_message(filters.command("eval") & filters.user(app.OWNER))
@app.on_edited_message(filters.command("eval") & filters.user(app.OWNER))
async def eval_handler(_, message: types.Message):
    if len(message.command) < 2:
        return await message.reply_text("What?")

    code = message.text.split(None, 1)[1]
    prefix, result = await run_eval(message, code)

    out = result.strip()
    output = f"{prefix}<b>Output:</b>\n<pre language='python'>{escape(out)}</pre>"

    if len(output) > 4096:
        with io.BytesIO(out.encode()) as file:
            file.name = f"{uuid.uuid4().hex[:8].upper()}.txt"
            return await message.reply_document(document=file, disable_notification=True)

    await message.reply_text(output)
