# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).
# import numpy
# import math

# lol xd
# def median(li1, li2):
#     li = li1 + li2
#     return numpy.median(li)

# def median(li1, li2):
#     li = li1 + li2
#     liLen = len(li)
#     if liLen % 2 == 1:
#         return li[int(math.floor(liLen/2))]
#     else:
#         return (li[int(liLen/2)] + li[int((liLen/2) - 1)])/2

# def listBuilder(li1, li2):
#     li = []
#     if not li1 and not li2:
#         return li
#     elif not li1:
#         return li2
#     elif not li2:
#         return li1
#
#     while li1 and li2:
#         e1 = li1[0]
#         e2 = li2[0]
#         if e1 <= e2:
#             li.append(li1.pop(0))
#         elif e2 < e1:
#             li.append(li2.pop(0))
#
#     if not li1:
#         li += li2
#     elif not li2:
#         li += li1
#
#     return li

# def medianHelper(li):
#     liLen = len(li)
#     index = (liLen - 1) // 2
#     if liLen % 2:
#         return li[index]
#     else:
#         return (li[index] + li[index + 1]) / 2.0

# def median(li1, li2):
#     median = 0
#     li = listBuilder(li1, li2)
#     if not li:
#         return median
#
#     median = medianHelper(li)
#     return median

def median(li1, li2):
    median = 0
    if not li1 and not li2:
        return median

    li = []
    # 2n
    li1.reverse()
    li2.reverse()
    # n
    while li1 and li2:
        len1 = len(li1)-1
        len2 = len(li2)-1
        e1 = li1[len1]
        e2 = li2[len2]
        if e1 <= e2:
            li.append(li1.pop(len1))
        elif e2 < e1:
            li.append(li2.pop(len2))

    # n
    if not li1:
        li2.reverse()
        li += li2
    elif not li2:
        li1.reverse()
        li += li1

    median = 0
    if not li:
        return median

    liLen = len(li)
    index = (liLen - 1) // 2
    if liLen % 2:
        median = li[index]
    else:
        median = (li[index] + li[index + 1]) / 2.0

    return median

def test():
    test1 = [1,2,3]
    test2 = [4,5,6]
    answer = 3.5
    if median(test1, test2) == answer:
        print("test 1 pass")
    else:
        print("test 1 fail")
        print(median(test1, test2), answer)

    test1 = [6,99,100]
    test2 = [4,10000]
    answer = 99
    if median(test1, test2) == answer:
        print("test 3 pass")
    else:
        print("test 3 fail")
        print(median(test1, test2), answer)

    test1 = [4,5,6,8,9]
    test2 = []
    answer = 6
    if median(test1, test2) == answer:
        print("test 3 pass")
    else:
        print("test 3 fail")
        print(median(test1, test2), answer)

test()