from random import randint
import os
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
grandparent_dir = os.path.abspath(os.path.join(parent_dir, os.pardir))

config_file_path = os.path.join(grandparent_dir, 'conf.json')

with open(config_file_path, "r") as file:
    conf = json.load(file)

profit_target = conf["profitTargets"]
print(profit_target)

mock_price = randint(100, 999)/100.00
#mock_price = 7

def transform_percentage(percentage_gains):
    number = 1 + (percentage_gains / 100)
    return number

print("The mock price is " + str(mock_price))

def generate_tps(buyin_price, percentage_gains):
	for i in range (10):
		print(transform_percentage(percentage_gains) ** (i + 1) * buyin_price)

generate_tps(mock_price, profit_target)
