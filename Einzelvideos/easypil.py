import discord
from discord.ext import commands
from discord.commands import slash_command

from easy_pil import Editor, Font, load_image_async


class Image(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def rank(self, ctx):
        background = Editor("space.png").resize((800, 250))

        avatar = await load_image_async(ctx.author.display_avatar.url)
        circle_avatar = Editor(avatar).resize((200, 200)).circle_image()
        background.paste(circle_avatar, (25, 25))

        big_text = Font.poppins(size=50, variant="bold")
        small_text = Font.poppins(size=30, variant="regular")

        background.text((490, 50), f"{ctx.author}", color="white", font=big_text, align="center")
        background.text(
            (490, 125), "Du hast 55 XP und bist Level 2", color="#00ced1", font=small_text, align="center"
        )

        file = discord.File(fp=background.image_bytes, filename='rank.png')
        return await ctx.respond(file=file)


def setup(bot):
    bot.add_cog(Image(bot))
