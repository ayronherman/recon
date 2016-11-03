#!/usr/bin/env python

import subprocess
import sys
import os

if len(sys.argv) != 3:
    print "Usage: mysqlenum.py <ip address> <port>"
    sys.exit(0)

ip_address = sys.argv[1].strip()
port = sys.argv[2].strip()

print "INFO: Running MYSQL nmap scripts for " + ip_address + ":" + port

MYSQLSCAN = "nmap -sV --script=mysql* -p %s -oN 'results/%s/mysql_%s.nmap' %s" % (port, ip_address, port, ip_address)
subprocess.check_output(MYSQLSCAN, shell=True)

CATMYSQL = "cat results/%s/mysql_%s.nmap" % (ip_address, port)
CATMYSQLRESULTS = subprocess.check_output(CATMYSQL, shell=True)
lines = CATMYSQLRESULTS.split("\n")
print "INFO: MYSQL nmap scripts found the following for " + ip_address + ":" + port
for line in lines:
        print "\t" + line

#build out brute force section
