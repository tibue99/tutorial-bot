from discord.ext import commands
from discord.commands import slash_command


class Cooldown(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def hey(self, ctx):
        await ctx.respond("Hey")

    @staticmethod
    def convert_time(seconds: int) -> str:
        if seconds < 60:
            return f"{round(seconds)} Sekunden"
        minutes = seconds / 60
        if minutes < 60:
            return f"{round(minutes)} Minuten"
        hours = minutes / 60
        return f"{round(hours)} Stunden"

    @commands.Cog.listener()
    async def on_application_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            seconds = ctx.command.get_cooldown_retry_after(ctx)
            await ctx.respond(f"Du musst noch {self.convert_time(seconds)} warten", ephemeral=True)


def setup(bot):
    bot.add_cog(Cooldown(bot))
