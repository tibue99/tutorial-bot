import discord
from discord.ext import commands
from discord.commands import slash_command

import aiosqlite
import random


class LevelSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.DB = "level.db"

    @staticmethod
    def get_level(xp):
        lvl = 1

        while True:
            xp -= 100
            if xp < 0:
                return lvl
            lvl += 1

    @commands.Cog.listener()
    async def on_ready(self):
        async with aiosqlite.connect(self.DB) as db:
            await db.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                msg_count INTEGER DEFAULT 0,
                xp INTEGER DEFAULT 0
                )"""
            )

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        xp = random.randint(10, 20)
        
        async with aiosqlite.connect(self.DB) as db:
            await db.execute(
                "INSERT OR IGNORE INTO users (user_id) VALUES (?)", (message.author.id,)
            )
            await db.execute(
                "UPDATE users SET msg_count = msg_count + 1, xp = xp + ? WHERE user_id = ?", (xp, message.author.id)
            )
            await db.commit()

    @slash_command()
    async def rank(self, ctx):
        async with aiosqlite.connect(self.DB) as db:
            async with db.execute("SELECT xp FROM users WHERE user_id = ?", (ctx.author.id,)) as cursor:
                result = await cursor.fetchone()
                if result is None:
                    await ctx.respond("Du bist noch nicht in der Datenbank.", ephemeral=True)
                    return

        xp = result[0]
        lvl = self.get_level(xp)
        await ctx.respond(f"Du hast **{xp}** XP und bist Level **{lvl}**")

    @slash_command()
    async def leaderboard(self, ctx):
        desc = ""
        counter = 1
        async with aiosqlite.connect(self.DB) as db:
            async with db.execute(
                    "SELECT user_id, xp FROM users WHERE msg_count > 0 ORDER BY xp DESC LIMIT 10"
            ) as cursor:
                async for user_id, xp in cursor:
                    desc += f"{counter}. <@{user_id}> - {xp} XP\n"
                    counter += 1

        embed = discord.Embed(
            title="Rangliste",
            description=desc,
            color=discord.Color.yellow()
        )
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(LevelSystem(bot))
