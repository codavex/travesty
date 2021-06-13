#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "ngramSize", help="size of textual ngram", type=int, choices=[1, 2, 3, 4, 5]
)
parser.add_argument("file", help="file to use as source")
args = parser.parse_args()

file = open(args.file, "r")

# read in first ngram size bytes
ngram = file.read(args.ngramSize)

stats = {}

while 1:
    char = file.read(1)
    if not char:
        break

    # update dictionary with char
    if ngram in stats:
        if char in stats[ngram]:
            stats[ngram][char] += 1
        else:
            stats[ngram][char] = 1
    else:
        stats[ngram] = {}
        stats[ngram][char] = 1

    # update ngram
    ngram = ngram[1:] + char

file.close()

for ngram in stats:
    runningTotal = 0
    for char in stats[ngram]:
        runningTotal += stats[ngram][char]
    rationalisedTotal = 0
    for char in stats[ngram]:
        percentageValue = stats[ngram][char] / runningTotal
        stats[ngram][char] = percentageValue + rationalisedTotal
        rationalisedTotal += percentageValue

print(stats)
