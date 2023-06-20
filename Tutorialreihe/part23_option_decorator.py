import discord
from discord.ext import commands
from discord.commands import slash_command, option


class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    @option("user", description="Wähle einen User")
    @option("auswahl", description="Beschreibung", choices=["Ja", "Nein"])
    async def hello(self, ctx, user: discord.User, auswahl: str = "Ja"):
        await ctx.respond(f"{auswahl}, {user.mention}")


def setup(bot):
    bot.add_cog(Base(bot))
