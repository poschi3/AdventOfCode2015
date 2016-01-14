import json
from pprint import pprint

with open('input.txt') as data_file:
    data = json.load(data_file)

def getSum(json):
    if type(json) is dict:
        return sumObject(json)
    elif type(json) is list:
        return sumArray(json)
    elif type(json) is int:
        return int(json)
    else:
        return 0


def sumObject(obj):
    sum = 0
    for key, value in obj.items():
        sum += getSum(value)
        if value == "red":
            return 0
    return sum

def sumArray(arr):
    sum = 0
    for value in arr:
        sum += getSum(value)
    return sum

print("Total. " + str(getSum(data)))