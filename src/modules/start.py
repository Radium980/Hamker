from pymongo import MongoClient
from config import MONGO_DB_URI
import asyncio
import random
import os

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message, InlineKeyboardButton, CallbackQuery
from src.database.chats_db import add_served_chat
from src import app

DATABASE = MongoClient(MONGO_DB_URI)
db = DATABASE["MAIN"]["USERS"]
collection = db["members"]

def add_user_database(user_id: int):
    check_user = collection.find_one({"user_id": user_id})
    if not check_user:
        return collection.insert_one({"user_id": user_id})


@app.on_message(filters.new_chat_members, group=69)
async def tgkichudai(client, message):
    for member in message.new_chat_members:
        if member.id == client.me.id:
            await add_served_chat(message.chat.id)
            await message.reply("ᴛʜᴀɴᴋs ғᴏʀ ᴀᴅᴅɪɴɢ ᴍᴇ ʜᴇʀᴇ !")


@app.on_message(filters.command("start"))
async def start(_, m: Message):
    add_user_database(m.from_user.id)
    await m.reply_photo("https://telegra.ph/file/a0d157254f58e0d1a8850.jpg", caption=f"""🥀 ʜᴇʏ {m.from_user.mention},\n\nᴛʜɪs ɪs {app.me.mention},\nᴛʜᴇ ᴍᴏsᴛ ᴜsᴇʟᴇss ᴛᴇʟᴇɢʀᴀᴍ ʙᴏᴛ ᴇᴠᴇʀ ᴍᴀᴅᴇ.""",
                         reply_markup=InlineKeyboardMarkup([
        [InlineKeyboardButton(text="ᴀᴅᴅ ᴍᴇ ᴇʟsᴇ ʏᴏᴜ ɢᴇʏ", url=f"https://t.me/{app.me.username}?startgroup=new")],
        [InlineKeyboardButton(text="ʜᴇʟᴘ", callback_data="help"), InlineKeyboardButton(text="ᴅᴇᴠᴇʟᴏᴘᴇʀs", url="t.me/unxsupportchat")]
    ]))

@app.on_callback_query(filters.regex("help"))
async def cb_func_help(_, query: CallbackQuery):
    await query.edit_message_reply_markup(
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="back")],
            [InlineKeyboardButton(text="Ai", callback_data="unx_ai")],
            [InlineKeyboardButton(text="image ai", callback_data="unx_imageai")]]))

@app.on_callback_query(filters.regex("unx_ai"))
async def cb_func_ai(_, query: CallbackQuery):
    await query.message.edit_text(text="↬ /ai : ᴜꜱᴇ ꜰʀᴇᴇ ᴀɪ ᴡɪᴛʜᴏᴜᴛ ᴀᴘɪ ᴋᴇʏ.", reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton(text="ʙᴀᴄᴋ", callback_data="back")]]))
        
@app.on_callback_query(filters.regex("unx_imageai"))
async def cb_func_imageai(_, query: CallbackQuery):
    await query.message.edit_text(text="↬ /imagine : ɢɪᴠᴇ ᴘʀᴏᴍᴘᴛ ᴛᴏ ɢᴇɴᴇʀᴀᴛᴇ 𝟾ᴋ ᴀɪ ɪᴍᴀɢᴇs.")

@app.on_callback_query(filters.regex("back"))
async def cb_func_back(_, query: CallbackQuery):
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
                        InlineKeyboardButton(text="sᴏᴜʀᴄᴇ", callback_data="source")
                    ]
                ]
            )
    )


