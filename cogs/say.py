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

class Say(commands.Cog, name= "Say"):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1,120,commands.BucketType.user)
    async def say(self,ctx, *, arg):

        lol = ["@",""]
        if "@" in arg:
            await ctx.send("No")
        else:
            await ctx.send(arg)

    @commands.command()
    async def alive(self,ctx):
        await ctx.send("Yo i am alive lol")
        await ctx.send("https://tenor.com/view/im-not-dead-i-survived-its-not-over-not-the-end-comeback-gif-14693671") 
        
    @commands.command()
    async def bruh(self,ctx):
        await ctx.send("bruh")
        await ctx.message.delete()

    @commands.command()
    async def eh(self,ctx):
        await ctx.send("eh?")
        await ctx.message.delete()

    @commands.command()
    async def e(self,ctx):
        await ctx.send("e?")
        await ctx.message.delete()

    @commands.command()
    async def ok(self,ctx):
        await ctx.send("https://tenor.com/view/ok-and-ok-and-caption-trade-gif-21164436")
        await ctx.message.delete()

    @commands.command()
    async def gaming(self,ctx):
        await ctx.send("<a:Vibing:854368542542397491>")
        await ctx.message.delete()

    @commands.command()
    async def tbc(self,ctx):
        await ctx.send("<:To_Be_Continued_3:861520261635637258><:ToBeContinued2:861520333450641409><:ToBeContinued3:861520434645958677>")
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(Say(bot))
    print("Say cog is loaded")



#IDK WHY THIS COG EXIST