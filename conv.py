
#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
#import chardet

inputfile = sys.argv[1]
outputfile = sys.argv[2]

#coding1 = "utf-8"
#coding2 = "ms-ansi"

f= open(inputfile, 'r', encoding='utf-8')
#f = open(inputfile, 'r')
content= f.read()
#code = chardet.detect(content.encode())
#print(code)
f.close()

f= open(outputfile, 'w', encoding='windows-1252')
f.write(content)
f.close()

print("done")
