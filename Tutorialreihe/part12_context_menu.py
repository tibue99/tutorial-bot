import discord
from discord.ext import commands
from discord.commands import message_command, user_command


class Context(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @message_command(name="Zeige die ID")
    async def get_id(self, ctx, message):
        await ctx.respond(f"Hier ist die Message ID: {message.id}")

    @user_command()
    async def stups(self, ctx, member: discord.Member):
        await ctx.respond(f"{ctx.author.mention} hat {member.mention} angestupst!")


def setup(bot):
    bot.add_cog(Context(bot))
