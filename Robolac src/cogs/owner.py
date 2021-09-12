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


class Owner(commands.Cog, name="Owner"):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden=True)
    @commands.is_owner()
    async def sa(self, ctx, *, arg):
        await ctx.send(arg)
        await ctx.message.delete()

    @commands.command(hidden=True)
    @commands.is_owner()
    async def spam(self, ctx, amount: int, *, message):
        for i in range(amount):
            await ctx.send(message)

    @commands.command(hidden=True)
    @commands.is_owner()
    async def annoy(self, ctx, arg):
        await ctx.send(f"<@{arg}> hehe pinged u cri")
        await ctx.message.delete()

    @commands.command(hidden=True)
    @commands.is_owner()
    async def purge(self, ctx, limit: int):
        await ctx.channel.purge(limit=limit)
        await ctx.message.delete()

    @commands.command(hidden=True, pass_context=True)
    @commands.is_owner()
    async def nick(self, ctx, member: discord.Member, nick):
        await member.edit(nick=nick)
        await ctx.send(f'Nickname was changed for {member.mention} ')

    @commands.command(hidden=True)  # LOAD A COG
    @commands.is_owner()
    async def load(self, ctx, extension):
        self.bot.load_extension(f'cogs.{extension}')
        await ctx.send(f'loaded {extension}')

    @commands.command(hidden=True)  # UNLOAD A COG
    @commands.is_owner()
    async def unload(self, ctx, extension):
        self.bot.unload_extension(f'cogs.{extension}')
        await ctx.send(f'unloaded {extension}')

    @commands.command(hidden=True)  # RELOAD A COG
    @commands.is_owner()
    async def reload(self, ctx, extension):
        self.bot.reload_extension(f'cogs.{extension}')
        await ctx.send(f'Reloaded {extension}')

    @commands.command(hidden=True, pass_context=True)
    @commands.has_role("Admin")
    async def giverole(self, ctx, user: discord.Member, role: discord.Role):
        await user.add_roles(role)
        await ctx.send(f"hey {ctx.author.name}, {user.name} has been giving a role called: {role.name}")

    @commands.command(hidden=True)  # HEHE
    @commands.is_owner()
    async def cs(self, ctx, huh, arg):

        channel = self.bot.get_channel(int(huh))

        await channel.send(arg)


def setup(bot):
    bot.add_cog(Owner(bot))
    print("Owner cog is loaded")