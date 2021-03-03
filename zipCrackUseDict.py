#!/usr/bin/python
# use dict crack zip file
#--------------------------------------------------
__author__ = 'lbbxsxlz@gmail.com'

import sys
import time
import zipfile
import threading

crackzip_str_zipfileName = "AAPRecovery4.54.31.zip"
crackzip_str_passfileName = "rainbow.txt"

print "use dict to crack zip file"

zipfile_state=0
timeout=0
ticks_begin = time.time()
# fun:extract file
def extractFile(zFile, password):
	try:
		global zipfile_state
		zFile.extractall(pwd=str.encode(password))
		print '\nFound Password = ' , password, 'in dict' '\n'
		zipfile_state=1
	except:
		pass

zfile = zipfile.ZipFile(crackzip_str_zipfileName)
passfile=open(crackzip_str_passfileName)

for line in passfile.readlines():
# strip \n
	password = line.strip('\n')
	# run thread extract file
	t = threading.Thread(target=extractFile, args=(zfile, password))
	# run thread
	t.start()
# waiting finish
while zipfile_state==0:
	print 'cracking,please wait'
	timeout=timeout+1
	if timeout>20:
		print 'can not find the password in dict take 20 seconds \n'
		break
	else:
		time.sleep(1)
ticks_end = time.time()
if zipfile_state==1:
	print 'extrac success! \n'
else:
	print 'extrac fail! \n'
print "take(s)=%d" % int(ticks_end-ticks_begin)
	
passfile.close()
zfile.close()
del passfile
del zfile
del zipfile_state
#--------------------------------------------------
sys.exit()
#--------------------------------------------------
