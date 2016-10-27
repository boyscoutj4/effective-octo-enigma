#!/usr/bin/python
#Description: This scripts resolves a given website and automatically add an Akamai staging IP to your host file.
#This will help us when testing rule in staging. Also creates a hidden log file in the directory you run the progam.
#Note: Please run this program as sudo.
#Created: 10.11.2016
#v1.0
#Author: Julio Betanco with an assist from ACE.

import argparse, re, commands, fileinput, datetime


#Setting arguments to either add or delete staging IPs to local host file.
parser = argparse.ArgumentParser() # Creating the parser object. 
parser.add_argument("-a", "--add", help="Use this option if you want to ADD staging IP to hosts file") #Created the "add" argument, requires a user input in order to run the program. Using the "-a" flag with the program will delete domain from host.
parser.add_argument("-d", "--delete", help="Use this option if you want to DELETE staging IP to hosts file") #Created the "delete" argument, requires a user input in order to run the program. Using the "-d" flag with the program will delete domain from host.
args = parser.parse_args() #Creates the args object that we can call later.

#If you choose the add argument then it will add the staging IP to host file.
if args.add: #If the user chooses the "-a" option/argument.
	if (args.add) in open('/etc/hosts').read(): # If the users argument is in '/etc/hosts' the print the line below.  
		print("%s ALREADY exists in hosts file" %(args.add))
	else: 
		stagingip = commands.getoutput('dig %s +short | grep edgekey | sed \'s/edgekey/edgekey-staging/\' | xargs dig +short | grep -Eo \'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\'' %(args.add)) #The 'command' module contains takes the input as a string sent it the OS and executes. Also get the results and puts it objects. 
		if (stagingip) == "": #If the object 'stagingip' contains no string then print below.
			print("%s is NOT Akamaized!!" %(args.add))
		else:
			openfile = open('/etc/hosts', 'a') #If the object 'stagingip' does contain a string open '/etc/hosts' in append mode, puts it 'openfile' object. 
			inputfile = str(stagingip) + "\t" + (args.add) + "\n" #Converts object 'stagingip' to a string concatenate with a tab concatenate again with the 'args.add' concatenate with a character return. 
			openfile.writelines(inputfile) #Execude what the object 'openfile' does with the option to writelines with object 'inputfile'
			addlog = '{:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()) + " ADDED " + str(stagingip) + " " + (args.add) + "\n" #Adds timestamp with datetime format concatenate with 'Added' concatenate with 'stagingip' concatenate with 'arg.add'
			logfile = open('./.dig2host.txt', 'a') #Creates or appends file in the current directory called '.dig2host.txt'
			logfile.writelines(addlog) #Execude what the object 'logfile' does with the option to writelines with object 'addlog'
			print(addlog)
			

#If you choose the delete argument then it will delete the domain/staging IP from the host file.
if args.delete: # If the user chooses the "-d" option/argument.
	if not (args.delete) in open('/etc/hosts').read(): #Check to see if the users arguments, is in '/etc/hosts'.
		print ("%s DOES NOT exists in host file" %(args.delete))
	else:
		for line in fileinput.input('/etc/hosts', inplace = True): #Creates a backup '/etc/host'. Then it takes the results and prints it to '/etc/host/'.
			if not re.search((args.delete),line): #It searches through it the regex argument that the users input and removes it.
				print line, #If the argument is not there then prints back to the original file.
		dellog = '{:%Y-%b-%d %H:%M:%S}'.format(datetime.datetime.now()) + " DELETED " + (args.delete) + "\n"
		logfile = open('./.dig2host.txt', 'a')
		logfile.writelines(dellog)
		print(dellog)
				








	