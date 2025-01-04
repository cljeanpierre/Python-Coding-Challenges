#Control Flow Challenges (Advanced)

'''
Challenge 
Test whether a number falls within a certain range. First, accept three parameters where the first parameter 
is the number being tested, the second parameter is the lower bound and the third parameter is the upper bound 
of the range. 
'''

#In Range

def in_range(num, lower, upper):
  if lower <= num <= upper:
    return True
  return False

print(in_range(10, 10, 10))
print(in_range(5, 10, 20))
