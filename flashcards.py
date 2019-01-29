#!/usr/bin/python
import random, time
d = dict()
n = 1
for line in open('words.txt', 'r'):
  if n < 1495: 
    var = line.split('\t')
    d[var[len(var)-1]] = var[0]
    n += 1	
#  elif n in range(600,800):
#    var = line.split('\t')
#    d[var[len(var)-1]] = var[0]
#    n += 1
  else: break
print 'Number of words: ' + str(len(d))
y = 1
for x in d:
  print x + '   ' + str(y)
  y += 1
#  raw_input()
  time.sleep(.75)
  print d[x]
  print '************************************'
