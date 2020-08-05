# sleepy.exe AKA birb.cc discord bot.
# Fully coded in python.
# Using discord.py recode. (Google for documentation. Will add to the read me at some point.)
# Not the most efficiant code ever, but it works.
#
# Coded by sleepy#7888 & Zankuro#9999
#
# not to hater but this is a fucking bullshit

import discord
import random
import os
import datetime
import requests
import json
import sys
from discord.ext import commands, tasks
from itertools import cycle

from dotenv import load_dotenv

#from cogs.utility import utility


if __name__ == "__main__":
    print("Bot idk")
    # If you are doing your fork of this change this shit for something
    # better, I don't have the mental health to fix recode this shit
    # + there is a lot of shit what we don't need so idk
    # Start up and prefix
    bot = commands.Bot(">")

    @bot.command()
    @commands.has_permissions(administrator=True)
    async def load(ctx, extension):
        bot.load_extension(f'cogs.{extension}')

    @bot.command()
    @commands.has_permissions(administrator=True)
    async def unload(ctx, extension):
        bot.unload_extension(f'cogs.{extension}')

    # What the fuck is this two functions above me?

    # Init

    @bot.event
    async def on_ready():
        print('>> Bot is initalized')
        print('>> We have logged in as {0.user}'.format(bot))

    # Checks latency

    @bot.command()
    async def ping(ctx):
        print()
        # await ctx.send(embed=Utility.embed_(f"Pong! {round(bot.latency * 1000)}", "Latency"))
        await ctx.send(f"Pong! {round(bot.latency * 1000)}")
    # honestly, I don't know who tf though it was a good idea add "cogs" shit on python
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')

    token = os.getenv("TOKEN")
    if isinstance(token, str):
        bot.run(token)
    else:
        print("Invalid token")
        exit()
