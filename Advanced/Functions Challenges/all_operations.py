#Functions Challenges (Advanced)

'''
Challenge

Create a function that performs multiple mathematical operations on multiple inputs. Begin with adding the first
two inputs, then subtract the third and fourth inputs. After that, multiply the first result and the second 
result. Finally, return the remainder of the previous result divided by the first input. Print each of the steps.

'''

#All Operations

def lots_of_math(a, b, c, d):
  sums = a + b
  print(sums)
  diff = c - d
  print(diff) 
  print(sums * diff)
  return (sums * diff) % a
  
print(lots_of_math(1, 2, 3, 4))
print(lots_of_math(1, 1, 1, 1))