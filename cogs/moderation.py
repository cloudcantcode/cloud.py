import discord
import random
import os
import datetime
import requests
from discord.ext import commands, tasks
from itertools import cycle

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Clear command
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount : int):
        await ctx.channel.purge(limit=amount)

        embed = discord.Embed(colour=0x95efcc, description=f"Purged {amount} message(s).")
        embed.set_author(name="Clear")
        embed.set_footer(text="birb.cc")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    # Shows an error when not providing a number of messages to clear
    @clear.error
    async def clear_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(colour=0x95efcc, description="Please specify an amount of messages to clear.")
            embed.set_author(name=">> Error")
            embed.set_footer(text="birb.cc")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

    # Kick command
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member : discord.Member, *, reason=None):
        await member.kick(reason=reason)

        embed = discord.Embed(colour=0x95efcc, description=f"Kicked {member}. \n\nReason: {reason}")
        embed.set_author(name="Kick")
        embed.set_footer(text="birb.cc")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    # Shows an error when not filling the user argument
    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):

            embed = discord.Embed(colour=0x95efcc, description="Please specify who you want me to kick. \n\nUsage: ,kick @user [reason]")
            embed.set_author(name=">> Error")
            embed.set_footer(text="birb.cc")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

    # Ban command
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member : discord.Member, *, reason=None):
        await member.ban(reason=reason)

        embed = discord.Embed(colour=0x95efcc, description=f"Banned {member.mention}. \n\nReason: {reason}")
        embed.set_author(name="Ban")
        embed.set_footer(text="birb.cc")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

    # Shows an error when not filling the user argument
    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(colour=0x95efcc, description="Please specify who you want me to ban. \n\nUsage: ,ban @user [reason]")
            embed.set_author(name=">> Error")
            embed.set_footer(text="birb.cc")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)

    # Unban command
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)

                embed = discord.Embed(colour=0x95efcc, description=f"Unbanned {user.mention}.")
                embed.set_author(name="Unban")
                embed.set_footer(text="birb.cc")
                embed.timestamp = datetime.datetime.utcnow()
                await ctx.send(embed=embed)

                return

    # Shows an error when not filling the user argument
    @unban.error
    async def unban_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            embed = discord.Embed(colour=0x95efcc, description="Please specify who you want me to unban. \n\nUsage: ,unban @user [reason]")
            embed.set_author(name=">> Error")
            embed.set_footer(text="birb.cc")
            embed.timestamp = datetime.datetime.utcnow()
            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(moderation(bot))
