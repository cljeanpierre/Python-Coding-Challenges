#Dictionary Challenges (Intermediate)

'''
Challenge 
Create a function that is able to find the maximum value in the dictionary and return the associated key. This 
is a twist on the max algorithm since it is using a dictionary rather than a list. 

'''

#Largest Value

def max_key(my_dictionary):
  start_key = 0
  start_val = 0
  for key, value in my_dictionary.items():
    if value > start_val:
      start_val = value
      start_key = key
  return start_key


print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"