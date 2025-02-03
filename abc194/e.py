from heapq import heappush, heappop, heapify
from collections import defaultdict

N, M = map(int, input().split())
A = [int(i) for i in input().split()]

use = [i for i in range(0, 15 * (10**5) + 10)]
heapify(use)

unuse = []
for i in range(M):
    unuse.append(A[i])
heapify(unuse)

mem = defaultdict(int)
while len(use) > 0 and len(unuse) > 0 and use[0] == unuse[0]:
    heappop(use)
    x = heappop(unuse)
    mem[x] += 1
    while len(unuse) > 0 and unuse[0] == x:
        heappop(unuse)
        mem[x] += 1

ret = float("inf")
ret = min(ret, use[0])
# print(use[0])

for i in range(M, N):
    a = A[i - M]
    mem[a] -= 1
    if mem[a] == 0:
        heappush(use, a)

    heappush(unuse, A[i])
    while len(use) > 0 and len(unuse) > 0 and use[0] == unuse[0]:
        heappop(use)
        x = heappop(unuse)
        mem[x] += 1
        while len(unuse) > 0 and unuse[0] == x:
            heappop(unuse)
            mem[x] += 1

    ret = min(ret, use[0])
    # print(use[0])

print(ret)
