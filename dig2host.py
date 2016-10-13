#!/usr/bin/python
#Description: This scripts resolves a given website and automatically add an Akamai staging IP to your host file. This will help us when testing rule in staging.
#Created: 10.11.2016
#v1.0
#Author: Julio Betanco


import socket, sys, re, getpass, datetime, os, optparse, pexpect

#Adding options to add/delete staging IP from host file
theparser = optparse.OptionParser()
myparser.add_option('-a', '--add', action='store', help='Use this option if you want to ADD staging IP to hosts file', dest='a')
myparser.add_option('-d', '--delete', action='store_true', help='Use this option if you want to DELETE staging IP from hosts file', dest='d')
(opt, args) = theparser.parse_args()

#Not allowing to choose both options add and delete.
if opt.d is True and opt.a is True:
	print "Please choose either -a or -d not both!"
	exit()
#Each option getting assigned task.  
else:
  if opt.a is True:
    wsite = raw_input("Type website you want to ADD to /etc/hosts: ")
    print("Resolving for %s" %(wsite))
    edgekey = os.system('dig %s +short | grep edgekey | sed \'s/edgekey/edgekey-staging/\' | xargs dig +short | grep -Eo \'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\'' %(wsite)) #This does the resolution of the site provided by user and gets the staging IP and puts it in a variable.
    




