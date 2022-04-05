# def countDecreasingRatings(ratings):
#     print(ratings)
#     count = len(ratings)
#     for i in range(len(ratings)):
#         rating = ratings[i]
#         for j in range(i, len(ratings)):
#             if ratings[j] == rating - 1:
#                 count += 1
#             else:
#                 break
#
#     return count


# def countDecreasingRatings(ratings):
#     print(ratings)
#     count = len(ratings)
#     for i in range(len(ratings)):
#         rating = ratings[i]
#         for j in range(i + 1, len(ratings)):
#             if ratings[j] == rating - 1:
#                 count += 1
#             else:
#                 break
#
#     return count
import math

def countDecreasingRatings(ratings):
    print(ratings)
    sequences = []
    i, j = 0, 1
    chain = 1
    while j < len(ratings):
        rating = ratings[i]
        if i + 1 < len(ratings):
            j = i + 1
        else:
            sequences.append(chain)
            break

        if ratings[j] == rating - 1:
            chain += 1
            i = j
        else:
            sequences.append(chain)
            chain = 1
            i = j

    out = 0
    for val in sequences:
        out += (val*val + val)/2

    return out

def countDecreasingRatings(ratings):
    sequences = []
    i, j = 0, 1
    chain = 1
    while j < len(ratings):
        rating = ratings[i]
        if j + 1 < len(ratings):
            j += 1
        else:
            sequences.append(chain)
            break

        if ratings[j] == rating - 1:
            chain += 1
            i = j
        else:
            sequences.append(chain)
            chain = 1
            i = j

    out = 0
    for val in sequences:
        out += (val * val + val) / 2

    return out

print(countDecreasingRatings([2,1,3]))