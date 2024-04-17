from pyrogram import Client, filters
import psutil
import datetime
from src import app

def get_uptime():
    uptime_seconds = psutil.boot_time()
    uptime_datetime = datetime.datetime.fromtimestamp(uptime_seconds)
    uptime_delta = datetime.datetime.now() - uptime_datetime
    hours, remainder = divmod(uptime_delta.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return hours, minutes, seconds

@app.on_message(filters.command("alive", prefixes="/"))
async def alive_command(client, message):
    hours, minutes, seconds = get_uptime()
    uptime_message = f"I'ᴍ ᴀᴡᴀᴋᴇ sɪɴᴄᴇ {hours} ʜᴏᴜʀs, {minutes}  ᴍɪɴᴜᴛᴇs, {seconds} sᴇᴄᴏɴᴅs"
    await message.reply_text(uptime_message)

