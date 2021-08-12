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

bot = commands.Bot(command_prefix='.')


class IMG(commands.Cog, name= "IMAGE"): #I AM IDIOT THAT IS WHY IT GETS A REQUEST ON EVERY USE

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def dog(self ,ctx):
        r = requests.get("https://dog.ceo/api/breeds/image/random")
        res = r.json()
        title = res["message"]
        m = discord.Embed(title = '' ,description=f"**[Woof...]({title})**" , color = ctx.author.color)
        m.set_image(url = f"{title}")
        
        
        await ctx.send(embed = m)

    @commands.command()
    async def cat(self , ctx):
        em = discord.Embed(title = 'Meow...', color = ctx.author.color)
        em.set_image(url = f"https://source.unsplash.com/1920x1080/?cat")           
        await ctx.send(embed = em)

    @commands.command()
    async def img(self,ctx, arg):
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://api.unsplash.com/search/photos?query={arg}&client_id=kt4I9LIgyzPpqPxmqkMYnTzqlTPmUNFQLJxjIahksd0') as r:
                res = await r.json()
                ri = random.randint(0,50)
                raw_results = res["results"]
                first_option = raw_results[0]
                raw_url = first_option["urls"]
                url = raw_url["regular"]
                m = discord.Embed(title = f'Here is your image for {arg}', description="" ,color = ctx.author.color)
                m.set_image(url = url)
                m.set_footer(test="😥 Same image on same query till i fix it 🙏Pls wait")

                await ctx.send(embed = m)


def setup(bot):
    bot.add_cog(IMG(bot))
    print("Image cog is loaded")