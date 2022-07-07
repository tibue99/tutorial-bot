import discord

intents = discord.Intents.default()
intents.message_content = True

bot = discord.Bot(intents=intents)


@bot.event
async def on_ready():
    print(f"{bot.user} ist online")


@bot.event
async def on_message(msg):
    if msg.author.bot:
        return

    await msg.channel.send("Du stinkst")


@bot.event
async def on_message_delete(msg):
    await msg.channel.send(f"Eine Nachricht von {msg.author} wurde gelöscht: {msg.content}")


bot.run("")   # hier token einfügen
