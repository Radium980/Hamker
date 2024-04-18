from pytube import YouTube, Search
import random
from pyrogram import filters
from pyrogram.types import Message
from src import app
import os
import re

def is_valid_url(url):
    return re.match(r'^https?://(?:www\.)?youtu\.?be(?:\.com)?/', url, re.IGNORECASE) is not None

@app.on_message(filters.command("yt"))
async def yt(_, msg: Message):
    try:
        query = msg.text.split(None, 1)[1]
        if is_valid_url(query):
            yt = YouTube(query)
        else:
            search_results = Search(query)
            video = search_results.results[0]
            yt = YouTube(video.watch_url)
        
        stream = yt.streams.get_highest_resolution()
        cutie = f"video_{random.randint(1000, 9999)}"
        stream.download(filename=cutie)
        pop = f"""
Hᴇʀᴇ ɪs ʏᴏᴜʀ ᴠɪᴅᴇᴏ.
Rᴇǫᴜᴇsᴛᴇᴅ ʙʏ {msg.from_user.mention}
Qᴜᴇʀʏ: ```{query}```
Dᴏᴡɴʟᴏᴀᴅᴇᴅ ʙʏ {app.me.mention}"""
        await msg.reply_video(video=cutie, caption=pop)
        os.remove(cutie)
    except Exception as e:
        # Log the error and inform the user
        await msg.reply_text(f"Failed to download the video: {e}")
