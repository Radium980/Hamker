from pyrogram import filters
from pyrogram.types import Message
from src import app
from src.database.welcome_db import *

@app.on_message(filters.command("welcome"))
async def welcomefunc(app, message) -> None:
    group_admin = await group_admins(message.chat.id)
    if message.from_user.id not in group_admin:
        return await message.reply("ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴀᴅᴍɪɴ.")
    
    if len(message.command) == 1:
        return await message.reply("Usage: /welcome on/off")
    status = message.command[1]
    if status == "on":
        check_status = WELCOME_DB.find_one({"group_id": message.chat.id})
        if not check_status:
            add_welcome_enable(message.chat.id)
            return await message.reply("template welcome turned on !")
        else:
            await message.reply("template welcome already enabled !")
    elif status == "off":
        check_status = WELCOME_DB.find_one({"group_id": message.chat.id})
        if not check_status:
            return await message.reply("template welcome already disabled !")
        else:
            remove_welcome_enable(message.chat.id)
            return await message.reply("template welcome turned off !")
    else:
        return await message.reply("invalid syntax !")
