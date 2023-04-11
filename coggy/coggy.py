import asyncio
import json
import os
import traceback

import discord
from discord.ext.commands import AutoShardedBot

COG_DIR = "coggy/cogs"


class Bot(AutoShardedBot):
    def __init__(self, *args, prefix=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.prefix = prefix

    async def on_message(self, msg):
        if not self.is_ready() or msg.author.bot:
            return

        await self.process_commands(msg)

    async def on_ready(self):
        print(f"Logged in as {self.user} (ID: {self.user.id})")


async def main():
    try:
        config = json.load(open("config.json", encoding="utf8"))
        bot = Bot(
            command_prefix=config["prefix"],
            prefix=config["prefix"],
            owner_ids=config["owners"],
            command_attrs=dict(hidden=True),
            intents=discord.Intents(  # https://discordpy.readthedocs.io/en/latest/api.html?highlight=intents#discord.Intents
                guilds=True, messages=True, message_content=True
            ),
        )

        # Automatically import extensions
        cogs = [
            f"{COG_DIR.replace('/', '.')}.{name}.{name}"
            for name in os.listdir(COG_DIR)
            if os.path.isdir(f"{COG_DIR}/{name}")
        ]
        for cog in cogs:
            name = cog.split(".")[-1].capitalize()
            print(f"Loading plugin: {name}")
            await bot.load_extension(cog)

        # Start client
        print("Logging in..")
        await bot.start(os.environ.get("DISCORD_TOKEN", config["discord_token"]))
    except Exception as e:
        print("Error while logging in!")
        traceback.print_exc()


def start():
    # Start async main loop
    asyncio.run(main())


if __name__ == "__main__":
    start()
