def getTotalImbalance(weight):
    # print(weight)
    imbalance = 0
    subs = subarrays(weight)
    for array in subs:
        imbalance += difference(array)

    return imbalance


def subarrays(array):
    arrays = []
    for i in range(len(array) + 1):
        for j in range(i):
            arrays.append(array[j: i])

    return arrays


def difference(array):
    max, min = array[0], array[0]
    for num in array:
        if num > max:
            max = num
        if num < min:
            min = num

    return max - min