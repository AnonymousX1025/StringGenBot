from pyrogram import types, __version__ as pv
from telethon import __version__ as tv

from config import SUPPORT_CHAT

class Inline:
    def __init__(self):
        self.ikm = types.InlineKeyboardMarkup
        self.ikb = types.InlineKeyboardButton

    def gen_key(self) -> types.InlineKeyboardMarkup:
        return self.ikm(
            [
                [
                    self.ikb(text=f"Pyrogram v{pv}", callback_data="pyrogram"),
                    self.ikb(text=f"Telethon v{tv}", callback_data="telethon"),
                ]
            ]
        )

    def pm_key(self, user_id: int) -> types.InlineKeyboardMarkup:
        return self.ikm(
            [
                [
                    self.ikb(
                        text="Saved Messages",
                        url=f"tg://openmessage?user_id={user_id}",
                    )
                ]
            ]
        )

    def retry_key(self) -> types.InlineKeyboardMarkup:
        return self.ikm(
            [[self.ikb(text="Try again", callback_data="generate")]]
        )

    def start_key(self) -> types.InlineKeyboardMarkup:
        return self.ikm(
            [
                [self.ikb(text="Generate Session", callback_data="generate")],
                [
                    self.ikb(text="Support", url=SUPPORT_CHAT),
                    self.ikb(text="Source", url="https://github.com/AnonymousX1025/StringGenBot"),
                ],
            ]
        )
