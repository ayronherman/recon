#!/usr/bin/env python

import subprocess
import sys
import os

if len(sys.argv) != 3:
    print "Usage: sshenum.py <ip address> <port>"
    sys.exit(0)

ip_address = sys.argv[1].strip()
port = sys.argv[2].strip()

print "INFO: Running SSH nmap banner grab and fingerprint script for " + ip_address + ":" + port

SSHSCAN = "nmap -sV --script=ssh-hostkey -p %s -oN 'results/%s/ssh_%s.nmap' %s" % (port, ip_address, port, ip_address)
subprocess.check_output(SSHSCAN, shell=True)

CATSSH = "cat results/%s/ssh_%s.nmap" % (ip_address, port)
CATSSHRESULTS = subprocess.check_output(CATSSH, shell=True)
lines = CATSSHRESULTS.split("\n")
print "INFO: SSH nmap banner grab and fingerprint found the following for " + ip_address + ":" + port
for line in lines:
	print "\t" + line

#build out brute force section
