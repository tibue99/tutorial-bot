import discord
from discord.ext import commands
from discord.commands import slash_command


class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def bild(self, ctx):
        embed = discord.Embed(
            title="Lecker",
            color=discord.Color.blue()
        )
        file = discord.File(f"cookie.png", filename="image.png")
        embed.set_image(url="attachment://image.png")
        await ctx.respond(embed=embed, file=file)


def setup(bot):
    bot.add_cog(Base(bot))
