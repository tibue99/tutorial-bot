from discord.ext import commands, tasks
from datetime import time, timezone


class Task(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        self.keks.start()
        self.time_task.start()

    @tasks.loop(seconds=5)
    async def keks(self):
        if self.keks.current_loop == 0:
            return

        channel = await self.bot.fetch_channel(123456789)  # hier channel id einfügen
        await channel.send("Keks")

    @tasks.loop(
        time=time(22, 0, tzinfo=timezone.utc)
    )
    async def time_task(self):
        print("Es ist 22:00 Uhr UTC")


def setup(bot):
    bot.add_cog(Task(bot))
