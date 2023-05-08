#!/usr/bin/python3
# -*- coding: utf-8 -*-
import sys
from PIL import Image

input = sys.argv[1]
output = sys.argv[2]
im = Image.open(input)
size = 272, 354
im.thumbnail(size)
out = input.split('.')[0] + '1.jpg'
im.save(out, quality=95)

newSize = im.resize((272, 354))
#newSize = im.resize((272, 354), Image.ANTIALIAS)
newSize.save(output,quality=95)

