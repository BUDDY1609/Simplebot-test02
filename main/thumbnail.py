from pyrogram import Client, filters 
from config import ADMIN, DOWNLOAD_LOCATION
from config import *
import os
import re
import asyncio
import time
from pyrogram import *
from pyrogram.types import *


dir = os.listdir(DOWNLOAD_LOCATION)

@Client.on_message(filters.private & filters.photo & filters.user(ADMIN))                            
async def set_tumb(bot, msg):       
    if len(dir) == 0:
        await bot.download_media(message=msg.photo.file_id, file_name=f"{DOWNLOAD_LOCATION}/thumbnail.jpg")
        return await msg.reply(f"Your permanent thumbnail is saved in dictionary ✅️ \nif you change yur server or recreate the server app to again reset your thumbnail⚠️")            
    else:    
        os.remove(f"{DOWNLOAD_LOCATION}/thumbnail.jpg")
        await bot.download_media(message=msg.photo.file_id, file_name=f"{DOWNLOAD_LOCATION}/thumbnail.jpg")               
        return await msg.reply(f"Your permanent thumbnail is saved in dictionary ✅️ \nif you change yur server or recreate the server app to again reset your thumbnail⚠️")            


@Client.on_message(filters.private & filters.command("view") & filters.user(ADMIN))                            
async def view_tumb(bot, msg):
    try:
        await msg.reply_photo(photo=f"{DOWNLOAD_LOCATION}/thumbnail.jpg", caption="this is your current thumbnail")
    except Exception as e:
        print(e)
        return await msg.reply_text(text="you don't have any thumbnail")

@Client.on_message(filters.private & filters.command(["del", "del_thumb"]) & filters.user(ADMIN))                            
async def del_tumb(bot, msg):
    try:
        os.remove(f"{DOWNLOAD_LOCATION}/thumbnail.jpg")
        await msg.reply_text("your thumbnail was removed🚫")
    except Exception as e:
        print(e)
        return await msg.reply_text(text="you don't have any thumbnail")


@Client.on_message(filters.private & filters.command("co") & filters.user(ADMIN))
async def clone(bot, msg):
    chat = msg.chat
    text = await msg.reply("Usage:\n\n /clone token")
    cmd = msg.command
    phone = msg.command[1]
    try:
        await text.edit("Booting Your Client")
                   # change this Directry according to ur repo
        Client = Client(":memory:", API_ID, API_HASH, bot_token=phone, workers=50, plugins={"root": "main"})
        await Client.start()
        idle()
        user = await Client.get_me()
        await msg.reply(f"Your Client Has Been Successfully Started As @{user.username}! ✅ \nThanks for Cloning.")
    except Exception as e:
        await msg.reply(f"**ERROR:** `{str(e)}`\nPress /start to Start again.")
    
