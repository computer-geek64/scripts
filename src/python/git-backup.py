#!/usr/bin/python3
# git-backup v1.2
# Ashish D'Souza
# December 27th, 2018

import os
import git
import requests
import json
import sys


if input("Are you sure you want to delete everything in \"" + os.getcwd() + "\"? Y/N >> ").lower() == "y":
	print("[+] Proceed.")
else:
	print("[!] Abort.")
	exit(0)

os.system("rm -rf *")

if len(sys.argv) == 1:
	json_response = json.loads(requests.get("https://api.github.com/users/computer-geek64/repos").text)
else:
	json_response = json.loads(requests.get("https://api.github.com/users/" + sys.argv[1] + "/repos").text)

repos = [json_response[i]["html_url"] for i in range(len(json_response))]
for repo in repos:
	git.Repo.clone_from(repo, [x for x in repo.split("/") if x][-1])
