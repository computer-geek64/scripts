#!/usr/bin/python3
# stocks.py v1.0
# Ashish D'Souza
# December 29th, 2018

try:
	import os
	import sys
	import requests
	from datetime import datetime
except ImportError:
	print("[-] Installing dependencies...")
	if os.system("pip install --upgrade requests datetime; pip3 install --upgrade requests datetime") == 0:
		print("[+] Dependencies successfully installed.")
	else:
		print("[!] Dependency installation failed. Script restart required.")
	sys.exit(0)

name = os.path.split(sys.argv[0])[-1]
version = 1.0
developer = "Ashish D'Souza"
developer_info_url = "https://computer-geek64.github.io/info"
rights = "All rights reserved."

def print_banner():
	print(name + " v" + str(version))
	print("Copyright " + str(datetime.now().year) + " " + developer + ". " + rights + "\n")

def print_usage():
	print("Usage: " + name + " [options]\n")
	print("Option\t\tLong Option\t\tDescription")
	print("-h\t\t--help\t\t\tShow this help screen")
	print("-b\t\t--no-banner\t\tSuppress banner")
	print("-d\t\t--developer\t\tDisplay information about developer")

banner = True
usage = False
developer_info = False

arg = 1
while arg < len(sys.argv):
	if sys.argv[arg] == "-h" or sys.argv[arg] == "--help":
		usage = True
	elif sys.argv[arg] == "-b" or sys.argv[arg] == "--no-banner":
		banner = False
	elif sys.argv[arg] == "-d" or sys.argv[arg] == "--developer":
		developer_info = True
	else:
		usage = True
	arg += 1

if banner:
	print_banner()

if usage:
	print_usage()
	sys.exit(0)

if developer_info:
	print(requests.get(developer_info_url).text)
	sys.exit(0)
