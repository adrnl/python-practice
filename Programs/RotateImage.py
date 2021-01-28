def rotate(lists):
    if not lists:
        return lists

    output = []
    for i in range(len(lists)):
        list = []
        for j in range(len(lists)-1, -1, -1):
            list.append(lists[j][i])

        output.append(list)

    return output

# def rotate(matrix):
#     if not matrix:
#         return matrix
#
#     output = []
#     for i in range(len(matrix)):
#         list = []
#         for j in range(len(matrix) - 1, -1, -1):
#             list.append(matrix[j][i])
#
#         output.append(list)
#
#     # print(matrix)
#     matrix = output
#     print(matrix)
#
# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# rotate(matrix)
# print(matrix)

matrix = [[1,2,3],[4,5,6],[7,8,9]]
if rotate(matrix) != [[7,4,1],[8,5,2],[9,6,3]]:
    print("Test 1 Failed")
else:
    print("Test 1 Passed")

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
if rotate(matrix) != [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]:
    print("Test 2 Failed")
else:
    print("Test 2 Passed")

matrix = [[1]]
if rotate(matrix) != [[1]]:
    print("Test 3 Failed")
else:
    print("Test 3 Passed")

matrix = [[1,2],[3,4]]
if rotate(matrix) != [[3,1],[4,2]]:
    print("Test 4 Failed")
else:
    print("Test 4 Passed")
