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


class Slash(commands.Cog, name= "Slash"):

    def __init__(self,bot):
        self.bot = bot



def setup(bot):
    bot.add_cog(Slash(bot))
    print("Slash cog is loaded")