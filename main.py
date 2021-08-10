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
bot.owner_ids = [842950909159145493,740906193312284715]
bot.remove_command('help')
bot.load_extension('jishaku')



@bot.event
async def on_guild_join(guild):
    with open('prefix.json','r') as f:
        prefix = json.load(f)
    prefix[str(guild.id)] = '.'

    with open('prefix.json','w') as f:
        json.dump(prefix,f,indent=4)

@bot.event
async def on_guild_remove(guild):
    with open('prefix.json','r') as f:
        prefix = json.load(f)
    prefix.pop(str(guild.id))

    with open('prefix.json','w') as f:
        json.dump(prefix,f,indent=4)

@bot.command()
@commands.has_permissions(manage_channels=True)
async def setprefix(ctx, prefixset):
    with open('prefix.json','r') as f:
        prefix = json.load(f)
    prefix[str(ctx.guild.id)] = prefixset

    with open('prefix.json','w') as f:
        json.dump(prefix,f,indent=4)
    
    await ctx.send(f"Prefix Changed To `{prefixset}`")
    


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
            'cogs.img'
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

if os.path.exists(os.getcwd()+"/prefix.json"):
    
    with open("./prefix.json") as f:
        configData = json.load(f)

else:
    configTemplate = {"GUILD ID HERE":"PREFIX"}
    with open(os.getcwd()+"/prefix.json" , "w+") as f:
        json.dump(configTemplate, f)

Token = configData["Token"]

@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send(f'loaded {extension}')

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send(f'unloaded {extension}')

@bot.command()
@commands.is_owner()
async def reload(ctx, extension):
    bot.reload_extension(f'cogs.{extension}')
    await ctx.send(f'Reloaded {extension}')

@bot.command()                                                                            
async def ping(ctx):
    await ctx.send(f'{round(bot.latency * 1000)}ms')

@bot.event                                                                                                                                       
async def on_message(message):
    if bot.user.mentioned_in(message):
        await message.add_reaction("<:ping:861565960154251264>")
    await bot.process_commands(message)

@bot.event
async def on_command_error(ctx,error):
    if isinstance(error , commands.CommandOnCooldown):
        msg = '**Command on cooldown wait**,{:.2f}s before trying again'.format(error.retry_after)
        await ctx.send(msg)
        await ctx.message.delete()

@bot.event
async def on_command(ctx):
    channel = bot.get_channel(873104600910143490)
    e = discord.Embed(title = f"Command Used in : `{ctx.guild.name}`", description = f"Used by : `{ctx.author.name}`",color = ctx.author.color)
    e.add_field(name=f"Command name : ",value=f"{ctx.command}")
    e.add_field(name=f"Channel : `{ctx.channel.name}`",value= f"ID : {ctx.channel.id}")
    e.add_field(name=f"Used at : ",value= f"<t:{int(time.time())}:F>")
    e.add_field(name=f"{ctx.message.jump_url}",value="_ _")

    await channel.send(embed = e)



@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Follow my Twitch lol", url="https://www.twitch.tv/hidden_black_"))
    DiscordComponents(bot)
    print("Bot is ready!")

bot.run(Token)