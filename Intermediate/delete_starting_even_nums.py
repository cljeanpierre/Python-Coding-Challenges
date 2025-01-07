#Loops Challenges (Intermediate)

'''
Challenge 
Create a function that will repeatedly remove the first element of a list until it finds an odd number or runs 
out of elements. Accept a list of numbers as an input parameter and return the modified list where any even 
numbers at the beginning of the list are removed.

'''

#Delete Starting Even Numbers

def delete_starting_evens(my_list):
    while len(my_list) != 0 and my_list[0] % 2 == 0:  
      my_list.pop(0)
    return my_list

print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
print(delete_starting_evens([4, 8, 10]))