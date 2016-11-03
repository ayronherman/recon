#!/usr/bin/env python

import subprocess
import sys
import os

if len(sys.argv) != 3:
    print "Usage: rdpenum.py <ip address> <port>"
    sys.exit(0)

ip_address = sys.argv[1].strip()
port = sys.argv[2].strip()

print "INFO: Running RDP nmap scripts for " + ip_address + ":" + port

RDPSCAN = "nmap -sV --script=rdp* -p %s -oN 'results/%s/rdp_%s.nmap' %s" % (port, ip_address, port, ip_address)
subprocess.check_output(RDPSCAN, shell=True)

CATRDP = "cat results/%s/rdp_%s.nmap" % (ip_address, port)
CATRDPRESULTS = subprocess.check_output(CATRDP, shell=True)
lines = CATRDPRESULTS.split("\n")
print "INFO: RDP nmap scripts found the following for " + ip_address + ":" + port
for line in lines:
        print "\t" + line

#build out brute force section

