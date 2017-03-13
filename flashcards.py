import random, time
d = dict()
for line in open('words.txt', 'r'):
  var = line.split('\t')
  d[var[len(var)-1]] = var[0]
print 'Number of words: ' + str(len(d))
print 'Approx time: ' + str(len(d)*2/60) + 'min'
for y in range(len(d)):
  x = random.choice(d.keys())
  print x
  raw_input()
  print d[x]
  print '************************************'
