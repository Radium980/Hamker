from pyrogram import filters
from pyrogram.types import Message
from src import app
from src.database.welcome_db import *
from src.modules.editmode import group_admins
from PIL import Image,ImageOps,ImageDraw,ImageChops, ImageFont


async def circle(pfp, size=(215, 215)):
    pfp = pfp.resize(size, Image.Resampling.LANCZOS).convert("RGBA")
    bigsize = (pfp.size[0] * 3, pfp.size[1] * 3)
    mask = Image.new("L", bigsize, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0) + bigsize, fill=255)
    mask = mask.resize(pfp.size, Image.Resampling.LANCZOS)
    mask = ImageChops.darker(mask, pfp.split()[-1])
    pfp.putalpha(mask)
    return pfp

async def pfp(pfp,chat,id):
    if len(chat) > 21:
        chat = chat[0:18] + ".."
    temp = Image.open("./src/pics/bg.jpg")
    pfp = Image.open(pfp).convert("RGBA")
    pfp = await circle(pfp,(363,363))
    m_font = ImageFont.load_default(35)    
    i_font = ImageFont.load_default(20)    
    nice = temp.copy()
    nice.paste(pfp, (58, 131), pfp)
    draw = ImageDraw.Draw(nice)
    draw.text((565,350),
                text=f"{chat.upper()}",
                font=m_font,
                fill=(275,275,275))
    
    draw.text((180,525),
                text=str(id),
                font=i_font,
                fill=(275,275,275))
    nice.save(f"./src/pics/nice{id}.png")
    return f"./src/pics/nice{id}.png"

@app.on_message(filters.command("welcome"))
async def welcomefunc(app, message) -> None:
    group_admin = await group_admins(message.chat.id)
    if message.from_user.id not in group_admin:
        return await message.reply("You are not an admin.")
    
    if len(message.command) < 2:
        return await message.reply("Usage: /welcome on/off")
    
    status = message.command[1].lower()  # Convert to lowercase for case-insensitive comparison
    if status == "on":
        check_status = WELCOME_DB.find_one({"group_id": message.chat.id})
        if not check_status:
            add_welcome_enable(message.chat.id)
            return await message.reply("Sure, I would like to welcome new members.")
        else:
            await message.reply("It's already enabled.")
    elif status == "off":
        check_status = WELCOME_DB.find_one({"group_id": message.chat.id})
        if not check_status:
            return await message.reply("Welcome message is already disabled.")
        else:
            remove_welcome_enable(message.chat.id)
            return await message.reply("Okay, I will be quiet when anyone joins.")
    else:
        return await message.reply("Invalid syntax!\nTry /welcome on/off")

@app.on_message(filters.new_chat_members, group=6)
async def okbaby(client, message):
    for user in message.new_chat_members:
        check = WELCOME_DB.find_one({"group_id": message.chat.id})
        if not check:
            continue  # Continue to the next iteration if welcome message is not enabled
        photo = await client.download_media(user.photo.big_file_id)
        accha = await pfp(photo, message.chat.title, user.id)
        await message.reply_photo(photo=accha)


