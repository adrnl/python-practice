# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.

# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

def fourSum(nums, target):
    out = []
    if len(nums) < 4:
        return out

    nums.sort()
    for i, num1 in enumerate(nums):
        if i > target and num1 == nums[i-1]:
            continue

        if num1 > target:
            return out

        for j, num2 in enumerate(nums[i+1:]):
            if num1 + num2 > target:
                break

            for k, num3 in enumerate(nums[i+j+2:]):
                if num1 + num2 + num3 > target:
                    break

                for num4 in nums[i+j+k+3:]:
                    total = num1 + num2 + num3 + num4
                    if total == target:
                        if [num1,num2,num3,num4] not in out:
                            out.append([num1,num2,num3,num4])

                    elif total > target:
                        break

    return out

# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

cases = (
    (([1,0,-1,0,-2,2],0), [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]),
)

def test(cases):
    for case in cases:
        out = fourSum(case[0][0],case[0][1])
        if out != case[1]:
            print("Test Fail")
            print(out, case[1])
        else:
            print("Test Pass")

test(cases)