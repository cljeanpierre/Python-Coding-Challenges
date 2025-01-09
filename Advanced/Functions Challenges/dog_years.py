#Functions Challenges (Advanced)

'''
Challenge

Create a function which calculates a dog’s age in dog years! This function will accept the name of the dog and
the age in human years. It will calculate the age of the dog in dog years and return a string describing the 
dog’s age. 

'''

#Dog Years

def dog_years(name, age):
  dog_age = age * 7
  return name + ", you are " + str(dog_age) + " years old in dog years."

print(dog_years("Lola", 16))
print(dog_years("Baby", 0))