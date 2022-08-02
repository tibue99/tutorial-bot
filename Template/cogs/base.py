from discord.ext import commands
from discord.commands import slash_command


class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def hello(self, ctx):
        await ctx.respond(f"Hey {ctx.author.mention}")


def setup(bot):
    bot.add_cog(Base(bot))
