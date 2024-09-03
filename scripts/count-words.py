#!/usr/bin/env python3
#
# Count the number of instances of each word in
# the input file. Save the results as JSON.

import sys
import json

if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <input_file> <output_file>")
    sys.exit(1)

words = {}
with open(sys.argv[1], "r") as inf:
    for line in inf.readlines():
        word = line.rstrip("\n")
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

with open(sys.argv[2], "w") as outf:
    json.dump(words, outf, indent=3)

