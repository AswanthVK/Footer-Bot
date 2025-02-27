# (c) @AbirHasan2005

import os
from os import getenv, environ


class Config(object):
    API_ID = int(os.environ.get("API_ID", 1234567))
    API_HASH = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    SESSION_NAME = os.environ.get("SESSION_NAME", "Footer-Bot")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -100))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", False))
    BOT_OWNER = int(os.environ.get("BOT_OWNER", 1445283714))
    BANNED_USERS = []
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001362659779")).split()))
    MONGODB_URI = os.environ.get("MONGODB_URI", "")
    START_TEXT = """
Hi, {}
I am Channel Custom Caption Bot!

I can add caption to Channel Media Messages. Just add me to the channel as Admin with all rights and setup /settings !!
"""
