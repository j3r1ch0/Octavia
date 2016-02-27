#Octavia 1.0 written in Python (Gattorete@Home)
#For more: http://www.gattorete.org
#Author: 0x8b30cc [Davide Pataracchia] (Gattorete@Home)
#Licensed under GNU GENERAL PUBLIC LICENSE (GPLv3)

import urllib2
import Data.output_writer

#Terminal colors and options 
HEADER = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLO = '\033[93m'
RED = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

ext = [".php", ".html", ".txt", ".htm", ".php3",".zip", ".tar", ".7z",".log", ".rtf", ".tex", ".csv", ".dat",".xml",".mp3",".wav",".wma",".db",".sql",".apk",".js",".cfg",".rar",
".zipx",".c",".class",".java",".py",".sh",".tmp",".old",".copy"]

#Check the url http response 
def http_response(url):		
	try:
	   	connection = urllib2.urlopen(url)
        	return connection.getcode()
        	connection.close()
    	except urllib2.HTTPError, e:
        	return e.getcode()

#Test the webserver for dirs
def test_dirs(data,target):
	Data.output_writer.append_to_list("++++++DIRECTORIES++++++")
	for line in data:
		line = line.replace("\n",""); 
		response = http_response(target + "/" + line)	
		if (response == 200):
			print GREEN + BOLD + "[SUCCESS] Found: " + target + "/" + line + ENDC
			Data.output_writer.append_to_list(target + "/" + line)
		elif (response == 403):
			print GREEN + BOLD + "[SUCCESS]" + YELLO + " 403 Forbidden: " + target + "/" + line + ENDC
			Data.output_writer.append_to_list("FORBIDDEN: " + target + "/" + line)
		elif (response == 301):
			print GREEN + BOLD + "[SUCCESS]" + YELLO + " 301: " + target + "/" + line + ENDC
			Data.output_writer.append_to_list(target + "/" + line)
	
#Test the webserver for files
def test_files(data,target):
	Data.output_writer.append_to_list("++++++FILES++++++")	
	for line in data:
		for a in ext:
			line = line.replace("\n",""); 
			response = http_response(target + "/" + line + a)
			if (response == 200):
				print GREEN + BOLD + "[SUCCESS] Found: " + target + "/" + line + a + ENDC
				Data.output_writer.append_to_list(target + "/" + line + a)
			elif (response == 403):
				print GREEN + BOLD + "[SUCCESS]" + YELLO + " 403 Forbidden: " + target + "/" + line + a + ENDC
				Data.output_writer.append_to_list("FORBIDDEN: "+ target + "/" + line + a)
			elif (response == 301):
				print GREEN + BOLD + "[SUCCESS]" + YELLO + " 301: " + target + "/" + line + a + ENDC
				Data.output_writer.append_to_list(target + "/" + line + a)
		

