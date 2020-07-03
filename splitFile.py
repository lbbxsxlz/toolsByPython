#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'lbbxsxlz@gmail.com'
import os
import sys

size = 100*1024*1024

def mk_SubFile(srcName,sub,buf):
	#文件名分割
    [des_filename, extname] = os.path.splitext(srcName)
    filename  = des_filename + '_' + str(sub) + extname
    print 'generate sub file: %s' %filename
    with open(filename,'wb') as fout:
        fout.write(buf)
        return sub+1
            
            
def split_By_size(filename,size):
    with open(filename,'rb') as fin:
        buf = fin.read(size)
        sub = 1
        while len(buf)>0:
            sub = mk_SubFile(filename,sub,buf)
            buf = fin.read(size)  
    print "Split File Success"
            

if __name__=="__main__":
    filename = sys.argv[1]
    split_By_size(filename, size)
