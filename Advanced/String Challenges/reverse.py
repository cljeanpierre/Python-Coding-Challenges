#String Challenges (Advanced)

'''
Challenge 
This one is similar to the Every Other Letter advanced String challenge. Instead of selecting every other letter,
we want to reverse the entire string. This can be performed in a similar manner, but we will need to modify the 
range we are using.
'''

#Reverse

def reverse_string(word):
  reversed = ""
  for i in range(len(word) - 1, -1, -1):
    reversed += word[i]
  return reversed

print(reverse_string("Codecademy"))
# should print ymedacedoC
print(reverse_string("Hello world!"))
# should print !dlrow olleH
print(reverse_string("Mosiah"))
# should print haisoM