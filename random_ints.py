import random

def array_of_randoms(length, rand):
  print 'Creating an random array of ' + str(length) + ' from ' + str(rand) + ' options'
  a = []
  for i in range(0, length):
    a.append(random.randint(0,rand))
  print 'Random array generated'
  return a

def inverted_array(length):
  l = length
  a = []
  while l > 0:
    a.append(l)
    l -= 1
  return a