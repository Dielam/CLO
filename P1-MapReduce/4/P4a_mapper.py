#!/usr/bin/python
#Diego Laguna
# el output tarda un poco

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
        words = line.split(',') # trocear linea
        valor = float(words[2])
        print(words[1] + "\t" + words[2])