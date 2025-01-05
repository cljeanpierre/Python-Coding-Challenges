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

# Alternative Approach

def append_sum(my_list):
  for i in range(3):
    # Get the sum of last two elements of the list and append it to the list
    my_list.append(my_list[-1] + my_list[-2])
  return my_list

print(append_sum([1, 1, 2]))