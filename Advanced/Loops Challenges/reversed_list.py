#Loops Challenges (Advanced)

'''
Challenge
Test two lists to see if the second list is the reverse of the first list. There are a few different ways to 
approach this, but try a method that iterates through each of the values in one direction for the first list 
and compares them against the values starting from the other direction in the second list. 

'''

#Reversed List

def reversed_list(list1, list2):
  for index in range(len(list1)):
   if list1[index] != list2[len(list2) - 1 - index]:
    return False
  return True

print(reversed_list([1, 2, 3], [3, 2, 1]))
print(reversed_list([1, 5, 3], [3, 2, 1]))