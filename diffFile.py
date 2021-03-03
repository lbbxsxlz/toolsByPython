#!/usr/bin/python
# -*- coding: utf-8 -*-
# diff file
__author__ = 'lbbxsxlz@gmail.com'

import sys
import difflib
import time
import os

def main():
    try:
        f1 = sys.argv[1]
        f2 = sys.argv[2]
    except  Exception as e:
        print("Error: "+ str(e))
        print("Usage : python compareFile.py filename1 filename2")
        sys.exit()

    if f1 == "" or f2 == "":
        print("Usage : python compareFile.py filename1 filename2")
        sys.exit()

    tf1 = readFile(f1)
    tf2 = readFile(f2)

    d = difflib.HtmlDiff()
    writeFile(d.make_file(tf1,tf2))

def readFile(filename):
    try:
        fileHandle = open(filename, "r")
        text = fileHandle.read().splitlines()
        fileHandle.close()
        return text
    except IOError as e:
        print("Read file error: "+ str(e))
        sys.exit()

def writeFile(file):
    diffFile = open('diff_{}_.html'.format(time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime())), "w")
    diffFile.write("<meta charset='UTF-8'>")
    diffFile.write(file)

    print("The file on {}".format(os.path.abspath(str(diffFile.name))))
    diffFile.close()


if __name__ == "__main__":
    main()
	
