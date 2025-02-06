#String Challenges (Intermediate)

'''
Challenge 
Create a function that is able to extract a portion of a string between two characters. The function will take 
three parameters where the first parameter is the string we are going to extract the substring from, the second 
input is the starting character of our substring and the third character is the ending character of our 
substring. 
'''

#Substring Between

def substring_between_letters(word, start, end):
  start_index = word.find(start)
  end_index = word.find(end)
  if start_index > -1 and end_index > -1:
    return(word[start_index+1:end_index])
  return word


print(substring_between_letters("apple", "p", "e"))