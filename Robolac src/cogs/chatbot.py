import os
import sys
import json
import random
import aiohttp
import discord
import jishaku
import asyncio
import requests
import clever_chat
import randomstuff
from discord import message
from datetime import datetime
from discord.ext import commands
from clever_chat import AsyncClient
from discord.ext.commands.core import command

'''


YES I STILL DONT KNOW HOW TO DO THIS COG
:(


'''


class Chatbot(commands.Cog, name= "Chatbot"):

    def __init__(self,bot):
        self.bot = bot


    @commands.group(aliases=["cb"])
    async def chatbot(self,ctx):
        e = discord.Embed(title='**Ai Chatbot**', description = '_ _')
        e.add_field(name='Enable With',value=f'`.cb enable`')
        e.add_field(name='Disable With',value=f'`.cb disable`')

        await ctx.send(embed=e)



    @chatbot.command()
    async def enable(self,ctx):
        await ctx.send(f'Enabled Chatbot in #{ctx.channel.name}')


    @chatbot.command()
    async def disable(self,ctx):
        await ctx.send(f'Disabled Chatbot in #{ctx.channel.name}')


    @commands.Cog.listener()
    async def on_message(self,message):
      if self.bot.user == message.author:
          return
      if message.channel.id == 874196102524600360:
          response = await AsyncClient.get_response(message.content, message.author.id,"Male", "Robolac", "HiddenBlack a pog person", "69 😳", "May 21st","https://pypi/project/clever-chat/", "Robot", "Ur mum")
          await message.reply(response)


def setup(bot):
    bot.add_cog(Chatbot(bot))
    print("Chatbot cog is loaded")