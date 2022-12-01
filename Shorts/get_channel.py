import discord
from discord.ext import commands
from discord.commands import slash_command


class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        channel_id = 123456789  # Hier Channel ID einfügen

        # Variante 1
        channel = self.bot.get_channel(channel_id)

        # Variante 2
        try:
            channel = await self.bot.fetch_channel(channel_id)
        except discord.Forbidden:
            print("Keine Rechte")
            return

        # Variante 3
        channel = await discord.utils.get_or_fetch(self.bot, "channel", channel_id, default=None)

        if channel is not None:
            await channel.send("Kekse sind lecker!")
        else:
            print("Channel wurde nicht gefunden :(")

    @slash_command()
    async def say(self, ctx):
        channel_id = 123456789  # Hier Channel ID einfügen

        # Variante 4
        channel = ctx.guild.get_channel(channel_id)  # Geht auch mit fetch

        # Variante 5
        channel = discord.utils.get(ctx.guild.text_channels, id=channel_id)  # Geht auch mit dem Namen des Channels

        if channel is not None:
            await channel.send("Kekse sind schmackhaft!")
            await ctx.respond("Nachricht gesendet.")
        else:
            await ctx.respond("Channel wurde nicht gefunden :(")


def setup(bot):
    bot.add_cog(Base(bot))
