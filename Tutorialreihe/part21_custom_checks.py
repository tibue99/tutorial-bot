import discord
from discord.ext import commands
from discord.commands import slash_command


async def custom_check(ctx):
    return ctx.author.id == 123456789  # hier user ID einfügen


class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    @commands.check(custom_check)
    async def hallo(self, ctx):
        await ctx.respond("Hey")

    @commands.Cog.listener()
    async def on_application_command_error(self, ctx, error):
        if isinstance(error, discord.CheckFailure):
            await ctx.respond(f"Du bist nicht würdig genug, um diesem Befehl zu nutzen!", ephemeral=True)
            return

        await ctx.respond(f"Es ist ein Fehler aufgetreten: ```{error}```", ephemeral=True)
        raise error


def setup(bot):
    bot.add_cog(Base(bot))
