import discord
from discord.ext import commands
from discord.commands import slash_command, Option


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(description="Kicke einen Member")
    @discord.default_permissions(administrator=True, kick_members=True)
    @discord.guild_only()
    async def kick(self, ctx, member: Option(discord.Member, "Wähle einen Member")):
        try:
            await member.kick()
        except discord.Forbidden:
            await ctx.respond("Ich habe keine Berechtigung, um diesen Member zu kicken", ephemeral=True)
            return
        await ctx.respond(f"{member.mention} wurde gekickt!")

    @slash_command()
    @commands.has_permissions(administrator=True)
    async def hallo(self, ctx):
        await ctx.respond("Hey")

    @commands.Cog.listener()
    async def on_application_command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            await ctx.respond(f"Nur Admins dürfen diesen Befehl ausführen!", ephemeral=True)
            return

        await ctx.respond(f"Es ist ein Fehler aufgetreten: ```{error}```", ephemeral=True)
        raise error


def setup(bot):
    bot.add_cog(Admin(bot))
