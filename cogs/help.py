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
bot.launch_time = datetime.utcnow()
bot.owner_ids = [842950909159145493,740906193312284715]

class Help(commands.Cog, name= "Help"):

    def __init__(self,bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)
    async def help(self,ctx):
        em = discord.Embed(title = "Help" , description = " **Prefix For all Commnds Is `.`** \n Use `.help <command>` for more info of the command \n Use `.help <category>` for more help in the category" , color = ctx.author.color)

        em.add_field(name = "Botsay", value = "`say`,`eh`,`bruh`,`ok`,`doge`" , inline= False)
        em.add_field(name = "Reddit", value = "`meme`,`joke`" , inline= False)
        em.add_field(name = "Fun", value = "`egirls`,`rps`,`av`,`8ball`,`kill`" , inline= False)
        em.add_field(name = "Image" , value = "`.img`,`.cat`,`.dog`" , inline= False)
        em.add_field(name = "Fact" , value = "`.fact`,`.fact cat`,`.fact dog`" , inline= False)
        em.add_field(name = "Invite The bot to your server with `.invite`" , value = "_ _" , inline= False)
        em.add_field(name = "_ _",value =f"**[Check out My Website!](https://main-index.thehiddenblack1.repl.co)**", inline= False)

        await ctx.send(embed = em)


    @help.command()
    async def botsay(self,ctx):

        em = discord.Embed(title = "**SAY**" , description = "Makes the bot say something for you" , color = ctx.author.color)

        em.add_field(name = "Say" , value = "`.say <what u want the bot to say>`", inline= False)
        em.add_field(name = "Eh" , value = "`.eh` make the bot say eh for you", inline= False)
        em.add_field(name = "Bruh" , value = "`.bruh` makes the bot say bruh yhea bruh", inline= False)
        em.add_field(name = "Ok" , value = "`.ok` Ok and dude ", inline= False)
        em.add_field(name = "Doge" , value = "`.doge` tells the world doge is an idiot", inline= False)

        await ctx.send(embed = em)

    @help.command()
    async def reddit(self,ctx):

        em = discord.Embed(title = "**Reddit**" , description = "Makes the bot say something for you" , color = ctx.author.color)

        em.add_field(name = "Meme" , value = "`.meme` gives random meme from reddit", inline= False)
        em.add_field(name = "Joke" , value = "`.joke` gives random joke drom reddit", inline= False)
        await ctx.send(embed = em)

    @help.command()
    async def fun(self,ctx):

        em = discord.Embed(title = "**FUN**" , description = "Fun commands :)" , color = ctx.author.color)

        em.add_field(name = "Egirls" , value = "`.egirls` Gives images of hot egirls", inline= False)
        em.add_field(name = "Rock Paper and Scissors" , value = "`.rps`", inline= False)
        em.add_field(name = "Avatar" , value = "`.av <user>` Gives the avatar of the mentioned user", inline= False)
        em.add_field(name = "Eightball" , value = "`.8ball <question>`", inline= False)
        em.add_field(name = "Kills" , value = "`.kill <user>` Kills the mentioned user in Minecraft Words", inline= False)
        await ctx.send(embed = em)

    @help.command()
    async def image(self , ctx):
        em = discord.Embed(title = "**Image**" , description = "Random Picure of animals and nature" , color = ctx.author.color)

        em.add_field(name = "Dog" , value = "`.dog` Cute duggo Pics :)", inline= False)
        em.add_field(name = "Cat" , value = "`.cat` Cute cats :)", inline= False)
        em.add_field(name = "Image Search" , value = "`.img <Image you want>`  Make sure there is no space", inline= False)

        await ctx.send(embed = em)

    @help.command()
    async def fact(self , ctx):
        em = discord.Embed(title = "**Facts**" , description = "Random Picure of animals and nature" , color = ctx.author.color)

        em.add_field(name = "Fact" , value = "`.fact` Cool facts", inline= False)
        em.add_field(name = "Cat Facts" , value = "`.fact cat` Facts about cats", inline= False)
        em.add_field(name = "Dog Facts" , value = "`.fact dog` Dog Facts ", inline= False)
        em.add_field(name = "**More info on `.help facts`**" , value = "_ _", inline= False)
        await ctx.send(embed = em)

    @help.command()
    async def say(self,ctx):

        em = discord.Embed(title = "say" , description = "cooldown of 2 minutes" , color = ctx.author.color)

        em.add_field(name = "**Example**" , value = ".say")

        await ctx.send(embed = em)

    @help.command()
    async def eh(self,ctx):

        em = discord.Embed(title = "Eh?" , description = "eh?" , color = ctx.author.color)

        em.add_field(name = "**Example**" , value = ".eh")

        await ctx.send(embed = em)
        
    @help.command()
    async def bruh(self, ctx):

        em = discord.Embed(title = "Bruh" , description = "Bot says bruh XD", color = ctx.author.color)

        em.add_field(name = "**Example**" , value = ".bruh")

        await ctx.send(embed = em)

    @help.command()
    async def ok(self,ctx):

        em = discord.Embed(title = "Ok and?" , description = "Ok and annoying gif", color = ctx.author.color)

        em.add_field(name = "**Example**" , value = ".ok")

        await ctx.send(embed = em)

    @help.command()
    async def doge(self,ctx):

        em = discord.Embed(title = "Doge" , description = "||Doge||", color = ctx.author.color)

        em.add_field(name = "**Example**" , value = ".doge")

        await ctx.send(embed = em)

    @help.command()
    async def rps(self,ctx):

        em = discord.Embed(title = "Rock Paper Scissors" , description = "Choose the buttons", color = ctx.author.color)

        em.add_field(name = "**Example**" , value = ".rps")

        await ctx.send(embed = em)

    @help.command()
    async def meme(self,ctx):

        em = discord.Embed(title = "Meme" , description = "Sends random meme", color = ctx.author.color)

        em.add_field(name = "**Example**" , value = ".meme")

        await ctx.send(embed = em)

    @help.command()
    async def egirls(self,ctx):

        em = discord.Embed(title = "Egils" , description = "Hot egirls 🥰🤤😋", color = ctx.author.color)

        em.add_field(name = "**Example**" , value = ".egirls")

        await ctx.send(embed = em)

    @help.command()
    async def invite(self,ctx):

        em = discord.Embed(title = "Invite" , description = "Create bat invite", color = ctx.author.color)

        em.add_field(name = "**Example**" , value = ".invite")

        await ctx.send(embed = em)

    @help.command()
    async def av(self,ctx):

        em = discord.Embed(title = "Av" , description = "Gives avatar of metioned user" , color = ctx.author.color)

        em.add_field(name = "**Example**" , value = f".av {ctx.author.mention}")

        await ctx.send(embed = em)

    @help.command(aliases=["8ball"])
    async def eightball(self,ctx):

        em = discord.Embed(title = "Eightball" , description = "Gives an answer to the question" , color = ctx.author.color)

        em.add_field(name = "**Example**" , value = f".eightball Am i an idiot?")

        await ctx.send(embed = em)

    @help.command()
    async def kill(self,ctx):

        em = discord.Embed(title = "Kill" , description = "Kills The mentioned user" , color = ctx.author.color)

        em.add_field(name = "**Example**" , value = f".kill {ctx.author.mention}")

        await ctx.send(embed = em)

    @help.command()
    async def joke(self,ctx):

        em = discord.Embed(title = "Joke" , description = "Joke directly from r/jokes" , color = ctx.author.color)

        em.add_field(name = "**Example**" , value =".joke")

        await ctx.send(embed = em)

    @help.command()
    async def dog(self,ctx):

        em = discord.Embed(title = "Dog" , description = "Cute duggos" , color = ctx.author.color)

        em.add_field(name = "**Example**" , value =".dog")

        await ctx.send(embed = em)

    @help.command()
    async def cat(self,ctx):

        em = discord.Embed(title = "Cat" , description = "Kittys :)" , color = ctx.author.color)

        em.add_field(name = "**Example**" , value =".cat")

        await ctx.send(embed = em)


    @help.command()
    async def img(self,ctx):

        em = discord.Embed(title = "Image Search" , description = "Saech Images from web" , color = ctx.author.color)

        em.add_field(name = "**Example**" , value =".img <image name>")

        await ctx.send(embed = em)

    @help.command()
    async def facts(self,ctx):

        em = discord.Embed(title = "Facts" , description = "Cool facts :o" , color = ctx.author.color)

        em.add_field(name = "**Example**" , value =".fact \n.fact cat \n.fact dog")

        await ctx.send(embed = em)



def setup(bot):
    bot.add_cog(Help(bot))
    print("Help cog is loaded")