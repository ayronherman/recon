#!/usr/bin/env python

import subprocess
import sys
import os

if len(sys.argv) != 3:
    print "Usage: ftpenum.py <ip address> <port>"
    sys.exit(0)

ip_address = sys.argv[1].strip()
port = sys.argv[2].strip()

print "INFO: Running FTP nmap scripts for " + ip_address + ":" + port

FTPSCAN = "nmap -sV --script=ftp* -p %s -oN 'results/%s/ftp_%s.nmap' %s" % (port, ip_address, port, ip_address)
subprocess.check_output(FTPSCAN, shell=True)

CATFTP = "cat results/%s/ftp_%s.nmap" % (ip_address, port)
CATFTPRESULTS = subprocess.check_output(CATFTP, shell=True)
lines = CATFTPRESULTS.split("\n")
print "INFO: FTP nmap scripts found the following for " + ip_address + ":" + port
for line in lines:
        print "\t" + line

#build out brute force section

