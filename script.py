
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

'''
Challenge 2
You are given a monthly budget and some expenses and need to check if the sum of the expenses goes over budget!
'''

#Challenge 2: Over Budget

budget = 2000

food_bill = 200
electricity_bill = 100
internet_bill = 60
rent = 1500

total = food_bill + electricity_bill + internet_bill + rent


if total > budget:
  over_budget = True
else:
  over_budget = False

print("Total: " + str(total))
print("Is it over budget? " + str(over_budget))