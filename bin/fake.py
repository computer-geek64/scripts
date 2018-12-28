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
		exit(0)
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
	print("-g [gender]\t--gender [gender]\tSpecify gender of fake profile to generate (m/f, male/female)")

banner = True
usage = False
developer_info = False
setup = False
gender = ""

arg = 1
while arg < len(sys.argv):
	if sys.argv[arg] == "-h" or sys.argv[arg] == "--help":
		usage = True
	elif sys.argv[arg] == "-d" or sys.argv[arg] == "--developer":
		developer_info = True
	elif sys.argv[arg] == "-b" or sys.argv[arg] == "--no-banner":
		banner = False
	elif sys.argv[arg] == "-s" or sys.argv[arg] == "--setup":
		setup = True
	elif sys.argv[arg] == "-g" or sys.argv[arg] == "--gender":
		arg += 1
		if sys.argv[arg].lower() == "m" or sys.argv[arg].lower() == "male":
			gender = "m"
		elif sys.argv[arg].lower() == "f" or sys.argv[arg].lower() == "female":
			gender = "f"
		else:
			usage = True
	else:
		usage = True
	arg += 1

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

if len(gender) > 0:
	rig = os.popen("rig -" + gender).read().split("\n")
else:
	rig = os.popen("rig").read().split("\n")
rig[3] = rig[3].split(" ")[0] + " " + str(int(random() * 900) + 100) + "-" + str(int(random() * 9000) + 1000)
rig = [x.replace("  ", " ") for x in rig if x]
print("\n".join(rig))
