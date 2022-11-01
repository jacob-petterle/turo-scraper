
# Sets the shell environment to bash
SHELL := /bin/bash

# Creates virtual environment in current working directory
venv:
	python3 -m venv venv


# Delete virtual environment in current working directory
venv-delete:
	sudo rm -r venv