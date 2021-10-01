# Given two strings, determine if they share a common substring. A substring may be as small as one character.

def hasSubstring(s1, s2):
    chars = list(s1)
    charDict = dict.fromkeys(chars,1)
    for char in s2:
        if char in charDict:
            return True

    return False

cases = [
    ["banana", "apple", True],
    ["z", "a", False],
    ["zebra", "xylophon", False],
    ["zebra", "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxa", True],
]

def test(cases):
    for case in cases:
        if hasSubstring(case[0], case[1]) != case[2]:
            print("Test Failure")

test(cases)