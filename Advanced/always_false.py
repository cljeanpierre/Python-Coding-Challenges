#Control Flow Challenges (Advanced)

'''
Challenge 
Create a function that contains a contradition, an occurrence when your condition will always be false 
no matter what value you pass into it. 
'''

#Always False

def always_false(num):
  if num < 10 and num > 12:
    return True
  return False

print(always_false(0))
print(always_false(-1))
print(always_false(1))
