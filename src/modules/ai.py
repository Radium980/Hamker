import urllib.parse
import urllib.request
import json
import pyrogram
from src import app
import requests

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

@app.on_message(pyrogram.filters.command("ai"))
async def gptAi(app: pyrogram.Client, m):
    so = m.text.split(None, 1)[1]
    await m.reply(chat_with_api("gpt", so))
