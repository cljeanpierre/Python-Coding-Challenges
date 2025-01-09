#Functions Challenges (Advanced)

'''
Challenge

Create a function which both prints and returns values. For this function, print out the first three multiples 
of a number and return the third multiple. 

'''

#First Three Multiples
def first_three_multiples(num):
  print(num)
  print(num * 2)
  print(num * 3)
  return num * 3


first_three_multiples(10)
# should print 10, 20, 30, and return 30
first_three_multiples(0)
# should print 0, 0, 0, and return 0