# You are given an unordered array consisting of consecutive integers e.g. [1, 2, 3, ..., n] without any duplicates.
# You are allowed to swap any two elements. Find the minimum number of swaps required to sort the array in ascending order.

def minSwaps(arr):
    reference = sorted(arr)
    indices = {v: i for i,v in enumerate(arr)}
    swaps = 0
    for i, v in enumerate(arr):
        correctValue = reference[i]
        if v != correctValue:
            swapTo = indices[correctValue]
            arr[swapTo], arr[i] = arr[i], arr[swapTo]
            indices[v], indices[correctValue] = swapTo, i
            # indices[correctValue] = i
            swaps += 1

    return swaps
