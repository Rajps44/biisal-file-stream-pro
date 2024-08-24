# (c) biisal (c) adarsh-goel
from pyrogram import Client
import pyromod.listen
from ..vars import Var
from os import getcwd

StreamBot = Client(
    name='Web Streamer',
    api_id=Var.API_ID,
    api_hash=Var.API_HASH,
    bot_token=Var.BOT_TOKEN,
    verify=Var.VERIFY,
    verify_tutorial=Var.VERIFY_TUTORIAL,
    bot_username=Var.BOT_USERNAME,
    sleep_threshold=Var.SLEEP_THRESHOLD,
    workers=Var.WORKERS
)

multi_clients = {}
work_loads = {}
