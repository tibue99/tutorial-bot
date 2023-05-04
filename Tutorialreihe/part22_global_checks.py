import discord
from discord.ext import commands
from discord.commands import slash_command


class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @staticmethod
    async def bot_check(ctx):
        if ctx.author.id != 123456789:  # hier user ID einfügen
            await ctx.respond("Du bist nicht würdig genug, um diesen Befehl zu nutzen!")
            return False
        return True

    @staticmethod
    async def cog_check(ctx):
        if ctx.author.voice is None:
            await ctx.respond("Tritt erst einem Voice Channel bei.")
            return False
        return True

    @slash_command()
    async def hey(self, ctx):
        await ctx.respond("Hey")

    @commands.Cog.listener()
    async def on_application_command_error(self, ctx, error):
        if isinstance(error, discord.CheckFailure):
            return
        raise error


def setup(bot):
    bot.add_cog(Base(bot))
