import io

import discord
import elevenlabs
from discord.commands import slash_command, option
from discord.ext import commands


elevenlabs.set_api_key("")  # hier den api key einfügen
CHOICES = [
    discord.OptionChoice(name=voice.name, value=voice.voice_id) for voice in elevenlabs.voices()
    if voice.category != "premade"
][:25]


class ElevenLabs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command()
    @option("text")
    @option("voice", choices=CHOICES)
    async def voice(self, ctx, text: str, voice: str):
        await ctx.defer()

        output = elevenlabs.generate(
            text=text,
            voice=elevenlabs.Voice(
                voice_id=voice,
                settings=elevenlabs.VoiceSettings(
                    stability=0.71, similarity_boost=0.5, style=0.0, use_speaker_boost=True
                ),
            ),
            model="eleven_multilingual_v2",
        )

        await ctx.respond(
            file=discord.File(io.BytesIO(output), filename="voice.mp3")
        )


def setup(bot):
    bot.add_cog(ElevenLabs(bot))
