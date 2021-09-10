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


class Fact(commands.Cog, name="FACT"):

    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def fact(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://uselessfacts.jsph.pl/random.json?language=en') as r:
                res = await r.json()
                text = res["text"]
                m = discord.Embed(
                    title='Fun fact', description=f"{text}", color=ctx.author.color)

                await ctx.send(embed=m)

    @fact.command()
    async def dog(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://dog-api.kinduff.com/api/facts?number=1') as r:
                res = await r.json()
                title = res["facts"][0]
                m = discord.Embed(title='Here is a Woofy Fact ...',
                                  description=f"{title}", color=ctx.author.color)
                await ctx.send(embed=m)

    @fact.command()
    async def cat(self, ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://catfact.ninja/facts?limit=1') as r:
                res = await r.json()
                title = res["data"][0]["fact"]
                m = discord.Embed(
                    title='Cat fact', description=f"{title}", color=ctx.author.color)
                await ctx.send(embed=m)


def setup(bot):
    bot.add_cog(Fact(bot))
    print("Fact cog is loaded")


"""
yey facts
"""
