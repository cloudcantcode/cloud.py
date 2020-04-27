import discord
import random
import os
import datetime
import requests
from discord.ext import commands, tasks
from itertools import cycle

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Array for 8ball
    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = ['It is certain.',
                    'It is decidedly so.',
                    'Without a doubt.',
                    'Yes, definitely',
                    'You may rely on it.',
                    'As I see it, yes.',
                    'Most likely.',
                    'Outlook good.',
                    'Yes',
                    'Signs point to yes.',
                    'Reply hazy, try again.',
                    'Ask again later.',
                    'Better not tell you now.',
                    'Cannot predict now.',
                    'Concentrate and ask again.',
                    "Don't count on it",
                    'My reply is no.',
                    'My sources say no.',
                    'Outlook not so good.',
                    'Very doubtful.',
                    'No.',
                    'Shut the fuck up newfag',
                    'How about fuck off.',
                    'No faNN.',
                    'Uh oh, retard alert.',
                    'Config issue. All I see is an amazing cheat - Aimware user 2019',
                    'Shut up 3rd world nigger - Arpac',
                    "Bro I stopped snorting coke from your moms pussy 6 months later I did it again :pensive: - Arpac"] # Don't mind these lmao

        embed = discord.Embed(colour=0x95efcc, description=f"Question: {question} \n\nAnswer: {random.choice(responses)}")
        embed.set_author(name="8Ball")
        embed.set_footer(text="birb.cc")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    # Shows an error when not filling the question argument
    @_8ball.error
    async def _8ball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(colour=0x95efcc, description="Please ask a question. \n\nUsage: ,8ball [question]")
            embed.set_author(name=">> Error")
            embed.set_footer(text="birb.cc")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

    # Array for dick sizes
    @commands.command()
    async def peepeesize(self, ctx, member : discord.Member):
        dickSizes = ['8D',
                    '8=D',
                    '8==D',
                    '8===D',
                    '8====D',
                    '8=====D',
                    '8======D',
                    '8=======D',
                    '8========D',
                    '8=========D',
                    '8==========D',
                    '8===========D',
                    '8============D',
                    '8=============D',
                    '8==============D',
                    '8===============D',
                    '8================D',
                    '8=================D',
                    '8==================D',
                    '8===================D',
                    '8====================D',
                    '8=====================D',
                    '8======================D']

        embed = discord.Embed(colour=0x95efcc, description=f"Your peepee size is: {random.choice(dickSizes)} , {member.mention}")
        embed.set_author(name="How big is peepee?")
        embed.set_footer(text="birb.cc")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    # Shows an error when not filling the user argument
    @peepeesize.error
    async def peepeesize_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):

            embed = discord.Embed(colour=0x95efcc, description="Please specify a user to measure. \n\nUsage: ,peepeesize @user")
            embed.set_author(name=">> Error")
            embed.set_footer(text="birb.cc")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

    # Array for gay measure
    @commands.command()
    async def howgay(self, ctx, member : discord.Member):
        gayness = ['0%',
                    '10%',
                    '20%',
                    '30%',
                    '40%',
                    '50%',
                    '60%',
                    '70%',
                    '80%',
                    '90%',
                    '100%',
                    'hella fucking']

        embed = discord.Embed(colour=0x95efcc, description=f"{member.mention} is {random.choice(gayness)} gay.")
        embed.set_author(name="How gay are you?")
        embed.set_footer(text="birb.cc")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    # Shows an error when not filling the member argument
    @howgay.error
    async def howgay_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(colour=0x95efcc, description="Please specify a user.\n\nUsage: ,howgay @user")
            embed.set_author(name=">> Error")
            embed.set_footer(text="birb.cc")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

    # Array for cringe measure
    @commands.command()
    async def howcringe(self, ctx, member : discord.Member):
        cringeness = ['not cringe.',
                    'a tiny bit cringe'
                    'sorta cringe.',
                    'cringe.',
                    'hella cringe.',
                    'please shut the fuck up levels of cringe.']

        embed = discord.Embed(colour=0x95efcc, description=f"{member.mention} is {random.choice(cringeness)}")
        embed.set_author(name="How cringe are you?")
        embed.set_footer(text="birb.cc")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    # Shows an error when not filling the member argument
    @howcringe.error
    async def howcringe_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):

            embed = discord.Embed(colour=0x95efcc, description="Please specify a user to measure their cringeness. \n\nUsage: ,howcringe @user")
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

        embed = discord.Embed(colour=0x95efcc, description="you fucking donkey, thx for the server cache key.")
        embed.set_author(name=">> sleepy.exe Exploit")
        embed.set_footer(text="birb.cc")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    # is chet done men? is this forum + cheat or just chet men?
    @commands.command()
    async def ishentaiwarecheatdone(self, ctx):
        embed = discord.Embed(colour=0x95efcc, description="no")
        embed.set_author(name="is chet done men? is this forum + cheat or just chet men?")
        embed.set_footer(text="birb.cc")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(fun(bot))
