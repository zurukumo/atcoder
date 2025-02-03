import sys
input = sys.stdin.readline
from heapq import heappush, heappop

N, M, S = map(int, input().split())
STATE = 50 * N + 1
vec = [[] for _ in range(STATE * N)]
for _ in range(M) :
  U, V, A, B = map(int, input().split())
  U -= 1
  V -= 1
  for silver in range(A, STATE) :
    vec[STATE * U + silver].append((STATE * V + silver - A, B))
    vec[STATE * V + silver].append((STATE * U + silver - A, B))
  
for i in range(N) :
  C, D = map(int, input().split())
  for silver in range(STATE - C) :
    vec[STATE * i + silver].append((STATE * i + silver + C, D))

dist = [float('inf')] * (STATE * N)

S = min(S, STATE - 1)
dist[S] = 0
q = [(0, S)]
while q :
  cc, cur = heappop(q)
  for nex, nc in vec[cur] :
    if dist[nex] <= cc + nc :
      continue
    dist[nex] = cc + nc
    heappush(q, (cc + nc, nex))

for i in range(1, N) :
  print(min(dist[STATE * i:STATE * (i + 1)]))