# Created by Admin at 1/16/2022
import csv
import pprint

with open('buzzers.csv') as data:
    for line in csv.reader(data):
        print(line)

with open('buzzers.csv') as data:
    for line in csv.DictReader(data):
        print(line)

with open('buzzers.csv') as data:
    ignore = data.readline()
    flights = {}
    for line in data:
        k, v = line.strip().split(',')
        flights[k] = v
    pprint.pprint(flights)
