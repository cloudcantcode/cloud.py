"""
    File by Zankuro
    ---------------
    It's done it doesn't need more shit to do
    Plase if you are going to do something to this file don't fucking spaghettify this shit
"""
import glob
import os
import pathlib
import random


class Imager():
    def __init__(self):
        self.img_names = glob.glob(os.path.join(
            pathlib.Path().absolute(), "img\\*"))

    def get_files(self):
        return self.img_names

    def get_random_files(self):
        return random.choice(self.img_names)
