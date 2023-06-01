import discord
from discord.ext import commands


class Base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):
        try:
            integrations = await guild.integrations()
        except discord.Forbidden:
            return

        for integration in integrations:
            if isinstance(integration, discord.BotIntegration):
                if integration.application.user == self.bot.user:
                    try:
                        await integration.user.send("Danke fürs Einladen!")
                    except discord.Forbidden:
                        return
                    break


def setup(bot):
    bot.add_cog(Base(bot))
