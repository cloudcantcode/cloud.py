import discord
import random
import os
import datetime
import requests
from discord.ext import commands, tasks
from itertools import cycle
import json


class fun(commands.Cog):
    with open('c_cfg.json') as f:
        data = json.load(f)

    def __init__(self, bot):
        self.bot = bot

    # Array for 8ball
    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = self.data["8ball"]

        embed = discord.Embed(
            colour=0x95efcc, description=f"Question: {question} \n\nAnswer: {random.choice(responses)}")
        embed.set_author(name="8Ball")
        embed.set_footer(text="birb.cc")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    # Shows an error when not filling the question argument
    @_8ball.error
    async def _8ball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(
                colour=0x95efcc, description="Please ask a question. \n\nUsage: ,8ball [question]")
            embed.set_author(name=">> Error")
            embed.set_footer(text="birb.cc")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

    # Array for dick sizes
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
                colour=0x95efcc, description="Please specify a user to measure. \n\nUsage: ,peepeesize @user")
            embed.set_author(name=">> Error")
            embed.set_footer(text="birb.cc")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

    # Array for gay measure
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
                colour=0x95efcc, description="Please specify a user.\n\nUsage: ,howgay @user")
            embed.set_author(name=">> Error")
            embed.set_footer(text="birb.cc")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

    # Array for cringe measure
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
                colour=0x95efcc, description="Please specify a user to measure their cringeness. \n\nUsage: ,howcringe @user")
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
            name="is chet done men? is this forum + cheat or just chet men?")
        embed.set_footer(text="birb.cc")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(fun(bot))
