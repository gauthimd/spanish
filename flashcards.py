#!/usr/bin/python
import random, time
d = dict()
n = 1
for line in open('words.txt', 'r'):
  if n <= 1200: 
    var = line.split('\t')
    d[var[len(var)-1]] = var[0]
    n += 1	
#  elif n in range(300,700):
#    var = line.split('\t')
#    d[var[len(var)-1]] = var[0]
#    n += 1
  else: break
print 'Number of words: ' + str(len(d))
y = 1
for x in d:
  print x + '   ' + str(y)
  y += 1
  raw_input()
  print d[x]
  print '************************************'
