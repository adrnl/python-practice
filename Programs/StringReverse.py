import math
# Write a function that reverses a string. The input string is given as an array of characters s.
# You must do this by modifying the input array in-place with O(1) extra memory.

# [0, 1, 2]
# [0,1,2,3]

def reverseString(chars):
    length = len(chars)
    if not chars or length == 1:
        return chars

    for i in range(0, math.floor(length/2)):
        charA = chars[i]
        charB = chars[length-1-i]
        chars[i] = charB
        chars[length-1-i] = charA

    return chars

testCases = [
    ([0],[0]),
    ([0,1],[1,0]),
    ([0,1,2],[2,1,0]),
    ([0,1,2,3],[3,2,1,0]),
]

def test(testCases):
    for case in testCases:
        if reverseString(case[0]) != case[1]:
            print("Test Fail")
        else:
            print("Test Pass")

test(testCases)