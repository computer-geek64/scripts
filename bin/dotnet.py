#!/usr/bin/python3
# dotnet.py v2.2
# Ashish D'Souza
# December 27th, 2018

try:
	import sys
	import os
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
	print("-h\t\t--help\t\t\tShow this help screen")
	print("-b\t\t--no-banner\t\tSuppress banner")
	print("-d\t\t--developer\t\tDisplay information about developer")

layers = list(map(int, sys.argv[1:-1]))

if len(sys.argv) < 4:
	print_banner()
	print_usage()
	exit(0)

banner = True
usage = False
developer_info = False
image_file = "image.png"

arg = 1
while arg < len(sys.argv):
	if sys.argv[arg] == "-h" or sys.argv[arg] == "--help":
		usage = True
	elif sys.argv[arg] == "-b" or sys.argv[arg] == "--no-banner":
		banner = False
	elif sys.argv[arg] == "-d" or sys.argv[arg] == "--developer":
		developer_info = True
	elif arg == len(sys.argv) - 1:
		image_file = sys.argv[arg] if sys.argv[arg][-4:] == ".png" else sys.argv[arg] + ".png"
	else:
		try:
			int(sys.argv[arg])
		except ValueError:
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

layers_str = ["Input"] + ["Hidden"] * (len(layers) - 2) + ["Output"]
layers_col = ["none"] + ["none"] * (len(layers) - 2) + ["none"]
layers_fill = ["black"] + ["gray"] * (len(layers) - 2) + ["black"]

penwidth = 15
font = "Hilda 10"
output = ""

output += "digraph G {\n"
output += "\tfontname = \"{}\"".format(font) + "\n"
output += "\trankdir=LR\n"
output += "\tsplines=line\n"
output += "\tnodesep=.08;\n"
output += "\tranksep=1;\n"
output += "\tedge [color=black, arrowsize=.5];\n"
output += "\tnode [fixedsize=true,label=\"\",style=filled,color=none,fillcolor=gray,shape=circle]\n\n"

# Clusters
for i in range(0, len(layers)):
    output += ("\tsubgraph cluster_{} {{".format(i)) + "\n"
    output += ("\t\tcolor={};".format(layers_col[i])) + "\n"
    output += ("\t\tnode [style=filled, color=white, penwidth={},fillcolor={} shape=circle];".format(penwidth,layers_fill[i])) + "\n"

    output += "\t\t "

    for a in range(layers[i]):
        output += "l{}{} ".format(i + 1, a) + " "

    output += ";" + "\n"
    output += ("\t\tlabel = {};".format(layers_str[i])) + "\n"

    output += "\t}\n\n"

# Nodes
for i in range(1, len(layers)):
    for a in range(layers[i - 1]):
        for b in range(layers[i]):
            output += "\tl{}{} -> l{}{}".format(i, a, i + 1, b) + "\n"

output += "}\n"

with open(os.path.join(os.getcwd(), "image.txt"), "w") as file:
	file.write(output)
	file.close()
os.system("cat " + os.path.join(os.getcwd(), "image.txt") +  " | dot -T png > " + os.getcwd() + "/" + image_file)
os.system("rm " + os.path.join(os.getcwd(), "image.txt"))
