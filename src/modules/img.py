from pyrogram import filters
from src import app
from pyrogram.types import Message
from pymongo import MongoClient
from config import MONGO_DB_URI

DATABASE = MongoClient(MONGO_DB_URI)
db = DATABASE["MAIN"]["USERS"]

def add_user_to_db(user_id):
    if db.find_one({"user_id": user_id}):
        return
    db.insert_one({"user_id": user_id})

@app.on_message(filters.command("img"))
async def image_info(_, msg: Message):
    add_user_to_db(msg.from_user.id)

    replied_message = msg.reply_to_message
    if replied_message:
        if replied_message.photo:
            photo_obj = replied_message.photo.file_id
            image_format = "JPEG" if photo_obj.endswith(".jpg") else "PNG"
            height = replied_message.photo.height
            width = replied_message.photo.width
            file_size = replied_message.photo.file_size
            mode = "RGB" if len(replied_message.photo.thumbs) == 1 else "RGBA"
            await msg.reply_text(
                f"ᴅᴇᴛᴀɪʟs ᴀʙᴏᴜᴛ ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ɪᴍᴀɢᴇ :\n\n"
                f"ғᴏʀᴍᴀᴛ : `{image_format}`\n"
                f"ᴍᴏᴅᴇ : `{mode}`\n"
                f"sɪᴢᴇ : `({width}, {height})`\n"
                f"ᴘᴀʟᴇᴛᴛᴇ : `None`\n"
                f"ғɪʟᴇ sɪᴢᴇ : {file_size} bytes"
            )
        else:
            await msg.reply_text("ᴛʜᴇ ʀᴇᴘʟɪᴇᴅ ᴍᴇꜱꜱᴀɢᴇ ᴅᴏᴇꜱɴ'ᴛ ᴄᴏɴᴛᴀɪɴ ᴀ ᴘʜᴏᴛᴏ.")
    else:
        await msg.reply_text("ʏᴏᴜ ʜᴀᴠᴇɴ'ᴛ ʀᴇᴘʟɪᴇᴅ ᴛᴏ ᴀɴʏ ᴍᴇꜱꜱᴀɢᴇ.")
