import discord
from discord.ext import commands
from discord.commands import slash_command


class ModalCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def modal(self, ctx):
        modal = TutorialModal(title="Erstelle ein Embed")
        await ctx.send_modal(modal)

    @slash_command()
    async def button_modal(self, ctx):
        await ctx.respond("Hey", view=TutorialView())


def setup(bot):
    bot.add_cog(ModalCog(bot))


class TutorialModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs):
        super().__init__(
            discord.ui.InputText(
                label="Embed Titel",
                placeholder="Placeholder"
            ),
            discord.ui.InputText(
                label="Embed Beschreibung",
                placeholder="Placeholder",
                style=discord.InputTextStyle.long
            ),
            *args,
            **kwargs
        )

    async def callback(self, interaction):
        embed = discord.Embed(
            title=self.children[0].value,
            description=self.children[1].value,
            color=discord.Color.green()
        )
        await interaction.response.send_message(embed=embed)


class TutorialView(discord.ui.View):
    @discord.ui.button(label="Klicke hier")
    async def button_callback(self, button, interaction):
        await interaction.response.send_modal(TutorialModal(title="Erstelle ein Embed"))
