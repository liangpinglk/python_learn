#!/usr/bin/env python

import SocketServer,os,tab,sys
from time import sleep
import ftpServerLog

class myTCPHandler(SocketServer.BaseRequestHandler):
	def handle(self):
		print 'Waiting...........'
		print self.client_address,' has connected'
		self.request.sendall('Connected successfully!')
		ftpServerLog.ftpLog(self.client_address,'Connect')
		

		while True:

			self.data = self.request.recv(1024)
			command = self.data.split()
			print self.client_address,command


			if command[0] == 'get':
				try:
					f= open(command[1],'rb')
					if f:
						self.request.sendall('ok')
						sleep(0.5)
	                		data = f.read()
        	       			self.request.sendall(data)
               				sleep(1)
             				self.request.sendall('done')
               				f.close()
               				print 'send done'
					ftpServerLog.ftpLog(self.client_address,command)
					self.request.sendall('\033[32;1msend done\033[0m')
				except IOError:
					self.request.sendall('fail')
					print('%s file not exist in server.'%(command[1]))
					command.append('File not exist')
					sleep(0.5)
					self.request.sendall('The file not exist in server')
					ftpServerLog.ftpLog(self.client_address,command)
				except IndexError:
					self.request.sendall('fail')
                                        command.append('NULL')
					sleep(0.5)
                                        self.request.sendall('Please input a file name')
                                        ftpServerLog.ftpLog(self.client_address,command)


			elif command[0] == 'send':
				clientInfo = ''
                		jungle = self.request.recv(4)
                		print jungle
                		if jungle == 'ok':
                       			print 'recivng.............'
                        		while 1:
                                		data = self.request.recv(2048)
                                		if data != 'done':
                                        		clientInfo += data
                                		else:
                                        		f = open(command[1],'wb')
                                        		f.write(clientInfo)
                                        		f.close()
                                        		print 'Recive done'
							ftpServerLog.ftpLog(self.client_address,command)
                                			self.request.sendall('\033[32;1mRecive done\033[0m')
                                        		break
                		else:
					print('Invalid file')
					command.append('Invalid file')
					ftpServerLog.ftpLog(self.client_address,command)
					self.request.sendall('\033[32;1mInvalid file\033[0m')
				

			elif self.data == 'ls':
				self.data+=' -lh'
				cmd = os.popen(self.data)
                       		result = '\033[32;1mResult:\n\033[0m'+cmd.read()
				ftpServerLog.ftpLog(self.client_address,command)
                       		self.request.sendall(result)

			elif self.data == 'quit':
				print self.client_address,' has disconnected.'
				ftpServerLog.ftpLog(self.client_address,command)
				self.request.sendall('quit')
				break

			elif self.data == 'local' or self.data == 'help':
				ftpServerLog.ftpLog(self.client_address,command)
                                self.request.sendall('client')

			else:
				ftpServerLog.ftpLog(self.client_address,'Wrong command')
				self.request.sendall("\033[32;1mWrong command!You can input 'help'\033[0m")

host = ''
port = int(sys.argv[1])
server = SocketServer.ThreadingTCPServer((host,port),myTCPHandler)
server.serve_forever()
