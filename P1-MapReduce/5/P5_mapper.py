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
        words = line.split(',') # trocear linea
        aux = words[3].split('"')
        if str(words[3]) != "Unknown":
            if len(aux) == 2:
                if str(words[5]) == "":
                    valor = 0
                    seq = str(words[3]) + str(words[4])
                    print(seq + "\t" + "0")
                else:
                    valor = float(words[5])
                    seq = str(words[3]) + str(words[4])
                    print(seq + "\t" + words[5])
            else:
                if str(words[4]) == "":
                    valor = 0
                    print(words[3] + "\t" + "0")
                else:
                    valor = float(words[4])
                    print(words[3] + "\t" + words[4])
        else:
            valor = 0
            print("Unknown" + "\t" + "0")