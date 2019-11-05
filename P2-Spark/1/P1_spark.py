#!/usr/bin/python
#Diego Laguna

from pyspark import SparkConf, SparkContext
import string
import sys

#Spark configuration
conf = SparkConf().setMaster('local').setAppName('WordSearchCount')
sc = SparkContext(conf=conf)

RDDvar = sc.textFile("input.txt")
wanted = sys.argv[1]  # palabra a buscar

words = RDDvar.flatMap(lambda line: line.split())

result = words.map(lambda word: (str(word.lower()).translate(None, string.punctuation), 1))

aggreg1 = result.reduceByKey(lambda a, b: a+b)

number = aggreg1.filter(lambda line: wanted in line)

number.saveAsTextFile("output.txt")