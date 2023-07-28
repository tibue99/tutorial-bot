import discord
from discord.commands import slash_command, option
from discord.ext import commands
from discord.ext.commands import ColorConverter, EmojiConverter


class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    @option("color", type=ColorConverter)
    async def converter(self, ctx: discord.ApplicationContext, color: discord.Color):
        embed = discord.Embed(
            title="Titel",
            color=color
        )
        await ctx.respond(embed=embed, ephemeral=True)

    @slash_command()
    @option("emoji", type=EmojiConverter)
    async def emoji(self, ctx: discord.ApplicationContext, emoji: discord.Emoji):
        embed = discord.Embed(
            title=f"Titel {emoji}",
        )
        await ctx.respond(embed=embed, ephemeral=True)

    @commands.Cog.listener()
    async def on_application_command_error(self, ctx, error):
        if isinstance(error, commands.BadColorArgument):
            await ctx.respond("Du hast eine ungültige Farbe gewählt.", ephemeral=True)
            return
        if isinstance(error, commands.EmojiNotFound):
            await ctx.respond("Du hast ein ungültiges Emoji gewählt.", ephemeral=True)
            return
        raise error


def setup(bot):
    bot.add_cog(Base(bot))
