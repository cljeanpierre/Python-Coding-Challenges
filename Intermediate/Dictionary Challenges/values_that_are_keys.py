#Dictionary Challenges (Intermediate)

'''
Challenge 
We are making a program that will create a family tree. Using a dictionary, we want to return a list of all 
the children who are also parents of other children. Using dictionaries we can consider those people to be 
values which are also keys in our dictionary of family data.

'''

#Values That Are Keys

def values_that_are_keys(my_dictionary):
  found_keys = []
  for vals in my_dictionary.values():
    if vals in my_dictionary:
      found_keys.append(vals)
  return found_keys

print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]