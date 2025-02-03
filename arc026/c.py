from heapq import heappush, heappop

N, L = map(int, input().split())
lrc = [[int(i) for i in input().split()] for _ in range(N)]

lrc.sort()

ret = float('inf')
q = [(0, 0)]
for l, r, c in lrc :
  while q and q[0][1] < l :
    heappop(q)
    
  nc = q[0][0] + c
  heappush(q, (nc, r))
  if r == L :
    ret = min(ret, nc)
  
print(ret)