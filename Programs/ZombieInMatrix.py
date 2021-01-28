def countHours(matrix):
    hours = 0
    if not matrix:
        return hours

    zombies = []
    width, height = len(matrix[0]), len(matrix)
    for i in range(height):
        for j in range(width):
            if matrix[i][j] == 1:
                zombies.append((j, i))

    zCounter = 0
    while zombies:
        for i in range(len(matrix)):
            print(matrix[i])

        print("\n")
        for _ in range(len(zombies)):
            i, j = zombies.pop(0)
            zCounter += 1
            adjacents = [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]
            for x, y in adjacents:
                if 0 <= x < width and 0 <= y < height and matrix[y][x] == 0:
                    matrix[y][x] = 1
                    zombies.append((x, y))

        if zCounter == height * width:
            break;

        hours += 1

    return hours

# print(countHours([
#     [0, 1, 1, 0, 1],
#     [0, 1, 0, 1, 0],
#     [0, 0, 0, 0, 1],
#     [0, 1, 0, 0, 0],
# ]))
# print(countHours([
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
#     [1, 1, 1, 1, 1],
# ]))
# print(countHours([
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0],
# ]))
# print(countHours([
#     [0],
# ]))
# print(countHours([
#     [1],
# ]))
# print(countHours([
#     [],
# ]))
print(countHours([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
]))

# 00100
# 10001
# 01010
# 10101
#
#
# Given a 2D grid, each cell is either a zombie 1 or a human 0.
# Zombies can turn adjacent (up/down/left/right) human beings into zombies every hour.
# Find out how many hours does it take to infect all humans?
#
# Example:
#
# Input:
# [[0, 1, 1, 0, 1],
#  [0, 1, 0, 1, 0],
#  [0, 0, 0, 0, 1],
#  [0, 1, 0, 0, 0]]
#
# Output: 2
#
# Explanation:
# At the end of the 1st hour, the status of the grid:
# [[1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1],
#  [0, 1, 0, 1, 1],
#  [1, 1, 1, 0, 1]]
#
# At the end of the 2nd hour, the status of the grid:
# [[1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1]]