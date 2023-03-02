from discord.ext import commands
from discord.commands import slash_command


class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def reaction(self, ctx):
        interaction = await ctx.respond("Hey")
        message = await interaction.original_response()
        await message.add_reaction("🍪")

    @slash_command()
    async def edit(self, ctx):
        interaction = await ctx.respond("Hey", ephemeral=True)
        await interaction.edit_original_response(content="🍪")


def setup(bot):
    bot.add_cog(Base(bot))
