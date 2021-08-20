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

bot = commands.Bot(command_prefix=",", intents= discord.Intents.all() , case_insensitive=True)
bot.launch_time = datetime.utcnow()

class Owner(commands.Cog, name= "Owner"):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()                                                                        
    @commands.is_owner()
    async def sa(self,ctx, *, arg):
        await ctx.send(arg)
        await ctx.message.delete()

    @commands.command()                                             
    @commands.is_owner()
    async def spam(self,ctx, amount:int, *, message):
        for i in range(amount):
            await ctx.send(message)

    @commands.command()                                                                               
    async def uptime(self,ctx):
        delta_uptime = datetime.utcnow() - bot.launch_time
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        await ctx.send(f"{days} Days {hours} Hrs {minutes} Min {seconds} Sec")

    @commands.command()
    @commands.is_owner()
    async def annoy(self,ctx,arg):
        await ctx.send(f"<@{arg}> hehe pinged u cri")
        await ctx.message.delete()

    @commands.command()
    @commands.is_owner()
    async def purge(ctx, limit: int):
            await ctx.channel.purge(limit=limit)
            await ctx.message.delete()

    @commands.command(pass_context=True)
    @commands.is_owner()
    async def nick(self,ctx, member: discord.Member, nick):
        await member.edit(nick=nick)
        await ctx.send(f'Nickname was changed for {member.mention} ')
            

def setup(bot):
    bot.add_cog(Owner(bot))
    print("Owner cog is loaded")


    # ANOTHER STUPID COG REMOVE IT IF U WANTs