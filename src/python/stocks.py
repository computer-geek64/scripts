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
	print("$" + requests.get("https://api.iextrading.com/1.0/stock/" + stock + "/price").text)

if company:
	company_json = json.loads(requests.get("https://api.iextrading.com/1.0/stock/" + stock + "/company").text)
	stock = company_json["symbol"]
	company_name = company_json["companyName"]
	exchange = company_json["exchange"]
	industry = company_json["industry"]
	website = company_json["website"]
	description = company_json["description"]
	ceo = company_json["CEO"]
	issue_type = company_json["issueType"]
	company_sector = company_json["sector"]
	tags = ", ".join(company_json["tags"])
#	print("Company:\t" + company_name + " (" + stock + ")")
#	print("Exchange:\t" + exchange)
#	print("Industry:\t" + industry)
#	print("Website:\t" + website)
#	print("Description:\t" + description)
#	print("CEO:\t\t" + ceo)
#	print("Issue Type:\t" + issue_type)
#	print("Sector:\t\t" + company_sector)
#	print("Tags:\t\t" + tags)
	print(company_name + " (" + stock + ")")
	print("CEO: " + ceo)
	print(website)
	print(exchange)
	print(company_sector + " Sector, " + industry + " Industry")
	print(description)

if relevant:
	relevant_json = json.loads(requests.get("https://api.iextrading.com/1.0/stock/" + stock + "/relevant").text)
	print("Relevant: " + ", ".join(relevant_json["symbols"]))

if sector_performance:
	sector_performance_json = json.loads(requests.get("https://api.iextrading.com/1.0/stock/market/sector-performance").text)
	for sector in sector_performance_json:
		print("Sector:\t\t" + sector["name"])
		print("Performance:\t" + str(sector["performance"]))
		print("Updated:\t" + datetime.fromtimestamp(int(sector["lastUpdated"] / 1000)).strftime("%c") + "\n" * int(sector != sector_performance_json[-1]))

sys.exit(0)
