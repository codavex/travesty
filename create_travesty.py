#!/usr/bin/python3

import argparse
import random

parser = argparse.ArgumentParser()
parser.add_argument( "textLength", help="length of text to generate", type=int )
parser.add_argument("file", help="file to use as source")
args = parser.parse_args()

travesty_file = open(args.file, "r")
travesty_text = travesty_file.read()
travesty_file.close()

travesty_dict = eval(travesty_text)

key=random.choice(list(travesty_dict.keys()))

print(key, end='')

i=0;
while i < args.textLength:
    char = random.choice(list(travesty_dict[key].keys()))
    print(char, end='')
    key = key[1:] + char
    i += 1

