#String Challenges (Advanced)

'''
Challenge 
You are creating an app that allows users to interact and share their coding project ideas online. The first 
step is to provide your name in the application and a greeting for other people to see which contains your name. 
Create a function that is able to check if a user’s name is located within their greeting.
'''

#Name Check

def check_for_name(sentence, name):
  if name.lower() in sentence.lower():
    return True
  return False
  
print(check_for_name("My name is Jamie", "Jamie"))
# should print True
print(check_for_name("My name is jamie", "Jamie"))
# should print True
print(check_for_name("My name is Samantha", "Jamie"))
# should print False