#Control Flow Challenges (Beginner)

'''
Challenge 
Create a function that tests whether the result of taking the power of one number to another number 
provides an answer that is greater than 5000. Use a conditional statement to return True if the result 
is greater than 5000 or return False if it is not. 

'''

#Large Power

def large_power(base, exponent):
  powerful = base ** exponent
  if powerful > 5000:
    return True
  return False

print(large_power(2, 13))
print(large_power(2, 12))
