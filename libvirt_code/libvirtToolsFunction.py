#!/usr/bin/env python
from __future__ import print_function
import sys,libvirt,re
conn = libvirt.open('qemu:///system')

def helpDoc():
	print('''\033[32;1m
	help: 
		Give you a help document
	create:
		create a new file of the virtual machine
	define: 
		Define a new domain
	start:
		Start a virtual machine
	shutdown:
		Shutdown a cirtual machine
	info:
		List virtual machine
	undefine:
		Undefien a domain
	pasue:
		Pause a machine
	resume:
		Resume a pasue machine
	listAll:
		List all domain
	quit:
		exit\033[0m
	''')

def defineXml(xmlFileName):
	xmlFile = 'xmlDir/'+xmlFileName+'.xml'
	try:
		f = open(xmlFile,'r')
		xmlStr = f.read()
		if xmlStr == '':
			print ('The file not exist!')
		else:
			conn.defineXML(xmlStr)
		f.close()
	except IOError,error:
		print(error)
	except libvirt.libvirtError,error:
                print (error)

def look(name):
	try:
		dom = conn.lookupByName(name)
		if dom !=None:
			return dom
		else:
			print ('\032[31;1mNo define domain\032[0m')
			return None
	except libvirt.libvirtError,error:
		print (error)


def startGuestByName(name):
	dom = look(name)
	if dom != None:
		dom.create()


def shutdown(name):
	dom = look(name)
	if dom != None:
		dom.destroy()


def undefineXml(name):
	dom = look(name)
	if dom != None:
		dom.undefine()


def checkInformation(name):
	dom = look(name)
	if dom != None:
		print('\033[32;1mID:%s\nUUID:%s\nOSType:%s\nCpus:%s\nMemory:%s\033[0m'%(str(dom.ID()),str(dom.UUIDString()),str(dom.OSType()),str(dom.maxVcpus()),str(dom.maxMemory())))


def pause(name):
	dom = look(name)
	if dom != None:
		dom.suspend()


def restart(name):
	dom = look(name)
	if dom != None:
		dom.resume()


def quit():
	conn.close()


def listAll():
	ids = conn.listDomainsID()
	names = conn.listDefinedDomains()
	if ids: 
		for i in ids:
			dom = conn.lookupByID(i)
			xmlContent = dom.XMLDesc()
        		vncPort = re.findall('\d[0-9]{3}',str(re.findall("port='+\d[0-9]{3}'",xmlContent)))
			stat,reason = dom.state()
			if  stat == libvirt.VIR_DOMAIN_PAUSED:
				print('\033[32;1mID:%d\tname:%s\tpaused\tvncPort:%s\033[0m'%(dom.ID(),dom.name(),vncPort[0]))
			else:
				print('\033[32;1mID:%d\tname:%s\trunning\tvncPort:%s\033[0m'%(dom.ID(),dom.name(),vncPort[0]))
	if names:
		for na in names:
			dom = conn.lookupByName(na)
			print('\033[32;1mID:-\tname:%s\tshutoff\tvncPort:-\033[0m'%(dom.name()))
