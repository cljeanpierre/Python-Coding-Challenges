#List Challenges (Intermediate)

'''
Challenge 
A factory produces a variety of different flavored snacks. The different types of snacks are represented by 
their id and are kept on a conveyor belt. Check if there are enough items of a certain snack in inventory.

The function should accept a list of numbers representing the ids of snack on the conveyor belt as its 
first input, the id of snack we are looking for as its second input, and the desired number of that type of 
snack on the conveyor belt as its third input.

The function should return True if the snack we are searching for appears more times in the list than the 
desired number given in the third parameter. Otherwise, it should return False.

'''

# More Than N

def more_than_n(my_list, item, n):
  num_of_items = my_list.count(item)
  if num_of_items > n:
    return True
  return False

print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))