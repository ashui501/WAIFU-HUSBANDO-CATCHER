from shivu import collection, user_collection, application
from pyrogram import filters
from Database.status_db import (
    get_user_data,
    get_user_Core,
)

@app.on_message(filters.command("inv"))
async def inv(app, message):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    current = await get_user_data(user_id)
    status_text = "___\n"
    status_text += f"🥋Name: {user_name}\n"
    status_text += f"🪪Id: {user_id}\n"
    status_text += "___\n"
    status_text += f"💠 coins: {current['Core']}\n"
    await message.reply(status_text)
