import discord
import random
import os
import datetime
import requests
from discord.ext import commands, tasks
from itertools import cycle

class utility(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def iss(self, ctx):
    # This is the latitude and longitude of New York City.
        parameters = {"lat": 40.71, "lon": -74}
        response = requests.get("http://api.open-notify.org/iss-pass.json", params=parameters)
        embed = discord.Embed(colour=0x95efcc, description=f"{response.content}")
        embed.set_author(name="Scuffed ISS Locator")
        embed.set_footer(text="birb.cc")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(utility(bot))
