# Find an arbitarily large number between 0 and infinity.
import math

def secretFinder(secret):
    guess, isLower = 1, True
    if guess == secret:
        return guess

    leaps = 0
    steps = 0
    while isLower:
        guess *= 2
        leaps += 1
        if guess == secret:
            # print("This took " + str(leaps) + " leaps and " + str(steps) + " steps")
            return guess
        elif guess > secret:
            isLower = False

    upper = guess
    lower = int(guess/2)
    while guess != secret:
        guess = math.ceil((upper+lower)/2)
        steps += 1
        if guess == secret:
            # print("This took " + str(leaps) + " leaps and " + str(steps) + " steps")
            return guess
        elif guess > secret:
            upper = guess
        elif guess < secret:
            lower = guess

cases = [
    1,
    2,
    3,
    10,
    100,
    500,
    20000000000000000000000,
]

def test(cases):
    for case in cases:
        if secretFinder(case) != case:
            print("TEST FAILED")

test(cases)