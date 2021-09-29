# LArray Rotation via Hackerrank

def rotLeft(a, d):
    l = len(a)
    if d % l == 0:
        return nums
    else:
        d = d % l

    f = a[:d]
    s = a[d:]

    return s + f