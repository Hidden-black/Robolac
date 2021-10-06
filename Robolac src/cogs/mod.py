import discord
from discord.ext import commands
import json

# This prevents staff members from being punished 
class Sinner(commands.Converter):
    async def convert(self, ctx, argument):
        argument = await commands.MemberConverter().convert(ctx, argument) # gets a member object
        permission = argument.guild_permissions.manage_messages # can change into any permission
        if not permission: # checks if user has the permission
            return argument # returns user object
        else:
            raise commands.BadArgument("You cannot punish other staff members") # tells user that target is a staff member

# Checks if you have a muted role
class Redeemed(commands.Converter):
    async def convert(self, ctx, argument):
        argument = await commands.MemberConverter().convert(ctx, argument) # gets member object
        muted = discord.utils.get(ctx.guild.roles, name="Muted") # gets role object
        if muted in argument.roles: # checks if user has muted role
            return argument # returns member object if there is muted role
        else:
            raise commands.BadArgument("The user was not muted.") # self-explainatory
            
# Checks if there is a muted role on the server and creates one if there isn't
async def mute(ctx, user, reason):
    role = discord.utils.get(ctx.guild.roles, name="Muted") # retrieves muted role returns none if there isn't 
    hell = discord.utils.get(ctx.guild.text_channels, name="hell") # retrieves channel named hell returns none if there isn't
    if not role: # checks if there is muted role
        try: # creates muted role 
            muted = await ctx.guild.create_role(name="Muted", reason="To use for muting")
            for channel in ctx.guild.channels: # removes permission to view and send in the channels 
                await channel.set_permissions(muted, send_messages=False,
                                              read_message_history=False,
                                              read_messages=False)
        except discord.Forbidden:
            return await ctx.send("I have no permissions to make a muted role") # self-explainatory
        await user.add_roles(muted) # adds newly created muted role
        await ctx.send(f"{user.mention} has been sent to hell for {reason}")
    else:
        await user.add_roles(role) # adds already existing muted role
        await ctx.send(f"{user.mention} has been sent to hell for {reason}")
       
    if not hell: # checks if there is a channel named hell
        overwrites = {ctx.guild.default_role: discord.PermissionOverwrite(read_message_history=False),
                      ctx.guild.me: discord.PermissionOverwrite(send_messages=True),
                      muted: discord.PermissionOverwrite(read_message_history=True)} # permissions for the channel
        try: # creates the channel and sends a message
            channel = await ctx.guild.create_text_channel('hell', overwrites=overwrites)
            await channel.send("Welcome to hell.. You will spend your time here until you get unmuted. Enjoy the silence.")
        except discord.Forbidden:
            return await ctx.send("I have no permissions to make #hell")
            
            
class Moderation(commands.Cog):
    """Commands used to moderate your guild"""
    
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases=["banish"])
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, user: Sinner=None, reason=None):
        """Casts users out of heaven."""
        
        if not user: # checks if there is a user
            return await ctx.send("You must specify a user")
        
        try: # Tries to ban user
            await ctx.guild.ban(user, f"By {ctx.author} for {reason}" or f"By {ctx.author} for None Specified")
            await ctx.send(f"{user.mention} was cast out of heaven for {reason}.")
        except discord.Forbidden:
            return await ctx.send("Are you trying to ban someone higher than the bot")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def softban(self, ctx, user: Sinner=None, reason=None):
        """Temporarily restricts access to heaven."""
        
        if not user: # checks if there is a user
            return await ctx.send("You must specify a user")
        
        try: # Tries to soft-ban user
            await ctx.guild.ban(user, f"By {ctx.author} for {reason}" or f"By {ctx.author} for None Specified") 
            await ctx.guild.unban(user, "Temporarily Banned")
        except discord.Forbidden:
            return await ctx.send("Are you trying to soft-ban someone higher than the bot?")
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def mute(self, ctx, user: Sinner, reason=None):
        """Gives them hell."""
        await mute(ctx, user, reason or "treason") # uses the mute function
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, user: Sinner=None, reason=None):
        if not user: # checks if there is a user 
            return await ctx.send("You must specify a user")
        
        try: # tries to kick user
            await ctx.guild.kick(user, f"By {ctx.author} for {reason}" or f"By {ctx.author} for None Specified") 
        except discord.Forbidden:
            return await ctx.send("Are you trying to kick someone higher than the bot?")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def purge(self, ctx, limit: int):
        """Bulk deletes messages"""
        
        await ctx.message.delete()
        await ctx.purge(limit=limit) # also deletes your own message
        await ctx.send(f"Bulk deleted `{limit}` messages") 
    
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unmute(self, ctx, user: Redeemed):
        """Unmutes a muted user"""
        await user.remove_roles(discord.utils.get(ctx.guild.roles, name="Muted")) # removes muted role
        await ctx.send(f"{user.mention} has been unmuted")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def block(self, ctx, user: Sinner=None):
                                
        if not user: # checks if there is user
            return await ctx.send("You must specify a user")
                                
        await ctx.channel.set_permissions(user, send_messages=False) # sets permissions for current channel
        await ctx.send(f"Blocked {user.mention} From #{ctx.channel.name}")

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unblock(self, ctx, user: Sinner=None):
        """Unblocks a user from current channel"""
                                
        if not user: # checks if there is user
            return await ctx.send("You must specify a user")
        
        await ctx.channel.set_permissions(user, send_messages=True) # gives back send messages permissions
        await ctx.send(f"Unblocked {user.mention} From #{ctx.channel.name}")






    @commands.command(aliases=['prefix'])  # COMMAND TO SET PREFIX
    @commands.has_permissions(manage_channels=True)
    async def setprefix(ctx, prefixset):
        with open('prefix.json', 'r') as f:
            prefix = json.load(f)
        prefix[str(ctx.guild.id)] = prefixset

        with open('prefix.json', 'w') as f:
            json.dump(prefix, f, indent=4)

        await ctx.send(f"Prefix Changed To `{prefixset}`")
                                

                             
def setup(bot):
    bot.add_cog(Moderation(bot))
    print("Moderation Cog Is loaded")