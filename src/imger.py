import glob
import os
import pathlib

class Imager():
    def __init__(self):
        self.img_names = glob.glob(os.path.join(pathlib.Path().absolute(), "img\\*"))
        
    def get_files(self):
        return self.img_names

    def get_random_files