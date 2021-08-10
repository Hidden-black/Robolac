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

class Reddit(commands.Cog, name= "Reddit"):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def meme(self,ctx):
        memepage = [
            "https://www.reddit.com/r/memes/hot.json",
            "https://www.reddit.com/r/dankmemes/hot.json",
            "https://www.reddit.com/r/meme/hot.json"]
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"{random.choice(memepage)}") as r:
                res = await r.json()
                rm = random.randint(1,25)
                ml = res['data']['children'] [rm]['data']['permalink']
                title = res['data']['children'] [rm]['data']['title']
                ups = res['data']['children'] [rm]['data']['ups']
                com = res['data']['children'] [rm]['data']['num_comments']
                subr = res['data']['children'] [rm]['data']["subreddit_name_prefixed"]
                em = discord.Embed(title = f'{title}' , description = f"**[Reddit link](http://www.reddit.com{ml})**" , color = ctx.author.color)
                em.set_image(url = res['data']['children'] [rm] ['data']['url'])
                em.set_footer(text = f'⬆️{ups} | 💬{com} | {subr}')

                await ctx.send(embed = em)

    @commands.command()
    async def joke(self ,ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/jokes/hot.json') as r:
                res = await r.json()
                random_joke = random.randint(1,25)
                jl = res['data']['children'] [random_joke]['data']['permalink']
                title = res['data']['children'] [random_joke]['data']['title']
                text = res['data']['children'] [random_joke]['data']["selftext"]
                ups = res['data']['children'] [random_joke]['data']['ups']
                com = res['data']['children'] [random_joke]['data']['num_comments']
                em = discord.Embed(title = '' ,description=f"**[{title}](http://www.reddit.com{jl})**" , color = ctx.author.color)
                em.add_field(name= f"{text}" , value = '_ _', inline = False)
                em.set_footer(text = f'⬆️{ups} | 💬{com}')


                    
                await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(Reddit(bot))
    print("Reddit cog is loaded")
    