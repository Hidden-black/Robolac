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

    # @commands.command()
    # async def meme(self,ctx):
    #     memepage = [
    #         "https://www.reddit.com/r/memes/hot.json",
    #         "https://www.reddit.com/r/dankmemes/hot.json",
    #         "https://www.reddit.com/r/meme/hot.json"
    #         ]


    #     async with aiohttp.ClientSession() as cs:
    #         async with cs.get(f"{random.choice(memepage)}") as r:
    #             res = await r.json()
    #             rm = random.randint(1,25)
    #             ml = res['data']['children'] [rm]['data']['permalink']
    #             title = res['data']['children'] [rm]['data']['title']
    #             ups = res['data']['children'] [rm]['data']['ups']
    #             com = res['data']['children'] [rm]['data']['num_comments']
    #             nsfw = res['data']['children'] [rm]['data']["over_18"]
    #             subr = res['data']['children'] [rm]['data']["subreddit_name_prefixed"]

    #             if nsfw == False:
    #                 em = discord.Embed(title = f'{title}' , description = f"**[Reddit link](http://www.reddit.com{ml})**" , colour = discord.Colour.from_hsv(random.random(), 1, 1))
    #                 em.set_image(url = res['data']['children'] [rm] ['data']['url'])
    #                 em.set_footer(text = f'⬆️{ups} | 💬{com} | {subr}')

    #                 await ctx.send(embed = em)
    #             else:
    #                 pass


    @commands.command()
    async def meme(self,ctx):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://meme-api.herokuapp.com/gimme') as r:
                res = await r.json()

                title = res['title']
                link = res['postLink']
                img = res['url']
                ups = res['ups']


                em = discord.Embed(title = '' ,description=f"**[{title}]({link})**" , colour = discord.Colour.from_hsv(random.random(), 1, 1))
                em.set_image(url = img)
                em.set_footer(text = f'⬆️{ups} | 💬 69')
                await ctx.send(embed=em)







    @commands.command()
    async def joke(self ,ctx):
        jokepage = [
            "https://www.reddit.com/r/jokes/hot.json"]

        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"{random.choice(jokepage)}") as r:
                res = await r.json()
                random_joke = random.randint(1,10)
                jl = res['data']['children'] [random_joke]['data']['permalink']
                title = res['data']['children'] [random_joke]['data']['title']
                text = res['data']['children'] [random_joke]['data']["selftext"]
                ups = res['data']['children'] [random_joke]['data']['ups']
                com = res['data']['children'] [random_joke]['data']['num_comments']
                nsfw = res['data']['children'] [random_joke]['data']["over_18"]


                em = discord.Embed(title = '' ,description=f"**[{title}](http://www.reddit.com{jl})**" , colour = discord.Colour.from_hsv(random.random(), 1, 1))
                em.add_field(name= f"_ _" , value = f'{text}', inline = False)
                em.set_footer(text = f'⬆️{ups} | 💬{com}')
                await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(Reddit(bot))
    print("Reddit cog is loaded")
