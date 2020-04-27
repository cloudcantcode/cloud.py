import discord
import random
import os
import datetime
from discord.ext import commands, tasks
from itertools import cycle

# Start up and prefix
bot = commands.Bot(command_prefix = ',')
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

# Scans for members joining the server
#@bot.event
#async def on_member_join(member):
#    print(f'{member} has joined a server. Welcome!')

# Scans for members leaving the server
#@bot.event
#async def on_member_remove(member):
#    print(f'{member} has left a server. Goodbye!')

# Checks latency
@bot.command()
async def ping(ctx):

    embed = discord.Embed(colour=0x95efcc, description=f"Pong! {round(bot.latency * 1000)}ms.")
    embed.set_author(name="Latency")
    embed.set_footer(text="birb.cc")
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)

# Array for 8ball
@bot.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
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
                "Bro I stopped snorting coke from your moms pussy 6 months later I did it again :pensive: - Arpac"]

    embed = discord.Embed(colour=0x95efcc, description=f"Question: {question} \n\nAnswer: {random.choice(responses)}")
    embed.set_author(name="8Ball")
    embed.set_footer(text="birb.cc")
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)

# Shows an error when not filling the question argument
@_8ball.error
async def _8ball_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(colour=0x95efcc, description="Please ask a question. \n\nUsage: ,8ball [question]")
        embed.set_author(name=">> Error")
        embed.set_footer(text="birb.cc")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

# Array for dick sizes
@bot.command()
async def peepeesize(ctx, member : discord.Member):
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
async def peepeesize_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):

        embed = discord.Embed(colour=0x95efcc, description="Please specify a user to measure. \n\nUsage: ,peepeesize @user")
        embed.set_author(name=">> Error")
        embed.set_footer(text="birb.cc")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

# Array for gay measure
@bot.command()
async def howgay(ctx, member : discord.Member):
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
async def howgay_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(colour=0x95efcc, description="Please specify a user.\n\nUsage: ,howgay @user")
        embed.set_author(name=">> Error")
        embed.set_footer(text="birb.cc")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

# Array for cringe measure
@bot.command()
async def howcringe(ctx, member : discord.Member):
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
async def howcringe_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):

        embed = discord.Embed(colour=0x95efcc, description="Please specify a user to measure their cringeness. \n\nUsage: ,howcringe @user")
        embed.set_author(name=">> Error")
        embed.set_footer(text="birb.cc")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)


# purge message command
@bot.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)

    embed = discord.Embed(colour=0x95efcc, description=f"Purged {amount} message(s).")
    embed.set_author(name="Clear")
    embed.set_footer(text="birb.cc")
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)

# Event for no command found
###@bot.event
###async def on_command_error(ctx, error):
###    if isinstance(error, commands.CommandNotFound):
###        await ctx.send('Command not found.')


# Shows an error when not filling the int argument
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(colour=0x95efcc, description="Please specify an amount of messages to clear.")
        embed.set_author(name=">> Error")
        embed.set_footer(text="birb.cc")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

# Kick command
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

    embed = discord.Embed(colour=0x95efcc, description=f"Kicked {member}. \n\nReason: {reason}")
    embed.set_author(name="Kick")
    embed.set_footer(text="birb.cc")
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)

# Shows an error when not filling the user argument
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):

        embed = discord.Embed(colour=0x95efcc, description="Please specify who you want me to kick. \n\nUsage: ,kick @user [reason]")
        embed.set_author(name=">> Error")
        embed.set_footer(text="birb.cc")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

# Ban command
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

    embed = discord.Embed(colour=0x95efcc, description=f"Banned {member.mention}. \n\nReason: {reason}")
    embed.set_author(name="Ban")
    embed.set_footer(text="birb.cc")
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)

# Shows an error when not filling the user argument
@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(colour=0x95efcc, description="Please specify who you want me to ban. \n\nUsage: ,ban @user [reason]")
        embed.set_author(name=">> Error")
        embed.set_footer(text="birb.cc")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

# Unban command
@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, *, member):
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
async def unban_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(colour=0x95efcc, description="Please specify who you want me to unban. \n\nUsage: ,unban @user [reason]")
        embed.set_author(name=">> Error")
        embed.set_footer(text="birb.cc")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

# Meme exploit
def sleepy_exploit(ctx):
    return ctx.author.id == 208026791749746690

@bot.command()
@commands.check(sleepy_exploit)
async def exploit(ctx):

    embed = discord.Embed(colour=0x95efcc, description="you fucking donkey, thx for the server cache key.")
    embed.set_author(name=">> sleepy.exe Exploit")
    embed.set_footer(text="birb.cc")
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)

# is chet done men? is this forum + cheat or just chet men?
@bot.command()
async def ishentaiwarecheatdone(ctx):
    embed = discord.Embed(colour=0x95efcc, description="no")
    embed.set_author(name="is chet done men? is this forum + cheat or just chet men?")
    embed.set_footer(text="birb.cc")
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)

bot.run('NzAzMjY1NzIxOTA3Njc1MjI3.XqMFUw.Ex2bAR0lbI5SHv1U_1y-z0tZiVk')
