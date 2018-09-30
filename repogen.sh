#!/usr/bin/env bash
# This script launches Readme generator with values defined in .env

# print_help - prints help messages
# @1 ["long"] prints long description, otherwise prints usage only
function print_help {
	if [ "$1" = "long" ]; then
		echo -e "Readme generator v0.3.0"
		echo -e "Automates creation of your projects, fellow-holbie\n"
		echo -e "AUTHORS:"

		while read line
		do
			echo -e "\t$line"
		done < ./AUTHORS

		echo -e "\t"
		echo -e "Usage:"
		echo -e "  repogen.sh <url> [-key -key ...], e.g. repo_gen.sh https://intranet.hbtn.io/projects/210\n"
		echo -e "  -h --help		displays this help and exit"
		echo -e "  -v --version  	outputs version information and exit"
		echo -e "     --readme-only	generates only folder and README.md"
		echo -e "     --all		loops throug the file 'projects.list' of this repo,"
		echo -e "			and generates folder, README.md and other files"
	else
		echo -e "Usage:"
		echo -e "  repogen.sh <url> [-key -key ...], e.g. repo_gen.sh https://intranet.hbtn.io/projects/210"
		echo -e "  repogen.sh --help for more instructions"
	fi
}

if [[ -z "$1" ]]; then
	echo -e "[Error]: no arguments found. Minimum one positional argument is requred."
	print_help 'short'
	exit 1
else
	if [ "$1" = "-h" ] || [ "$1" = "--help" ]; then
		print_help 'long'
		exit 0
	elif [ "$1" = "-v" ] || [ "$1" = "--version" ]; then
		echo -e "Readme generator: v.0.3.0"
		exit 0
	fi

	# exports all variables from .env to the current scope
	export $(egrep -v '^#' .env | xargs)

	# if virtualenvwrapper is not instaled
	if [ ! -f /usr/local/bin/virtualenvwrapper.sh ]; then
		# runs repo_gen.py without virtual environment
		echo -e "virtualenvwrapper.sh not found, running script within a default context.\n"
		python3 ./repo_gen.py "$@"
	else
		# tries to use the `repo_generator` virtual environment
		echo -e "virtualenvwrapper.sh found, trying to run script within the context of the 'repo_generator' virtual environment.\n"
		source /usr/local/bin/virtualenvwrapper.sh
		workon repo_generator
		# runs repo_generator within the virtual environment
		python ./repo_gen.py "$@"
	fi
fi
