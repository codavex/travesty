#!/usr/bin/python3

import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument("textLength", help="length of text to generate", type=int)
parser.add_argument("file", help="file to use as source")
args = parser.parse_args()

# read in statistics
statisticsFile = open(args.file, "r")
statisticsText = statisticsFile.read()
statisticsFile.close()

statisticsDict = eval(statisticsText)

# get 'seed' text to start the generated string
key = random.choice(list(statisticsDict.keys()))

# end option to stop newline on print
print(key, end="")

# pick character at random, print, then update key
for i in range(args.textLength):
    probability = random.random()
    nextChar = ""
    for char in statisticsDict[key]:
        nextChar = char
        if float(statisticsDict[key][char]) < probability:
            break
    print(nextChar, end="")
    key = key[1:] + nextChar
    if key not in statisticsDict:
        # on off-chance the key doesn't exist, select a new one
        # (eg last key size string of source text is unique)
        key = random.choice(list(statisticsDict.keys()))

print("")
