#!/usr/bin/env python
import time

def ftpLog(address,command):
	date = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
	logInfo = '\nClient:%-20s\tCommand:%-30s\tTime:%-30s'%(address,command,date)
	f = open('ftp.log','a')
	f.write(logInfo)
	f.close()
