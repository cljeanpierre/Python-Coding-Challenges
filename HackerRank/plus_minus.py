#HackerRank (Basic)

'''
Challenge 
Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print 
the decimal value of each fraction on a new line with places after the decimal.

'''

#Plus-Minus

def plusMinus(arr):
    n = len(arr)
    
    pos = 0
    neg = 0
    zero = 0
    
    for index in range(n):
        if arr[index] < 0:
            neg += 1
        elif arr[index] == 0:
            zero += 1
        else: #arr[index] > 0
            pos += 1
    
    print("{:.6f}".format(pos/n))
    print("{:.6f}".format(neg/n))
    print("{:.6f}".format(zero/n))

# {:.6f} means:
#{} is a placeholder for a value.
#:.6f specifies floating-point formatting with 6 decimal places.
#.format(end_time - start_time) replaces {:.6f} with the actual computed time.