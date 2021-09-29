# Harold is a kidnapper who wrote a ransom note, but now he is worried it will be traced back to him through his handwriting.
# He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note.
# The words in his note are case-sensitive and he must use only whole words available in the magazine.
# He cannot use substrings or concatenation to create the words he needs.
#
# Given the words in the magazine and the words in the ransom note,
# print Yes if he can replicate his ransom note exactly using whole words from the magazine;
# otherwise, print No.

def checkMagazine(magazine, note):
    noteList = note.split()
    magDict = dictBuilder(magazine)
    for word in noteList:
        if word not in magDict:
            return False
        else:
            if magDict[word] < 1:
                return False
            else:
                magDict[word] -= 1


    return True


def dictBuilder(str):
    wordList = str.split()
    wordCount = {}
    for word in wordList:
        if word in wordCount:
            wordCount[word] += 1
        else:
            wordCount[word] = 1

    return wordCount

testCases = (
    ("give me one grand today night", "give one grand today", True),
    ("two times three is not four", "two times two is four", False),
    ("ive got a lovely bunch of coconuts", "ive got some coconuts", False),
)

def test(cases):
    for case in cases:
        if checkMagazine(case[0], case[1]) != case[2]:
            print("Test Failed")

test(testCases)