#! /usr/bin/env python3

import functools
import math
import random
import sys

from PIL import Image

MACAROON_IMAGE_SIZE = 270 # square

# In order of luminance (guessing)
MACAROON_IMAGES = [
    'navy.png',
    'brown.png',
    'pink.png',
    'red.png',
    'orange.png',
    'mintgreen.png',
    'white.png',
]


@functools.lru_cache()
def get_macaroon(idx):
    return Image.open(MACAROON_IMAGES[idx])

def get_luminous_index(lum):
    base = lum/256
    assert 0 <= base < 1
    macaroon_index = math.floor(base*len(MACAROON_IMAGES))
    r = random.random()
    if r < .4 and macaroon_index > 0:
        return macaroon_index - 1
    elif r > .7 and macaroon_index < (len(MACAROON_IMAGES) - 1):
        return macaroon_index + 1
    else:
        return macaroon_index

def macaroonize(input_name, output_name):
    im = Image.open(input_name)
    im.convert('L') # Convert to greyscale
    width, height = im.size
    target_size = (width*MACAROON_IMAGE_SIZE, height*MACAROON_IMAGE_SIZE)
    output = Image.new('RGB', target_size)
    for x in range(width):
        for y in range(height):
            lum = im.getpixel((x,y))
            idx = get_luminous_index(lum)
            macaroon = get_macaroon(idx)
            target_coord = (x*MACAROON_IMAGE_SIZE, y*MACAROON_IMAGE_SIZE)
            output.paste(macaroon, target_coord)
    output.save(output_name)
    print("Saved", output_name)

def usage():
    print("Usage: %s <input_image_filename> <output_image_filename>" % sys.argv[0])
    sys.exit(1)

def main():
    if len(sys.argv) < 3:
        usage()
    input_name = sys.argv[1]
    output_name = sys.argv[2]
    macaroonize(input_name, output_name)

if __name__ == '__main__':
    main()
