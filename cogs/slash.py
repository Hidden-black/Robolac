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

bot = commands.Bot(command_prefix='.', intents= discord.Intents.all() , case_insensitive=True)
bot.remove_command('help')
bot.load_extension('jishaku')

class tt(commands.Cog):

    def __init__(self, client):
        self.client = client

"""
WILL USE THIS COG WHEN MY BOT GET VERIFIED LMAO XD
"""

def setup(bot):
    bot.add_cog(tt(bot))
    print("tt cog is loaded")