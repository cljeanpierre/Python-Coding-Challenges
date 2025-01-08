#Loops Challenges (Advanced)

'''
Construct a device that is able to measure the power level of your coding abilities and according to the device, 
it will be impossible for your power levels to be over 9000. Because of this, as you iterate through a list of 
power values, count up each of the numbers until your sum reaches a value greater than 9000. Once this happens, 
stop adding the numbers and return the value where the counter stopped.

'''

#Over 9000

def over_nine_thousand(lst):
  sum = 0
  for num in lst:
    sum += num
    if sum > 9000:
      break
  return sum

print(over_nine_thousand([8000, 900, 120, 5000]))