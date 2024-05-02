import discord
from discord.ext import commands
from discord import slash_command


class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def greet(self, ctx: discord.ApplicationContext):
        view = TutorialView()
        await ctx.respond(view=view)
        await view.wait()
        print(view.value)


def setup(bot):
    bot.add_cog(Base(bot))


class TutorialView(discord.ui.View):
    def __init__(self):
        super().__init__(disable_on_timeout=True)
        self.value = None

    @discord.ui.button(emoji="1️⃣")
    async def one(self, _, interaction: discord.Interaction):
        self.value = 1
        await interaction.respond("Du hast **1** gewählt")
        self.stop()

    @discord.ui.button(label="2️⃣")
    async def two(self, _, interaction: discord.Interaction):
        self.value = 2
        await interaction.respond("Du hast **2** gewählt")
        self.stop()
