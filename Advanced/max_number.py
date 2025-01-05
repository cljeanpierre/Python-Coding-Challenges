#Control Flow Challenges (Advanced)

'''
Challenge

Select which number from three input values is the greatest using conditional statements. To do this, check the
different combinations of values to see which number is greater than the other two.

'''

#Max Number

def max_num(num1, num2, num3):
  if num1 > num2 and num1 > num3:
    return num1
  if num2 > num1 and num2 > num3:
    return num2
  if num3 > num1 and num3 > num2:
    return num3
  return "It's a tie!"

print(max_num(-10, 0, 10))
print(max_num(-10, 5, -30))
print(max_num(-5, -10, -10))
print(max_num(2, 3, 3))
