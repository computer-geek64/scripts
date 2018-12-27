#!/usr/bin/python3
# pomodoro.py v2.2
# Ashish D'Souza
# December 26th, 2018

try:
	import os
	import sys
	import requests
	import keyboard
	import time
	import notify2
	from datetime import datetime
except ImportError:
	print("[-] Installing dependencies...")
	if os.system("pip install --upgrade requests datetime keyboard notify2; pip3 install --upgrade requests datetime keyboard notify2") == 0:
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
notify2.init("Pomodoro")

def print_banner():
	print(name + " v" + str(version))
	print("Copyright " + str(datetime.now().year) + " " + developer + ". " + rights + "\n")

def print_usage():
	print("Usage: " + name + " [options]\n")
	print("Option\t\tLong Option\t\tDescription")
	print("-h\t\t--help\t\t\tShow this help screen")
	print("-b\t\t--no-banner\t\tSuppress banner")
	print("-d\t\t--developer\t\tDisplay information about developer")
	print("-P\t\t--pomodoros\t\tSpecify pomodoro count")
	print("-p\t\t--pomodoro-length\tSpecify pomodoro length (minutes)")
	print("-s\t\t--short-break\t\tSpecify short break length (minutes)")
	print("-l\t\t--long-break\t\tSpecify long break length (minutes)")
	print("-t\t\t--task\t\t\tSpecify task to complete (default is \"pomodoro\")")

class Timer:
	def __init__(self, limit):
		self.elapsed_time = 0
		self.start_time = 0
		self.time_limit = limit
		self.paused = False

	def start(self):
		keyboard.add_hotkey("ctrl+alt+space", self.pause)
		self.start_time = time.time()
		while self.elapsed_time < self.time_limit:
			time.sleep(5)
			if not self.paused:
				self.elapsed_time = time.time() - self.start_time
		self.stop()

	def pause(self):
		if self.paused:
			self.paused = False
			self.start_time = time.time() - self.elapsed_time
			minutes = round(self.elapsed_time / 60)
			minutes = str(minutes)
			seconds = round(self.elapsed_time % 60)
			seconds = str(seconds) if seconds > 9 else "0" + str(seconds)
			print("Resumed at " + minutes + ":" + seconds)
			notify2.Notification("Pomodoro Timer", "Resumed at " + str(minutes) + ":" + str(seconds)).show()
		else:
			self.paused = True
			self.elapsed_time = time.time() - self.start_time
			minutes = round(self.elapsed_time / 60)
			minutes = str(minutes)
			seconds = round(self.elapsed_time % 60)
			seconds = str(seconds) if seconds > 9 else "0" + str(seconds)
			print("Paused at " + minutes + ":" + seconds)
			notify2.Notification("Pomodoro Timer", "Paused at " + str(minutes) + ":" + str(seconds)).show()

	def stop(self):
		keyboard.unhook_all()

banner = True
usage = False
developer_info = False
pomodoros = 3
pomodoro_length = 8
short_break_length = 3
long_break_length = 5
task = "Pomodoro"

arg = 1
while arg < len(sys.argv):
	if sys.argv[arg] == "-h" or sys.argv[arg] == "--help":
		usage = True
	elif sys.argv[arg] == "-d" or sys.argv[arg] == "--developer":
		developer_info = True
	elif sys.argv[arg] == "-b" or sys.argv[arg] == "--no-banner":
		banner = False
	elif sys.argv[arg] == "-P" or sys.argv[arg] == "--pomodoros":
		arg += 1
		pomodoros = int(sys.argv[arg])
	elif sys.argv[arg] == "-p" or sys.argv[arg] == "--pomodoro-length":
		arg += 1
		pomodoro_length = int(sys.argv[arg])
	elif sys.argv[arg] == "-s" or sys.argv[arg] == "--short-break":
		arg += 1
		short_break_length = int(sys.argv[arg])
	elif sys.argv[arg] == "-l" or sys.argv[arg] == "--long-break":
		arg += 1
		long_break_length = int(sys.argv[arg])
	elif sys.argv[arg] == "-t" or sys.argv[arg] == "--task":
		arg += 1
		task = sys.argv[arg]
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

for i in range(pomodoros):
	print(task + " for " + str(pomodoro_length))
	notify2.Notification("Pomodoro Timer", task + " for " + str(pomodoro_length) + " minutes").show()
	Timer(pomodoro_length * 60).start()
	if i == pomodoros - 1:
		print("Long break for " + str(long_break_length) + " minutes")
		notify2.Notification("Pomodoro Timer", "Long break for " + str(long_break_length) + " minutes").show()
		Timer(long_break_length * 60).start()
		break
	print("Short break for " + str(short_break_length))
	notify2.Notification("Pomodoro Timer", "Short break for " + str(short_break_length) + " minutes").show()
	Timer(short_break_length * 60).start()
print(task + " finished!")
notify2.Notification("Pomodoro Timer", task + " finished!").show()
