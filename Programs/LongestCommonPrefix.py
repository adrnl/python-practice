# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".

def longestPrefix(strings):
    if not strings:
        return("")

    shortest = min(strings, key=len)
    for i, char in enumerate(shortest):
        for string in strings:
            if string[i] != char:
                return shortest[:i]

    return shortest

cases = [
    (["flower","flow","flight"], "fl"),
    (["dog","racecar","car"], ""),
]

def test(cases):
    for case in cases:
        if longestPrefix(case[0]) != case[1]:
            print("Test Fail")
        else:
            print("Test Pass")

test(cases)