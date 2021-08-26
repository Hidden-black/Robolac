"""
Need Help in this cog pls help :/
IDK How to store the prefixes
When 
"""



import os
import sys
import json
import random
import aiohttp
import discord
import jishaku
import requests
import randomstuff
from discord import message
from datetime import datetime
from discord.ext import commands
from discord.ext.commands.core import command


import clever_chat
from clever_chat import AsyncClient
import asyncio


def cbl(bot, message):
  with open('chb.json', 'r') as f:
    prefix = json.load(f)
    return prefix[str(message.channel.id)]

bot = commands.Bot(command_prefix=',', intents= discord.Intents.all() , case_insensitive=True)
bot.launch_time = datetime.utcnow()
bot.owner_ids = [842950909159145493,740906193312284715]
bot.remove_command('help')
bot.load_extension('jishaku')

if os.path.exists(os.getcwd()+"/config.json"):
    
    with open("./config.json") as f:
        configData = json.load(f)
else:
    configTemplate = {"Token":""}
    with open(os.getcwd()+"/config.json" , "w+") as f:
        json.dump(configTemplate, f)

Token = configData["Token"]


# HELP HERE PLS :(


@bot.command()
async def ecb(ctx):
  e = ctx.channel.id
  await ctx.send(f"Enabled chatbot")

@bot.command()
async def dcb(ctx):
  e = ctx.channel.id
  await ctx.send('Disabled chatbot')


@bot.event
async def on_message(message):
  if bot.user == message.author:
    return
  if message.channel.id == cbl:
    response = await AsyncClient.get_response(message.content,message.author.id,
    "Male","Robolac","HiddenBlack a pog person","idk","May 21",
    "Discord dev portal","Robot","Juice WRLD")
    await message.reply(response)
  await bot.process_commands(message)

@bot.event
async def on_ready():
  print("Bot is ready!")

bot.run(Token)