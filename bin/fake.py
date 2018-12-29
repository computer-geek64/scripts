#!/usr/bin/python3
# fid.py v1.3
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
area_codes = {"Mississippi": [228, 601, 662, 769], "Northern Mariana Islands": [670], "Oklahoma": [405, 539, 580, 918], "Delaware": [302], "Minnesota": [218, 320, 507, 612, 651, 763, 952], "Illinois": [217, 224, 309, 312, 331, 618, 630, 708, 773, 779, 815, 847, 872], "Arkansas": [479, 501, 870], "New Mexico": [505, 575], "Indiana": [219, 260, 317, 574, 765, 812], "Maryland": [240, 301, 410, 443, 667], "Louisiana": [225, 318, 337, 504, 985], "Idaho": [208], "Wyoming": [307], "Tennessee": [423, 615, 731, 865, 901, 931], "Arizona": [480, 520, 602, 623, 928], "Iowa": [319, 515, 563, 641, 712], "Michigan": [231, 248, 269, 313, 517, 586, 616, 734, 810, 906, 947, 989], "Kansas": [316, 620, 785, 913], "Utah": [385, 435, 801], "American Samoa": [684], "Oregon": [458, 503, 541, 971], "Connecticut": [203, 475, 860], "Montana": [406], "California": [209, 213, 310, 323, 408, 415, 424, 442, 510, 530, 559, 562, 619, 626, 650, 657, 661, 669, 707, 714, 747, 760, 805, 818, 831, 858, 909, 916, 925, 949, 951], "Massachusetts": [339, 351, 413, 508, 617, 774, 781, 857, 978], "Puerto Rico": [787, 939], "South Carolina": [803, 843, 864], "New Hampshire": [603], "Wisconsin": [262, 414, 534, 608, 715, 920], "Vermont": [802], "Georgia": [229, 404, 470, 478, 678, 706, 762, 770, 912], "North Dakota": [701], "Pennsylvania": [215, 267, 272, 412, 484, 570, 610, 717, 724, 814, 878], "West Virginia": [304, 681], "Florida": [239, 305, 321, 352, 386, 407, 561, 727, 754, 772, 786, 813, 850, 863, 904, 941, 954], "Hawaii": [808], "Kentucky": [270, 502, 606, 859], "Alaska": [907], "Nebraska": [308, 402, 531], "Missouri": [314, 417, 573, 636, 660, 816], "Ohio": [216, 234, 330, 419, 440, 513, 567, 614, 740, 937], "Alabama": [205, 251, 256, 334, 938], "Rhode Island": [401], "Washington, DC": [202], "Virgin Islands": [340], "South Dakota": [605], "Colorado": [303, 719, 720, 970], "New Jersey": [201, 551, 609, 732, 848, 856, 862, 908, 973], "Virginia": [276, 434, 540, 571, 703, 757, 804], "Guam": [671], "Washington": [206, 253, 360, 425, 509], "North Carolina": [252, 336, 704, 828, 910, 919, 980, 984], "New York": [212, 315, 347, 516, 518, 585, 607, 631, 646, 716, 718, 845, 914, 917, 929], "Texas": [210, 214, 254, 281, 325, 346, 361, 409, 430, 432, 469, 512, 682, 713, 737, 806, 817, 830, 832, 903, 915, 936, 940, 956, 972, 979], "Nevada": [702, 725, 775], "Maine": [207]}

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
# fake["password"] = randomuser["results"][0]["login"]["password"]
fake["password"] = uinames["password"]
fake["street"] = " ".join([x.capitalize() for x in randomuser["results"][0]["location"]["street"].split(" ")])
fake["ssn"] = randomuser["results"][0]["id"]["value"]
fake["name"] = uinames["title"].capitalize() + ". " + uinames["name"] + " " + uinames["surname"]
fake["email"] = uinames["email"].split("@")[0] + "@gmail.com"
fake["credit_card_expiration"] = uinames["credit_card"]["expiration"]
fake["credit_card_number"] = uinames["credit_card"]["number"]
fake["credit_card_pin"] = str(uinames["credit_card"]["pin"])
fake["credit_card_security"] = str(uinames["credit_card"]["security"])

if len(fake["credit_card_number"].replace("-", "")) == 15:
	fake["credit_card_company"] = "American Express"
else:
	if fake["credit_card_number"][0] == "3":
		fake["credit_card_company"] = "American Express"
	elif fake["credit_card_number"][0] == "4":
		fake["credit_card_comapny"] = "Visa"
	elif fake["credit_card_number"][0] == "5":
		fake["credit_card_company"] = "MasterCard"
	elif fake["credit_card_number"][0] == "6":
		fake["credit_card_company"] = "Discover"
	else:
		fake["credit_card_company"] = "Unknown"

locationiq = json.loads(requests.get("https://us1.locationiq.com/v1/search.php?key=a6485e7c311089&format=json&q=" + fake["street"] + ", us").text)

fake["latitude"] = locationiq[0]["lat"]
fake["longitude"] = locationiq[0]["lon"]
fake["city"] = locationiq[0]["display_name"].split(", ")[-5]
fake["county"] = locationiq[0]["display_name"].split(", ")[-4]
fake["state"] = locationiq[0]["display_name"].split(", ")[-3]
fake["zip_code"] = locationiq[0]["display_name"].split(", ")[-2]
fake["country"] = locationiq[0]["display_name"].split(", ")[-1]
possible_area_codes = area_codes[" ".join([x.capitalize() for x in fake["state"].split(" ")])]
fake["phone_number"] = "(" + str(possible_area_codes[int(random() * len(possible_area_codes))]) + ") " + str(int(random() * 900) + 100) + "-" + str(int(random() * 9000) + 1000)

print("Name:\t\t\t" + fake["name"])
print("Age:\t\t\t" + str(fake["age"]))
print("Address:\t\t" + fake["street"])
print("\t\t\t" + fake["city"] + ", " + fake["state"] + " " + fake["zip_code"] + ", " + fake["country"])
print("County:\t\t\t" + fake["county"])
# print("\t\t" + fake["city"] + ", " + fake["county"] + ", " + fake["state"] + " " + fake["zip_code"] + ", " + fake["country"])
print("Location:\t\t" + fake["latitude"] + ", " + fake["longitude"])
if str(fake["birthday"].day)[-1] == "1" and not fake["birthday"].day == 11:
	print("Date of Birth:\t\t" + fake["birthday"].strftime("%B %-dst, %Y"))
elif str(fake["birthday"].day)[-1] == "2" and not fake["birthday"].day == 12:
	print("Date of Birth:\t\t" + fake["birthday"].strftime("%B %-dnd, %Y"))
elif str(fake["birthday"].day)[-1] == "3" and not fake["birthday"].day == 13:
	print("Date of Birth:\t\t" + fake["birthday"].strftime("%B %-drd, %Y"))
else:
	print("Date of Birth:\t\t" + fake["birthday"].strftime("%B %-dth, %Y"))
print("Phone Number:\t\t" + fake["phone_number"])
print("Email:\t\t\t" + fake["email"])
print("Username:\t\t" + fake["username"])
print("Password:\t\t" + fake["password"])
print("Social Security Number:\t" + fake["ssn"])
print("Credit Card Company:\t" + fake["credit_card_company"])
print("Credit Card Number:\t" + fake["credit_card_number"])
print("Credit Card Expiration:\t" + fake["credit_card_expiration"])
print("Credit Card Pin:\t" + fake["credit_card_pin"])
print("Credit Card Security:\t" + fake["credit_card_security"])
