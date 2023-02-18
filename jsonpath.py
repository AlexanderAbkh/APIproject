import requests
import os
import json
from jsonpath_ng.ext import parse


CURR_DIR = os.path.dirname(os.path.realpath(__file__))  # path to dir
TEST_FILE = str(CURR_DIR) + '\\test.json'  # concetinate to json file

with open(TEST_FILE) as test_json:
    info = json.load(test_json)  # load the data from json

parsed_age = parse("$.Europe[0].Italy[0]")  # jsonpath defining
print(parsed_age)

def parsing_age():
    for match in parsed_age.find(info):
        return match.value  # parse the data by jsonpath

parsed_value = parsing_age()

print(parsed_value)

#