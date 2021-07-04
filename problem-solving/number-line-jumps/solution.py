YES = "YES"
NO = "NO"


def numberlinejumps(x1, v1, x2, v2):
    if x1 == x2 and v1 == v2:
        return YES

    if x1 > x2 and v1 >= v2 \
            or x1 < x2 and v1 <= v2 \
            or x1 == x2 and v1 != v2:
        return NO

    if x1 > x2:
        while x1 > x2:
            x1 += v1
            x2 += v2
    if x1 == x2:
        return YES

    if x1 < x2: 
        while x1 < x2:
            x1 += v1
            x2 += v2
    if x1 == x2:
        return YES

    return NO

