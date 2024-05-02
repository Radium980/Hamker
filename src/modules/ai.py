import urllib.parse
import urllib.request
import json
import pyrogram
from pyrogram.types import Message
from src import app
import requests
from pymongo import MongoClient
from config import MONGO_DB_URI
from Quartny import Ai

DATABASE = MongoClient(MONGO_DB_URI)
db = DATABASE["MAIN"]["USERS"]
collection = db["members"]

def add_user_database(user_id: int):
    check_user = collection.find_one({"user_id": user_id})
    if not check_user:
        return collection.insert_one({"user_id": user_id})



@app.on_message(filters.command("ai", ["!", "/", "."]))
async def ai_machuda(app, m: Message):
    ask = m.text.split(None, 1)
    so = Ai.gemini(ask[1])
    await m.reply_text(so["results"])
