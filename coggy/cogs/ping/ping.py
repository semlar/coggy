import time

from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """Pong!"""
        start_time = time.monotonic()
        socket_latency = int(self.bot.latency * 1000 + 0.5)
        message = await ctx.send("🏓  Pong")
        chat_latency = int((time.monotonic() - start_time) * 1000 + 0.5)
        await message.edit(
            content=f"🏓  WebSocket: {socket_latency}ms  |  Chat latency: {chat_latency}ms"
        )


async def setup(bot):
    await bot.add_cog(Ping(bot))
