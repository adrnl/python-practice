# https://leetcode.com/problems/zigzag-conversion/
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:

# Input: string = "PAYPALISHIRING", rows = 3
# Output: "PAHNAPLSIIGYIR"

# P   A   H   N
# A P L S I I G
# Y   I   R

# Input: string = "PAYPALISHIRING", rows = 4
# Output: "PINALSIGYAHRPI"

# P     I    N
# A   L S  I G
# Y A   H R
# P     I



def zigZag(string, rows):
    # if you only have 1 row, the string will not change
    if rows == 1:
        return string

    # create an array of arrays containing empty strings = to the number of rows
    rowArray = [""] * rows
    rowIndex = 1
    increment = True

    for char in string:
        # add the char to the appropriate row of characters
        rowArray[rowIndex - 1] += char
        # if you have reached the "bottom" reverse direction
        if rowIndex == rows:
            increment = False
        # if you have reached the "top" reverse direction again
        elif rowIndex == 1:
            increment = True

        if increment:
            rowIndex += 1
        else:
            rowIndex -= 1

    return "".join(rowArray)

print(zigZag("PAYPALISHIRING",3))
