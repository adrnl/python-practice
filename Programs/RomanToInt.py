TRANSLATOR = {
    "I" :1,
    "V" :5,
    "X" :10,
    "L" :50,
    "C" :100,
    "D" :500,
    "M" :1000,
}

def romanToInt(string):
    integer = 0
    place = 0
    while place < len(string):
        if place < len(string) - 1 and TRANSLATOR[string[place]] < TRANSLATOR[string[place+1]]:
            integer += TRANSLATOR[string[place+1]] - TRANSLATOR[string[place]]
            place += 2
        else:
            integer += TRANSLATOR[string[place]]
            place += 1

    return integer

cases = [
    (3, "III"),
    (4, "IV"),
    (9, "IX"),
    (58, "LVIII"),
    (1994, "MCMXCIV"),
    (3999, "MMMCMXCIX")
]

def test(cases):
    for case in cases:
        if romanToInt(case[1]) != case[0]:
            print("Test Fail")
        else:
            print("Test Pass")

test(cases)