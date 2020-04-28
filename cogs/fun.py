import discord
import random
import os
import datetime
import requests
from discord.ext import commands, tasks
from itertools import cycle
import json

from .utility import utility

Utility = utility()

class fun(commands.Cog):
    data = Utility.file("c_cfg.json")
    def __init__(self, bot):
        self.bot = bot

    # *ball function
    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = self.data["8ball"]
        await ctx.send(embed=Utility.embed_(f"Question: {question} \n\nAnswer: {random.choice(responses)}", "8Ball"))

    # Shows an error when not filling the question argument
    @_8ball.error
    async def _8ball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=Utility.embed_(f"Please ask a question. \n\nUsage: [prefix]8ball [question]", "8Ball"))


    # Dicksizes function
    @commands.command()
    async def peepeesize(self, ctx, member: discord.Member):
        dickSizes = self.data["dickSizes"]

        embed = discord.Embed(
            colour=0x95efcc, description=f"Your peepee size is: {random.choice(dickSizes)} , {member.mention}")
        embed.set_author(name="How big is peepee?")
        embed.set_footer(text="birb.cc")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    # Shows an error when not filling the user argument
    @peepeesize.error
    async def peepeesize_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):

            embed = discord.Embed(
                colour=0x95efcc, description="Please specify a user to measure. \n\nUsage: [prefix]peepeesize @user")
            embed.set_author(name=">> Error")
            embed.set_footer(text="birb.cc")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

    # Gay measure function
    @commands.command()
    async def howgay(self, ctx, member: discord.Member):
        gayness = self.data["gayness"]
        embed = discord.Embed(
            colour=0x95efcc, description=f"{member.mention} is {random.choice(gayness)} gay.")
        embed.set_author(name="How gay are you?")
        embed.set_footer(text="birb.cc")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    # Shows an error when not filling the member argument
    @howgay.error
    async def howgay_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                colour=0x95efcc, description="Please specify a user.\n\nUsage: [prefix]howgay @user")
            embed.set_author(name=">> Error")
            embed.set_footer(text="birb.cc")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

    # cringe measure function
    @commands.command()
    async def howcringe(self, ctx, member: discord.Member):
        cringeness = self.data["cringeness"]

        embed = discord.Embed(
            colour=0x95efcc, description=f"{member.mention} is {random.choice(cringeness)}")
        embed.set_author(name="How cringe are you?")
        embed.set_footer(text="birb.cc")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    # Shows an error when not filling the member argument
    @howcringe.error
    async def howcringe_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):

            embed = discord.Embed(
                colour=0x95efcc, description="Please specify a user to measure their cringeness. \n\nUsage: [prefix]howcringe @user")
            embed.set_author(name=">> Error")
            embed.set_footer(text="birb.cc")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

    # Meme exploit
    def sleepy_exploit(ctx):
        return ctx.author.id == 208026791749746690

    @commands.command()
    @commands.check(sleepy_exploit)
    async def exploit(self, ctx):

        embed = discord.Embed(
            colour=0x95efcc, description="you fucking donkey, thx for the server cache key.")
        embed.set_author(name=">> sleepy.exe Exploit")
        embed.set_footer(text="birb.cc")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    # is chet done men? is this forum + cheat or just chet men?
    @commands.command()
    async def ishentaiwarecheatdone(self, ctx):
        embed = discord.Embed(colour=0x95efcc, description="no")
        embed.set_author(
            name="is chet done men? is this forum + cheat or just chet men? where do download cheat?????")
        embed.set_footer(text="birb.cc")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(fun(bot))
