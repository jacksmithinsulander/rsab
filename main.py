import os
import argparse
import json
from modules.setup.setup import conf_checker

parser = argparse.ArgumentParser(
	prog="Rug Safe Ape Bot",
	description="This is the executeable for handling the Rug Safe Ape Bot")
#parser.add_argument("-i", "--init", help="Redo the configuration fil")
#parser.add_argument("-u","--update", help="Update to latest version")
#parser.add_argument("-r", "--restart", help="Stop and restart the bot")
#parser.add_argument("-f","--flagRemoval", help="Removes the record flag")

flag_file = ".flag.txt"
check_file = os.path.isfile("./conf.json")

if os.path.exists(flag_file):
	print("This program has been run before")
else: 
	print("First time running the program")
	conf_checker(check_file, 0)
	open(flag_file, "w").close()
