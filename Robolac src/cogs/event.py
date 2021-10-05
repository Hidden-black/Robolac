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
from datetime import *
from discord.ext import commands
from asyncio import TimeoutError



class Event(commands.Cog, name= "Event"):
    def __init__(self,bot):
        self.bot = bot
    

    @commands.Cog.listener()
    async def on_message(self,message):
        if self.bot.user.mentioned_in(message):
            await message.add_reaction("<:ping:861565960154251264>")
        await self.bot.process_commands(message)

    # @commands.Cog.listener()
    # async def on_message(self,message):
        # if message.author.id == 740906193312284715:
    #         if 'sus' in message.content.lower():
    #             await message.delete()



    @commands.Cog.listener()  # PREFIX BEING ADDED ON GUILD JOIN
    async def on_guild_join(self,guild):
        with open('prefix.json', 'r') as f:
            prefix = json.load(f)
        prefix[str(guild.id)] = '.'

        with open('prefix.json', 'w') as f:
            json.dump(prefix, f, indent=4)

        channel = self.bot.get_channel(877428062336192542)

        e = discord.Embed(
            title=f"Bot added in :`{guild.name}`", description=f"_ _", color=0x00FF00)
        e.add_field(
            name=f"No of members : {len(guild.members)}", value=f"<t:{int(time.time())}:F>")
        await channel.send(embed=e)


    @commands.Cog.listener()  # PREFIX BEING REMOVED ON GUILD JOIN
    async def on_guild_remove(self,guild):

        channel = self.bot.get_channel(877428062336192542)

        e = discord.Embed(
            title=f"Bot removed in :`{guild.name}`", description=f"_ _", color=0xFF0000)
        e.add_field(
            name=f"No of members : {len(guild.members)}", value=f"<t:{int(time.time())}:F>")
        await channel.send(embed=e)



def setup(bot):
    bot.add_cog(Event(bot))
    print("Event cog is loaded")