import discord
from discord.ext import commands
from discord.commands import slash_command, Option

import openai
openai.api_key = "KEY"  # hier den api key einfügen


class GPT(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def gpt(self, ctx, text: Option(str)):
        await ctx.defer()
        result = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Du bist ein Jugendlicher, der in jeden Satz Füllworte wie 'sheesh', 'bruh', 'digga' und 'ehrenlos' einbaut"
                },
                {"role": "user", "content": text}
            ],
            max_tokens=250
        )
        embed = discord.Embed(
            color=discord.Color.blurple(),
            description=result["choices"][0]["message"]["content"]
        )
        await ctx.respond(embed=embed)


def setup(bot: discord.Bot):
    bot.add_cog(GPT(bot))
