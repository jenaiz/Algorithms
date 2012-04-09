from random_ints import array_of_randoms

def duplicated_numbers(array):
  """Find duplicated numbers in an array, given as result the duplicated numbers and the not duplicated numbers"""
  not_duplicated = []
  duplicated = []
  for i in range(len(array)):
    if array[i] in not_duplicated:
      duplicated.append(array[i])
    else:
      not_duplicated.append(array[i])
  return not_duplicated, duplicated
  
def duplicated_numbers2(array):
  """Find duplicated numbers and return as an array"""
  duplicated = []
  for i in range(len(array)):
    for j in range(len(array)):
      if j != i and array[i] == array[j] and (array[j] not in duplicated):
        duplicated.append(array[j])
        
  return duplicated

def print_duplicated(a):
  not_d, d = duplicated_numbers(a)
  print 'not duplicated = ' + str(not_d)
  print 'duplicated = ' + str(d)

i10 = array_of_randoms(10, 9)
print i10
print_duplicated(i10)

print duplicated_numbers2(i10)

print 'Test with 10000...'

i10000 = array_of_randoms(10000, 10000)
print_duplicated(i10000)
print duplicated_numbers2(i10000)