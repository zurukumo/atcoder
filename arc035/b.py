from heapq import heappush, heappop
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
vec = [[] for _ in range(N)]

for _ in range(M) :
    A, B, C = map(int, input().split())
    vec[A-1].append((B-1, C))
    vec[B-1].append((A-1, C))

def dijikstra(s) :
  dist = [-1] * N
  dist[s] = 0
  q = [(0, s)]
  while q :
    cco, cur = heappop(q)
    if dist[cur] < cco :
      continue
    for nex, nco in vec[cur] :
      if 0 <= dist[nex] <= cco + nco : continue
      dist[nex] = cco + nco
      heappush(q, (dist[nex], nex))
  return dist

fw = [dijikstra(i) for i in range(N)]

K = int(input())
ret = 0
for i in range(N) :
  for j in range(i + 1, N) :
    ret += fw[i][j]

for _ in range(K) :
  X, Y, Z = map(int, input().split())
  if Z < fw[X-1][Y-1] :
    for i in range(N) :
      for j in range(i + 1, N) :
        ndist = min(fw[i][j], fw[i][X-1] + fw[Y-1][j] + Z, fw[j][X-1] + fw[Y-1][i] + Z)
        ret -= (fw[i][j] - ndist)
        fw[i][j] = fw[j][i] = ndist
  print(ret)