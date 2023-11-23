# Für diesen Code muss der Message Content Intent im Discord Dev Portal
# und in der Main-Datei aktiviert sein.

import discord
from discord.ext import commands
from discord.commands import message_command

import aiohttp  # Alternative: https://pypi.org/project/deepl/


class Translate(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.session = None

    @commands.Cog.listener()
    async def on_ready(self):
        self.session = aiohttp.ClientSession()

    @message_command()
    async def translate(self, ctx, message):
        await ctx.defer()
        params = {
            "auth_key": "",  # Hier den API Key einfügen: https://www.deepl.com/de/pro-api
            "text": message.content,
            "target_lang": "DE"
        }

        async with self.session.get(
                "https://api-free.deepl.com/v2/translate", params=params
        ) as response:
            result = await response.json()

        lang = result["translations"][0]["detected_source_language"]
        text = result["translations"][0]["text"]

        embed = discord.Embed(description=text)
        embed.set_author(name=message.author, icon_url=message.author.display_avatar.url)
        embed.set_footer(text=f"Übersetzt aus: {lang}")

        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(Translate(bot))
