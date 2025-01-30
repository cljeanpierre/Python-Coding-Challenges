#String Challenges (Intermediate)

'''
Challenge 
Count the number of occurrences of a certain letter within a string. Our function will accept a parameter for a 
string and another for the character which we are going to count. For example, providing the word "mississippi" 
and the character 's' would result in an answer of 4. 

'''

#Count X

def count_char_x(word, x):
  num_of_x = 0
  for letter in word:
    if letter == x:
      num_of_x += 1
  return num_of_x

print(count_char_x("Mosiah", "z"))
print(count_char_x("Obi", "i"))
print(count_char_x("Mississippi", "s"))