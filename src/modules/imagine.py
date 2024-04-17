from pyrogram import filters
import requests
import time
import os
from src import app 

url = 'https://ai-api.magicstudio.com/api/ai-art-generator'

@app.on_message(filters.command("imagine", prefixes=["/", "!"]))
async def draw_prompt(app, message):
    prompt = message.text.split(maxsplit=1)[1] if len(message.text.split()) > 1 else "A Cat"
    form_data = {
        'prompt': prompt,
        'output_format': 'bytes',
        'request_timestamp': str(int(time.time())),
        'user_is_subscribed': 'false',
    }
    response = requests.post(url, data=form_data)

    if response.status_code == 200:
        try:
            if response.content:
                destination_dir = ''
                destination_path = os.path.join(destination_dir, 'generated_image.jpg')
                
                with open(destination_path, 'wb') as f:
                    f.write(response.content)
                
                await app.send_photo(
                    chat_id=message.chat.id,
                    photo=destination_path
                )
            else:
                await app.send_message(message.chat.id, "Failed to get image from the server.")
        except Exception as e:
            await app.send_message(message.chat.id, f"Error: {e}")
    else:
        await app.send_message(message.chat.id, f"Error: {response.status_code}")
