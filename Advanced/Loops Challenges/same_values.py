#Loops Challenges (Advanced)

'''
Find the indices in two equally sized lists where the numbers match. Iterate through both of them at the same
time and compare the values. If the numbers are equal, then record the index. 

'''

#Same Values

def same_values(list1, list2):
  match = []
  for index in range(len(list1)):
    if list1[index] == list2[index]:
      match.append(index)
  return match


print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))