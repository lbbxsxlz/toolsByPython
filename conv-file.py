#!/usr/bin/python3
# -*- coding: utf-8 -*-
# a script to convert file encoding

import os
import sys

path = sys.argv[1]

def changeEncoding(filePath):
    print filePath
    tempName = filePath+'.m'
    print tempName

    inputFile = open(filePath,'rb')
    content = unicode(inputFile.read(),'ascii')
    inputFile.close()

    outputFile = open(tempName,'wb')
    outputFile.write(content.encode('utf-16'))
    outputFile.close()

    #os.rename(tempName,filePath)

def fileFilter(dummyArg, thisDir, dirChildrenList):
    for child in dirChildrenList:
        changeEncoding(thisDir+'/'+child)

os.path.walk(path, fileFilter, None)
