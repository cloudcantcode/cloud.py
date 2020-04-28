import discord
import random
import os
import datetime
import requests
from discord.ext import commands, tasks
from itertools import cycle
import json

"""
This file will contain all functions related to utilities.
"""


class utility(commands.Cog):

    def file(self, file, write=False, data=None):
        if not write:
            with open(file, 'r') as f:
                return json.load(f)
        else:
            with open(file, 'w') as f:
                json.dump(data, f, indent=4)

    def embed_(self, description, author, footer="birb.cc", color=0x95efcc, Timestamp = True):
        if Timestamp:
            _embed = discord.Embed(colour=color, description=description)
            _embed.set_author(name=author)
            _embed.set_footer(text=footer)
            _embed.timestamp = datetime.datetime.utcnow()
            return _embed
        else:
            _embed = discord.Embed(colour=color, description=description)
            _embed.set_author(name=author)
            _embed.set_footer(text=footer)
            return _embed


def setup(bot):
    bot.add_cog(utility(bot))
