import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**5)

N, M = map(int, input().split())
A = list(map(int, input().split()))
xy = [[int(i) - 1 for i in input().split()] for _ in range(M)]

xy.sort()

stock = [[-float('inf')] * N for _ in range(2)]
BOUGHT = 0
SOLD = 1
for x, y in xy:
    stock[BOUGHT][x] = max(stock[BOUGHT][x], -A[x])
    stock[BOUGHT][y] = max(stock[BOUGHT][y], stock[BOUGHT][x], -A[y])
    stock[SOLD][y] = max(stock[SOLD][y], stock[BOUGHT][x] + A[y])

ans = -float('inf')
for i in range(N):
    ans = max(ans, stock[SOLD][i])

print(ans)
