#!/usr/bin/python
#Diego Laguna

import sys
import re

siguiente = False

for line in sys.stdin:
    line = re.sub( r'^\W+|\W+$', '', line )
    words = re.split(r"\W+", line)

    # Recorremos las palabras hasta que encontramos la peticion y nos quedamos con la url
    for words in words:
        if siguiente:
            print(words.lower() + "\t1")
            siguiente = False
        if words =="GET" or words == "POST":
            siguiente = True