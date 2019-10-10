#!/usr/bin/python
#Diego Laguna

import sys
import re

linea = 0


for line in sys.stdin:
    linea = linea + 1

    patron = sys.argv[1]
    line = re.sub(r'^\W+|\W+$', '', line)
    words = re.split(r"\W+", line)

    for word in words:
        if patron == word:
            print(word.lower() + "\t" + str(linea))

