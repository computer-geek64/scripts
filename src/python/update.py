#!/usr/bin/python3
# update.py 2.8
# Ashish D'Souza
# February 11th, 2019

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
version = 2.7
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
	print("-ua\t\t--update-args\t\tSpecify \"apt-get update\" arguments with a comma-separated list")
	print("-da\t\t--dist-upgrade-args\tSpecify \"apt-get dist-upgrade\" arguments with a comma-separated list")
	print("-aa\t\t--autoremove-args\tSpecify \"apt-get autoremove\" arguments with a comma-separated list")
	print("-ca\t\t--clean-args\t\tSpecify \"apt-get clean\" arguments with a comma-separated list")

banner = True
usage = False
developer_info = False
update_command = "apt-get update -y"
dist_upgrade_command = "apt-get dist-upgrade -y"
autoremove_command = "apt-get autoremove -y"
clean_command = "apt-get clean -y"

arg = 1
while arg < len(sys.argv):
	if sys.argv[arg] == "-h" or sys.argv[arg] == "--help":
		usage = True
	elif sys.argv[arg] == "-d" or sys.argv[arg] == "--developer":
		developer_info = True
	elif sys.argv[arg] == "-b" or sys.argv[arg] == "--no-banner":
		banner = False
	elif sys.argv[arg] == "-ua" or sys.argv[arg] == "--update-args":
		arg += 1
		update_command += " " + " ".join(sys.argv[arg].split(","))
	elif sys.argv[arg] == "-da" or sys.argv[arg] == "--dist-upgrade-args":
		arg += 1
		dist_upgrade_command += " " + " ".join(sys.argv[arg].split(","))
	elif sys.argv[arg] == "-aa" or sys.argv[arg] == "--autoremove-args":
		arg += 1
		autoremove_command += " " + " ".join(sys.argv[arg].split(","))
	elif sys.argv[arg] == "-ca" or sys.argv[arg] == "--clean-args":
		arg += 1
		clean_command += " " + " ".join(sys.argv[arg].split(","))
	else:
		usage = True
		break
	arg += 1

if banner:
	print_banner()

if usage:
	print_usage()
	sys.exit(0)

if developer_info:
	print(requests.get(developer_info_url).text)
	sys.exit(0)

os.system(update_command)
os.system(dist_upgrade_command)
os.system("update-initramfs -u -k all")
os.system(autoremove_command)
os.system(clean_command)
