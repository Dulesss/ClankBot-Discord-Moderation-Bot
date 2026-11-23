# Main file: starts ClankBot and loads the cogs.
import logging
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

# Read the bot token from the .env file.
load_dotenv()
token = os.getenv("DISCORD_TOKEN")
if not token:
    raise SystemExit("No DISCORD_TOKEN found. Add it to your .env file.")

# Write Discord's log messages to discord.log (useful when debugging).
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")

# Intents: which events Discord sends the bot.
# members is needed for /stats (member count, joins and leaves).
intents = discord.Intents.default()
intents.members = True

# The cogs (feature files) to load. Remove the # from a line once
# that file has a setup() function, otherwise loading it will fail.
COGS = [
    "cogs.stats",
    # "cogs.moderation",
    # "cogs.minigames",
    # "cogs.tickets",
]


class ClankBot(commands.Bot):
    async def setup_hook(self):
        # Runs once when the bot starts, before it connects.
        for cog in COGS:
            await self.load_extension(cog)
            print(f"Loaded {cog}")

        # Send the slash commands to Discord so they show up in servers.
        synced = await self.tree.sync()
        print(f"Synced {len(synced)} slash command(s)")


# ClankBot uses slash commands, so the prefix is only "mention the bot".
bot = ClankBot(command_prefix=commands.when_mentioned, intents=intents)


@bot.event
async def on_ready():
    print(f"Connected to {bot.user.name}!")


bot.run(token, log_handler=handler, log_level=logging.INFO)
