#Control Flow Challenges (Beginner)

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