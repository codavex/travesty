#!/usr/bin/python3

import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument("textLength", help="length of text to generate", type=int)
parser.add_argument("file", help="file to use as source")
args = parser.parse_args()

# read in statistics
travestyFile = open(args.file, "r")
travestyText = travestyFile.read()
travestyFile.close()

travestyDict = eval(travestyText)

# get 'seed' text to start the generated string
key = random.choice(list(travestyDict.keys()))

# end option to stop newline on print
print(key, end="")

# pick character at random, print, then update key
for i in range(args.textLength):
    char = random.choice(list(travestyDict[key].keys()))
    print(char, end="")
    key = key[1:] + char
