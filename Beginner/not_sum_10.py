#Control Flow Challenges (Beginner)

'''
Challenge 1
You are given two numbers stored in num1 and num2. 
If the sum of num1 and num2 is NOT equal to 10, then store True into a variable called not_ten, 
otherwise store False in not_ten.

'''

#Challenge 1: Not Sum Ten

num1 = 6
num2 = 3

if num1 + num2 != 10:
  not_ten = True
else:
  not_ten = False

print("Is the sum of the numbers not equal to 10? " + str(not_ten))