# This file is a part of TG-FileStreamBot
# Coding: Jyothis Jayanth [@EverythingSuckz]

import sys
from os import environ
from dotenv import load_dotenv
from pyrogram.types import User  # Add this import

load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(environ.get("API_ID", "15070966"))
    API_HASH = str(environ.get("API_HASH", "636638d9c79d98996e395a82b1b7a21e"))
    BOT_TOKEN = str(environ.get("BOT_TOKEN", "6532913422:AAEUNgYYI3-k9Q2U2scj6uHB_1pMPgqMQhs"))
    SLEEP_THRESHOLD = int(environ.get("SLEEP_THRESHOLD", "60"))  # 1 minute
    WORKERS = int(environ.get("WORKERS", "6"))  # 6 workers = 6 commands at once
    BIN_CHANNEL = int(environ.get("BIN_CHANNEL", "-1001615768866"))  # Your channel ID
    PORT = int(environ.get("PORT", 8080))
    BIND_ADDRESS = str(environ.get("WEB_SERVER_BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    HAS_SSL = str(environ.get("HAS_SSL", "1").lower()) in ("1", "true", "t", "yes", "y")
    NO_PORT = str(environ.get("NO_PORT", "1").lower()) in ("1", "true", "t", "yes", "y")
    HASH_LENGTH = int(environ.get("HASH_LENGTH", 6))
    if not 5 < HASH_LENGTH < 64:
        sys.exit("Hash length should be greater than 5 and less than 64")
    FQDN = str(environ.get("FQDN", BIND_ADDRESS))
    URL = "http{}://{}{}/".format(
            "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(PORT)
        )
    KEEP_ALIVE = str(environ.get("KEEP_ALIVE", "0").lower()) in  ("1", "true", "t", "yes", "y")
    DEBUG = str(environ.get("DEBUG", "0").lower()) in ("1", "true", "t", "yes", "y")
    USE_SESSION_FILE = str(environ.get("USE_SESSION_FILE", "0").lower()) in ("1", "true", "t", "yes", "y")
    ALLOWED_USERS = [x.strip("@ ") for x in str(environ.get("ALLOWED_USERS", "") or "").split(",") if x.strip("@ ")]

    # Change the next line to use the User class correctly
    user = User(Var.BIN_CHANNEL)
    CHANNEL_ID = Var.BIN_CHANNEL
    CHANNEL_INVITE_LINK = "https://t.me/film4movieee"  # Your channel invite link
Certainly! Here's the corrected full code:

```python
# This file is a part of TG-FileStreamBot
# Coding: Jyothis Jayanth [@EverythingSuckz]

import sys
from os import environ
from dotenv import load_dotenv
from pyrogram.types import User  # Add this import

load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(environ.get("API_ID", "15070966"))
    API_HASH = str(environ.get("API_HASH", "636638d9c79d98996e395a82b1b7a21e"))
    BOT_TOKEN = str(environ.get("BOT_TOKEN", "6532913422:AAEUNgYYI3-k9Q2U2scj6uHB_1pMPgqMQhs"))
    SLEEP_THRESHOLD = int(environ.get("SLEEP_THRESHOLD", "60"))  # 1 minute
    WORKERS = int(environ.get("WORKERS", "6"))  # 6 workers = 6 commands at once
    BIN_CHANNEL = int(environ.get("BIN_CHANNEL", "-1001615768866"))  # Your channel ID
    PORT = int(environ.get("PORT", 8080))
    BIND_ADDRESS = str(environ.get("WEB_SERVER_BIND_ADDRESS", "0.0.0.0"))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    HAS_SSL = str(environ.get("HAS_SSL", "1").lower()) in ("1", "true", "t", "yes", "y")
    NO_PORT = str(environ.get("NO_PORT", "1").lower()) in ("1", "true", "t", "yes", "y")
    HASH_LENGTH = int(environ.get("HASH_LENGTH", 6))
    if not 5 < HASH_LENGTH < 64:
        sys.exit("Hash length should be greater than 5 and less than 64")
    FQDN = str(environ.get("FQDN", BIND_ADDRESS))
    URL = "http{}://{}{}/".format(
            "s" if HAS_SSL else "", FQDN, "" if NO_PORT else ":" + str(PORT)
        )
    KEEP_ALIVE = str(environ.get("KEEP_ALIVE", "0").lower()) in  ("1", "true", "t", "yes", "y")
    DEBUG = str(environ.get("DEBUG", "0").lower()) in ("1", "true", "t", "yes", "y")
    USE_SESSION_FILE = str(environ.get("USE_SESSION_FILE", "0").lower()) in ("1", "true", "t", "yes", "y")
    ALLOWED_USERS = [x.strip("@ ") for x in str(environ.get("ALLOWED_USERS", "") or "").split(",") if x.strip("@ ")]

    # Change the next line to use the User class correctly
    user = User(Var.BIN_CHANNEL)
    CHANNEL_ID = Var.BIN_CHANNEL
    CHANNEL_INVITE_LINK = "https://t.me/film4movieee"  # Your channel invite link
