import discord
from discord.ext import commands
from discord.commands import slash_command, Option


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="Kicke einen Member")
    async def kick(self, ctx, member: Option(discord.Member, "Wähle einen Member")):
        try:
            await member.kick()
        except discord.Forbidden:
            await ctx.respond("Ich habe keine Berechtigung, um diesen Member zu kicken")
            return
        await ctx.respond(f"{member.mention} wurde gekickt!")

    @commands.Cog.listener()
    async def on_application_command_error(self, ctx, error):
        await ctx.respond(f"Es ist ein Fehler aufgetreten: ```{error}```")
        raise error


def setup(bot):
    bot.add_cog(Admin(bot))
