import discord
from discord.commands import slash_command
from discord.ext import commands

import aiohttp


webhook_url = ""  # hier die webhook URL einfügen


class Webhook(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    async def webhook1(self, ctx):
        async with aiohttp.ClientSession() as session:
            webhook = discord.Webhook.from_url(
                webhook_url,
                session=session,
                bot_token=self.bot.http.token,
            )
            # webhook = await webhook.fetch()
            # print(webhook.is_partial())

            await webhook.send(
                "Keks",
                username=ctx.user.global_name,
                avatar_url=ctx.user.display_avatar.url,
                wait=True,
            )

    @slash_command()
    async def webhook2(self, ctx):
        final_webhook = None
        for webhook in await ctx.channel.webhooks():
            if webhook.url == webhook_url:
                final_webhook = webhook

        if final_webhook is None:
            return await ctx.respond("Webhook nicht gefunden")

        msg = await final_webhook.send(
            "Keks",
            username=ctx.user.global_name,
            avatar_url=ctx.user.display_avatar.url,
            wait=True
        )
        await msg.add_reaction("🍪")

    @slash_command()
    async def webhook3(self, ctx):
        webhook = await ctx.channel.create_webhook(name="Timo")
        await webhook.send(
            "Keks",
            username=ctx.user.global_name,
            avatar_url=ctx.user.display_avatar.url,
            wait=True,
            view=TutorialView()
        )


def setup(bot):
    bot.add_cog(Webhook(bot))


class TutorialView(discord.ui.View):
    @discord.ui.button(label="Fortnite?")
    async def callback(self, button, interaction):
        await interaction.response.send_message("Fortnite!", ephemeral=True)
