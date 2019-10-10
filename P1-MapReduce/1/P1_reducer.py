#!/usr/bin/python
#Diego Laguna

import sys

previous = None

result = ""
word = ""
line = 0
for line in sys.stdin:
    word, line = line.split('\t')
    result = result + line + " "

print(word + ' ' + result)
