import discord
from discord.ext import commands
from discord.commands import slash_command, Option


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def activity(
            self, ctx,
            typ: Option(str, choices=["game", "stream"]),
            name: Option(str)
    ):
        if typ == "game":
            act = discord.Game(name=name)
        else:
            act = discord.Streaming(
                name=name,
                url="https://www.twitch.tv/keks"
            )

        await self.bot.change_presence(activity=act, status=discord.Status.online)
        await ctx.respond("Status wurde geändert!")


def setup(bot):
    bot.add_cog(Commands(bot))
