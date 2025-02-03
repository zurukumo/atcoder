from heapq import heappush, heappop

N, M = map(int, input().split())
A = [int(i) for i in input().split()]

c = []
for a in A :
    heappush(c, -a)
    
for _ in range(M) :
    b = heappop(c)
    heappush(c, (b + 1) // 2)
    
print(-sum(c))