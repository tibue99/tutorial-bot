# Für dieses Beispiel muss der Message Content Intent im Dev Portal und in der Main-Datei aktiviert sein
#
# intents = discord.Intents.default()
# intents.message_content = True
#
# bot = discord.Bot(
#     intents=intents,
#     debug_guilds=[123456789],  # hier server id einfügen
# )

from discord.ext import commands
from discord.commands import slash_command

import asyncio


class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def wait(self, ctx):
        await ctx.respond("Gib eine Zahl ein.")

        def check(message):
            return message.author == ctx.author and message.content.isdigit()

        try:
            answer = await self.bot.wait_for("message", check=check, timeout=5.0)
        except asyncio.TimeoutError:
            await ctx.send_followup(f"Bruh, du warst zu langsam!")
            return

        await answer.reply(f"Du hast die Zahl {answer.content} eingegeben.")


def setup(bot):
    bot.add_cog(Base(bot))
