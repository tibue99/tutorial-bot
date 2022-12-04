# Für dieses Beispiel muss der Server Member Intent im Dev Portal und in der Main-Datei aktiviert sein
#
# intents = discord.Intents.default()
# intents.members = True
#
# bot = discord.Bot(
#     intents=intents,
#     debug_guilds=[123456789],  # hier server id einfügen
# )

import discord
from discord.ext import commands
from discord.commands import slash_command


class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def greet(self, ctx):
        await ctx.respond(f"Hey {ctx.author.mention}")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        embed = discord.Embed(
            title="Willkommen",
            description=f"Hey {member.mention}",
            color=discord.Color.orange()
        )

        channel = await self.bot.fetch_channel(123456789)  # hier channel id einfügen
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Base(bot))
