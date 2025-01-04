#Control Flow Challenges (Advanced)

'''
Challenge 
Write a program that checks different names and determines if they are equal. Accept two strings and 
compare them.

'''

#Same Name

def same_name(your_name, my_name):
  if your_name == my_name:
    return True
  return False

print(same_name("Colby", "Colby"))
print(same_name("Tina", "Amber"))