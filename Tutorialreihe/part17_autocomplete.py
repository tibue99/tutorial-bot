import discord
from discord.utils import basic_autocomplete
from discord.ext import commands
from discord.commands import slash_command, Option

food = ["Pizza", "Pommes", "Döner"]


def get_food(ctx: discord.AutocompleteContext):
    if "99" in ctx.interaction.user.display_name:
        return food + ["Kekse"]

    return food


class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def essen(
            self, ctx, auswahl: Option(str, autocomplete=basic_autocomplete(get_food))
    ):
        await ctx.respond(f"Du hast ✨ **{auswahl}** ✨ gewählt")


def setup(bot):
    bot.add_cog(Base(bot))
