import asyncio

import os
import time
import requests
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

                
@app.on_message(
    command(["سورس","‹ السورس ›","الالماني", "سورس الالماني"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/4980eb521b9ccebee927f.jpg",
        caption=f"""╭──── • ◈ • ────╮
么 [َ  𝘴ꪮꪊ𝘳𝘴 ꪖᠻ𝘳ꪮ𝓽ꪮꪮ(t.me/ALMA1NY)
么 [َ ᦔꫀꪜ ꪖᠻ𝘳ꪮ𝓽ꪮꪮ](t.me/ALMA1NY)
么 [َ ᥉υρρ᥆ᖇƚ ](t.me/St5art)
╰──── • ◈ • ────╯
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼""",
        reply_markup=InlineKeyboardMarkup(
        [
            [
                    InlineKeyboardButton(
                        "‹  ᦔꫀꪜ  . 🕷 › ", url=f"https://t.me/ALMA1NY"),
                ],[
                    InlineKeyboardButton(
                        "‹ ᥴ𝗁ᥲ️ꪀꪀᥱᥣ›", url=f"https://t.me/St7art"), 
                    InlineKeyboardButton(
                        "‹ ᥉υρρ᥆ᖇƚ›", url=f"https://t.me/St5art"),
                ],[
                    InlineKeyboardButton(
                        "‹ اضف البوت لمجموعتك ›", url=f"https://t.me/A_Rn_obot?startgroup=true"),
            ]
        ]
         ),
     )
  
