#Loops Challenges (Intermediate)

'''
Challenge 
Use nested loops in order to raise a list of numbers to the power of a list of other numbers. For every number 
in the first list, raise that number to the power of every number in the second list. If you provide the first 
list with 2 elements and the second list with 3 numbers, then there will be 6 final answers. 

'''

#Exponents

def exponents(bases, powers):
  raised_list = []
  for num in bases:
    for nums in powers:
      raised_num = num ** nums
      raised_list.append(raised_num)
  return raised_list

print(exponents([2, 3, 4], [1, 2, 3]))