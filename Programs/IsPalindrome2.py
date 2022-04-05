# Given a string s, return true if the s can be palindrome after deleting at most one character from it.

def isPalindrome(input):
    if input == input[::-1]:
        return True

    i, j = 0, len(input)-1
    while i < j:
        if input[i] != input[j]:
            testA = input[:i] + input[i+1:]
            testB = input[:j] + input[j+1:]
            if testA == testA[::-1] or testB == testB[::-1]:
                return True
            else:
                return False

        i += 1
        j -= 1

    return True


testCases = [
    ("a",True),
    ("aba",True),
    ("abca",True),
    ("ebcbbececabbacecbbcbe",True),
]

def test(testCases):
    for case in testCases:
        if isPalindrome(case[0]) != case[1]:
            print("Test Fail")
        else:
            print("Test Pass")

test(testCases)