#!/usr/bin/python3
# git-backup v1.3
# Ashish D'Souza
# December 27th, 2018

try:
	import os
	import git
	import requests
	import json
	import sys
	from datetime import datetime
except ImportError:
	print("[-] Installing dependencies...")
	if os.system("pip install --upgrade requests datetime git; pip3 install --upgrade requests datetime git") == 0:
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
	print("-y\t\t--yes\t\t\tDo not ask for confirmation (batch mode)")
	print("-p [path]\t--path [path]\t\tSpecify git backup path (default is current working directory)")
	print("-u [username]\t--user [username]\tSpecify user for git backup (default is developer: @computer-geek64)")
	print("-P [file]\t--private [file]\tSpecify private repositories in [file]")

banner = True
usage = False
developer_info = False
confirm = True
path = os.getcwd()
user = "computer-geek64"
private_repositories = ""

arg = 1
while arg < len(sys.argv):
	if sys.argv[arg] == "-h" or sys.argv[arg] == "--help":
		usage = True
	elif sys.argv[arg] == "-b" or sys.argv[arg] == "--no-banner":
		banner = False
	elif sys.argv[arg] == "-d" or sys.argv[arg] == "--developer":
		developer_info = True
	elif sys.argv[arg] == "-y" or sys.argv[arg] == "--yes":
		confirm = False
	elif sys.argv[arg] == "-p" or sys.argv[arg] == "--path":
		arg += 1
		path = sys.argv[arg]
		os.chdir(path)
	elif sys.argv[arg] == "-u" or sys.argv[arg] == "--user":
		arg += 1
		user = sys.argv[arg]
	elif sys.argv[arg] == "-P" or sys.argv[arg] == "--private":
		arg += 1
		private_repositories = sys.argv[arg]
	else:
		usage = True
	arg += 1

if banner:
	print_banner()

if usage:
	print_usage()
	exit(0)

if developer_info:
	print(requests.get(developer_info_url).text)
	exit(0)

if confirm:
	if input("Are you sure you want to delete everything in \"" + os.getcwd() + "\"? Y/N >> ").lower() == "y":
		print("[+] Proceed.")
	else:
		print("[!] Abort.")
		exit(0)
# Clean directory
os.system("rm -rf *")

# Get repositories JSON response from GitHub API
json_response = json.loads(requests.get("https://" + user + "@api.github.com/users/" + user.split(":")[0] + "/repos").text)

# Exctract and clone repositories
repos = [json_response[i]["html_url"] for i in range(len(json_response))]
for repo in repos:
	git.Repo.clone_from(repo.replace("://", "://" + user + "@"), [x for x in repo.split("/") if x][-1])

# Extract and clone private repositories
if len(private_repositories) > 0:
	with open(private_repositories, "r") as file:
		lines = file.readlines()
		file.close()
	for line in lines:
		git.Repo.clone_from("https://" + user + "@github.com/" + user.split(":")[0] + "/" + line.strip(), line.strip())
