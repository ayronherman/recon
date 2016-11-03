#!/usr/bin/env python

import subprocess
import sys
import os

if len(sys.argv) != 3:
    print "Usage: mssqlenum.py <ip address> <port>"
    sys.exit(0)

ip_address = sys.argv[1].strip()
port = sys.argv[2].strip()

print "INFO: Running MSSQL nmap scripts for " + ip_address + ":" + port

MSSQLSCAN = "nmap -sV --script=ms-sql* -p %s -oN 'results/%s/mssql_%s.nmap' %s" % (port, ip_address, port, ip_address)
subprocess.check_output(MSSQLSCAN, shell=True)

CATMSSQL = "cat results/%s/mssql_%s.nmap" % (ip_address, port)
CATMSSQLRESULTS = subprocess.check_output(CATMSSQL, shell=True)
lines = CATMSSQLRESULTS.split("\n")
print "INFO: MSSQL nmap scripts found the following for " + ip_address + ":" + port
for line in lines:
        print "\t" + line

#build out brute force section
