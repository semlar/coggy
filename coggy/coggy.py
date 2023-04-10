import discord
import json
import os
import traceback

from discord.ext.commands import AutoShardedBot

class Bot(AutoShardedBot):
    def __init__(self, *args, prefix=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.prefix = prefix

    async def on_message(self, msg):
        if not self.is_ready() or msg.author.bot:
            return

        await self.process_commands(msg)

def main():
    print("Logging in..")
    try:
        config = json.load(open("config.json", encoding="utf8"))
        bot = Bot(
            command_prefix=config["prefix"],
            prefix=config["prefix"],
            owner_ids=config["owners"],
            command_attrs=dict(hidden=True),
            intents=discord.
            Intents(  # https://discordpy.readthedocs.io/en/latest/api.html?highlight=intents#discord.Intents
                guilds=True,
                messages=True,
                message_content=True
            ),
        )

        bot.run(os.environ.get("DISCORD_TOKEN", config["token"]))
    except Exception as e:
        print("Error while logging in!")
        traceback.print_exc()

if __name__ == "__main__":
	main()
