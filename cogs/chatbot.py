import os
import sys
import json
import random
import asyncio
import aiohttp
import discord
import jishaku
import requests
import randomstuff
from discord import *
from discord import message
from random import choice
from datetime import datetime
from discord.ext import commands
from asyncio import TimeoutError
from discord.ext.commands.core import command



bot = commands.Bot(command_prefix='.')
bot.launch_time = datetime.utcnow()

class Chatbot(commands.Cog, name= "Owner"):

  def __init__(self,bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_message(self,message):
    if bot.user == message.author:
      return
    if message.channel.id == 10:
      responce = await randomstuff(message.content)
      await message.reply(responce)




def setup(bot):
    bot.add_cog(Chatbot(bot))
    print("Chatbot is loaded")