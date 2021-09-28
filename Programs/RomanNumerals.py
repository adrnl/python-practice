# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000

# For example, 2 is written as II in Roman numeral, just two one's added together.
# 12 is written as XII, which is simply X + II.
# The number 27 is written as XXVII, which is XX + V + II.

# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII.
# Instead, the number four is written as IV.
# Because the one is before the five we subtract it making four.
# The same principle applies to the number nine, which is written as IX.

# There are six instances where subtraction is used:
# I can be placed before V (5) and X (10) to make 4 and 9.
# X can be placed before L (50) and C (100) to make 40 and 90.
# C can be placed before D (500) and M (1000) to make 400 and 900.

# Given an integer, convert it to a roman numeral.
# Constraints:
# 1 <= num <= 3999

NUMERALS = [
    ("I","V","X"),
    ("X","L","C"),
    ("C","D","M"),
    ("M","V","X"),
]

def romanize(integer):
    if integer > 9999:
        return "Invalid input"

    string = str(integer)
    pos = len(string) - 1
    romanized = ""

    for char in string:
        if char == "0":
            pos -= 1
            continue

        numerals = NUMERALS[pos]
        a = numerals[0]
        b = numerals[1]
        c = numerals[2]

        translator = {
            "1": a,
            "2": a*2,
            "3": a*3,
            "4": a+b,
            "5": b,
            "6": b+a,
            "7": b+(a*2),
            "8": b+(a*3),
            "9": a+c,
        }

        romanized += translator[char]
        pos -= 1

    return romanized

# Example 1:
# Input: num = 3
# Output: "III"

# Example 2:
# Input: num = 4
# Output: "IV"

# Example 3:
# Input: num = 9
# Output: "IX"

# Example 4:
# Input: num = 58
# Output: "LVIII"
# Explanation: L = 50, V = 5, III = 3.

# Example 5:
# Input: num = 1994
# Output: "MCMXCIV"
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

cases = [
    (3, "III"),
    (4, "IV"),
    (9, "IX"),
    (58, "LVIII"),
    (1994, "MCMXCIV"),
    (9999, "MXCMXCIX")
]

def test(cases):
    for case in cases:
        if romanize(case[0]) != case[1]:
            print("Test Fail")
        else:
            print("Test Pass")

test(cases)