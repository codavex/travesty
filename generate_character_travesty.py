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
ngram = random.choice(list(statisticsDict.keys()))

# end option to stop newline on print
print(ngram, end="")

# pick character at random, print, then update ngram
for i in range(args.textLength):
    probability = random.random()
    nextChar = ""
    for char in statisticsDict[ngram]:
        nextChar = char
        if float(statisticsDict[ngram][char]) < probability:
            break
    print(nextChar, end="")
    ngram = ngram[1:] + nextChar
    if ngram not in statisticsDict:
        # on off-chance the ngram doesn't exist, select a new one
        # (eg last ngram size string of source text is unique)
        ngram = random.choice(list(statisticsDict.keys()))

print("")
