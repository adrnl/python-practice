def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums) - 1, i, -1):
            if nums[i] + nums[j] == target:
                return [i, j]

inArr = [2, 7, 11, 15]
inInt = 9
if twoSum(inArr, inInt) == [0, 1]:
    print("Test1 Pass")
else:
    print("Test1 Fail")

inArr = [2, 7, 11, 19, 15, 100000, 69, 81, 25, 0, 1, 12]
inInt = 30
if twoSum(inArr, inInt) == [2, 3]:
    print("Test2 Pass")
else:
    print("Test2 Fail")

inArr = [1, 3]
inInt = 4
if twoSum(inArr, inInt) == [0, 1]:
    print("Test3 Pass")
else:
    print("Test3 Fail")

inArr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 99]
inInt = 100
if twoSum(inArr, inInt) == [0, 10]:
    print("Test4 Pass")
else:
    print("Test4 Fail")

# inArr = [2, 7, 11, 15]
# inInt = 9
# if twoSum(inArr, inInt) == [0, 1]:
#     print("Test5 Pass")
# else:
#     print("Test5 Fail")


# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].