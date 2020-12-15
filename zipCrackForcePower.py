#!/usr/bin/python
# author: libinbin1@dahuatech.com
# force crack zip file
#--------------------------------------------------
import sys
import time
import zipfile

crackzip_str_zipfile99999Name = "rainbow.zip"
#
print "force power to crack zip file"
print "Use 5 nums to crack zipfile single thread include 0-9 00-99 000-999 0000-9999 00000-99999"
fzfile = zipfile.ZipFile(crackzip_str_zipfile99999Name)
zipfile_state=0;
ticks_begin = time.time()
zfile_cmt=0;
# fun:extract file
def extractFile(zFile, password):
	try:
		global zipfile_state
		zFile.extractall(pwd=str.encode(password))
		print '\nFound Password = ' , password, '\n'
		zipfile_state=1
	except:
		pass

def str_setlen(d,l):
	s=str(d)
	while len(s) < l:
		s='0'+s
	return s
	
for num in range(1,6):
	f_password=0
	dmax = pow(10,num)-1
	while 1:
		extractFile(fzfile,str_setlen(f_password,num))
		if f_password>dmax or zipfile_state==1:
			break;
		if zfile_cmt%1000==0:
			print "%02d %%" % int((zfile_cmt*100)/(9+99+999+9999+99999))
		f_password = f_password+1
		zfile_cmt = zfile_cmt+1
ticks_end = time.time()
if zipfile_state==0:
	print "single thread crack fail take(s)=%d" % int(ticks_end-ticks_begin)
else:        
	print "single thread crack success take(s)=%d password = %d" % (int(ticks_end-ticks_begin), f_password)
fzfile.close()
del fzfile
del zipfile_state
del ticks_begin
del ticks_end
del zfile_cmt
#--------------------------------------------------
sys.exit()
#--------------------------------------------------
