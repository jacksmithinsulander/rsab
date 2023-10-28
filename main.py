#!/home/debian/rsab/.rsab_venv/bin/python3

from modules.scanner.scanner_main import Scanner
from modules.setup.setup import conf_checker
from modules.ta.ta_iterate import iterate as iterate_ta
from modules.fa.fa_iterate import iterate as iterate_fa
from time import sleep
from web3 import Web3
import db.main as db
from web3.middleware import geth_poa_middleware
from datetime import datetime
import subprocess
import json
import argparse
import os
from loguru import logger
import sys


def in_venv():
    return sys.prefix != sys.base_prefix


if not in_venv():
    logger.error("NOT IN VENV")
    logger.info("Please start this script in a virtual environment")
    logger.info("Exiting")
    exit()


def start_bot():
    subprocess.run(["make", "start"])


def start_scanner():
    scanner = Scanner()
    scanner.start()


parser = argparse.ArgumentParser(
    prog="Rug Safe Ape Bot",
    description="This is the executeable for handling the Rug Safe Ape Bot")

parser.add_argument(
    "-i", "--init", action="store_true", help="Redo the configuration file"
)
# parser.add_argument("-u", "--update", help="Update to latest version")
# parser.add_argument("-r", "--restart", help="Stop and restart the bot")
# parser.add_argument("-f", "--flagRemoval", help="Removes the record flag")
parser.add_argument(
    "-fs", "--fa_scan", action="store_true", help="Do the FA scan")
parser.add_argument(
    "-ts", "--ta_scan", action="store_true", help="Do the TA scan")
# parser.add_argument("-s","--start", help="Start the bot")
parser.add_argument(
    "-fe", "--fetch", action="store_true", help="Perform new scan to fetch tokens")
parser.add_argument(
    "-t", "--test", action="store_true", help="Temporary dev test")

args = parser.parse_args()

logger.debug(args)

flag_file = ".flag.txt"
conf_file_exist = os.path.isfile("./conf.json")

if conf_file_exist:
    with open('conf.json', "r") as file:
        conf = json.load(file)
    logger.add(conf['logger']['file'], rotation=conf['logger']['sizeLimit'])
    logger.debug(
        f"Saving logs to {conf['logger']['file']} with limit set to {conf['logger']['sizeLimit']}")


def mainfunc():
    if os.path.exists(flag_file):
        logger.info("This program has been run before")
    else:
        logger.info("First time running the program")
        conf_checker(conf_file_exist, 0)
        logger.info("Setup successful, ")
        start_bot = input("Do you want to start the bot? (Y / N)")
        if start_bot == "Y":
            logger.info("Starting bot...")
            start_bot()
        elif start_bot == "N":
            logger.info(
                "Alrighty, you can start the bot at anytime now using the -s flag")
        else:
            logger.info("Sorry, didn't understant the input, retry please")
            return mainfunc()
        open(flag_file, "w").close()


if args.fetch:
    logger.debug("Starting start_scanner")
    start_scanner()
elif args.fa_scan:
    logger.debug("Starting iterate_fa")
    iterate_fa()
elif args.ta_scan:
    logger.debug("Starting iterate_ta")
    iterate_ta()
