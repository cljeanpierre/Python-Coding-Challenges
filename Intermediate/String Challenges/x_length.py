#String Challenges (Intermediate)

'''
Challenge 
Using the split method in a different way, create a new function that is able to accept two inputs: one for a 
sentence and another for a number. The function returns True if every single word in the sentence has a length 
greater than or equal to the number provided. 
'''

#X Length

def x_length_words(sentence, x):
  complete_sentence = sentence.split()
  for word in complete_sentence:
    if len(word) < x:
      return False
  return True