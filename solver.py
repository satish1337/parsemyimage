import sys
import os
import re
import subprocess
from PIL import Image


def threshold(filename, limit=40):
    """
    Make text more clear by thresholding all pixels above / below this limit to white / black
    """

    # read in colour channels
    img = Image.open(filename)
    
    # resize to make more clearer
    m = 1.5
    img = img.resize((int(img.size[0]*m), int(img.size[1]*m))).convert('RGBA')
    pixdata = img.load()

    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y][0] < limit:
                # make dark color black
                pixdata[x, y] = (0, 0, 0, 255)
            else:
                # make light color white
                pixdata[x, y] = (255, 255, 255, 255)
    img.save('solved.png')
    return img.convert('L') # convert image to single channel greyscale

	
threshold('images/cap2.jpg')