#String Challenges (Intermediate)

'''
Challenge 
Count the number of unique letters in a string. In other words, any new letters should be counted and any 
duplicates should not be counted. There are a few ways to solve this, but we will use the provided alphabet 
string to ensure that duplicates are not counted. Uppercase and lowercase letters should be counted as
different letters

'''

#Count Letters

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def unique_english_letters(word):
  unique_letters = 0
  for letter in letters: 
    if letter in word:
      unique_letters += 1
  return unique_letters

print(unique_english_letters("Sample"))
print(unique_english_letters("perpendicular"))