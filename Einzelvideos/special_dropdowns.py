import discord
from discord.ext import commands
from discord.commands import slash_command


class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def select(self, ctx):
        await ctx.respond(view=Dropdown())


def setup(bot):
    bot.add_cog(Base(bot))


class Dropdown(discord.ui.View):
    @discord.ui.role_select(placeholder="Wähle Rollen aus", min_values=1, max_values=3)
    async def role_callback(self, select, interaction):
        mentions = [f"{roles.mention}" for roles in select.values]
        role_list = ", ".join(mentions)
        await interaction.response.send_message(f"Du hast folgende Rollen ausgewählt: {role_list}")

    @discord.ui.channel_select(placeholder="Wähle einen Channel", min_values=1, max_values=1)
    async def channel_callback(self, select, interaction):
        await interaction.response.send_message(f"Du hast {select.values[0].mention} gewählt.")

    @discord.ui.user_select(placeholder="Wähle einen User", min_values=1, max_values=1)
    async def user_callback(self, select, interaction):
        await interaction.response.send_message(f"Du hast {select.values[0].mention} gewählt.")
