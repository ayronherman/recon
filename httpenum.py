#!/usr/bin/env python

import subprocess
import sys
import os

if len(sys.argv) != 3:
    print "Usage: httpenum.py <ip address> <port>"
    sys.exit(0)

ip_address = sys.argv[1].strip()
port = sys.argv[2].strip()

print "INFO: Running HTTP scripts for header, robots, Gobuster and Nikto for " + ip_address + ":" + port

HEADERGRAB = "curl -s -I -m 300 http://%s:%s > results/%s/curl_headder_%s.txt" % (ip_address,port,ip_address,port)
subprocess.check_output(HEADERGRAB, shell=True)

CATHEADER = "cat results/%s/curl_headder_%s.txt" % (ip_address, port)
CATHEADERRESULTS = subprocess.check_output(CATHEADER, shell=True)
lines = CATHEADERRESULTS.split("\n")
print "INFO: HTTP curl header found the following for " + ip_address + ":" + port
for line in lines:
        print "\t" + line

ROBOTSGRAB = "curl -s -m 300 -L -H \"User-Agent: Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)\" http://%s:%s/robots.txt | html2text > results/%s/curl_robots_%s.txt" % (ip_address,port,ip_address,port)
subprocess.check_output(ROBOTSGRAB, shell=True)

CATROBOTS = "cat results/%s/curl_robots_%s.txt" % (ip_address, port)
CATROBOTSRESULTS = subprocess.check_output(CATROBOTS, shell=True)
lines = CATROBOTSRESULTS.split("\n")
print "INFO: HTTP curl robots.txt found the following for " + ip_address + ":" + port
for line in lines:
        print "\t" + line

GOBUSTER = "gobuster -u http://%s:%s -w /usr/share/seclists/Discovery/Web_Content/common.txt -s '200,204,301,302,307,403,500' -e > results/%s/gobuster_common_%s.txt" % (ip_address, port,ip_address,port)
subprocess.check_output(GOBUSTER, shell=True)

CATGO = "cat results/%s/gobuster_common_%s.txt" % (ip_address, port)
CATGORESULTS = subprocess.check_output(CATGO, shell=True)
lines = CATGORESULTS.split("\n")
print "INFO: HTTP Gobuster common found the following for " + ip_address + ":" + port
for line in lines:
        print "\t" + line
print "INFO: HTTP Dont forget to try the big.txt file"

GOBUSTER = "gobuster -u http://%s:%s -w /usr/share/seclists/Discovery/Web_Content/Top1000-RobotsDisallowed.txt -s '200,204,301,302,307,403,500' -e > results/%s/gobuster_robotdis_%s.txt" % (ip_address, port,ip_address,port)
subprocess.check_output(GOBUSTER, shell=True)

CATGO = "cat results/%s/gobuster_robotdis_%s.txt" % (ip_address, port)
CATGORESULTS = subprocess.check_output(CATGO, shell=True)
lines = CATGORESULTS.split("\n")
print "INFO: HTTP Gobuster robots disallow found the following for " + ip_address + ":" + port
for line in lines:
        print "\t" + line

NIKTOSCAN = "nikto -port %s -host %s -maxtime 45m -o results/%s/nikto_%s.txt" % (port, ip_address, ip_address, port)
subprocess.check_output(NIKTOSCAN, shell=True)

CATNIKTO = "cat results/%s/nikto_%s.txt" % (ip_address, port)
CATNIKTORESULTS = subprocess.check_output(CATNIKTO, shell=True)
lines = CATNIKTORESULTS.split("\n")
print "INFO: HTTP Nikto found the following for " + ip_address + ":" + port
for line in lines:
        print "\t" + line

