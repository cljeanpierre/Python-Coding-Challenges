#List Challenges (Intermediate)

'''
Challenge 
You are working with two conveyor belts that contain items represented by a numerical ID. If one conveyor belt 
contains more items than the other, return the ID of the last item on that belt. In the case where the belts 
have the same number of items, return the last item from the first conveyor belt.

'''

#Larger List

def larger_list(my_list1, my_list2):
  if len(my_list1) >= len(my_list2):
    return my_list1[-1]
  return my_list2[-1]
  
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))