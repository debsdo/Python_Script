#!/usr/bin/python
from PIL import Image
import os, sys
import glob

def resize():
    for name in glob.glob('*.jpg'):
            im = Image.open(name)
            imResize = im.resize((256,256), Image.ANTIALIAS)
            imResize.save(name + ' resized.jpg', 'JPEG', quality=90)

resize()

