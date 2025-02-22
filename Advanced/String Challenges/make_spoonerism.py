#String Challenges (Advanced)

'''
Challenge 
A Spoonerism is an error in speech when the first syllables of two words are switched. For example, a Spoonerism
is made when someone says “Belly Jeans” instead of “Jelly Beans”. We are going to make a function that is 
similar, but instead of using the first syllable, we are going to switch the first character of two words. 
'''

#Make Spoonerism
def make_spoonerism(word1, word2):
  first_char1 = word1[0] 
  first_char2 = word2[0]
  remain_char1 = word1[1:]
  remain_char2 = word2[1:]
  spooned = first_char2 + remain_char1 + " " + first_char1 + remain_char2
  return spooned

print(make_spoonerism("Codecademy", "Learn"))
# should print Lodecademy Cearn
print(make_spoonerism("Hello", "world!"))
# should print wello Horld!
print(make_spoonerism("a", "b"))
# should print b a