# sleepy.py

Fully open-source discord bot coded in python using discord.py recode.

## Usage

Make sure to install all the dependencies, they're in `install.txt`. Then make a file called `cfg.yaml`. and add this:

```yaml
# Config file for private stuff like discord's token, api tokens etc...
# This file wont be uploaded to github so you're safe my friend.
Bot:
  Token: token # Change this for the token
```

This file will contain all your personal information and it won't be uploaded to GitHub.

Before inviting the bot to your server, make sure the bot is running first. If you invite the bot to the server then run it, it wont be able to set it's default prefix. You only have to do this once unless you reset the ```prefixes.json``` file.

## Additional

Information Updated frequently.

Utilizes cogs for more efficiency.
It comes pre-made with moderation commands, some fun commands, and some utility commands.
Coded by sleepy#7888 & Zankuro#9999

## [CHANGELOG]

27/04/20 @ 7:06 PM: Made it so you need admin to use the "setprefix" command.


27/04/20 @ 6:42 PM: Fixed the issue with the bot not setting the default prefix. Read Usage for how to do the first setup properly.


27/04/20 @ 6:32 PM: Added .json files for setting custom prefixes. Doesn't work properly at the moment. Zankuro pls fix.


27/04/20 @ 5:19 PM: Added configuration files.  


27/04/20 @ 4:15 AM: Made scanning for files ending in .py more efficient, meaning cogs can be loaded faster.
