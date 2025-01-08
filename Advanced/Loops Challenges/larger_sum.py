#Loops Challenges (Advanced)

'''
Challenge 
Calculate which list of two inputs has the larger sum. Iterate through each of the list and calculate the sums.
Afterwards compare the two and return which one has a greater sum.

'''

#Larger Sum

def larger_sum(lst1, lst2):
  sum_lst1 = 0
  sum_lst2 = 0
  for num in lst1:
    sum_lst1 += num
  for num in lst2:
    sum_lst2 += num 
  if sum_lst1 >= sum_lst2:
    return lst1
  return lst2


print(larger_sum([1, 9, 5], [2, 3, 7]))