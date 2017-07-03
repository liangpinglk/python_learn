#!/usr/bin/env python
def create():
	f = open('xmlDir/demo.xml','r')
	xmlList = f.readlines()
	f.close()

	domainName = raw_input('name:')
	domainMemory = raw_input('memory:')
	domainCurrentMemory = raw_input('currentMemory:')
	domainCpuSmp = raw_input('cpu:')
	domainSourceFile = raw_input('image:')
	xmlList[1] = '<name>'+domainName+'</name>\n'
	xmlList[2] = '<memory>'+domainMemory+'</memory>\n'
	xmlList[3] = '<currentMemory>'+domainCurrentMemory+'</currentMemory>\n'
	xmlList[4] = '<vcpu>'+domainCpuSmp+'</vcpu>\n'
	xmlList[23] = "<source file='"+domainSourceFile+"'/>\n"

	xmlStr = ''
	for line in xmlList:
		xmlStr+=line

	newXmlFileName = 'xmlDir/'+domainName+'.xml'
	f = open(newXmlFileName,'w')
	f.write(xmlStr)
	f.close()

