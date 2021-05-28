#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser()
parser.add_argument( "keySize",
                     help="size of textual key",
                     type=int,
                     choices=[1, 2, 3, 4] )
parser.add_argument("file", help="file to use as source")
args = parser.parse_args()

file = open(args.file, "r")

key = file.read(args.keySize)

while 1:
    char = file.read(1)
    if not char:
        break

    print("{0} {1}".format(key, char))
    key = key[1:] + char

file.close()
