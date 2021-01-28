import math
def loadBalancer(numbers):
    upperLim = math.floor(sum(numbers)/3)
    current = 0

    for i in range(len(numbers)):
        if (current+numbers[i]) <= upperLim:
            current += numbers[i]
        eli

    print upperLim

loadBalancer([2, 4, 5, 3, 3, 9, 2, 2, 2])

# Given an array containing only positive integers, return if you can pick two integers from the array which cuts the
# array into three pieces such that the sum of elements in all pieces is equal.
#
# Example 1:
#
# Input:  array = [2, 4, 5, 3, 3, 9, 2, 2, 2]
#
# Output: true
#
# Explanation: choosing the number 5 and 9 results in three
# pieces[2, 4], [3, 3] and [2, 2, 2].Sum = 6.
#
# Example 2:
#
# Input:  array = [1, 1, 1, 1],
#
# Output: false