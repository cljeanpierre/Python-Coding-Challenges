#Dictionary Challenges (Intermediate)

'''
Challenge 
For this coding challenge, we are going to look at only the values in a dictionary. This function should sum up
all of the values from the key-value pairs in the dictionary.
'''

#Sum Values

def sum_values(my_dictionary):
  sum_vals = 0
  for vals in my_dictionary.values():
    sum_vals += vals
  return sum_vals
  

print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
print(sum_values({10:1, 100:2, 1000:3}))
# should print 6