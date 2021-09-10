import os  # WORST HELP COMMAND
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


def get_prefix(bot, message):
    with open('prefix.json', 'r') as f:
        prefix = json.load(f)
    return prefix[str(message.guild.id)]


bot = commands.Bot(command_prefix='.')
bot.launch_time = datetime.utcnow()


class Help(commands.Cog, name="Help"):  # added muti prefix support

    def __init__(self, bot):
        self.bot = bot


'''
UNDER WORK USING MINIMAL TILL THEN :/
I am not an idiot
'''


def setup(bot):
    bot.add_cog(Help(bot))
    print("Help cog is loaded")
