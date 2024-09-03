#!/usr/bin/env python3
#
# Normalise the text in a project Gutenberg book.
# This strips non-alpha, converts to lower case,
# and removes stop words. This implementation is
# an inefficient hack.

import sys

stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your",
              "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she",
              "her", "hers", "herself", "it", "its", "itself", "they", "them", "their",
              "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
              "these", "those", "am", "is", "are", "was", "were", "be", "been", "being",
              "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an",
              "the", "and", "but", "if", "or", "because", "as", "until", "while", "of",
              "at", "by", "for", "with", "about", "against", "between", "into", "through",
              "during", "before", "after", "above", "below", "to", "from", "up", "down",
              "in", "out", "on", "off", "over", "under", "again", "further", "then",
              "once", "here", "there", "when", "where", "why", "how", "all", "any", "both",
              "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not",
              "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will",
              "just", "don", "should", "now"]

if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <input_file> <output_file>")
    sys.exit(1)

with open(sys.argv[1], "r") as inf:
    content = inf.read()

stripped = []
for elem in content:
    if elem.isalpha() or elem.isspace():
        stripped.append(elem)

with open(sys.argv[2], "w") as outf:
    for word in "".join(stripped).split():
        if word.strip().lower() in stop_words:
            continue
        print(word.strip().lower(), file=outf)

