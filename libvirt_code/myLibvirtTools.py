#!/usr/bin/env python

import libvirtToolsFunction,tab,libvirt,createNewXml
while True:
	try:
		myLibvirtManage = raw_input('myLibvirtManage>>')
		command = myLibvirtManage.split()
		if command:
			if command[0] == 'help':
				libvirtToolsFunction.helpDoc()
	
			elif command[0] == 'define':
				libvirtToolsFunction.defineXml(command[1])

			elif command[0] == 'start':
				libvirtToolsFunction.startGuestByName(command[1])

			elif command[0] == 'shutdown':
       				libvirtToolsFunction.shutdown(command[1])

			elif command[0] == 'info':
				libvirtToolsFunction.checkInformation(command[1])

			elif command[0] == 'undefine':
        			libvirtToolsFunction.undefineXml(command[1])

			elif command[0] == 'pause':
				libvirtToolsFunction.pause(command[1])

			elif command[0] == 'resume':
				libvirtToolsFunction.restart(command[1])

			elif command[0] == 'listAll':
				libvirtToolsFunction.listAll()

			elif command[0] == 'quit':
				libvirtToolsFunction.quit()
				break
		
			elif command[0] == 'pause':
				libvirtToolsFunction.pause(command[1])

			elif command[0] == 'resume':
				libvirtToolsFunction.restart(command[1])
			elif command[0] == 'create':
				createNewXml.create()
				print('xml file has file has been generated.')
			else:
				print('Wrong command!')
	except KeyboardInterrupt:
		print("If you want to quit,please input 'quit'")
	except EOFError:
		print("If you want to quit,please input 'quit'")
	except IndexError:
		print("Not full command")
