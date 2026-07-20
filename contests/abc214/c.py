import heapq
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N = int(input())
S = [int(i) for i in input().split()]
T = [int(i) for i in input().split()]

ret = [float("inf")] * N
queue = []
for i, t in enumerate(T):
    heapq.heappush(queue, (t, i))

while queue:
    t, i = heapq.heappop(queue)
    if t >= ret[i]:
        continue
    ret[i] = t
    heapq.heappush(queue, (t + S[i], (i + 1) % N))

print(*ret)
