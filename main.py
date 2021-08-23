import os
import sys
import json
import random
import asyncio
import aiohttp
import time
import discord
import jishaku
import requests
import pymongo
import randomstuff
from discord.ext import menus
from discord_components import *
from discord import message
from random import choice
from datetime import datetime
from discord.ext import commands
from asyncio import TimeoutError
from discord.ext.commands.core import command


def get_prefix(bot,message):
    with open('prefix.json','r') as f:
        prefix = json.load(f)
    return prefix[str(message.guild.id)]


bot = commands.Bot(command_prefix=get_prefix, intents= discord.Intents.all() , case_insensitive=True)
bot.launch_time = datetime.utcnow()
bot.remove_command('help')


@bot.event                                                      #PREFIX BEING ADDED ON GUILD JOIN
async def on_guild_join(guild):
    with open('prefix.json','r') as f:
        prefix = json.load(f)
    prefix[str(guild.id)] = '.'

    with open('prefix.json','w') as f:
        json.dump(prefix,f,indent=4)

@bot.event                                                      #PREFIX BEING REMOVED ON GUILD JOIN
async def on_guild_remove(guild):
    with open('prefix.json','r') as f:
        prefix = json.load(f)
    prefix.pop(str(guild.id))

    with open('prefix.json','w') as f:
        json.dump(prefix,f,indent=4)

@bot.command()                                                  #COMMAND TO SET PREFIX
@commands.has_permissions(manage_channels=True)
async def setprefix(ctx, prefixset):
    with open('prefix.json','r') as f:
        prefix = json.load(f)
    prefix[str(ctx.guild.id)] = prefixset

    with open('prefix.json','w') as f:
        json.dump(prefix,f,indent=4)
    
    await ctx.send(f"Prefix Changed To `{prefixset}`")
    

os.environ["JISHAKU_FORCE_PAGINATOR"] = "True"


extensions=[
            'cogs.say',
            'cogs.owner',
            'cogs.fun',
            'cogs.reddit',
            'cogs.do',
            'cogs.slash',
            'cogs.help',
            'cogs.error',
            'cogs.fact',
            'cogs.img',
            'jishaku'
]


if __name__ == "__main__":
    for extension in extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'error loading {extension}' , file=sys.stderr)


if os.path.exists(os.getcwd()+"/config.json"):
    
    with open("./config.json") as f:
        configData = json.load(f)
else:
    configTemplate = {"Token":""}
    with open(os.getcwd()+"/config.json" , "w+") as f:
        json.dump(configTemplate, f)


Token = configData["Token"]


@bot.command()                                                  #LOAD A COG
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'loaded {extension}')

@bot.command()                                                  #UNLOAD A COG
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'unloaded {extension}')

@bot.command()                                                  #RELOAD A COG
@commands.is_owner()
async def reload(ctx, extension):
    bot.reload_extension(f'cogs.{extension}')
    await ctx.send(f'Reloaded {extension}')

@bot.command()                                                  #PING TEST                                  
async def ping(ctx):
    await ctx.send(f'{round(bot.latency * 1000)}ms')

@bot.event                                                      #IDK WHY I PUT IT HERE LMAO                                                                                                       
async def on_message(message):
    if bot.user.mentioned_in(message):
        await message.add_reaction("<:ping:861565960154251264>")
    await bot.process_commands(message)

@bot.event                                                      #ERROR HANDLER FOR COOLCOWN COMMANDS
async def on_command_error(ctx,error):
    if isinstance(error , commands.CommandOnCooldown):
        msg = '**Command on cooldown wait**,{:.2f}s before trying again'.format(error.retry_after)
        await ctx.send(msg)
        await ctx.message.delete()

@bot.event                                                     #activity
async def on_ready():
    DiscordComponents(bot)
    print("-------------------------------------")
    print("Bot is ready!")


bot.run(Token)


"""
Hi lol contribute kek
"""