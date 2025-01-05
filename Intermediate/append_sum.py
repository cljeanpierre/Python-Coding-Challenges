#List Challenges (Intermediate)

'''
Challenge 
Create a function that calculates the sum of the last two elements of an input list and appends it to the end 
of the original list. After doing so, it repeats this process two more times and returns the resulting list.

'''

#Append Sum

def append_sum(my_list):
  sum_last2 = my_list[-1] + my_list[-2]
  my_list.append(sum_last2)
  nextsum = my_list[-1] + my_list[-2]
  my_list.append(nextsum)
  lastsum = my_list[-1] + my_list[-2]
  my_list.append(lastsum)
  return my_list


print(append_sum([1, 1, 2]))