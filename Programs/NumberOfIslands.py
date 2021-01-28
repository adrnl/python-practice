def numberOfIslands(grid):
    def sink(i, j):
        # if i is a number within the y axis and j is within the x axis, and the location is land:
        if 0 <= i < len(grid) and 0 <= j < len(grid[i]) and grid[i][j] == "1":
            # turn the land into water
            grid[i][j] = "0"
            # run sink on all adjacent tiles
            list(map(sink, (i+1, i-1, i, i), (j, j, j+1, j-1)))
            return 1
        return 0
    # run sink on every tile in the grid, and sum up the number of 1's
    return sum(sink(i, j) for i in range(len(grid)) for j in range(len(grid[i])))

# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.

# Example1:

input = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "1"]
]
output = 2
# print(numberOfIslands(input))
if numberOfIslands(input) != output:
    print("fail")
else:
    print("pass")

# Example2:

input = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]
output = 3
if numberOfIslands(input) != output:
    print("fail")
else:
    print("pass")
    