#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PIL import Image

im = Image.open('./security.png')
size = 272, 354
im.thumbnail(size)
im.save('security-1.jpg', quality=95)

newSize = im.resize((272, 354))
newSize.save('security-2.jpg')

