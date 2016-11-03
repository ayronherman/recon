#!/usr/bin/env python

import subprocess
import sys
import os

if len(sys.argv) != 3:
    print "Usage: snmpenum.py <ip address> <port>"
    sys.exit(0)

ip_address = sys.argv[1].strip()
port = sys.argv[2].strip()

print "INFO: Running SNMP nmap scripts for " + ip_address + ":" + port

SNMPSCAN = "nmap -sV --script=snmp* -p %s -oN 'results/%s/snmp_%s.nmap' %s" % (port, ip_address, port, ip_address)
subprocess.check_output(SNMPSCAN, shell=True)

CATSNMP = "cat results/%s/snmp_%s.nmap" % (ip_address, port)
CATSNMPRESULTS = subprocess.check_output(CATSNMP, shell=True)
lines = CATSNMPRESULTS.split("\n")
print "INFO: SNMP nmap scripts found the following for " + ip_address + ":" + port
for line in lines:
        print "\t" + line

#build out brute force section
