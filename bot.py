# sleepy.exe AKA birb.cc discord bot.
# Fully coded in python.
# Using discord.py recode. (Google for documentation. Will add to the read me at some point.)
# Not the most efficiant code ever, but it works.
#
# Coded by sleepy#7888

import discord
import random
import os
import datetime
import requests
from discord.ext import commands, tasks
from itertools import cycle

# Start up and prefix
bot = commands.Bot(command_prefix = ',')

@bot.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')

@bot.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')

status = cycle(['with my balls',
        "with sleepy's balls",
        "with Jordan's balls",
        "with Cadan's balls",
        'with thigh.life',
        'with birb.cc',
        'with Hentaiware.moe',
        'with Hentaihook'])

# Init
@bot.event
async def on_ready():
    change_status.start()
    print('>> Bot is initalized')
    print('>> We have logged in as {0.user}'.format(bot))

# Status Loop
@tasks.loop(seconds=20)
async def change_status():
    await bot.change_presence(activity=discord.Game(next(status)))

# Checks latency
@bot.command()
async def ping(ctx):
    embed = discord.Embed(colour=0x95efcc, description=f"Pong! {round(bot.latency * 1000)}ms.")
    embed.set_author(name="Latency")
    embed.set_footer(text="birb.cc")
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)

# Scans for members joining the server
#@bot.event
#async def on_member_join(member):
#    print(f'{member} has joined a server. Welcome!')

# Scans for members leaving the server
#@bot.event
#async def on_member_remove(member):
#    print(f'{member} has left a server. Goodbye!')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run('your token here')
