# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

# The algorithm for myAtoi(string s) is as follows:

# Read in and ignore any leading whitespace.
# Check if the next character (if not already at the end of the string) is '-' or '+'.
# Read this character in if it is either. This determines if the final result is negative or positive respectively.
# Assume the result is positive if neither is present.
# Read in next the characters until the next non-digit character or the end of the input is reached.
# The rest of the string is ignored.
# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0.
# Change the sign as necessary (from step 2).
# If the integer is out of the 32-bit signed integer range [-(2 ** 31), 2 ** 31 - 1], then clamp the integer so that it remains in the range.
# Return the integer as the final result.

# Note:
# Only the space character ' ' is considered a whitespace character.
# Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.

def myAtoi(string):
    string = string.lstrip(" ")
    if not string:
        return 0
    
    translator = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7,
        "8": 8,
        "9": 9,
        "0": 0,
    }

    max = 2 ** 31 - 1
    min = -(2 ** 31)
    
    sign = 1
    if string[0] == "-":
        string = string[1:]
        sign = -1
    elif string[0] == "+":
        string = string[1:]

    number = 0
    for char in string:
        if char not in translator:
            break

        number *= 10
        number += translator[char]

    number *= sign
    if number > max:
        return max
    elif number < min:
        return min
    else:
        return number

testCases = [
    ("42",42),
    ("          -42",-42),
    ("4193 with words",4193),
    ("words and 987",0),
    ("-91283472332",-2147483648),
]

def test(testCases):
    for case in testCases:
        if myAtoi(case[0]) != case[1]:
            print("Test Fail")
        else:
            print("Test Pass")

test(testCases)