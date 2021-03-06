import os
import sys
import json
import random
import asyncio
import aiohttp
import typing
import discord
import jishaku
import requests
from discord.ext import menus
from discord.ext import tasks
from datetime import *
from discord.ext import commands

def get_prefix(bot, message):
    try:
        with open('prefix.json', 'r') as f:
            prefix = json.load(f)
        return prefix[str(message.guild.id)]

    except Exception as e:
        return "."
   
 

bot = commands.Bot(command_prefix= get_prefix , intents=discord.Intents.all(), case_insensitive=True)
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

os.environ["JISHAKU_FORCE_PAGINATOR"] = "True"

print(r"""
    ______ ___________ _____ _      ___  _____ 
    | ___ \  _  | ___ \  _  | |    / _ \/  __ \
    | |_/ / | | | |_/ / | | | |   / /_\ \ /  \/
    |    /| | | | ___ \ | | | |   |  _  | |    
    | |\ \\ \_/ / |_/ \ \_/ / |____ | | | \__/\
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
    'cogs.minecraft',
    'cogs.event',
    'jishaku'
]


if __name__ == "__main__":
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'error loading {extension}', file=sys.stderr)
            print(e)
            
# make a meme command using the reddit api and sent it in an embed
@bot.command()
async def meme3(ctx):
    url = 'https://www.reddit.com/r/memes/top/.json?sort=top&t=day'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as r:
            data = await r.json()
            post = random.choice(data['data']['children'])
            embed = discord.Embed(title=post['data']['title'], url=post['data']['url'], color=0x00ff00)
            embed.set_image(url=post['data']['url'])
            await ctx.send(embed=embed)


@bot.command(aliases=['prefix'])  # COMMAND TO SET PREFIX
@commands.has_permissions(manage_channels=True)
async def setprefix(ctx, prefixset):
    with open('prefix.json', 'r') as f:
        prefix = json.load(f)
    prefix[str(ctx.guild.id)] = prefixset
    with open('prefix.json', 'w') as f:
        json.dump(prefix, f, indent=4)
    await ctx.send(f"Prefix Changed To `{prefixset}`")

@bot.event  # activity
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Follow my Twitch lol", url="https://www.twitch.tv/hidden_black_"))
    print("-----------------------------------")
    print("Bot is ready!")


with open("./config.json") as f:
    configData = json.load(f)

Token = configData["Token"]

bot.run(Token)
