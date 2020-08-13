from telethon.sync import TelegramClient, events
from .storage.engine import migrate

from .handlers.score import (
    achieve_score,
    lose_score,
    achieve_score_by_emoji,
    lose_score_by_emoji
)

from dotenv import load_dotenv
import os

# export .env variables
load_dotenv()

# get ORM ready
migrate()

# get .env variables
api_id = int(os.getenv("api_id"))
api_hash = str(os.getenv("api_hash"))

with TelegramClient('anika', api_id, api_hash) as client:
    print("bot is alive.")


    @client.on(events.NewMessage(pattern='(?i)[+]'))
    async def plus_handler(event):
        await achieve_score(event)


    @client.on(events.NewMessage(pattern='(?i)[-]'))
    async def negative_handler(event):
        await lose_score(event)


    @client.on(events.NewMessage(pattern='(?i)[🐣]'))
    async def positive_score_by_emoji(event):
        await achieve_score_by_emoji(event)


    @client.on(events.NewMessage(pattern='(?i)[🔪]'))
    async def negative_score_by_emoji(event):
        await lose_score_by_emoji(event)

    client.run_until_disconnected()
