#Control Flow Challenges (Beginner)

'''
Challenge 
Create a function that determines whether or not a number is divisible by ten. 
A number is divisible by ten if the remainder of the number divided by 10 is 0
'''

#Divisible by 10

def divisible_by_ten(num):
  result = num % 10
  if result == 0:
    return True
  return False

print(divisible_by_ten(20))
print(divisible_by_ten(25))
