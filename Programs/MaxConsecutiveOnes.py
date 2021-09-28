# Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

def bruteForce(list, flips):
    max = 0
    listL = len(list)
    for i in range(listL):
        zCount = 0
        window = []
        for j in range(i, listL):
            if list[j] == 1:
                window.append(list[j])
            elif list[j] == 0 and zCount < flips:
                window.append(list[j])
                zCount += 1
            else:
                if len(window) > max:
                    max = len(window)
                break
        if len(window) > max:
            max = len(window)

    return max

list = [0,1,1,1,0,0,1,1,0]
flips = 2
answer = 7
if bruteForce(list, flips) != answer:
    print("TEST FAIL")
    print("EXPECTED " + str(answer) + ", RECIEVED " + str(bruteForce(list, flips)))
else:
    print("TEST PASS")

list = [0,1,1,1,0,0,1,1,0]
flips = 1
answer = 4
if bruteForce(list, flips) != answer:
    print("TEST FAIL")
    print("EXPECTED " + str(answer) + ", RECIEVED " + str(bruteForce(list, flips)))
else:
    print("TEST PASS")

list = [1,1,1,0,0,1,1]
flips = 2
answer = 7
if bruteForce(list, flips) != answer:
    print("TEST FAIL")
    print("EXPECTED " + str(answer) + ", RECIEVED " + str(bruteForce(list, flips)))
else:
    print("TEST PASS")

list = [0,0,0,0]
flips = 2
answer = 2
if bruteForce(list, flips) != answer:
    print("TEST FAIL")
    print("EXPECTED " + str(answer) + ", RECIEVED " + str(bruteForce(list, flips)))
else:
    print("TEST PASS")

list = [0,1,1,1,1,1,1,0]
flips = 2
answer = 8
if bruteForce(list, flips) != answer:
    print("TEST FAIL")
    print("EXPECTED " + str(answer) + ", RECIEVED " + str(bruteForce(list, flips)))
else:
    print("TEST PASS")

# def maxOnes(list, flips):
#     zHolder = []
#     for i in range(len(list)):
#         if list[i] == 0:
#             zHolder.append(i+1)
#
#     zCounter = 0
#     first = zHolder[0]
#     # the index of the first zero INCLUDED in our flipped zeroes
#     leading = 0
#     trailing = 0
#     max = 0
#     # the best solution thus far
#     for i in range(1, len(zHolder)):
#         print(zCounter, flips)
#         if zCounter < flips:
#             trailing = zHolder[i+1]
#             max = trailing
#             zCounter += 1
#         else:
#             leading = first
#             first = zHolder[i-flips]
#             # check or index out of bounds
#             # print("GTG")
#             print(i+1, len(zHolder))
#             if i+1 < len(zHolder):
#                 trailing = zHolder[i+1]
#             delta = leading - trailing
#             if max < delta:
#                 max = delta
#
#     return (zHolder, len(zHolder), max)

# maxOnes(list, 2)
# print(maxOnes(list, 2))
