#Dictionary Challenges (Intermediate)

'''
Challenge 
Similar to Even Keys, we are going to loop through the keys again, but this time we are going to modify the 
values within the dictionary. Our function should add 10 to every value in the dictionary and return the 
modified dictionary. 

'''

#Add Ten

def add_ten(my_dictionary):
  for key in my_dictionary.keys():
    my_dictionary[key] += 10
  return my_dictionary

print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}