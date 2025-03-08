#HackerRank (Basic)

'''
Challenge 
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly 
four of the five integers. Then print the respective minimum and maximum values as a single line of two 
space-separated long integers.

'''

#Mini-Max Sum

def miniMaxSum(arr):
    # sort the list of numbers called arr
    arr.sort()
    # find the min sum by adding the first four numbers in the list
    min_sum = sum(arr[:4])
    # find the max sum by adding the last four numbers in the list
    max_sum = sum(arr[1:])
    print(min_sum, max_sum)

miniMaxSum([1, 3, 5, 7, 9])  # Output: 16 24
miniMaxSum([5, 5, 5, 5, 5])  # Output: 20 20 (all numbers are the same)
miniMaxSum([2, 4, 6, 8, 10]) # Output: 20 28
