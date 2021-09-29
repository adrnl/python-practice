# Array Hourglass via Hackerrank

# Given a 6x6 2D array, arr:
# 1 1 1 0 0 0
# 0 1 0 0 0 0
# 1 1 1 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# 0 0 0 0 0 0
# An hourglass in A is a subset of values with indices falling in this pattern in arr's graphical representation:
# a b c
#   d
# e f g
# There are 16 hourglasses in arr. An hourglass sum is the sum of an hourglass' values.
# Calculate the hourglass sum for every hourglass in arr, then print the maximum hourglass sum. The array will always be 6x6.
# Example: arr =
# -9 -9 -9  1 1 1
#  0 -9  0  4 3 2
# -9 -9 -9  1 2 3
#  0  0  8  6 6 0
#  0  0  0 -2 0 0
#  0  0  1  2 4 0
# The 16 Hourglass Sums are:
# -63, -34, -9, 12,
# -10,   0, 28, 23,
# -27, -11, -2, 10,
#   9,  17, 25, 18
# The highest hourglass sum is 28 from the hourglass beginning at row 1, column 2:
# 0 4 3
#   1
# 8 6 6

def hourglassSums(arr):
    lSum = None
    if len(arr) != 6:
        return lSum
    for ar in arr:
        if len(ar) != 6:
            return lSum

    for y in range(4):
        for x in range(4):
            sum = (
                arr[y][x]+
                arr[y][x+1]+
                arr[y][x+2]+
                arr[y+1][x+1]+
                arr[y+2][x]+
                arr[y+2][x+1]+
                arr[y+2][x+2]
            )
            if lSum is None:
                lSum = sum
            elif sum > lSum:
                lSum = sum

    return lSum

def hourglassSums(grid):
    lSum = None
    if len(grid) != 6:
        return lSum
    for arr in grid:
        if len(arr) != 6:
            return lSum

    for y in range(4):
        for x in range(4):
            sum = (
                grid[y][x]+
                grid[y][x+1]+
                grid[y][x+2]+
                grid[y+1][x+1]+
                grid[y+2][x]+
                grid[y+2][x+1]+
                grid[y+2][x+2]
            )
            if lSum is None:
                lSum = sum
            elif sum > lSum:
                lSum = sum

    return lSum
