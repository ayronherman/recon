#!/usr/bin/env python

#######################################################################################
## recon.py -- Used for active recon of ip addresses
## Ayron Herman
#######################################################################################


import multiprocessing
import subprocess
import os
import time

def nmap(ip_address):
	ip_address = ip_address.strip()
  	print "INFO: Running light top 10 TCP/UDP port scans for " + ip_address
  	service_dict = {}
  	TOP10TCPSCAN = "nmap --top-ports 10 --open -oN 'results/%s/top10_tcp.nmap' %s"  % (ip_address, ip_address)
  	top10tcpresults = subprocess.check_output(TOP10TCPSCAN, shell=True)
	lines = top10tcpresults.split("\n")
	print "INFO: Light top 10 port scanning found the following open ports for " + ip_address
  	for line in lines:
    		line = line.strip()
    		if ("tcp" in line):
			print "\t" + line
	TOP10UDPSCAN = "nmap -sU --top-ports 10 --open -oN 'results/%s/top10_udp.nmap' %s" % (ip_address, ip_address)
	subprocess.check_output(TOP10UDPSCAN, shell=True)
	print "TASK: Look at the light top 10 UDP port scan results."
	print "INFO: Running heavy TCP port scan for " + ip_address
	HEAVYTCPSCAN = "nmap -p- -sV --reason --dns-server 10.11.1.220 --open --max-retries 1 --stats-every 3m --max-scan-delay 20 --defeat-rst-ratelimit -oN 'results/%s/heavy_tcp.nmap' %s"  % (ip_address, ip_address)
        heavytcpresults = subprocess.check_output(HEAVYTCPSCAN, shell=True)
	lines = heavytcpresults.split("\n")
	print "INFO: Heavy port scanning found the following open ports for " + ip_address
	for line in lines:
		ports = []
		if ("tcp" in line) and ("open" in line) and not ("Discovered" in line):
      			linesplit = line.split()
			print "\t" + line
      			port = linesplit[0]
     			service = linesplit[2]
      			if service in service_dict:
        			ports = service_dict[service]
      			ports.append(port)
      			service_dict[service] = ports
# Now its time to fire off more enumeration scripts.
  	for sname in service_dict:
    		ports = service_dict[sname]
		if (sname == "ssl/http") or "https" in sname:
      			for port in ports:
        			port = port.split("/")[0]
        			multiproc(httpsenum, ip_address, port)
		elif (sname == "http"):
			for port in ports:
				port = port.split("/")[0]
				multiproc(httpenum, ip_address, port)
		elif "microsoft-ds" in sname:
 	 		for port in ports:
	    			port = port.split("/")[0]
	    			multiproc(smbenum, ip_address, port)
		elif ("ftp" in sname):
      			for port in ports:
        			port = port.split("/")[0]
        			multiproc(ftpenum, ip_address, port)
		elif "snmp" in sname:
		    	for port in ports:
        			port = port.split("/")[0]
        			multiproc(snmpenum, ip_address, port)
		elif "ssh" in sname:
			for port in ports:
				port = port.split("/")[0]
				multiproc(sshenum, ip_address, port)
                elif sname == 'msSql' or sname == 'ms-sql-s' or sname == 'ms-sql':
                        for port in ports:
                                port = port.split("/")[0]
                                multiproc(mssqlenum, ip_address, port)
                elif "mysql" in sname:
                        for port in ports:
                                port = port.split("/")[0]
                                multiproc(mysqlenum, ip_address, port)
                elif sname == 'rdp' or sname == ' microsoft-rdp' or sname == 'ms-wbt-server' or sname == 'ms-term-serv':
                        for port in ports:
                                port = port.split("/")[0]
		                multiproc(rdpenum, ip_address, port)
                elif "smtp" in sname:
                        for port in ports:
                                port = port.split("/")[0]
                                multiproc(smtpenum, ip_address, port)
	return

def multiproc(modname, ip_addr, port):
  jobs = []
  p = multiprocessing.Process(target=modname, args=(ip_addr,port))
  jobs.append(p)
  p.start()
  return

def httpenum(ip_address, port):
	print "INFO: Detected HTTP on " + ip_address + ":" + port
	HTTPSCAN = "./httpenum.py %s %s" % (ip_address, port)
        subprocess.call(HTTPSCAN, shell=True)
	return

def httpsenum(ip_address, port):
        print "INFO: Detected HTTPS on " + ip_address + ":" + port
        HTTPSSCAN = "./httpsenum.py %s %s" % (ip_address, port)
        subprocess.call(HTTPSSCAN, shell=True)
        return

def sshenum(ip_address, port):
	print "INFO: Detected SSH on " + ip_address + ":" + port
	SSHSCAN = "./sshenum.py %s %s" % (ip_address, port)
	subprocess.call(SSHSCAN, shell=True)
	return

def smbenum(ip_address, port):
	print "INFO: Detected SMB on " + ip_address + ":" + port
	NBTSCAN = "./smbenum.py %s" % (ip_address)
	subprocess.call(NBTSCAN, shell=True)
	return

def ftpenum(ip_address, port):
        print "INFO: Detected FTP on " + ip_address + ":" + port
        FTPSCAN = "./ftpenum.py %s %s" % (ip_address, port)
        subprocess.call(FTPSCAN, shell=True)
        return

def mssqlenum(ip_address, port):
        print "INFO: Detected MS-SQL on " + ip_address + ":" + port
        MSSQLSCAN = "./mssqlenum.py %s %s" % (ip_address, port)
        subprocess.call(MSSQLSCAN, shell=True)
        return

def mysqlenum(ip_address, port):
        print "INFO: Detected MY-SQL on " + ip_address + ":" + port
        MYSQLSCAN = "./mysqlenum.py %s %s" % (ip_address, port)
        subprocess.call(MYSQLSCAN, shell=True)
        return

def rdpenum(ip_address, port):
        print "INFO: Detected RDP on " + ip_address + ":" + port
        RDPSCAN = "./rdpenum.py %s %s" % (ip_address, port)
        subprocess.call(RDPSCAN, shell=True)
        return

def smtpenum(ip_address, port):
        print "INFO: Detected SMTP on " + ip_address + ":" + port
        SMTPSCAN = "./smtpenum.py %s %s" % (ip_address, port)
        subprocess.call(SMTPSCAN, shell=True)
        return

def snmpenum(ip_address, port):
        print "INFO: Detected SNMP on " + ip_address + ":" + port
        SNMPSCAN = "./snmpenum.py %s %s" % (ip_address, port)
        subprocess.call(SNMPSCAN, shell=True)
        return

print "######################################################"
print "##                HERM WORM RECON                   ##"
print "##                 Worming my in!                   ##"
print "##                                                  ##"
print "##    http, https, ssh, smb, ftp, mssql, mysql,     ##"
print "##                rdp, smtp, snmp                   ##"
print "######################################################"
print ("\n" * 2)

if __name__ == '__main__':
  	f = None
	try:
		f = open('targets.txt', 'r') # This is a list of IPs to scan
  		jobs = []
  		for ip in f:
			if ip[0]=='#':
                        	pass
                    	else:
				ip = ip.strip()
				if not os.path.exists('results/'+ip):
    					os.makedirs('results/'+ip)
    				p = multiprocessing.Process(target=nmap, args=(ip,))
    				jobs.append(p)
    				p.start()
	finally:
		if f is not None:
			f.close()
