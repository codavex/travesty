#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    "keySize", help="size of textual key", type=int, choices=[1, 2, 3, 4]
)
parser.add_argument("file", help="file to use as source")
args = parser.parse_args()

file = open(args.file, "r")

# read in first keySize bytes
key = file.read(args.keySize)

stats = {}

while 1:
    char = file.read(1)
    if not char:
        break

    # update dictionary with char
    if key in stats:
        if char in stats[key]:
            stats[key][char] += 1
        else:
            stats[key][char] = 1
    else:
        stats[key] = {}
        stats[key][char] = 1

    # update key
    key = key[1:] + char

file.close()
print(stats)
