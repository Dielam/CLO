#!/usr/bin/python
#Diego Laguna

import sys
import re

linea = 0
ignorar = ""

for line in sys.stdin:
    if linea == 0:
        re.sub( r'^\W+|\W+$', '' , ignorar)
        linea = linea + 1
    else:
        line = re.sub( r'^\W+|\W+$', '', line ) # parsear linea
        words = line.split(',', 7) # trocear linea
        valor = (float(words[4]) + float(words[1]))/2
        print(words[0][0:4] + "\t" + words[4])