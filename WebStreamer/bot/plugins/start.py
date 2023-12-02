from pyrogram import filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.types import User  # Fix the import line

from WebStreamer.vars import Var
from WebStreamer.bot import StreamBot

@StreamBot.on_message(filters.command(["start", "help"]) & filters.private)
async def start(_, m: Message):
    # Check if the user is in the allowed list
    if Var.ALLOWED_USERS and not ((str(m.from_user.id) in Var.ALLOWED_USERS) or (m.from_user.username in Var.ALLOWED_USERS)):
        return await m.reply(
            "You are not in the allowed list of users who can use me. \
            Check <a href='https://github.com/EverythingSuckz/TG-FileStreamBot#optional-vars'>this link</a> for more info.",
            disable_web_page_preview=True, quote=True
        )

    # Check if the user is a member of the channel
    if Var.CHANNEL_ID:
        channel_member = await User(Var.CHANNEL_ID).get_member(m.from_user.id)
        if not channel_member.status == "member":
            # If not a member, send a message and invite to join channel
            invite_text = (
                "You need to be a member of the channel to use this bot. Join the channel and try again.\n\n"
                f"Join here: {Var.CHANNEL_INVITE_LINK}"
            )
            return await m.reply(invite_text, disable_web_page_preview=True, quote=True)

    # Your new message
    message_text = "I am Telegram File to Link Generator Bot with Channel support.\nSend me any file and get a direct download link and streamable link."

    # Create buttons with emojis
    buttons = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("👤 Bot owner", url="https://t.me/being_ram_esh")],
            [InlineKeyboardButton("💬 Chat support", url="https://t.me/+ZrS7H52Qeik0NjM1")]
        ]
    )

    # Reply with the new message and buttons
    await m.reply(
        text=message_text,
        reply_markup=buttons
                                 )
