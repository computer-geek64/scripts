#!/usr/bin/python3
# stocks.py v1.0
# Ashish D'Souza
# December 29th, 2018

try:
	import os
	import sys
	import json
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
	print("Usage: " + name + " [options] [stock]\n")
	print("Option\t\tLong Option\t\tDescription")
	print("-h\t\t--help\t\t\tShow this help screen")
	print("-b\t\t--no-banner\t\tSuppress banner")
	print("-d\t\t--developer\t\tDisplay information about developer")
	print("-q\t\t--quote [stock]\t\tGet quote for stock")
	print("-p\t\t--price [stock]\t\tGet latest price for stock")
	# print("-c\t\t--chart [stock]\t\tGet price chart for past month")
	print("-c\t\t--company [stock]\tGet information about company")
	print("-r\t\t--relevant [stock]\tGet relevant market symbols")
	print("-s\t\t--sectors\t\tGet sector performances")

banner = True
usage = False
developer_info = False
stock = ""
quote = False
price = False
company = False
relevant = False
sector_performance = False

arg = 1
while arg < len(sys.argv):
	if sys.argv[arg] == "-h" or sys.argv[arg] == "--help":
		usage = True
	elif sys.argv[arg] == "-b" or sys.argv[arg] == "--no-banner":
		banner = False
	elif sys.argv[arg] == "-d" or sys.argv[arg] == "--developer":
		developer_info = True
	elif sys.argv[arg] == "-q" or sys.argv[arg] == "--quote":
		stock = sys.argv[-1]
		quote = True
	elif sys.argv[arg] == "-p" or sys.argv[arg] == "--price":
		stock = sys.argv[-1]
		price = True
	elif sys.argv[arg] == "-c" or sys.argv[arg] == "--company":
		stock = sys.argv[-1]
		company = True
	elif sys.argv[arg] == "-r" or sys.argv[arg] == "--relevant":
		stock = sys.argv[-1]
		relevant = True
	elif sys.argv[arg] == "-s" or sys.argv[arg] == "--sector":
		sector_performance = True
	else:
		if not arg == len(sys.argv) - 1:
			usage = True
	arg += 1

if stock == "" and not sector_performance:
	usage = True

if banner:
	print_banner()

if usage:
	print_usage()
	sys.exit(0)

if developer_info:
	print(requests.get(developer_info_url).text)
	sys.exit(0)

if quote:
	print(json.loads(requests.get("https://api.iextrading.com/1.0/stock/" + stock + "/quote").text))

if price:
	print(json.loads(requests.get("https://api.iextrading.com/1.0/stock/" + stock + "/price").text))

if company:
	print(json.loads(requests.get("https://api.iextrading.com/1.0/stock/" + stock + "/company").text))

if relevant:
	print(json.loads(requests.get("https://api.iextrading.com/1.0/stock/" + stock + "/relevant").text))

if sector_performance:
	print(json.loads(requests.get("https://api.iextrading.com/1.0/stock/market/sector-performance").text))

sys.exit(0)
