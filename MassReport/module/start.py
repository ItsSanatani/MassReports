from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from MassReport.module import report
from MassReport import app


LOG_CHANNEL_ID = -1002640038102

@app.on_message(filters.command("start") & filters.private)
async def start_command(client, message):
    buttons = [
        [InlineKeyboardButton("➕ Start Reporting", callback_data="start_report")]
    ]
    await message.reply_photo(
        photo="https://files.catbox.moe/31g9nf.jpg",
        caption="**Welcome to Mass Report Bot!**\n\nClick the button below to start reporting.",
        reply_markup=InlineKeyboardMarkup(buttons)
    )

    user = message.from_user
    log_text = f"""
🚀 **New User Started Bot!**

👤 **User:** [{user.first_name}](tg://user?id={user.id})

🆔 **Username:** @{user.username if user.username else 'N/A'}

🌐 **Language:** {user.language_code if user.language_code else 'N/A'}

🆔 **User ID:** `{user.id}`
"""

    try:
        await app.send_message(
            chat_id=LOG_CHANNEL_ID,
            text=log_text,
            disable_web_page_preview=True
        )
    except Exception as e:
        print(f"Logging Error: {e}")
