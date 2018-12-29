#!/usr/bin/python3
# update.py 2.4
# Ashish D'Souza
# December 28th, 2018

try:
	import os
	import sys
	import requests
	from datetime import datetime
except ImportError:
	print("[-] Installing dependencies...")
	if os.system("pip install --upgrade requests datetime; pip3 install --upgrade requests datetime") == 0:
		print("[+] Dependencies successfully installed.")
		exit(0)
	else:
		print("[!] Dependency installation failed. Script restart required.")
		exit(0)

name = os.path.split(sys.argv[0])[-1]
version = 2.4
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
	print("-dua\t\t--dist-upgrade-args\tSpecify \"apt-get dist-upgrade\" arguments with a comma-separated list")
	print("-ara\t\t--autoremove-args\tSpecify \"apt-get autoremove\" arguments with a comma-separated list")
	print("-ca\t\t--clean-args\t\tSpecify \"apt-get clean\" arguments with a comma-separated list")

banner = True
usage = False
developer_info = False

arg = 1
while arg < len(sys.argv):
	if sys.argv[arg] == "-h" or sys.argv[arg] == "--help":
		usage = True
	elif sys.argv[arg] == "-d" or sys.argv[arg] == "--developer":
		developer_info = True
	elif sys.argv[arg] == "-b" or sys.argv[arg] == "--no-banner":
		banner = False
	else:
		usage = True
		break
	arg += 1

if banner:
	print_banner()

if usage:
	print_usage()
	exit(0)

if developer_info:
	print(requests.get(developer_info_url).text)
	exit(0)

update_args = "-y"
dist_upgrade_args = "-y"
autoremove_args = "-y"
clean_args = "-y"

if "--update-args" in sys.argv:
	update_args += " " + " ".join(sys.argv[sys.argv.index("--update-args") + 1].split(","))
elif "-ua" in sys.argv:
	update_args += " " + " ".join(sys.argv[sys.argv.index("-ua") + 1].split(","))

if "--dist-upgrade-args" in sys.argv:
	dist_upgrade_args += " " + " ".join(sys.argv[sys.argv.index("--dist-upgrade-args") + 1].split(","))
elif "-dua" in sys.argv:
	dist_upgrade_args += " " + " ".join(sys.argv[sys.argv.index("-dua") + 1].split(","))

if "--autoremove-args" in sys.argv:
	autoremove_args += " " + " ".join(sys.argv[sys.argv.index("--autoremove-args") + 1].split(","))
elif "-ara" in sys.argv:
	autoremove_args += " " + " ".join(sys.argv[sys.argv.index("-ara") + 1].split(","))

if "--clean-args" in sys.argv:
	clean_args += " " + " ".join(sys.argv[sys.argv.index("--clean-args") + 1].split(","))
elif "-ca" in sys.argv:
	clean_args += " " + " ".join(sys.argv[sys.argv.index("-ca") + 1].split(","))

update_command = "apt-get update"
dist_upgrade_command = "apt-get dist-upgrade"
autoremove_command = "apt-get autoremove"
clean_command = "apt-get clean"

os.system(update_command + " " + update_args)
os.system(dist_upgrade_command + " " + dist_upgrade_args)
os.system(autoremove_command + " " + autoremove_args)
os.system(clean_command + " " + clean_args)
