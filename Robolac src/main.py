import os
import sys
import json
import random
import asyncio
import aiohttp
import typing
import time
import discord
import jishaku
import requests
import pymongo
import clever_chat
from clever_chat import AsyncClient
from typing import List
import randomstuff
from discord.ext import menus
from discord import message
from random import choice
from datetime import datetime
from discord.ext import commands
from asyncio import TimeoutError


def get_prefix(bot, message):
    try:
        with open('prefix.json', 'r') as f:
            prefix = json.load(f)
        return prefix[str(message.guild.id)]

    except Exception as e:
        return "."


bot = commands.Bot(command_prefix=",", intents=discord.Intents.all(
), case_insensitive=True)
bot.owner_ids = [842950909159145493, 740906193312284715]
bot.launch_time = datetime.utcnow()

class MyHelpCommand(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        e = discord.Embed(colour = discord.Colour.from_hsv(random.random(), 1, 1), description='')
        for page in self.paginator.pages:
            e.description += page
        await destination.send(embed=e)

bot.help_command = MyHelpCommand()

@bot.event  # PREFIX BEING ADDED ON GUILD JOIN
async def on_guild_join(guild):
    with open('prefix.json', 'r') as f:
        prefix = json.load(f)
    prefix[str(guild.id)] = ','

    with open('prefix.json', 'w') as f:
        json.dump(prefix, f, indent=4)

    channel = bot.get_channel(877428062336192542)

    e = discord.Embed(
        title=f"Bot added in :`{guild.name}`", description=f"_ _", color=0x00FF00)
    e.add_field(
        name=f"No of members : {len(guild.members)}", value=f"<t:{int(time.time())}:F>")
    await channel.send(embed=e)


@bot.event  # PREFIX BEING REMOVED ON GUILD JOIN
async def on_guild_remove(guild):
    with open('prefix.json', 'r') as f:
        prefix = json.load(f)
    prefix.pop(str(guild.id))

    with open('prefix.json', 'w') as f:
        json.dump(prefix, f, indent=4)

    channel = bot.get_channel(877428062336192542)

    e = discord.Embed(
        title=f"Bot removed in :`{guild.name}`", description=f"_ _", color=0xFF0000)
    e.add_field(
        name=f"No of members : {len(guild.members)}", value=f"<t:{int(time.time())}:F>")
    await channel.send(embed=e)


@bot.command()  # COMMAND TO SET PREFIX
@commands.has_permissions(manage_channels=True)
async def setprefix(ctx, prefixset):
    with open('prefix.json', 'r') as f:
        prefix = json.load(f)
    prefix[str(ctx.guild.id)] = prefixset

    with open('prefix.json', 'w') as f:
        json.dump(prefix, f, indent=4)

    await ctx.send(f"Prefix Changed To `{prefixset}`")


os.environ["JISHAKU_FORCE_PAGINATOR"] = "True"

print("""
        ______ ___________ _____ _      ___  _____ 
        | ___ \  _  | ___ \  _  | |    / _ \/  __ \\
        | |_/ / | | | |_/ / | | | |   / /_\ \ /  \/
        |    /| | | | ___ \ | | | |   |  _  | |    
        | |\ \\\\ \_/ / |_/ \ \_/ / |____ | | | \__/\\
        \_| \_|\___/\____/ \___/\_____\_| |_/\____/
                        An Idiot Bot By HiddenBlack
    """)



extensions = [
    'cogs.say',
    'cogs.owner',
    'cogs.fun',
    'cogs.reddit',
    'cogs.slash',
    # 'cogs.help',
    'cogs.chatbot',
    'cogs.error',
    'cogs.fact',
    'cogs.img',
    'cogs.mod',
    'jishaku'
]


if __name__ == "__main__":
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'error loading {extension}', file=sys.stderr)
            print(e)

if os.path.exists(os.getcwd()+"/config.json"):

    with open("./config.json") as f:
        configData = json.load(f)
else:
    configTemplate = {"Token": ""}
    with open(os.getcwd()+"/config.json", "w+") as f:
        json.dump(configTemplate, f)


Token = configData["Token"]


@bot.event  # IDK WHY I PUT IT HERE LMAO
async def on_message(message):
    if bot.user.mentioned_in(message):
        await message.add_reaction("<:ping:861565960154251264>")
    await bot.process_commands(message)


@bot.event  # activity
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Follow my Twitch lol", url="https://www.twitch.tv/hidden_black_"))
    print("-----------------------------------")
    print("Bot is ready!")



bot.run(Token)
