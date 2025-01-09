#Functions Challenges (Intermediate)

'''
Challenge 
Create a function which takes the average of two numbers. These two numbers will be the input of the function
and the output will be the average of the two.

'''

#Average

def average(num1, num2):
  sum_num = num1 + num2
  return sum_num / 2

print(average(1, 100))
# The average of 1 and 100 is 50.5
print(average(1, -1))
# The average of 1 and -1 is 0
