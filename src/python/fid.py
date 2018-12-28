#!/usr/bin/python3
# fid.py v1.1
# Ashish D'Souza
# December 28th, 2018

try:
	import os
	import sys
	import requests
	import json
	from datetime import datetime
	from random import random
except ImportError:
	print("[-] Installing dependencies...")
	if os.system("pip install --upgrade requests datetime; pip3 install --upgrade requests datetime") == 0:
		print("[+] Dependencies successfully installed.")
	else:
		print("[!] Dependency installation failed.")
	print("Script restart required.")
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
	print("-g [gender]\t--gender [gender]\tSpecify gender of fake profile (m/f, male/female)")
	print("-a [age]\t--age [age]\t\tSpecify age of fake profile (default is random)")

banner = True
usage = False
developer_info = False
gender = ""
age = datetime.now().year - 2000

arg = 1
while arg < len(sys.argv):
	if sys.argv[arg] == "-h" or sys.argv[arg] == "--help":
		usage = True
	elif sys.argv[arg] == "-b" or sys.argv[arg] == "--no-banner":
		banner = False
	elif sys.argv[arg] == "-d" or sys.argv[arg] == "--developer":
		developer_info = True
	elif sys.argv[arg] == "-g" or sys.argv[arg] == "--gender":
		arg += 1
		if sys.argv[arg] == "m" or sys.argv[arg] == "male":
			gender = "&gender=male"
		elif sys.argv[arg] == "f" or sys.argv[arg] == "female":
			gender = "&gender=female"
		else:
			usage = True
	elif sys.argv[arg] == "-a" or sys.argv[arg] == "--age":
		arg += 1
		try:
			age = int(sys.argv[arg])
		except ValueError:
			usage = True
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

fake = {"age": age, "birthday": datetime(datetime.now().year - age, int(random() * datetime.now().month) + 1, int(random() * datetime.now().day) + 1)}
randomuser = json.loads(requests.get("https://randomuser.me/api/?noinfo&nat=us" + gender).text)
uinames = json.loads(requests.get("https://uinames.com/api/?ext&region=united states" + gender).text)

fake["gender"] = randomuser["results"][0]["gender"].capitalize()
fake["login"] = randomuser["results"][0]["login"]
fake["username"] = randomuser["results"][0]["login"]["username"]
fake["password"] = randomuser["results"][0]["login"]["password"]
fake["street"] = " ".join([x.capitalize() for x in randomuser["results"][0]["location"]["street"].split(" ")])
fake["ssn"] = randomuser["results"][0]["id"]["value"]
fake["name"] = uinames["title"].capitalize() + ". " + uinames["name"] + " " + uinames["surname"]
fake["email"] = uinames["email"].split("@")[0] + "@gmail.com"
fake["credit_card"] = uinames["credit_card"]

locationiq = json.loads(requests.get("https://us1.locationiq.com/v1/search.php?key=a6485e7c311089&format=json&q=" + fake["street"] + ", us").text)

fake["latitude"] = locationiq[0]["lat"]
fake["longitude"] = locationiq[0]["lon"]
fake["city"] = locationiq[0]["display_name"].split(", ")[-5]
fake["county"] = locationiq[0]["display_name"].split(", ")[-4]
fake["state"] = locationiq[0]["display_name"].split(", ")[-3]
fake["zip_code"] = locationiq[0]["display_name"].split(", ")[-2]
fake["country"] = locationiq[0]["display_name"].split(", ")[-1]

print("Physical identity:")
print(fake["name"] + ", " + str(fake["age"]))
print(fake["street"])
print(fake["city"] + ", " + fake["state"] + " " + fake["zip_code"] + ", " + fake["country"])
# print(fake["city"] + ", " + fake["county"] + ", " + fake["state"] + " " + fake["zip_code"] + ", " + fake["country"])
print("Latitude: " + fake["latitude"])
print("Longitude: " + fake["longitude"])
print("Date of Birth: " + fake["birthday"].strftime("%B %-d, %Y"))

print("\nDigital identity:")
print(fake["email"])
print("Username: " + fake["username"])
print("Password: " + fake["password"])
print("Social Security Number: " + fake["ssn"])
print("Credit Card: " + str(fake["credit_card"]))
