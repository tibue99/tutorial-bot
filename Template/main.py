import discord
import os

intents = discord.Intents.default()

bot = discord.Bot(
    intents=intents,
    debug_guilds=[123456789]  # hier server id einfügen
)


@bot.event
async def on_ready():
    print(f"{bot.user} ist online")


bot.run(os.getenv("TOKEN"))
