# Install the requests library
# pip install requests

import logging
from pyrogram import filters, errors
from WebStreamer.vars import Var
from urllib.parse import quote_plus
from WebStreamer.bot import StreamBot, logger
from WebStreamer.utils import get_hash, get_name
from pyrogram.enums.parse_mode import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import requests  # Import the requests library
import json  # Import the json library

# Shortener Configuration
SHORTENER_ENDPOINT = "https://mplaylink.com/api"
MPAYLINK_API_KEY = Var.MPAYLINK_API_KEY

@StreamBot.on_message(
    filters.private
    & (
        filters.document
        | filters.video
        | filters.audio
        | filters.animation
        | filters.voice
        | filters.video_note
        | filters.photo
        | filters.sticker
    ),
    group=4,
)
async def media_receive_handler(_, m: Message):
    if Var.ALLOWED_USERS and not ((str(m.from_user.id) in Var.ALLOWED_USERS) or (m.from_user.username in Var.ALLOWED_USERS)):
        return await m.reply("You are not <b>allowed to use</b> this <a href='https://github.com/EverythingSuckz/TG-FileStreamBot'>bot</a>.", quote=True)
    log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
    file_hash = get_hash(log_msg, Var.HASH_LENGTH)
    stream_link = f"{Var.URL}{log_msg.id}/{quote_plus(get_name(m))}?hash={file_hash}"

    # Shorten the URL using mplaylink.com
    short_link = shorten_url(stream_link)

    logger.info(f"Generated link: {stream_link} for {m.from_user.first_name}")
    try:
        await m.reply_text(
            text="<code>{}</code>".format(
                stream_link,
            ),
            quote=True,
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton(f"Open ({short_link})", url=short_link)]]
            ),
        )
    except errors.ButtonUrlInvalid:
        await m.reply_text(
            text="<code>{}</code>".format(
                stream_link,
            ),
            quote=True,
            parse_mode=ParseMode.HTML,
        )

def shorten_url(url):
    api_key = MPAYLINK_API_KEY
    api_url = f"https://mplaylink.com/api?api={api_key}&url={url}"

    # Make a GET request to mplaylink.com
    response = requests.get(api_url)

    # Parse the JSON response
    try:
        data = response.json()
        short_url = data.get("shortenedUrl", url)
        return short_url
    except json.decoder.JSONDecodeError:
        # Handle the case where JSON decoding fails
        print("Error decoding JSON response:", response.text)
        return url
