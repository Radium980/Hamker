from pymongo import MongoClient
from config import MONGO_DB_URI
import asyncio
import random
import os

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message, InlineKeyboardButton, CallbackQuery
from src import app

DATABASE = MongoClient(MONGO_DB_URI)
db = DATABASE["MAIN"]["USERS"]
collection = db["members"]

def add_user_database(user_id: int):
    check_user = collection.find_one({"user_id": user_id})
    if not check_user:
        return collection.insert_one({"user_id": user_id})

@app.on_message(filters.command("help"))
async def unxhelp(_, msg: Message):
    await msg.reply_animation("https://telegra.ph/file/86b7ee349bb6cacb7ae83.mp4", caption=f"""➻ ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ᴍᴇɴᴜ ᴏғ {app.me.mention} :

↬ /ai : ᴜꜱᴇ ꜰʀᴇᴇ ᴀɪ ᴡɪᴛʜᴏᴜᴛ ᴀᴘɪ ᴋᴇʏ.
↬ /imagine : ɢɪᴠᴇ ᴘʀᴏᴍᴘᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ 𝟾ᴋ ᴀɪ ɪᴍᴀɢᴇs.
↬ /mid : ɢɪᴠᴇ ᴘʀᴏᴍᴘᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ ᴍɪᴅ ᴀɪ ɪᴍᴀɢᴇs                                                                                              
↬ /alive : sʜᴏᴡs ᴛʜᴇ ᴀʟɪᴠᴇ sᴛᴀᴛᴜs ᴏғ ᴛʜᴇ ʙᴏᴛ.
↬ /echo : sᴇɴᴅs ᴛʜᴇ ɢɪᴠᴇɴ ᴛᴇxᴛ.
↬ /figlet : ɢᴇɴᴇʀᴀᴛᴇs ᴀ ғɪɢʟᴇᴛ ᴏғ ɢɪᴠᴇɴ ɴᴀᴍᴇ.
↬ /img : sʜᴏᴡs ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ɪᴍᴀɢᴇ.
↬ /ping : sʜᴏᴡs ᴛʜᴇ ᴘɪɴɢ ʟᴀᴛᴇɴᴄʏ ᴀɴᴅ sʏsᴛᴇᴍ sᴛᴀᴛs ᴏғ ᴛʜᴇ ʙᴏᴛ.
↬ /q : ᴍᴀᴋᴇ's ᴀ ǫᴜᴏᴛᴇ ᴏғ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴍᴇssᴀɢᴇ.
↬ /shorturl : sʜᴏʀᴛᴇɴs ᴛʜᴇ ɢɪᴠᴇɴ ᴜʀʟ.
↬ /start : sᴛᴀʀᴛs ᴍᴇ.
↬ /sname : ᴅᴇᴄᴏᴅᴇs ᴛʜᴇ ɴᴀᴍᴇ ᴏғ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴜsᴇʀ ᴡɪᴛʜ ᴜɴɪᴅᴇᴄᴏᴅᴇ.
↬ /yt : ʟɪɴᴋ ᴏʀ ɴᴀᴍᴇ ᴏғ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ.
↬ /editmode : ᴇᴅɪᴛᴍᴏᴅᴇ ᴏɴ/ᴏғғ ᴛᴏ ᴅᴇʟᴇᴛᴇ ᴇᴅɪᴛᴇᴅ ᴍᴇssᴀɢᴇ ғʀᴏᴍ ɢʀᴏᴜᴘs.
↬ /song : ᴜsᴇ sᴏɴɢ ᴄᴏᴍᴍᴀɴᴅ ᴛᴏ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴʏ ᴍᴜsɪᴄ.
↬ /webss : ᴄᴀᴘᴛᴜʀᴇs ᴀ sᴄʀᴇᴇɴsʜᴏᴛ ᴏғ ᴛʜᴇ ɢɪᴠᴇɴ sɪᴛᴇ.""", 
                                  reply_markup=InlineKeyboardMarkup([
                                      [InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="back")]]))


@app.on_callback_query(filters.regex("back"))
async def cbfunback(_, query: CallbackQuery):
    check_user = collection.find_one({"user_id": query.from_user.id})
    if not check_user:
        add_user_database(query.from_user.id)
    await query.message.edit_text(text=f"""🥀 ʜᴇʏ {query.from_user.mention},\n\nᴛʜɪs ɪs {app.me.mention},\nᴛʜᴇ ᴍᴏsᴛ ᴜsᴇʟᴇss ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴇᴠᴇʀ ᴍᴀᴅᴇ.""",        
        reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ᴇʟsᴇ ʏᴏᴜ ɢᴇʏ", url=f"https://t.me/{app.me.username}?startgroup=new")
                    ],
                    [
                        InlineKeyboardButton(text="ʜᴇʟᴘ", callback_data="help"),
                        InlineKeyboardButton(text="ᴏᴡɴᴇʀ", user_id=6950368169)
                    ]
                ]
            )
    )
