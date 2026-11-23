# Stats cog: commands for member count and server activity.
import discord
from discord import app_commands
from discord.ext import commands


class Stats(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # /membercount: shows how many members the server has.
    @app_commands.command(name="membercount", description="Show the total number of members in this server")
    @app_commands.guild_only()  # Only works in a server, not in DMs.
    async def membercount(self, interaction: discord.Interaction):
        guild = interaction.guild

        embed = discord.Embed(
            title=f"{guild.name} Members",
            description=f"This server has **{guild.member_count}** members.",
            color=discord.Color.blurple(),
        )
        if guild.icon:
            embed.set_thumbnail(url=guild.icon.url)

        await interaction.response.send_message(embed=embed)


# discord.py calls this when bot.py loads "cogs.stats".
async def setup(bot: commands.Bot):
    await bot.add_cog(Stats(bot))
