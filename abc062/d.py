from heapq import heappush, heappop, heapify
import sys

input = sys.stdin.readline

N = int(input())
a = [int(i) for i in input().split()]

dpl = [0] * (N * 3)
dpr = [0] * (N * 3)
l = [a[i] for i in range(N)]
r = [-a[i] for i in range(2 * N, 3 * N)]
heapify(l)
heapify(r)

dpl[N - 1] = sum(l)
for i in range(N, 2 * N):
    heappush(l, a[i])
    m = heappop(l)
    dpl[i] = dpl[i - 1] + a[i] - m

dpr[2 * N] = -sum(r)
for i in range(2 * N - 1, N - 1, -1):
    heappush(r, -a[i])
    M = heappop(r)
    dpr[i] = dpr[i + 1] + a[i] + M

M = -float("inf")
for i in range(N - 1, 2 * N):
    M = max(M, dpl[i] - dpr[i + 1])
print(M)
