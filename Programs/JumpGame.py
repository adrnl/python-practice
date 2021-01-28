def jump(nums):
    if not nums or len(nums) == 1:
        return 0

    maximum = 0
    previousMaximum = 0
    jumps = 0

    for i in range(len(nums)):
        if i + nums[i] >= maximum:
            maximum = i + nums[i]

        if i == previousMaximum:
            jumps += 1
            previousMaximum = maximum
            if maximum >= len(nums)-1:
                return jumps

input = [2,3,1,1,4]
if jump(input) != 2:
    print("Test 1 FAIL")
else:
    print("Test 1 PASS")

input = [3,1,2,0,9,0,0,0,0,0,0,1]
if jump(input) != 3:
    print("Test 2 FAIL")
else:
    print("Test 2 PASS")


# Given an array of non-negative integers, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# Your goal is to reach the last index in the minimum number of jumps.
#
# Example:
#   Input: [2,3,1,1,4]
#   Output: 2
#
# Explanation: The minimum number of jumps to reach the last index is 2.
#              Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Note: You can assume that you can always reach the last index.
#
# Results:
#     Time Submitted    | Status    | Runtime | Memory  | Language
#     09/01/2020 16:17  | Accepted  | 92 ms   | 16.2 MB | python3
#     09/01/2020 16:17  | Accepted  | 160 ms  | 16.1 MB | python3
#     09/01/2020 16:17  | Accepted  | 176 ms  | 16.3 MB | python3
#     09/01/2020 16:17  | Accepted  | 100 ms  | 16.2 MB | python3
#     09/01/2020 16:16  | Accepted  | 124 ms  | 15.8 MB | python3
#     09/01/2020 16:16  | Accepted  | 96 ms   | 16.2 MB | python3
#     09/01/2020 16:12  | Accepted  | 152 ms  | 16.2 MB | python3
#     09/01/2020 16:11  | Accepted  | 176 ms  | 16.1 MB | python3
#     09/01/2020 16:03  | Accepted  | 148 ms  | 16.2 MB | python3