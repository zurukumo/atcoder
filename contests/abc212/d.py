import heapq
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

Q = int(input())
query = [input() for _ in range(Q)]

s = 0
queue = []
for q in query:
    t = int(q.split()[0])
    if t == 1:
        x = int(q.split()[1])
        heapq.heappush(queue, x - s)
    elif t == 2:
        x = int(q.split()[1])
        s += x
    elif t == 3:
        m = heapq.heappop(queue)
        print(m + s)
