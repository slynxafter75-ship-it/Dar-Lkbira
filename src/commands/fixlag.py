import discord
from discord import app_commands
from discord.ext import commands


class FixLag(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="fixlag", description="Set voice region to Automatic to fix lag")
    @app_commands.describe(channel="Voice channel li bghiti t-fixi")
    @app_commands.default_permissions(manage_channels=True)
    async def fixlag(self, interaction: discord.Interaction, channel: discord.VoiceChannel):
        await channel.edit(rtc_region=None)  # None = Automatic
        await interaction.response.send_message(
            f"✅ Region dyal {channel.mention} tbedlet l **Automatic**. "
            f"Ila mazal audio unstable, 3awd join voice channel.",
            ephemeral=True
        )


async def setup(bot):
    await bot.add_cog(FixLag(bot))
