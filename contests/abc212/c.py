import bisect
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N, M = map(int, input().split())
A = [-float("inf")] + sorted([int(i) for i in input().split()]) + [float("inf")]
B = [-float("inf")] + sorted([int(i) for i in input().split()]) + [float("inf")]

ret = float("inf")
for a in A:
    bl = bisect.bisect_right(B, a) - 1
    br = bisect.bisect_left(B, a)

    ret = min(ret, a - B[bl], B[br] - a)

print(ret)
