from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyfiglet import figlet_format
from src import app

@app.on_message(filters.command("figlet"))
async def figlet_command(_, message):
    text = " ".join(message.command[1:])
    figlet_text = figlet_format(text)
    response = f"Here is your figlet of '{text}':\n```\n{figlet_text}\n```"
    close_button = InlineKeyboardMarkup([[InlineKeyboardButton("Close", callback_data="figletclose")]])
    await message.reply_text(response, reply_markup=close_button)

@app.on_callback_query(filters.regex("figletclose"))
async def close_callback(_, query: CallbackQuery):
    await query.message.delete()
