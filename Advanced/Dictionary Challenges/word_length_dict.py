#Dictionary Challenges (Advanced)

'''
Challenge 
Write a function that creates a new dictionary based on a list of strings. The keys of the dictionary will be 
every string in the list of strings, while the values will be the length of each of the words in the string list. 

'''

#Word Length Dictionary

def word_length_dictionary(words):
  word_lengths = {}
  for word in words:
    word_lengths[word] = len(word)
  return word_lengths

print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}