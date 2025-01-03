#Control Flow Challenges (Beginner)

'''
Challenge 
Determine if one number is twice as large as another number. 
To do this, Compare the first number with two times the second number.
'''

#Twice as Large

def twice_as_large(num1, num2):
  result = num2 * 2
  if num1 > result:
    return True
  return False

print(twice_as_large(10, 5))
print(twice_as_large(11, 5))
