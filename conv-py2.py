#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys

inputfile = sys.argv[1]
outputfile = sys.argv[2]

f= open(inputfile, 'rb')
content= unicode(f.read(), 'utf-8')
f.close()

f= open(outputfile, 'wb')
f.write(content.encode('ascii'))
f.close()

print("done")
