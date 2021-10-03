import os
import sys
import json
import random
import asyncio
import aiohttp
import discord
import jishaku
import traceback
import io
import requests
import randomstuff
from discord import *
from discord import message
from random import choice
from datetime import datetime
from discord.ext import commands
from asyncio import TimeoutError
from discord.ext.commands.core import command
import textwrap
import importlib
from contextlib import redirect_stdout

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

    @commands.command()
    @commands.is_owner()
    async def disable(self, ctx, command):
        command = self.bot.get_command(command)
        if not command.enabled:
            return await ctx.send("This command is already disabled.")
        command.enabled = False
        await ctx.send(f"Disabled {command.name} command.")

    @commands.command()
    @commands.is_owner()
    async def enable(self, ctx, command):
        command = self.bot.get_command(command)
        if command.enabled:
            return await ctx.send("This command is already enabled.")
        command.enabled = True
        await ctx.send(f"Enabled {command.name} command.")

    @commands.command(pass_context=True, hidden=True, name='eval')
    @commands.is_owner()
    async def _eval(self, ctx, *, body: str):
        """Evaluates a code"""

        env = {
            'bot': self.bot,
            'ctx': ctx,
            'channel': ctx.channel,
            'author': ctx.author,
            'guild': ctx.guild,
            'message': ctx.message,
            '_': self._last_result
        }

        env.update(globals())

        body = self.cleanup_code(body)
        stdout = io.StringIO()

        to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

        try:
            exec(to_compile, env)
        except Exception as e:
            return await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')

        func = env['func']
        try:
            with redirect_stdout(stdout):
                ret = await func()
        except Exception as e:
            value = stdout.getvalue()
            await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
        else:
            value = stdout.getvalue()
            try:
                await ctx.message.add_reaction('\u2705')
            except:
                pass

            if ret is None:
                if value:
                    await ctx.send(f'```py\n{value}\n```')
            else:
                self._last_result = ret
                await ctx.send(f'```py\n{value}{ret}\n```')

def setup(bot):
    bot.add_cog(Owner(bot))
    print("Owner cog is loaded")
