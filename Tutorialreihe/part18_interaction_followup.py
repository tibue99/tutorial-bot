import discord
from discord.ext import commands
from discord.commands import slash_command


class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def button(self, ctx):
        await ctx.respond(view=TutorialView(), ephemeral=True)


def setup(bot):
    bot.add_cog(Base(bot))


class TutorialView(discord.ui.View):
    @discord.ui.button(label="Keks", style=discord.ButtonStyle.primary, emoji="🍪")
    async def button_callback(self, button, interaction):
        await interaction.response.edit_message(content="Keks1")
        await interaction.followup.send("Keks2", ephemeral=True)
