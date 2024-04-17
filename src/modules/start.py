from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup 
from pyrogram import filters
import config
from config import OWNER_ID
from src import app
# Define a list to store sudo users
sudo_users = []

# Function to check if a user is a sudo user
def is_sudo(user_id):
    return user_id in sudo_users

# Handle the /start command
@app.on_message(filters.command("start"))
async def strt(app, message: Message):
    await message.reply_photo(
        photo="https://graph.org/file/cf76e89dbee87a7ac0a76.jpg",
        caption=f"{app.me.mention} ɪs ᴀʟɪᴠᴇ ʙᴀʙʏ.",
        reply_markup=InlineKeyboardMarkup([
            [InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{app.me.username}?startgroup=true")]
        ])
    )
