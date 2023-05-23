import os
import argparse

parser = argparse.ArgumentParser(
	prog="Rug Safe Ape Bot"
	description="This is the executeable for handling the Rug Safe Ape Bot")
#parser.add_argument("-i", "--init", help="Redo the configuration fil")
#parser.add_argument("u","--update", help="Update to latest version")
#parser.add_argument("-r", "--restart", help="Stop and restart the bot")

flag_file = ".flag.txt"

if os.path.exists(flag_file):
	print("This program has been run before")
else: 
	print("First time running the program")
	open(flag_file, "w").close()
