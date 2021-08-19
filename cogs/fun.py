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
from discord_components import *
from discord import message
from random import choice
from datetime import datetime
from discord.ext import commands
from asyncio import TimeoutError
from discord.ext.commands.core import command


bot = commands.Bot(command_prefix='.')

class Fun(commands.Cog, name= "Fun"):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()                                                                  #address of egirls 
    async def egirls(self,ctx):
        await ctx.send("https://imgur.com/CPLIwdO")
        await ctx.send("Get rickrolled lol 😉")

    @commands.command()
    async def av(self,ctx, *,  avamember : discord.Member=None):
        if avamember == None:
            avamember = ctx.author


        em = discord.Embed(title=f"{avamember}'s PfP", color = ctx.author.color)
        userAvatarUrl = avamember.avatar_url
        em.set_image(url = userAvatarUrl)
        em.set_footer(icon_url= ctx.author.avatar_url , text=f"Genrated by {ctx.author.name}")

        await ctx.send(embed = em)

    @commands.command()
    async def whois(self, ctx , member : discord.Member):
        if member == None:
            member = ctx.author

        em = discord.Embed(title = member.name , description = member.mention , color = ctx.author.color)
        em.add_field(name = "ID" , value = member.id , inline = False)
        em.set_thumbnail(url = member.avatar_url)
        em.set_footer(icon_url = ctx.author.avatar_url , text =f"Asked by {ctx.author.name}")
        await ctx.send(embed = em)

    @commands.command()
    async def invite(self, ctx):
        link = "https://discord.com/api/oauth2/authorize?client_id=845248927652905011&permissions=0&scope=bot%20applications.commands"
        em = discord.Embed(title = "Invite Bad Bot", description = f"**[Invite Link]({link})**" , color = ctx.author.color)

        await ctx.send(embed = em)


    @commands.command(aliases=["8ball"])
    async def eightball(self,ctx,*,arg):
        responses = ["It is certain.",
                    "It is decidedly so.",
                    "Without a doubt.",
                    "Yes - definitely.",
                    "You may rely on it.",
                    "As I see it, yes.",
                    "Most likely.",
                    "Outlook good.",
                    "Yes.",
                    "Signs point to yes.",
                    "Reply hazy, try again.",
                    "Ask again later.",
                    "Better not tell you now.",
                    "Cannot predict now.",
                    "Concentrate and ask again.",
                    "Don't count on it.",
                    "My reply is no.",
                    "My sources say no.",
                    "Outlook not so good.",
                    "Very doubtful."]
        
        m = discord.Embed(title = f":8ball: Question: {arg}",description =f"**Answer :** {random.choice(responses)}",color=ctx.author.color)
        await ctx.send(embed=m)

    @commands.command()
    async def kill(self,ctx, mem:discord.Member=None):
        if mem == None:
            mem = ctx.author
        
        item = [
            "sword",
        ]

        mob = [
            "Cat",
            "Zombie",
            "Skeleton",
            "Husk",
            "Blaze",
            "Creeper",
            "Drowned",
            "Elder Guardian",
            "Endermite",
            "Evoker",
            "Ghast",
            "Guardian",
            "Hoglin",
            "Magma Cube",
            "Ravenger",
            "Silverfish"
        ]

        pla = [
            "HiddenBlack",
        ]

        arw = [
            "Skeleton",
            "Husk"
        ]

        msg = [
            f"{mem} was shot by an Arrow",
            f"{mem} was shot by {random.choice(arw)} using Bow"
            f"{mem} was pummeled by Snowballs Shot by A Snow Golem",
            f"{mem} was pummeled by A Snow Golem using Snowballs",
            f"{mem} was pricked to death",
            f"{mem} walked into a cactus whilst trying to escape {random.choice(mob)}",
            f"{mem} drowned",
            f"{mem} drowned whilst trying to escape {random.choice(mob)}",
            f"{mem} experienced kinetic energy",
            f"{mem} experienced kinetic energy whilst trying to escape {random.choice(mob)}",
            f"{mem} blew up",
            f"{mem} was blown up by TNT <a:tnt:871971148341080065>",
            f"{mem} was killed by [Intentional Game Design]",
            f"{mem} hit the ground too hard",
            f"{mem} hit the ground too hard whilst trying to escape {random.choice(mob)}",
            f"{mem} fell from a high place",
            f"{mem} fell off a ladder",
            f"{mem} fell off some vines",
            f"{mem} fell off some weeping vines",
            f"{mem} fell off some twisting vines",
            f"{mem} fell off scaffolding",
            f"{mem} fell while climbing",
            "death.fell.accident.water",
            f"{mem} was impaled on a stalagmite",
            f"{mem} was impaled on a stalagmite whilst fighting {random.choice(mob)}",
            f"{mem} was squashed by a falling anvil",
            f"{mem} was squashed by a falling anvil whilst fighting {random.choice(mob)}",
            f"{mem} was squashed by a falling block",
            f"{mem} was squashed by a falling block whilst fighting {random.choice(mob)}",
            f"{mem} was skewered by a falling stalactite",
            f"{mem} was skewered by a falling stalactite whilst fighting {random.choice(mob)}",
            f"{mem} went up in flames",
            f"{mem} walked into fire whilst fighting {random.choice(mob)}",
            f"{mem} burned to death",
            f"{mem} was burnt to a crisp whilst fighting {random.choice(mob)}"
            f"{mem} went off with a bang",
            f"{mem} tried to swim in lava",
            f"{mem} tried to swim in lava to escape {random.choice(mob)}",
            f"{mem} was struck by lightning"
            f"{mem} was struck by lightning whilst fighting {random.choice(mob)}",
            f"{mem} discovered the floor was lava",
            f"{mem} walked into danger zone due to {random.choice(mob)}",
            f"{mem} was killed by magic",
            f"{mem} was killed by magic whilst trying to escape {random.choice(mob)}"
            f"{mem} was killed by {random.choice(mob)} using magic",
            f"{mem} was killed by {random.choice(mob)} using <item>",
            f"{mem} froze to death",
            f"{mem} was frozen to death by {random.choice(mob)}",
            f"{mem} was slain by {random.choice(mob)}",
            f"{mem} was fireballed by {random.choice(mob)}",
            f"{mem} was fireballed by {random.choice(mob)} using <item>",
            f"{mem} was stung to death",
            "death.attack.sting.item",
            f"{mem} was shot by a skull from {random.choice(mob)}",
            "death.attack.witherSkull.item",
            f"{mem} starved to death",
            f"{mem} starved to death whilst fighting {random.choice(mob)}",
            f"{mem} suffocated in a wall",
            f"{mem} suffocated in a wall whilst fighting {random.choice(mob)}",
            f"{mem} was squished too much",
            f"{mem} was squashed by {random.choice(mob)}",
            f"{mem} was poked to death by a sweet berry bush",
            f"{mem} was poked to death by a sweet berry bush whilst trying to escape {random.choice(mob)}",
            f"{mem} was killed trying to hurt {random.choice(mob)}",
            f"{mem} was killed by <item> trying to hurt {random.choice(mob)}",
            f"{mem} was impaled by Trident",
            f"{mem} was impaled by {random.choice(mob)} with Trident",
            f"{mem} fell out of the world",
            f"{mem} didn't want to live in the same world as {random.choice(mob)}",
            f"{mem} withered away",
            f"{mem} withered away whilst fighting Wither",
            f"{mem} died",
            f"{mem} died because of {random.choice(mob)}",
            f"{mem} was doomed to fall",
            f"{mem} fell too far and was finished by Fall Damage",
            f"{mem} was stung to death by a Bee",
        ]

        
        await ctx.send(f"{random.choice(msg)}")


    @commands.command()
    async def rps(self,ctx):
        rpso = ["Rock", "Paper","Scissors"]
        comp = choice(rpso)
        yet = discord.Embed(title = f"{ctx.author.display_name} Choose lol" , description ="> Click On your Option",color = ctx.author.color)
        win = discord.Embed(title  = f"{ctx.author.display_name} Won!", description =f"> **You won!**\nThe Bot Chose {comp}",color = 0x00FF00)
        out = discord.Embed(title = f"{ctx.author.display_name} You didnot clicked on Time", description = "**Timeout**", color = 0xFFFFFF)
        lost = discord.Embed(title = f"{ctx.author.display_name} You Lost!", description = f"> **You lost** \nThe Bot chose {comp}", color = 0xff0000)
        tie = discord.Embed(title = f"{ctx.author.display_name} LOL A TIE", description = f"> **There Was A tie** \nThe bot chose {comp}", color = 0xFFFF00)


        rck = self.bot.get_emoji(int("<:Rock:868501425720807444>".split(":")[2].replace(">", "")))
        pap = self.bot.get_emoji(int("<:Paper:868501529106198578>".split(":")[2].replace(">", "")))
        sci = self.bot.get_emoji(int("<:Scissors:868502651388698674>".split(":")[2].replace(">", "")))

        m = await ctx.send(
            embed=yet,
            components=[
                [Button(style=1, label = "Rock", emoji = rck),
                Button(style=2,label="Paper", emoji = pap),
                Button(style=3,label="Scissors", emoji = sci)],
            ],
        )

        def check(res):
            return ctx.author == res.user and res.channel == ctx.channel
    
        try:
            res = await self.bot.wait_for("button_click",check=check,timeout=60)
            player = res.component.label

            if player==comp:
                await m.edit(embed=tie,components=[])

            if player=="Rock" and comp=="Paper":
                await m.edit(embed=lost,components=[])

            if player=="Rock" and comp=="Scissors":
                await m.edit(embed=win,components=[])

            if player=="Paper" and comp=="Scissors":
                await m.edit(embed=lost,components=[])

            if player=="Paper" and comp=="Rock":
                await m.edit(embed=win,components=[])

            if player=="Scissors" and comp=="Rock":
                await m.edit(embed=lost,components=[])

            if player=="Scissors" and comp=="Paper":
                await m.edit(embed=win,components=[])

        except TimeoutError:
            await m.edit(
                embed=out,
                components=[]
                )


def setup(bot):
    bot.add_cog(Fun(bot))
    print("Fun cog is loaded")


"""
U ARE here for this cog lol 
best cog in my whole bot with all stuff needed to have fun might add tictaktoe
chatbot is also being worked on
"""