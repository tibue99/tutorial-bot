import random

import asyncpraw
import discord
from discord.ext import commands
from discord.commands import slash_command


class Reddit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def meme(self, ctx):
        await ctx.defer()

        # hier die daten von reddit einfügen: https://www.reddit.com/prefs/apps/
        async with asyncpraw.Reddit(
            client_id="",
            client_secret="",
            username="",
            password="",
            user_agent=''
        ) as reddit:
            subreddit = await reddit.subreddit("ich_iel")
            hot = subreddit.hot(limit=25)

            all_posts = []
            async for post in hot:
                if not post.is_video:
                    all_posts.append(post)

            random_post = random.choice(all_posts)

            embed = discord.Embed(title=random_post.title, color=discord.Color.blurple())
            embed.set_image(url=random_post.url)

            await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(Reddit(bot))
