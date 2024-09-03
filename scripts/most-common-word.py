#!/usr/bin/env python3
#
# Find the most commonly used word in the list of input files

import sys
import json

if len(sys.argv) < 3:
    print(f"Usage: {sys.argv[0]} <input_files> <output_file>")
    sys.exit(1)

most_word  = ""
most_count = 0

for infile in sys.argv[1:-1]:
    with open(infile, "r") as inf:
        words = json.load(inf)
        for word in words:
            if words[word] > most_count:
                most_word  = word
                most_count = words[word]

with open(sys.argv[-1], "w") as outf:
    print(f"{most_word} {most_count}", file=outf)


