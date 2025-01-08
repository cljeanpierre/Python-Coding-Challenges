#List Challenges (Intermediate)

'''
Challenge 
Create a function that combines two different lists together and then sorts them. To do this, combine the lists 
with an operation and then sort using a function call.

'''

#Combine Sort

def combine_sort(my_list1, my_list2):
  onelist = my_list1 + my_list2
  onelist.sort()
  return onelist

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))