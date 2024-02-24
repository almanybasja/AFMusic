import asyncio

import os
import time
import requests
from config import START_IMG_URL
from pyrogram import filters
import random
from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from strings.filters import command
from ZeMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)
from ZeMusic import app
from random import  choice, randint

#          
                
@app.on_message(filters.command(["الالماني","مطور السورس","مبرمج السورس","المطور"],"")
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/4980eb521b9ccebee927f.jpg",
        caption=f"""◉ 𝙽𝙰𝙼𝙴 : ❪[ْ𓆩⧛ َ الالماني ⧚𓆪](https://t.me/ALMA1NY)❫
◉ 𝚄𝚂𝙴𝚁 : ❪ @ALMA1NY ❫
◉ 𝙸𝙳      : ❪ `1715562844` ❫
◉ 𝙱𝙸𝙾    : ❪ for me (@St7art)  ❫""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "ْ𓆩⧛ َ الالماني ⧚𓆪", url=f"https://t.me/IIUll_l"), 
                 ],[
                   InlineKeyboardButton(
                        "「𝚂𝙾𝚞𝚁𝚂 」", url=f"https://t.me/St7art"),
                ],

            ]

        ),

    )
