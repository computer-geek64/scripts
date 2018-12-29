#!/usr/bin/python3
# pomodoro.py v2.5
# Ashish D'Souza
# December 29th, 2018

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
	else:
		print("[!] Dependency installation failed. Script restart required.")
	sys.exit(0)

name = os.path.split(sys.argv[0])[-1]
version = 2.5
developer = "Ashish D'Souza"
developer_info_url = "https://computer-geek64.github.io/info"
rights = "All rights reserved."
notify2.init("Pomodoro")
exit_all = False

def print_banner():
	print(name + " v" + str(version))
	print("Copyright " + str(datetime.now().year) + " " + developer + ". " + rights + "\n")

def print_usage():
	print("Usage: " + name + " [options]\n")
	print("Option\t\tLong Option\t\tDescription")
	print("-h\t\t--help\t\t\tShow this help screen")
	print("-b\t\t--no-banner\t\tSuppress banner")
	print("-d\t\t--developer\t\tDisplay information about developer")
	print("-P\t\t--pomodoros\t\tSpecify pomodoro count (default is 4)")
	print("-p\t\t--pomodoro-length\tSpecify pomodoro length (minutes, default is 12)")
	print("-s\t\t--short-break\t\tSpecify short break length (minutes, default is 3)")
	print("-l\t\t--long-break\t\tSpecify long break length (minutes, default is 8)")
	print("-t\t\t--task\t\t\tSpecify task to complete (default is \"pomodoro\")")
	print("-u\t\t--update\t\tSpecify update interval (seconds, default is 1)")
	print("-w\t\t--workspace\t\tSwitch workspaces")
	print("-S\t\t--screensaver\t\tEmploy screensaver")

class Timer:
	def __init__(self, limit, task_name):
		self.elapsed_time = 0
		self.start_time = 0
		self.time_limit = limit
		self.task = task_name
		self.paused = False
		self.output_base = self.task + " " * 10

	def start(self, update_interval):
		keyboard.add_hotkey("ctrl+alt+space", self.pause)
		keyboard.add_hotkey("ctrl+alt+x", self.stop, args=(True,))
		keyboard.add_hotkey("ctrl+alt+s", self.status)
		self.start_time = time.time()
		print()
		while self.elapsed_time < self.time_limit:
			if exit_all:
				sys.exit(0)
			if not self.paused:
				self.elapsed_time = time.time() - self.start_time
				minutes = str(int(self.elapsed_time / 60))
				minutes = "0" * (2 - len(minutes)) + minutes
				seconds = str(int(self.elapsed_time % 60))
				seconds = "0" * (2 - len(seconds)) + seconds
				percentage = int(100 * self.elapsed_time / self.time_limit)
				print("\033[A" + self.output_base + " " * (3 - len(str(percentage))) + str(percentage) + "% [" + "=" * percentage + ">" + " " * (100 - percentage) + "] " + minutes + ":" + seconds)
			time.sleep(1)
		self.stop()

	def pause(self):
		if self.paused:
			self.paused = False
			self.start_time = time.time() - self.elapsed_time
			minutes = str(int(self.elapsed_time / 60))
			minutes = "0" * (2 - len(minutes)) + minutes
			seconds = str(int(self.elapsed_time % 60))
			seconds = "0" * (2 - len(seconds)) + seconds
			percentage = int(100 * self.elapsed_time / self.time_limit)
			print("\033[A" + self.output_base + " " * (3 - len(str(percentage))) + str(percentage) + "% [" + "=" * percentage + ">" + " " * (100 - percentage) + "] " + minutes + ":" + seconds)
			notify2.Notification("Pomodoro Timer", "Resumed at " + minutes + ":" + seconds).show()
		else:
			self.paused = True
			self.elapsed_time = time.time() - self.start_time
			minutes = str(int(self.elapsed_time / 60))
			minutes = "0" * (2 - len(minutes)) + minutes
			seconds = str(int(self.elapsed_time % 60))
			seconds = "0" * (2 - len(seconds)) + seconds
			percentage = int(100 * self.elapsed_time / self.time_limit)
			print("\033[A" + self.task + " (Paused) " + " " * (3 - len(str(percentage))) + str(percentage) + "% [" + "=" * percentage + ">" + " " * (100 - percentage) + "] " + minutes + ":" + seconds)
			notify2.Notification("Pomodoro Timer", "Paused at " + minutes + ":" + seconds).show()

	def status(self):
		self.elapsed_time = time.time() - self.start_time
		minutes = str(int(self.elapsed_time / 60))
		minutes = "0" * (2 - len(minutes)) + minutes
		seconds = str(int(self.elapsed_time % 60))
		seconds = "0" * (2 - len(seconds)) + seconds
		percentage = int(100 * self.elapsed_time / self.time_limit)
		notify2.Notification("Pomodoro Timer", " ".join([x for x in self.task.split(" ") if x]) + " at " + minutes + ":" + seconds + " (" + str(percentage) + "%)").show()

	def stop(self, stop=False):
		keyboard.unhook_all()
		if stop:
			global exit_all
			exit_all = True
			sys.exit(0)

banner = True
usage = False
developer_info = False
pomodoros = 4
pomodoro_length = 12 # 25 for longer session
short_break_length = 3 # 5 for longer session
long_break_length = 8 # 15 for longer session
task = "Pomodoro"
timer_update_interval = 1
workspace = False
screensaver = False

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
	elif sys.argv[arg] == "-u" or sys.argv[arg] == "--update":
		arg += 1
		timer_update_interval = int(sys.argv[arg])
	elif sys.argv[arg] == "-w" or sys.argv[arg] == "--workspace":
		workspace = True
	elif sys.argv[arg] == "-S" or sys.argv[arg] == "--screensaver":
		screensaver = True
	else:
		usage = True
	arg += 1

if banner:
	print_banner()

if usage:
	print_usage()
	sys.exit(0)

if developer_info:
	print(requests.get(developer_info_url).text)
	sys.exit(0)

for i in range(pomodoros):
	spacing = max(len(task), len("Short break"), len("Long break"))
	notify2.Notification("Pomodoro Timer", task + " for " + str(pomodoro_length) + " minutes").show()
	time.sleep(3)
	if workspace:
		os.system("wmctrl -s 0")
	if screensaver:
		os.system("gnome-screensaver-command -a")
		time.sleep(1)
		os.system("gnome-screensaver-command -d")
	Timer(pomodoro_length * 60, task + " " * (spacing - len(task))).start(timer_update_interval)
	if i == pomodoros - 1:
		notify2.Notification("Pomodoro Timer", "Long break for " + str(long_break_length) + " minutes").show()
		time.sleep(3)
		if workspace:
			os.system("wmctrl -s 1")
		if screensaver:
			os.system("gnome-screensaver-command -a")
			time.sleep(1)
			os.system("gnome-screensaver-command -d")
		Timer(long_break_length * 60, "Long break" + " " * (spacing - len("Long break"))).start(timer_update_interval)
		break
	notify2.Notification("Pomodoro Timer", "Short break for " + str(short_break_length) + " minutes").show()
	time.sleep(3)
	if workspace:
		os.system("wmctrl -s 1")
	if screensaver:
		os.system("gnome-screensaver-command -a")
		time.sleep(1)
		os.system("gnome-screensaver-command -d")
	Timer(short_break_length * 60, "Short break" + " " * (spacing - len("Short break"))).start(timer_update_interval)
print(task + " finished!")
notify2.Notification("Pomodoro Timer", task + " finished!").show()
sys.exit(0)
