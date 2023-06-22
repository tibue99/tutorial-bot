import discord
from discord.ext import commands
from discord.commands import slash_command, Option

import chat_exporter
import io


class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def export(self, ctx, anzahl: Option(int, default=100)):
        await ctx.defer()
        transcript = await chat_exporter.export(
            ctx.channel,
            limit=anzahl,
            bot=self.bot,
            tz_info="Europe/Berlin"
        )

        file = discord.File(
            io.BytesIO(transcript.encode()),
            filename="transcript.html"
        )

        msg = await ctx.send(file=file)
        link = await chat_exporter.link(msg)

        embed = discord.Embed(
            description=f"Hier ist der Link zum [Transkript]({link})",
            color=discord.Color.blurple()
        )

        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(Base(bot))
