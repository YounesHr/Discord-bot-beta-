import os
import discord
from discord.ext import commands
#prefix
intents = discord.Intents.default()  
intents.members = True  
client = commands.Bot(command_prefix="*", intents=intents)
#start here
@client.event
async def on_ready():
    print("bot is ready")
#ban and kick command
@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason = None):
  await member.kick(reason = reason)
@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason = None):
  await member.ban(reason = reason)
#mute and unmute command
@client.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")
    await guild.create_role(name="Muted")
    await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=True)
    await member.add_roles(mutedRole, reason=reason)
@client.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
   mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")
   await member.remove_roles(mutedRole) 
