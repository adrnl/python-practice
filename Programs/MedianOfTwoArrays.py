# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).
import math

# index
# 0,(1,2),3
# value
# 1,(2,3),4
# index
# 0,1,(2),3,4
# value
# 1,2,(3),4,5

# # n(log(n))
# def median(list1, list2):
#     combined = sorted(list1 + list2)
#     length = len(combined)
#     if length % 2 == 1:
#         out = combined[math.floor(length/2)]
#         return(out)
#     elif length % 2 == 0:
#         a = combined[int(length/2 - 1)]
#         b = combined[int(length/2)]
#         out = (a + b)/2
#         return(out)

# # O(n + m)
# def median(list1, list2):
#     combined = []
#     while list1 or list2:
#         if len(list1) == 0:
#             combined.append(list2[0])
#             list2.pop(0)
#         elif len(list2) == 0:
#             combined.append(list1[0])
#             list1.pop(0)
#         elif list1[0] < list2[0]:
#             combined.append(list1[0])
#             list1.pop(0)
#         else:
#             combined.append(list2[0])
#             list2.pop(0)
#
#     length = len(combined)
#     if length % 2 == 1:
#         out = combined[math.floor(length / 2)]
#         return (out)
#     elif length % 2 == 0:
#         a = combined[int(length / 2 - 1)]
#         b = combined[int(length / 2)]
#         out = (a + b) / 2
#         return out

# space and time optimized
def median(list1, list2):
    length = len(list1) + len(list2)
    median = math.ceil(length/2)
    m1 = 0
    m2 = 0
    counter = 0
    while counter < median + 1:
        if len(list1) == 0:
            m2 = m1
            m1 = list2[0]
            list2.pop(0)
        elif len(list2) == 0:
            m2 = m1
            m1 = list1[0]
            list1.pop(0)
        elif list1[0] < list2[0]:
            m2 = m1
            m1 = list1[0]
            list1.pop(0)
        else:
            m2 = m1
            m1 = list2[0]
            list2.pop(0)

        counter += 1

    if length % 2 == 1:
        return m2
    else:
        return (m1 + m2)/2


def test():
    test1 = [1,2,3]
    test2 = [4,5,6]
    answer = 3.5
    if median(test1, test2) == answer:
        print("test 1 pass")
    else:
        print("test 1 fail")
        print(median(test1, test2), answer)

# Test Case for non sorted lists
    # test1 = [3,2,1]
    # test2 = [4,5,6]
    # answer = 3.5
    # if median(test1, test2) == answer:
    #     print("test 2 pass")
    # else:
    #     print("test 2 fail")
    #     print(median(test1, test2), answer)

    test1 = [6,99,100]
    test2 = [4,10000]
    answer = 99
    if median(test1, test2) == answer:
        print("test 3 pass")
    else:
        print("test 3 fail")
        print(median(test1, test2), answer)

test()