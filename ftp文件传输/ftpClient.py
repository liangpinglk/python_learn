#!/usr/bin/env python

import socket,os,tab,sys,ftpHelpDoc
from time import sleep


host = sys.argv[1]
port = int(sys.argv[2])
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
print s.recv(1024)


while True:
	command = raw_input('ftp>').strip()


	if command:
		s.sendall(command)
		sleep(0.5)
	else:
		continue


	if command.split()[0] == 'send':
		try:     
			print command
			f= open(command.split()[1],'rb')                
			if f:
                                s.sendall('ok')
                                sleep(0.5)
                        data = f.read()
                        s.sendall(data)
                        sleep(1)
                        s.sendall('done')
                        f.close()
                        print 'send done'
		except IOError:
			s.sendall('fail')
			print 'please input a right file name'
		except IndexError:
			s.sendall('fail')
			print 'please input a file name'

	elif command.split()[0] == 'get':
		clientInfo = ''
                jungle = s.recv(4)
		sleep(0.5)
		print jungle
		if jungle == 'ok':
			print 'Downloading.............'
			while 1:
        	       		data = s.recv(2048)
                		if data != 'done':
                			clientInfo += data
                		else:
                			f = open(command.split()[1],'wb')
                			f.write(clientInfo)
                			f.close()
                			print 'Download done'
                			break
		else:
			print('The File not exist in server')


	elif command.split()[0] == 'local':
		while True:
			localCommand = raw_input('localMachine#').strip()
			if localCommand == 'quitLocal':
				break
			else:
				os.system(localCommand)
	elif command.split()[0] == 'help':
		ftpHelpDoc.help()		
	else:
		pass
	serverInfo = s.recv(2048)
	if serverInfo == 'quit':
		print 'exit!'
		break

	elif serverInfo == 'client':
		pass
	else:
		print 'server:\n',serverInfo
s.close()
