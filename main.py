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

@bot.event                                                      #JUST A COMMAND TO KEEP LOGS
async def on_command(ctx):
    channel = bot.get_channel("CHANNEL ID IN STR FORMAT")
    e = discord.Embed(title = f"Command Used in : `{ctx.guild.name}`", description = f"Used by : `{ctx.author.name}`",color = ctx.author.color)
    e.add_field(name=f"Command name : ",value=f"{ctx.command}")
    e.add_field(name=f"Channel : `{ctx.channel.name}`",value= f"ID : {ctx.channel.id}")
    e.add_field(name=f"Used at : ",value= f"<t:{int(time.time())}:F>")
    e.add_field(name=f"{ctx.message.jump_url}",value="_ _")

    await channel.send(embed = e)



@bot.event                                                     #activity
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Follow my Twitch lol", url="https://www.twitch.tv/hidden_black_"))
    DiscordComponents(bot)
    print("Bot is ready!")

bot.run(Token)


"""
MIT License

Copyright (c) 2021 TheHiddenBlack1

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""