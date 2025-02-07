import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N = int(input())
LR = [[int(i) for i in input().split()] for _ in range(N)]


ma = 0
for l, r in LR:
    ma += r

if ma < 0:
    print("No")
    sys.exit()

ans = []
for l, r in LR:
    diff = min(r - l, ma)
    ans.append(r - diff)
    ma -= diff


if ma == 0:
    print("Yes")
    print(*ans)
else:
    print("No")
