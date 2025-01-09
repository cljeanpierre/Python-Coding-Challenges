#Functions Challenges (Intermediate)

'''
Challenge 
Take the remainder of two numbers while performing other mathematical operations on them. Multiply the numerator
by 2 and divide the denominator by 2. After the two values have been modified, divide them and return the 
remainder.

'''

#Remainder

def remainder(num1, num2):
  operation1 = num1 * 2
  operation2 = num2 / 2
  return operation1 % operation2

print(remainder(15, 14))
# should print 2
print(remainder(9, 6))
# should print 0