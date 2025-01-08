#Loop Challenges (Intermediate)

'''
Challenge 
Count how many numbers are divisible by ten from a list of numbers. Create a function that will accept a list 
of numbers as an input parameter and use a loop to check each of the numbers in the list. Every time a number 
is divisible by 10, a counter will be incremented and the final count will be returned. 

'''

#Divisible by Ten

def divisible_by_ten(nums):
  counter = 0
  for num in nums:
    if num % 10 == 0: 
      counter += 1
  return counter

print(divisible_by_ten([20, 25, 30, 35, 40]))
