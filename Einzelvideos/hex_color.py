import discord
from discord.ext import commands
from discord.commands import slash_command, Option


class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def embed(self, ctx, hexcode: Option(str)):
        hex_string = f"0x{hexcode}"
        color = int(hex_string, 16)

        embed = discord.Embed(
            description="Dies ist ein sehr cooler Text"
                        "\n\n🔹 Kekse sind lecker",
            color=color
        )
        embed.set_thumbnail(url=ctx.author.display_avatar)
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(Base(bot))
