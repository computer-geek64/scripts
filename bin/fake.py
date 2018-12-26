#!/usr/bin/python3
# fake.py v1.3
# Ashish D'Souza
# December 26th, 2018

try:
	import os
	import sys
	from random import random
	from datetime import datetime
	import requests
except ImportError:
	print("[-] Installing dependencies...")
	if os.system("pip install --upgrade requests datetime; pip3 install --upgrade requests datetime") == 0:
		print("[+] Dependencies successfully installed.")
	else:
		print("[!] Dependency installation failed. Script restart required.")
		exit(0)

name = os.path.split(sys.argv[0])[-1]
with open(sys.argv[0], "r") as file:
	lines = file.readlines()
	file.close()
version = float(lines[1].split(" ")[-1][1:])
developer = " ".join(lines[2].split(" ")[-2:]).strip()
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
	print("-s\t\t--setup\t\t\tRun one-time setup to install \"rig\" package")

banner = True
usage = False
developer_info = False
setup = False

for arg in sys.argv[1:]:
	if arg == "-h" or arg == "--help":
		usage = True
	elif arg == "-d" or arg == "--developer":
		developer_info = True
	elif arg == "-b" or arg == "--no-banner":
		banner = False
	elif arg == "-s" or arg == "--setup":
		setup = True
	else:
		usage = True

if banner:
	print_banner()

if usage:
	print_usage()
	exit(0)

if setup:
	print("[-] Installing dependencies...")
	if os.system("apt-get update --fix-missing -y; apt-get install rig -y; apt-get autoremove -y; apt-get clean -y") == 0:
		print("[+] Dependencies successfully installed.")
	else:
		print("[!] Dependency installation failed. Script restart required.")

if developer_info:
	print(requests.get(developer_info_url).text)
	exit(0)

rig = os.popen("rig").read().split("\n")
rig[3] = rig[3].split(" ")[0] + " " + str(int(random() * 900) + 100) + "-" + str(int(random() * 9000) + 1000)
rig = [x.replace("  ", " ") for x in rig if x]
print("\n".join(rig))
