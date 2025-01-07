#Loop Challenges (Beginner)

'''
Challenge 
You are invited to a social gathering, but you are tired of greeting everyone there. Luckily you can create a 
function to accomplish this task for you. Take a list of names and prepend the string 'Hello, ' before each name.
'''

#Greetings
def add_greetings(names):
  new_strings = []
  for name in names:
    new_strings.append("Hello, " + name)
  return new_strings

print(add_greetings(["Owen", "Max", "Sophie"]))