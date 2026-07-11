import math
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

T = int(input())
CD = [[int(i) for i in input().split()] for _ in range(T)]


for c, d in CD:
    ret = 0
    clength = len(str(c + 1))
    cdlength = len(str(c + d))
    for digit in range(clength, cdlength + 1):
        if clength == digit:
            mi = int(str(c) + str(c + 1))
        else:
            mi = int(str(c) + "1" + "0" * (digit - 1))

        if cdlength == digit:
            ma = int(str(c) + str(c + d))
        else:
            ma = int(str(c) + "9" * digit)

        ret += math.isqrt(ma) - math.isqrt(mi - 1)
    print(ret)
