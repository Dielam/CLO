#!/usr/bin/python
#Diego Laguna

from pyspark import SparkConf, SparkContext
import string
import sys

#Spark configuration
conf = SparkConf().setMaster('local').setAppName('MassMeteorites')
sc = SparkContext(conf=conf)

RDDvar = sc.textFile("Meteorite_Landings.csv")

meteorite = RDDvar.map(lambda line: (line.split(','))) 
data = meteorite.filter(lambda line: '"' not in line[4])
numAux = data.map(lambda line: (line[3].encode("ascii", "ignore"), line[4].encode("ascii", "ignore")))
numAux2 = numAux.filter(lambda line: line[1] != '') #Elimina las filas con masa vacia [tipo-masa]
num = numAux2.map(lambda line: (line[0], float(line[1])))
count = numAux2.map(lambda line: (line[0], 1))
aggreg1 = num.reduceByKey(lambda a, b: a+b)
aggreg2 = count.reduceByKey(lambda a, b: a+b)
union = aggreg1.join(aggreg2) 

avg = union.map(lambda line: (line[0], line[1][0]/line[1][1]))

avg.saveAsTextFile("meteorites.txt")
