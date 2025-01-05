#List Challenges (Intermediate)

'''
Challenge 
Calculate the length of an input list and append it to the end of the original list. 

'''

#Append Size

def append_size(my_list):
  listlength = len(my_list)
  my_list.append(listlength)
  return my_list


print(append_size([23, 42, 108]))