#Dictionary Challenges (Intermediate)

'''
Challenge 
Similar to Sum Values, but we are going to use the keys in order to retrieve the values. Additionally, we are
going to only look at every even key within the dictionary. 
'''

#Even Keys

def sum_even_keys(my_dictionary):
  total = 0
  for key in my_dictionary.keys():
    if key % 2 == 0:
      total += my_dictionary[key]
  return total

print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6