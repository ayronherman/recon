#!/usr/bin/env python

import subprocess
import sys
import os

if len(sys.argv) != 3:
    print "Usage: smtpenum.py <ip address> <port>"
    sys.exit(0)

ip_address = sys.argv[1].strip()
port = sys.argv[2].strip()

print "INFO: Running SMTP nmap scripts for " + ip_address + ":" + port

SMTPSCAN = "nmap -sV --script=smtp* -p %s -oN 'results/%s/smtp_%s.nmap' %s" % (port, ip_address, port, ip_address)
subprocess.check_output(SMTPSCAN, shell=True)

CATSMTP = "cat results/%s/smtp_%s.nmap" % (ip_address, port)
CATSMTPRESULTS = subprocess.check_output(CATSMTP, shell=True)
lines = CATSMTPRESULTS.split("\n")
print "INFO: SMTP nmap scripts found the following for " + ip_address + ":" + port
for line in lines:
        print "\t" + line

#build out brute force section

