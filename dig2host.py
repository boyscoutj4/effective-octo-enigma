#!/usr/bin/python
#Description: This scripts resolves a given website and automatically add an Akamai staging IP to your host file. This will help us when testing rule in staging.
#Note: Please run this program as sudo.
#Created: 10.11.2016
#v1.0
#Author: Julio Betanco with an assist from ACE.

import os, argparse, sys, re, commands, fileinput, datetime


#Setting arguments to either add or delete staging IPs to local host file.
parser.add_argument("-a", "--add", help="Use this option if you want to ADD staging IP to hosts file") #Created the "add" argument, requires a user input in order to run the program. Using the "-a" flag with the program will delete domain from host.
parser.add_argument("-d", "--delete", help="Use this option if you want to DELETE staging IP to hosts file") #Created the "delete" argument, requires a user input in order to run the program. Using the "-d" flag with the program will delete domain from host.

#If you choose the add argument then it will add the staging IP to host file.
	if (args.add) in open('/etc/hosts').read(): # If the users argument is in '/etc/hosts' the print the line below.  
		print("%s ALREADY exists in hosts file" %(args.add))
		if (stagingip) == "":
	else: 
			print("%s is NOT Akamaized!!" %(args.add))
		else:
			openfile = open('/etc/hosts', 'a')
			inputfile = str(stagingip) + "\t" + (args.add) + "\n"
			openfile.writelines(inputfile)
			addlog = '{:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()) + " ADDED " + str(stagingip) + " " + (args.add) + "\n"
			logfile = open('./.dig2host.txt', 'a')
			logfile.writelines(addlog)
			print(addlog)
			

#If you choose the delete argument then it will delete the domain/staging IP from the host file.
if args.delete:
	if not (args.delete) in open('/etc/hosts').read():
		print ("%s DOES NOT exists in host file" %(args.delete))
	else:
		for line in fileinput.input('/etc/hosts', inplace = True):
			if not re.search((args.delete),line):
				print line,
		dellog = '{:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()) + " DELETED " + (args.delete) + "\n"
		logfile = open('./.dig2host.txt', 'a')
		logfile.writelines(dellog)
		print(dellog)
				








	