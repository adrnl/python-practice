def rotate(matrix, clockwise):
    # x = 0
    # y = 0
    output = []
    # for x in range(len(matrix)):
    #     list = []
    #     for y in range(len(matrix)):

    return output

# EXAMPLES:
# [[1,2,3], 00,01,02
#  [4,5,6], 10,11,12
#  [7,8,9]] 20,21,22
#
# [[7,4,1], 20,10,00
#  [8,5,2], 21,11,01
#  [9,6,3]] 22,12,02

clockwise = True
matrix = [[1,2,3],[4,5,6],[7,8,9]]
if rotate(matrix, clockwise) != [[7,4,1],[8,5,2],[9,6,3]]:
    print("Test 1 Failed")
else:
    print("Test 1 Passed")

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
if rotate(matrix, clockwise) != [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]:
    print("Test 2 Failed")
else:
    print("Test 2 Passed")

matrix = [[1]]
if rotate(matrix, clockwise) != [[1]]:
    print("Test 3 Failed")
else:
    print("Test 3 Passed")

matrix = [[1,2],[3,4]]
if rotate(matrix, clockwise) != [[3,1],[4,2]]:
    print("Test 4 Failed")
else:
    print("Test 4 Passed")
