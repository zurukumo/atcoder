from heapq import heappush, heappop

N, M = map(int, input().split())
ABCD = [[int(i) for i in input().split()] for _ in range(M)]

vec = [[] for _ in range(N)]
for A, B, C, D in ABCD:
  vec[A - 1].append((B - 1, C, D))
  vec[B - 1].append((A - 1, C, D))
  
def bs(d):
  ng, ok = -1, 10 ** 9
  while ok - ng > 1:
    m = (ng + ok) // 2
    if d <= (m + 1) * (m + 2):
      ok = m
    else:
      ng = m
      
  return ok

q = [(0, 0)]
visited = [float('inf')] * N
while q:
  ct, cur = heappop(q)
  if ct > visited[cur]:
    continue
    
  for nex, c, d in vec[cur]:
    t = max(bs(d), ct)
    nt = t + c + d // (t + 1)
    if nt < visited[nex]:
      visited[nex] = nt
      heappush(q, (nt, nex))

if visited[-1] == float('inf'):
  print(-1)
else:
  print(visited[-1])