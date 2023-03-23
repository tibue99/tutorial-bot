import discord
from discord.ext import commands
from discord.commands import slash_command


class Radio(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="Starte das Radio")
    async def play(self, ctx):
        if ctx.author.voice is None:
            return await ctx.respond("Du musst erst einem Voice Channel beitreten.")

        if not ctx.author.voice.channel.permissions_for(ctx.guild.me).connect:
            return await ctx.respond("Ich habe keine Rechte, um deinem Channel beizutreten.")

        if ctx.voice_client is None:
            await ctx.author.voice.channel.connect()  # Bot ist in keinem Voice Channel
        else:
            await ctx.voice_client.move_to(ctx.author.voice.channel)  # Bot ist schon in einem anderen Voice Channel

        if ctx.voice_client.is_playing():
            ctx.voice_client.stop()

        ctx.voice_client.play(
            discord.FFmpegPCMAudio("https://streams.ilovemusic.de/iloveradio1.mp3")
        )
        await ctx.respond("Das Radio wurde gestartet")

    @slash_command(description="Stoppe das Radio")
    async def leave(self, ctx):
        if ctx.voice_client is None:
            return await ctx.respond("Ich bin mit keinem Voice Channel verbunden.")

        await ctx.voice_client.disconnect()
        await ctx.respond("Bis bald")


def setup(bot):
    bot.add_cog(Radio(bot))
