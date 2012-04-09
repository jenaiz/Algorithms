from random_ints import *

def insertion_sort(a):
  for i in range(1, len(a)):
    key = a[i]
    j = i
    while (j > 0 and a[j - 1] > key):
      a[j], a[j - 1] = a[j - 1], key
      j -= 1

i10 = inverted_array(10)
print i10
insertion_sort(i10)
print i10

i100 = array_of_randoms(100, 100)
insertion_sort(i100)

i10000 = array_of_randoms(10000, 10000)
insertion_sort(i10000)
