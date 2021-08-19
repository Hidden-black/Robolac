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
bot.owner_ids = [842950909159145493,740906193312284715]
bot.remove_command('help')


class Error(commands.Cog, name= "Error"):

    def __init__(self,bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_command_error(self ,ctx ,error):
        if isinstance(error,commands.NotOwner):
            em = discord.Embed(title = 'Error While executing command' ,description="You are not the Bot owner" , color = ctx.author.color)

            await ctx.send(embed=em)

        elif isinstance(error,commands.MissingRequiredArgument):
            em = discord.Embed(title = 'Error While executing command' ,description="Wrong usage missing required argument" , color = ctx.author.color)

            await ctx.send(embed=em)

        elif isinstance(error,commands.MissingPermissions):
            em = discord.Embed(title = 'Error While executing command' ,description="You don't have the permission to execute this command <:youtried:856440614881984522>" , color = ctx.author.color)

            await ctx.send(embed=em)

        elif isinstance(error,commands.BotMissingPermissions):
            em = discord.Embed(title = 'Error While executing command' ,description="Bot dont have perms <:cri:871406715797655592>" , color = ctx.author.color)

            await ctx.send(embed=em)
        else:
            pass



def setup(bot):
    bot.add_cog(Error(bot))
    print("Error cog is loaded")