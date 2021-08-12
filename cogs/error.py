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
    
    @commands.Cog.listener()                            #ERROR HANDLING
    async def on_command_error(self ,ctx ,error):
        if isinstance(error,commands.NotOwner):
            em = discord.Embed(title = 'Error While executing command' ,description="You are not the Bot owner" , color = ctx.author.color)

            await ctx.send(embed=em)
        elif isinstance(error,commands.MissingRequiredArgument):
            em = discord.Embed(title = 'Error While executing command' ,description="Wrong usage missing required argument" , color = ctx.author.color)

            await ctx.send(embed=em)
        else:
            channel = bot.get_channel(873104600910143490)
            e = discord.Embed(title = f"**ERROR** in `{ctx.guild.name}`", description = f"Used by : `{ctx.author.name}`",color = 0xff0000)
            e.add_field(name=f"Command name : ",value=f"{ctx.command}")
            e.add_field(name=f"Channel : `{ctx.channel.name}`",value= f"ID : {ctx.channel.id}")
            e.add_field(name=f"Used at : ",value= f"<t:{int(time.time())}:F>")
            e.add_field(name=f"{error}",value="lol")
            e.add_field(name=f"{ctx.message.jump_url}",value="_ _")
            
            await channel.send(embed = e)


def setup(bot):
    bot.add_cog(Error(bot))
    print("Error cog is loaded")