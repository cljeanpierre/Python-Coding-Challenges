#Functions Challenges (Advanced)

'''
Challenge
Re-create a famous movie scene through code. The function is going to concatenate strings together in order to 
replace James Bond’s name with whatever name you want. The input to your function will be two strings, one for 
a first name and another for a last name. The function will return a string consisting of the famous phrase but
replaced with our inputs.

'''

#Bond, James Bond

def introduction(first_name, last_name):
  return (last_name + ", " + first_name + " " + last_name)

print(introduction("James", "Bond"))
print(introduction("Maya", "Angelou"))
print(introduction("Mosiah", "Jeanpierre"))