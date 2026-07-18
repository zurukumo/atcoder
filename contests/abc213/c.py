import bisect
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

H, W, N = map(int, input().split())
AB = [[int(i) for i in input().split()] for _ in range(N)]

xset = set()
yset = set()

for a, b in AB:
    xset.add(a)
    yset.add(b)

xlist = list(xset)
ylist = list(yset)
xlist.sort()
ylist.sort()

for a, b in AB:
    x = bisect.bisect_left(xlist, a) + 1
    y = bisect.bisect_left(ylist, b) + 1
    print(x, y)
