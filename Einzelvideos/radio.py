import discord
from discord.ext import commands
from discord.commands import slash_command


class Radio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="Starte das Radio")
    async def play(self, ctx):
        await ctx.author.voice.channel.connect()

        ctx.voice_client.play(
            discord.FFmpegPCMAudio("https://streams.ilovemusic.de/iloveradio1.mp3")
        )
        await ctx.respond("Das Radio wurde gestartet")

    @slash_command(description="Stoppe das Radio")
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()
        await ctx.respond("Bis bald")


def setup(bot):
    bot.add_cog(Radio(bot))
