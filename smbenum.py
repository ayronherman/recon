#!/usr/bin/env python

import sys
import subprocess
import os

if len(sys.argv) != 2:
    print "Usage: smbrecon.py <ip address>"
    sys.exit(0)

ip_address = sys.argv[1]

print "INFO: Running SMB enum4linux, nbtscan and nmap script scan for " + ip_address

E4LSCAN = "enum4linux -a %s > results/%s/enum4linux.txt" % (ip_address, ip_address)
subprocess.check_output(E4LSCAN, shell=True)

CATE4L = "cat results/%s/enum4linux.txt" % (ip_address)
CATE4LRESULTS = subprocess.check_output(CATE4L, shell=True)
lines = CATE4LRESULTS.split("\n")
print "INFO: Enum4linux found the following for " + ip_address
for line in lines:
        print "\t" + line

NMAPSMB = "nmap -sV -p139,445 --script=\'smb* and not (smb-flood or smb-brute)\' -oN results/%s/smb_tcp.nmap %s" % (ip_address, ip_address)
subprocess.check_output(NMAPSMB, shell=True)

CATNMAP = "cat results/%s/smb_tcp.nmap" % (ip_address)
CATNMAPRESULTS = subprocess.check_output(CATNMAP, shell=True)
lines = CATNMAPRESULTS.split("\n")
print "INFO: SMB nmap script found the following for " + ip_address
for line in lines:
        print "\t" + line

NTBSCAN = "nbtscan -r -v -h %s > results/%s/nbtscan.txt" % (ip_address, ip_address)
subprocess.check_output(NTBSCAN, shell=True)

CATNTB = "cat results/%s/nbtscan.txt" % (ip_address)
CATNTBRESULTS = subprocess.check_output(CATNTB, shell=True)
lines = CATNTBRESULTS.split("\n")
print "INFO: Nbtscan found the following for " + ip_address
for line in lines:
        print "\t" + line

