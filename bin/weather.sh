#!/bin/bash
# weather.sh 1.2
# Ashish D'Souza
# December 25th, 2018

name="${0##*/}"
version="1.2"
date=$(date)
developer="Ashish D'Souza"
developer_info_url="https://computer-geek64.github.io/info"
rights="All rights reserved."

print_banner() {
	if [[ $1 == true || $# -eq 0 ]]; then
		echo "${name} v${version}"
		echo "Copyright ${date##* } ${developer}. ${rights}"
		echo
	fi
}

print_usage() {
	echo -e "Usage: ${name} [options]\n"
	echo -e "Option\t\tLong Option\t\tDescription"
	echo -e "-h\t\t--help\t\t\tShow this help screen"
	echo -e "-b\t\t--no-banner\t\tSuppress banner"
	echo -e "-d\t\t--developer\t\tDisplay information about developer"
	echo -e "-l\t\t--location\t\tSet location (city, state, country, zip code, area code, GPS coordinates)"
	echo -e "-c\t\t--color\t\t\tColorize output"
	echo -e "-t\t\t--time\t\t\tDisplay time (0 is current weather, 1-2 are days)"
	echo -e "-n\t\t--narrow\t\t\tSet narrow format (only noon and nighttime weather)"
}

if [[ -z $(dpkg -l | grep " curl ") ]]; then
	print_banner
	echo '[-] Installing dependencies...'
	apt-get update --fix-missing -y > /dev/null
	apt-get install curl -y > /dev/null
	apt-get autoremove -y > /dev/null
	apt-get clean -y > /dev/null
	if [[ ! $(dpkg --get-selections curl | grep -i "no packages found") ]]; then
		echo '[+] Dependencies successfully installed.'
	else
		echo '[!] Dependency installation failed. Script restart required.'
	fi
	exit
fi

banner=true
location=""
color=false
timespan=""
narrow=false

while [[ ! -z $1 ]]; do
	case $1 in
		-h|--help)
			print_banner
			print_usage
			exit
			;;
		-b|--no-banner)
			banner=false
			;;
		-d|--developer)
			print_banner
			curl $developer_info_url
			exit
			;;
		-l|--location)
			shift
			location=$1
			;;
		-c|--color)
			color=true
			;;
		-t|--time)
			shift
			timespan="${1}"
			;;
		-n|--narrow)
			narrow=true
			;;
		*)
			echo -e "Unrecognized option: ${1}\n"
			print_usage
			exit
			;;
	esac
	shift
done

print_banner $banner

command="curl wttr.in"

if [[ ! -z $location ]]; then
	command="${command}/${location}"
fi

if [[ $color == false ]]; then
	command="${command}?T"
fi

if [[ ! -z $timespan ]]; then
	command="${command}?${timespan}"
fi

if [[ $narrow == true ]]; then
	command="${command}?n"
fi

$command
