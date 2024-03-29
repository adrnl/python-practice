# Given an array of distinct integers candidates and a target integer target,
# return a list of all unique combinations of candidates where the chosen numbers sum to target.
# You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.

# It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

def combinationSum(candidates, target):
    ret = []
    dfs(candidates, target, [], ret)
    return ret

def dfs(nums, target, path, ret):
    if target < 0:
        return
    if target == 0:
        ret.append(path)
        return
    for i in range(len(nums)):
        dfs(nums[i:], target - nums[i], path + [nums[i]], ret)

cases = [
    [[2,3,6,7], 7],
    [[2], 1],
    [[1], 1],
    [[1], 2],
]

def test(cases):
    for case in cases:
        print(combinationSum(case[0], case[1]))

test(cases)