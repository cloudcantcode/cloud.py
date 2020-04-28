import os
import json

# simple list, Add here all the modules.
os.system("python -m pip install --upgrade pip")
os.system("python -m pip install discord.py  ")
os.system("python -m pip install requests    ")
os.system("python -m pip install ruamel.yaml ")

file = """
# Make a file in the root dir called cfg.yaml and paste this in

# Config file for private stuff like discord's token, api tokens etc...
# This file wont be uploaded to github so you're safe my friend.
Bot:
  Token: token123  # Change this for the token
"""

with open("cfg.yaml", "w") as f:
    f.write(file)
    pass

with open("prefixes.json", "w") as f:
    json.dump("{}", f, indent=4)
    pass
