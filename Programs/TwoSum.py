# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

def twoSum(nums, target):
    length = len(nums)
    for i1 in range(length-1):
        for i2 in range(i1, length):
            if nums[i1] + nums[i2] == target:
                return (nums[i1], nums[i2])

nums = [1, 2, 5, 9, 15]
out = twoSum(nums, 3)
if out != (1, 2):
    print("TEST 1 FAIL")
else:
    print("TEST 1 PASS")

out = twoSum(nums, 14)
if out != (5, 9):
    print("TEST 2 FAIL")
else:
    print("TEST 2 PASS")