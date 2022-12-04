import discord
from discord.ext import commands
from discord.commands import slash_command


options = [
    discord.SelectOption(label="Python", description="Python Beschreibung", emoji="👑"),
    discord.SelectOption(label="Java", description="Java Beschreibung", emoji="💻"),
    discord.SelectOption(label="Javascript", description="Javascript Beschreibung", emoji="🚩", value="JS")
]

keks = discord.SelectOption(label="Keks", emoji="🍪")


class Dropdown(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(TutorialView())

    @slash_command()
    async def select1(self, ctx):
        await ctx.respond("Wähle Programmiersprachen aus", view=TutorialView())

    @slash_command()
    async def select2(self, ctx):
        select = TutorialSelect()
        select.append_option(keks)

        view = discord.ui.View(timeout=None)
        view.add_item(select)

        await ctx.respond(view=view)


def setup(bot):
    bot.add_cog(Dropdown(bot))


class TutorialSelect(discord.ui.Select):
    def __init__(self):
        super().__init__(
            min_values=1,
            max_values=1,
            placeholder="Triff eine Auswahl",
            options=options
        )

    async def callback(self, interaction):
        await interaction.response.send_message(f"Du hast {self.values[0]} gewählt")


class TutorialView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.select(
        min_values=1,
        max_values=2,
        placeholder="Triff eine Auswahl",
        options=options,
        custom_id="keks"
    )
    async def select_callback(self, select, interaction):
        if "Python" in select.values:
            labels = [option.label for option in select.options]
            if "Keks" not in labels:
                select.append_option(keks)
            else:
                select.disabled = True

            await interaction.response.edit_message(view=self)
        else:
            s = ""
            for auswahl in select.values:
                s += f"- {auswahl}\n"

            await interaction.response.send_message(f"Du hast folgendes ausgewählt:\n{s}")
