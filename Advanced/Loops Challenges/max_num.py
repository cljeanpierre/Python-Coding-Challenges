#Loops Challenges (Advanced)

'''
Create a function that will be used to find the maximum number in a list of numbers. This can be accomplished
using the max() function in python, but as a challenge, manually implement this function.

'''

#Max Num

def max_num(nums):
  max_val = nums[0]
  for num in nums:
    if num > max_val:
      max_val = num
  return max_val

print(max_num([50, -10, 0, 75, 20]))