import discord
from discord.ext import commands
from discord.commands import slash_command

import requests
import random
import os

from pprint import pprint


class API(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def keks(self, ctx):
        key = os.getenv("API_KEY")

        params = {
            "q": "keks",
            "key": key,
            "limit": "10",
            "client_key": "discord_bot",
            "media_filter": "gif"
        }
        result = requests.get("https://tenor.googleapis.com/v2/search", params=params)
        data = result.json()
        # pprint(data)

        number = random.randint(0, 9)
        url = data['results'][number]['media_formats']['gif']['url']

        embed = discord.Embed(
            title="Keks",
            color=discord.Color.yellow()
        )
        embed.set_image(url=url)
        embed.set_footer(text="Via Tenor")
        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(API(bot))
