import sys

input = sys.stdin.readline

N = int(input())
xy = [[int(i) for i in input().split()] for _ in range(N)]

d1 = []
d2 = []
for x, y in xy:
    d1.append(x + y)
    d2.append(x - y)

d1.sort(reverse=True)
d2.sort(reverse=True)

print(
    max(
        d1[0] - d1[-1],
        d2[0] - d2[-1],
    )
)
