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


@bot.slash_command(name="userinfo", description="Zeige Infos über einen User")
async def info(
        ctx,
        alter: Option(int, "Das Alter", min_value=1, max_value=99),
        user: Option(discord.Member, "Gib einen User an", default=None),
):
    if user is None:
        user = ctx.author

    embed = discord.Embed(
        title=f"Infos über {user.name}",
        description=f"Hier siehst du alle Details über {user.mention}",
        color=discord.Color.blue()
    )

    time = discord.utils.format_dt(user.created_at, "R")

    embed.add_field(name="Account erstellt", value=time, inline=False)
    embed.add_field(name="ID", value=user.id)
    embed.add_field(name="Alter", value=alter)

    embed.set_thumbnail(url=ctx.author.display_avatar.url)
    embed.set_footer(text="Das ist ein Footer")

    await ctx.respond(embed=embed)


bot.run("")  # hier bot token einfügen
