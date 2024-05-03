import urllib.parse
import urllib.request
import json
import pyrogram
from src import app
import requests
from pymongo import MongoClient
from config import MONGO_DB_URI

DATABASE = MongoClient(MONGO_DB_URI)
db = DATABASE["MAIN"]["USERS"]
collection = db["members"]

def add_user_database(user_id: int):
    check_user = collection.find_one({"user_id": user_id})
    if not check_user:
        return collection.insert_one({"user_id": user_id})

def chat_with_api(model, prompt):
    url = f"https://tofu-api.onrender.com/chat/{model}/{prompt}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data["code"] == 2:
            return data["content"]
        else:
            return "Error: Unable to get response from the API"
    else:
        return "Error: Unable to connect to the API"

@app.on_message(pyrogram.filters.command("ai", ["!", "/", "."]))
async def gptAi(app: pyrogram.Client, m):
    add_user_database(m.from_user.id)  # Add user to the database
    so = m.text.split(None, 1)[1]
    await m.reply(chat_with_api("gpt", so))
