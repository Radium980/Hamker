from pyrogram import filters
from html import escape, unescape
from src import app

@app.on_message(filters.command("echo"))
async def echo(app, message):
    if message.reply_to_message:
        text = message.reply_to_message.text
        await message.reply_text(text)
    else:
        try:
            text = message.text.split(maxsplit=1)[1]
            if text.strip() == "":
                await message.reply_text("ᴘʟᴇᴀꜱᴇ ᴘʀᴏᴠɪᴅᴇ ᴛᴇxᴛ ᴛᴏ ᴇᴄʜᴏ.")
            else:
                await message.reply_text(unescape(text))
        except IndexError:
            await message.reply_text("ᴘʟᴇᴀꜱᴇ ᴘʀᴏᴠɪᴅᴇ ᴛᴇxᴛ ᴛᴏ ᴇᴄʜᴏ")
