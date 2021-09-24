# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

def reverse(integer):
    positive = True
    if integer < 0:
        positive = False
        integer *= -1

    string = str(integer)
    reversed = int(string[::-1])
    if not positive:
        return (-1  * reversed)

    return reversed

def test():
    input = 1000000
    out = reverse(input)
    if out != 1:
        print("test 1 fail")

    input = -21
    out = reverse(input)
    if out != -12:
        print("test 2 fail")

    input = -12345678910111213141516
    out = reverse(input)
    if out != -61514131211101987654321:
        print("test 3 fail")

test()