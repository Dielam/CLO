#!/usr/bin/python
#Diego Laguna

from pyspark import SparkConf, SparkContext
import string
import sys

#Spark configuration
conf = SparkConf().setMaster('local').setAppName('MovieRatings')
sc = SparkContext(conf=conf)

RDDrating = sc.textFile("ratings.csv")

ratingsData = RDDrating.filter(lambda line: "userId" not in line).map(lambda line: (int(line.split(',')[1]), float(line.split(',')[2])))
numRatings = RDDrating.filter(lambda line: "userId" not in line).map(lambda line: (int(line.split(',')[1]), 1))
aggreg1 = ratingsData.reduceByKey(lambda a, b: a+b)
aggreg2 = numRatings.reduceByKey(lambda a, b: a+b)
union = aggreg1.join(aggreg2)

avg = union.map(lambda line: (line[0], line[1][0]/line[1][1]))

avg1 = avg.filter(lambda line: line[1] <= 1.0).filter(lambda line: line[1] >= 0.0)
avg2 = avg.filter(lambda line: line[1] <= 2.0).filter(lambda line: line[1] > 1.0)
avg3 = avg.filter(lambda line: line[1] <= 3.0).filter(lambda line: line[1] > 2.0)
avg4 = avg.filter(lambda line: line[1] <= 4.0).filter(lambda line: line[1] > 3.0)
avg5 = avg.filter(lambda line: line[1] <= 5.0).filter(lambda line: line[1] > 4.0)

avg1.saveAsTextFile("ratings1.txt")
avg2.saveAsTextFile("ratings2.txt")
avg3.saveAsTextFile("ratings3.txt")
avg4.saveAsTextFile("ratings4.txt")
avg5.saveAsTextFile("ratings5.txt")