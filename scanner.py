#!/usr/bin/python3
import pyfiglet as py
import termcolor as tc
from socket import *
from optparse import OptionParser
from threading import *
from datetime import datetime
import os
import platform
#optparse library for help option
#threading library to run multiple threads
def connScan(host,port):
	try:
		sock = socket(AF_INET,SOCK_STREAM)
		sock.connect((host,port))
		banner = sock.recv(1024)
		print(tc.colored(f"[+] Port {port} is open {banner}",color="green"))
	except KeyboardInterrupt:
		print('\n KeyboardInterrupt: Exiting Program')
		sys.exit()
	except:
		print(tc.colored(f"[-] Port {port} is closed",color="red"))
	finally:
		sock.close()


def portscan(host,port):
	try:
		Ip = gethostbyname(host)
		print(tc.colored(py.figlet_format('PORTSCANNER'),color="green"))
		print('Created by: Abhishek Rautela (Twitter:deltsandtraps)')
		print('Github: https://github.com/abhishekrautela')
		print('Current Version: 1.0')
		print('Time Started: ' + str(datetime.now()))
		print(f"Scanning from : {os.name} {platform.system()} {platform.release()}")
		print('-' * 60)
	except:
		print(f"Can't resolve specified host: {host}")
	try:
		Name = gethostbyaddr(Ip)
		print(tc.colored(py.figlet_format('PORTSCANNER'),color="green"))
		print('Created by: Abhishek Rautela')
		print('Github: https://github.com/abhishekrautela')
		print('Current Version: 1.0')
		print('Time Started: ' + str(datetime.now()))
		print(f"Scanning from : {os.name} {platform.system()} {platform.release()}")
		print('-' * 60)
		print("[+] Scan results for: "+ Name[0])

	except:
		print("[+] Scan results for: "+ Ip)
	setdefaulttimeout(2)
	for p in port:
		t = Thread(target=connScan,args=(host,int(p)))
		t.start()

def main():
	parser = OptionParser('To scan a host use the following syntax: '+ '--host <target ip> --p <port>')
	parser.add_option('--host' , dest='target' , type="string" , help='Specify target Host ')
	parser.add_option('--p' , dest='targetports' , type="string" , help='Specify target ports seperated by comma or You can provide a range of ports seperated by \'-\'  \"For example --p 80,443 or --p 80-443\"')
	(options,args) = parser.parse_args()
	target = options.target
	targetports = str(options.targetports)
	# targetports = str(options.targetports).split(',')
	if '-' in targetports:
		tp = targetports.split('-')
		targetports = []
		for ports in range(int(tp[0]),int(tp[1])+1):
			targetports.append(ports)
	elif ',' in targetports:
		tp = targetports.split(',')
		targetports = tp
	else:
		raise TypeError('Weird Syntax. Type --help for help info')
		exit(0)
	if target == None or targetports[0] == None:
		print(parser.usage)
		exit()
	portscan(target,targetports)
if __name__ == '__main__':
	main()
