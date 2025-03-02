#Dictionary Challenges (Advanced)

'''
Challenge 
Read a dictionary as input and find how many values are unique. The function should return a 
number which is the count of all values from the dictionary without including duplicates.

'''

#Unique Values

def unique_values(my_dictionary):
  new_dict = []
  for value in my_dictionary.values():
    if value not in new_dict:
      new_dict.append(value)
  return len(new_dict)

print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1