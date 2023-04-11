from discord.ext import commands


class CommandCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
