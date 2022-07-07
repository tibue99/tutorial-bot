import discord
from discord.commands import Option

intents = discord.Intents.default()

bot = discord.Bot(
    intents=intents,
    debug_guilds=[123456789]  # hier server id einfügen
)


@bot.event
async def on_ready():
    print(f"{bot.user} ist online")


@bot.slash_command(description="Grüße einen User")
async def greet(ctx, user: Option(discord.User, "Der User, den du grüßen möchtest")):
    await ctx.respond(f"Hallo {user.mention}")


@bot.slash_command(description="Lass den Bot eine Nachricht senden")
async def say(
        ctx,
        text: Option(str, "Der Text, den du senden möchtest"),
        channel: Option(discord.TextChannel, "Der Channel, in den du die Nachricht senden möchtest")
):
    await channel.send(text)
    await ctx.respond("Nachricht gesendet", ephemeral=True)


bot.run("")  # hier bot token einfügen
