import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

N = int(input())
APX = [[int(i) for i in input().split()] for _ in range(N)]

ret = float("inf")
for a, p, x in APX:
    if x - a > 0:
        ret = min(ret, p)

if ret == float("inf"):
    print(-1)
else:
    print(ret)
