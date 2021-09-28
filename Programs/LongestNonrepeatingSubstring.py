# Given a string s, find the length of the longest substring without repeating characters.

def bruteForce(string):
    chars = list(string)
    charsLen = len(chars)
    max = 0

    for i in range(charsLen):
        substring = []
        for j in range(i, charsLen):
            if chars[j] in substring:
                if len(substring) > max:
                    max = len(substring)
                break
            else:
                substring.append(chars[j])
                if len(substring) > max:
                    max = len(substring)

    return(max)


def optimized(string):
    start = 0
    # the index of the beginning of our current attempted string
    max = 0
    strLen = len(string)
    usedChar = {}

    for i in range(strLen):
        if string[i] in usedChar and start <= usedChar[string[i]]:
        # if the character is in the hashmap, and start is <= the index of the last appearance of this character
            start = usedChar[string[i]] + 1
            # set start to the index of the
        else:
            maxLength = max(maxLength, i - start + 1)

        usedChar[string[i]] = i
        # set the hashmaps value to the index of the most recently found instance of the character

    return maxLength

def test():
    test = "abcdefghijklmnopqrstuvwxyz"
    answer = 26
    if bruteForce(test) == answer:
        print("test 1 pass")
    else:
        print("test 1 fail")
        print(bruteForce(test), answer)

    test = "abcdefghijklmnopa"
    answer = 16
    if bruteForce(test) == answer:
        print("test 2 pass")
    else:
        print("test 2 fail")
        print(bruteForce(test), answer)

    test = "abcaijklmna"
    answer = 9
    if bruteForce(test) == answer:
        print("test 3 pass")
    else:
        print("test 3 fail")
        print(bruteForce(test), answer)

test()