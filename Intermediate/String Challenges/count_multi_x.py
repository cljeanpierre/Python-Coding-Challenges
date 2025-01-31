#String Challenges (Intermediate)

'''
Challenge 
Unlike our function in count_x, we are going to compare against an entire string instead of a single character. 
This function should accept a string and a substring to compare against. Return the number of occurrences of
second parameter within the first parameter.  In other words, we are checking the number of occurrences of the 
shorter string (second parameter) within the longer string (first parameter). 
'''

#Count Multi X

def count_multi_char_x(word, x):
  word_parts = word.split(x)
  count_word_parts = len(word_parts) - 1
  return count_word_parts

print(count_multi_char_x("apple", "pp"))
print(count_multi_char_x("mississippi", "iss"))