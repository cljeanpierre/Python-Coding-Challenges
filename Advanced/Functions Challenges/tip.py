#Functions Challenges (Advanced)

'''
Challenge

Create a function to easily calculate the amount to tip based on the total cost of the food and a percentage. 

'''

#Tip

def tip(total, percentage):
  return (total * percentage) / 100

print(tip(10, 25))
# should print 2.5
print(tip(0, 100))
# should print 0.0