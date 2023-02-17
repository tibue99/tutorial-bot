import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup


class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    eat = SlashCommandGroup("eat", description="Essen ist lecker")

    @eat.command()
    async def cookie(self, ctx):
        await ctx.respond("Du hast dir einen Keks gegönnt")

    @eat.command()
    async def pizza(self, ctx):
        await ctx.respond("Du hast dir eine Pizza gegönnt")

    give = SlashCommandGroup(
        "give",
        default_member_permissions=discord.Permissions(administrator=True)
    )

    keks = give.create_subgroup("keks")

    @keks.command()
    async def schoko(self, ctx):
        await ctx.respond("Ein legendärer Schokokeks wurde vergeben")

    @keks.command()
    async def subway(self, ctx):
        await ctx.respond("Subway Cookie wurde vergeben!!!")


def setup(bot):
    bot.add_cog(Base(bot))
