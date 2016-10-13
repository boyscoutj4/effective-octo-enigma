#!/usr/bin/python
#Description: This scripts resolves a given website and automatically add an Akamai staging IP to your host file. This will help us when testing rule in staging.
#Created: 10.11.2016
#v1.0
#Author: Julio Betanco


import socket, sys, re, getpass, datetime, os

#Asking for www site to add to your /etc/hosts file and puts into a variable.
wsite = raw_input("Type website you want to add to /etc/hosts: ")
print("Resolving for %s" %(wsite))

#This does the resolution of the site provided by user in previous command.
edgekey = os.system('dig %s | grep -h edgekey | awk \'{print $5}\' | grep -v akamaiedge' %(wsite))

#Getting staging IP from the edgekey.net site and puts into a variable.


