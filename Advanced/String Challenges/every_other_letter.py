#String Challenges (Advanced)

'''
Challenge 
Create a function that extracts every other letter from a string and returns the resulting string. 
'''

#Every Other Letter

def every_other_letter(word):
  new_string = ""
  for i in range(0, len(word), 2):
    new_string += word[i]
  return new_string


print(every_other_letter("Codecademy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd