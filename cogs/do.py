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
bot.remove_command('help')



class DO(commands.Cog, name= "Do"):

    def __init__(self,bot):
        self.bot = bot

    @commands.command()
    async def speed(self, ctx, member : discord.Member = None):
        if member is None:
            await ctx.send("Please run the command again but this time mention the person who you want to play with.")
            return
        
        if member.bot:
            
            await ctx.send("You can't play with bots.")
            return

        if member.id == ctx.author.id:
            return await ctx.send("You can't play with yourself!")

        await ctx.send("Let's see who presses the correct button faster.")
        await asyncio.sleep(5)
        choices = ["red", "green", "blue", "gray"]
        random_color = random.choice(choices)
        button_list = [
            Button(style=ButtonStyle.green, label="green"),
            Button(style=ButtonStyle.red, label="red"),
            Button(style=ButtonStyle.blue, label="blue"),
            Button(style=ButtonStyle.gray, label="gray"),
        ]

        button2 = [
            Button(style=ButtonStyle.green, label="Potato")
        ]

        random_buttons_list = random.sample(button_list, len(button_list))
        msg = await ctx.send(
            f"Click the {random_color} button",
            components = [                
                random_buttons_list 
            ]
            )
        def check(temp):
            return temp.component.label == f"{random_color}" and ((temp.user.id == ctx.author.id) or (temp.user.id == member.id))
        try:
            interaction = await self.bot.wait_for("button_click", check=check, timeout=20)
            await interaction.respond(            
                content=f"{interaction.user} pressed the {interaction.component.label} button. They win", ephemeral=False
            )
            await msg.edit(
                content=f"{interaction.user} won",
                components = []
            )
        except asyncio.TimeoutError:
            await ctx.send("Sorry, you didn't reply in time!")

def setup(bot):
    bot.add_cog(DO(bot))
    print("Do cog is loaded")