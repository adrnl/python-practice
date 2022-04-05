testCases = [
    (input,output),
]

def test(testCases):
    for case in testCases:
        if func(case[0]) != case[1]:
            print("Test Fail")
        else:
            print("Test Pass")

test(testCases)