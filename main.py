#!/home/debian/rsab/.rsab_venv/bin/python3

import os
import argparse
import json
import subprocess
from datetime import datetime
from web3.middleware import geth_poa_middleware
import db.main as db
from web3 import Web3
from time import sleep

from modules.fa.fa_iterate import iterate
from modules.setup.setup import conf_checker
from modules.scanner.scanner_main import Scanner
from modules.calculation.price_fetch import ta_scanner

scanner = Scanner()

def start_bot():
	subprocess.run(["make", "start"])

def start_scanner():
	scanner.start()

parser = argparse.ArgumentParser(
	prog="Rug Safe Ape Bot",
	description="This is the executeable for handling the Rug Safe Ape Bot")

parser.add_argument(
	"-i", "--init", action="store_true", help="Redo the configuration file"
	)
#parser.add_argument("-u", "--update", help="Update to latest version")
#parser.add_argument("-r", "--restart", help="Stop and restart the bot")
#parser.add_argument("-f", "--flagRemoval", help="Removes the record flag")
parser.add_argument(
	"-fs", "--fa_scan", action="store_true", help="Do the FA scan")
parser.add_argument(
	"-ts","--ta_scan", action="store_true", help="Do the TA scan")
#parser.add_argument("-s","--start", help="Start the bot")
parser.add_argument(
	"-fe", "--fetch", action="store_true", help="Perform new scan to fetch tokens")
parser.add_argument(
	"-t", "--test", action="store_true", help="Temporary dev test")

args = parser.parse_args()

print(args)

flag_file = ".flag.txt"
check_file = os.path.isfile("./conf.json")

def mainfunc():
	if os.path.exists(flag_file):
		print("This program has been run before")
	else: 
		print("First time running the program")
		conf_checker(check_file, 0)
		print("Setup successful, ")
		start_bot = input("Do you want to start the bot? (Y / N)")
		if start_bot == "Y":
			print("Starting bot...")
			start_bot()
		elif start_bot == "N":
			print("Alrighty, you can start the bot at anytime now using the -s flag")
		else:
			print("Sorry, didn't understant the input, retry please")
			return mainfunc()
		open(flag_file, "w").close()

if args.fetch:
	start_scanner()
elif args.fa_scan:
	iterate()
elif args.ta_scan:
