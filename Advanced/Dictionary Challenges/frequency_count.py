#Dictionary Challenges (Advanced)

'''
Challenge 
This function is similar to Word Length Dictionary, but instead of counting the length of each string in the 
list of strings, we will be counting the frequency of each string. This function will also accept a list of 
strings as input and return a new dictionary. 

'''

#Frequency Count

def frequency_dictionary(words):
  word_frequency = {}
  for word in words:
    if word not in word_frequency:
      word_frequency[word] = 0
    word_frequency[word] += 1
  return word_frequency

print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}