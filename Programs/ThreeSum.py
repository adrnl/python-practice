# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# def threeSum(numbers):
#     solutions = []
#     if len(numbers) < 3:
#         return solutions
#
#     numbers.sort()
#     for i, num1 in enumerate(numbers[:-2]):
#         if num1 > 0:
#             break
#         for j, num2 in enumerate(numbers[i+1:-1]):
#             if num1 + num2 > 0:
#                 break
#             for num3 in numbers[i+j+2:]:
#                 if num1 + num2 + num3 > 0:
#                     break
#                 elif num1 + num2 + num3 == 0:
#                     if [num1, num2, num3] not in solutions:
#                         solutions.append([num1, num2, num3])
#
#     return solutions

def threeSum(numbers):
    solutions = []
    if len(numbers) < 3:
        return solutions

    numbers.sort()
    for i, num1 in enumerate(numbers[:-2]):
        if i > 0 and num1 == numbers[i-1]:
            continue

        j, k = i+1, len(numbers)-1
        while j < k:
            num2, num3 = numbers[j], numbers[k]
            total = num1 + num2 + num3
            if total < 0:
                j += 1
            elif total > 0:
                k -= 1
            elif total == 0:
                if [num1, num2, num3] not in solutions:
                    solutions.append([num1, num2, num3])
                j += 1
                k -= 1

    return solutions

cases = [
    ([1,2,-2,-1], []),
    ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
    ([], []),
    ([0], []),
]

def test(cases):
    for case in cases:
        out = threeSum(case[0])
        if out != case[1]:
            print("Test Fail")
            print(out, case[1])
        else:
            print("Test Pass")

test(cases)