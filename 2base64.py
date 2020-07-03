#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'lbbxsxlz@gmail.com'

import os
import sys
import base64
filename = sys.argv[1]

f = open(filename, 'rb') 
#读取文件内容，转换为base64编码
ls_f = base64.b64encode(f.read()) 
f.close()
print(ls_f)

[des_file, extname] = os.path.splitext(filename)
newfile = des_file + '_new' + extname
imgdata=base64.b64decode(ls_f)
file=open(newfile, 'wb')
file.write(imgdata)
file.close()