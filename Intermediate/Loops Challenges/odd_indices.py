#Loops Challenges (Intermediate)

'''
Challenge 
Create a function that will give the values from a list at every odd index. Accept a list of numbers as an input
parameter and loop through the odd indices instead of the elements.

'''

#Odd Indices

def odd_indices(my_list):
  new_list = []
  for index in range(1, len(my_list), 2):
    new_list.append(my_list[index])
  return new_list    

print(odd_indices([4, 3, 7, 10, 11, -2]))
print(odd_indices([19, 21, 3, 5, 39, -9]))