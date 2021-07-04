# PROBLEM:
#
# You are choreographing a circus show with various animals. For one act, you are given two
# kangaroos on a number line ready to jump in the positive direction (i.e, toward positive
# infinity).
#
# ∙ The first kangaroo starts at location and moves at a rate of meters per jump.
# ∙ The second kangaroo starts at location and moves at a rate of meters per jump.
#
# You have to figure out a way to get both kangaroos at the same location at the same time as part
# of the show. If it is possible, return YES, otherwise return NO.
#
# Link:    https://www.hackerrank.com/challenges/kangaroo/problem
# Result:  10/10 Stars
#
# My Solution:
YES = "YES"
NO  = "NO"

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

