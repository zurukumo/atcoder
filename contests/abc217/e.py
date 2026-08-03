import collections
import heapq
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**7)

Q = int(input())
nq = collections.deque([])
sq = []
for _ in range(Q):
    query = input().split()
    if query[0] == "1":
        x = int(query[1])
        nq.append(x)
    elif query[0] == "2":
        if sq:
            print(heapq.heappop(sq))
        else:
            print(nq.popleft())
    else:
        while nq:
            heapq.heappush(sq, nq.pop())
