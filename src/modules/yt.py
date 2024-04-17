from pytube import YouTube, Search
import random
from pyrogram import filters
from pyrogram.types import Message
from src import app
import os
import re

pop = f"""Tʜᴀɴᴋs ғᴏʀ ʏᴏᴜʀ ᴘᴀᴛɪᴇɴᴄᴇ. Hᴇʀᴇ ɪs ʏᴏᴜʀ ᴠɪᴅᴇᴏ.

Dᴏᴡɴʟᴏᴀᴅᴇᴅ ʙʏ {app.me.mention}"""

def is_valid_url(url):
    regex = (
        r'^https?://'  
        r'(?:(?:[A-Z0-9-]+\.)+[A-Z]{2,}|'  
        r'localhost|' 
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  
        r'(?::\d+)?' 
        r'(?:/?|[/?]\S+)$'
    )
    return re.match(regex, url, re.IGNORECASE) is not None

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
        await msg.reply_video(video=cutie, caption=pop)
        os.remove(cutie)
    except Exception as e:
        await msg.reply_text("Failed to download the video:", e)
