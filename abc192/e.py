import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
from heapq import heappush, heappop

N, M, X, Y = map(int, input().split())
ABTK = [[int(i) for i in input().split()] for _ in range(M)]

vec = [[] for i in range(N)]
for A, B, T, K in ABTK :
  A, B = A - 1, B - 1
  vec[A].append((B, T, K))
  vec[B].append((A, T, K))
  
q = [(0, X - 1)]
dist = [float('inf')] * N
dist[X - 1] = 0
while q :
  ccost, cur = heappop(q)
  if dist[cur] < ccost :
    continue
    
  for nex, t, k in vec[cur] :
    rest = (k - (ccost % k)) % k
    ncost = rest + ccost + t
    if ncost < dist[nex] :
      heappush(q, (ncost, nex))
      dist[nex] = ncost

if dist[Y - 1] == float('inf') :
  print(-1)
else :
  print(dist[Y - 1])