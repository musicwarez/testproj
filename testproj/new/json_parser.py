#!/usr/bin/python
import json
import sys


'''
For start this script just type
python json_parser.py < downstream.json
script read JSON from STDIN
and then print out to STDOUT
'''


json_data = sys.stdin.read()
data = json.loads(json_data)
for line in data["trades"]:
    print((str(line['Sequence']) + ":"
        + str(line['ObjectId']) + ":"
        + str(line['TradeId']) + ":"
        + str(line['TradeSize']) + ":"
        + str(line['ExchangeReport']) + ":"
        + str(line['ParserSend']) + ":"
        + str(line['TkrsendrRecv'])))