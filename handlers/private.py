from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from helpers.filters import other_filters2

STICKER = "CAACAgQAAx0CQ2C8OgACsqNhiisoWUQROohUrpaGzDsHsot3dQACVxYAAtqjlSznBlAxygdMwyIE"

TEXT = "👋 Hey [{}](tg://user?id={}), I am an Telegram Groups Music Player, I let you play music in your group's voice chat.\n\n**Commands** [Here](telegra.ph/A-Simple-Group-Music-player-bot-by-SDBotsz-11-09-2)\n\nJoin @SDBotsz. 🔥"

BUTTONS = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Channel 🙋‍♀️", url="https://t.me/SDBOTs_inifinity"
                    ),
                    InlineKeyboardButton(
                        "Developer 👩‍💻", url="https://t.me/Itz_Sadew"
                    )
                ]
            ]
        )
    )

@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_sticker(STICKER)
    await message.reply_text(
        text=TEXT,
        reply_markup=BUTTONS,
        disable_web_page_preview=True
    )
        
