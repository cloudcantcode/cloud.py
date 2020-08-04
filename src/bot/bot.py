# sleepy.exe AKA birb.cc discord bot.
# Fully coded in python.
# Using discord.py recode. (Google for documentation. Will add to the read me at some point.)
# Not the most efficiant code ever, but it works.
#
# Coded by sleepy#7888 & Zankuro#9999


import discord
import random
import os
import datetime
import requests
import json
import sys
from discord.ext import commands, tasks
from itertools import cycle
from ruamel.yaml import YAML

from cogs.utility import utility


Utility = utility()
yaml = YAML()


if __name__ == "__main__":
    def get_prefix(bot, message):
        prefixes = Utility.file("prefixes.json")
        return prefixes[str(message.guild.id)]

    # Start up and prefix
    bot = commands.Bot(command_prefix=get_prefix)


    @bot.command()
    @commands.has_permissions(administrator=True)
    async def load(ctx, extension):
        bot.load_extension(f'cogs.{extension}')


    @bot.command()
    @commands.has_permissions(administrator=True)
    async def unload(ctx, extension):
        bot.unload_extension(f'cogs.{extension}')


    _status = Utility.file("c_cfg.json")
    status = _status["status"]



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


    @bot.event
    async def on_guild_join(guild):
        prefixes = Utility.file("prefixes.json")
        prefixes[str(guild.id)] = '>'
        Utility.file("prefixes.json", True, prefixes)


    @bot.event
    async def on_guild_remove(guild):
        prefixes = Utility.file("prefixes.json")
        prefixes.pop(str(guild.id))
        Utility.file("prefixes.json", True, prefixes)


    @bot.command()
    @commands.has_permissions(administrator=True)
    async def setprefix(ctx, prefix):
        prefixes = Utility.file("prefixes.json")
        prefixes[str(ctx.guild.id)] = prefix
        Utility.file("prefixes.json", True, prefixes)

        await ctx.send(embed=Utility.embed_(f"Prefix set to {prefix}","Set Prefix"))

    @setprefix.error
    async def setprefixerror(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=Utility.embed_(f"Please specify a prefix. \n\nUsage: {get_prefix()}setprefix `prefix`", ">> Error", 0x95efcc, 0xff0000))

    # Checks latency

    @bot.command()
    async def ping(ctx):
        print()
        await ctx.send(embed=Utility.embed_(f"Pong! {round(bot.latency * 1000)}","Latency"))



    # Scans for members joining the server
    # @bot.event
    # async def on_member_join(member):
    #    print(f'{member} has joined a server. Welcome!')

    # Scans for members leaving the server
    # @bot.event
    # async def on_member_remove(member):
    #    print(f'{member} has left a server. Goodbye!'

    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            bot.load_extension(f'cogs.{filename[:-3]}')


    cfg = yaml.load(open("../cfg.yaml", "r"))
    token = cfg["Bot"]["Token"]

    if isinstance(token, str):
        bot.run(token)
    else:
        print("Invalid token")
        exit()
